#!/usr/bin/python3
"""
Convert a FASTA nucleic acid sequence to my ACGT format
---
The ACGT is a binary format; each nucleotide is represented by two bits, and these bits are concat'd in order to form the sequence
The list of two bit patterns:

00 - DNA: A, RNA: A
01 - DNA: C, RNA: C
10 - DNA: G, RNA: G
11 - DNA: T, RNA: U

There are several benefits to this.
When DNA is converted into RNA, the DNA sequence is effectively "inverted."
This can be done by literally inverting the value of every byte in the sequence:
For example, DNA A is represented by 00. If 00 is inverted, you get 11, which corresponds to RNA U.
This can be done in the same way for simply finding the complement of a strand of DNA, i.e. the strand that would match up with the original strand.
In addition, in FASTA, each letter in the sequence occupies 8 bits; whereas in ACGT, each letter takes up 2 bits, a reduction by three quarters.
While some may argue that a simple compression algorithm on FASTA could reduce the size substantially, a FASTA sequence pretty much always contains the character '>'
which means that a smart algorithm can't just use a 2-bit alphabet. Additionally, this compression comes with at least some overhead, which is not desirable.

This encoding doesn't come without some caveats, though.
For example, there is no checksum implemented. It is up to the user to solve that problem. However, the FASTA format does not require a checksum either.
Also, should the sequence be 1 bit off at some point, it would screw up everything following the mistake.
This usually isn't a problem though, as the bits are aligned to byte boundaries. It is pretty much guaranteed that files won't be corrupted in this way,
as any communication between parts of a computer either encodes the data in (multi)byte-sized chunks, or signals the start and/or end of these chunks.
This is only a problem in serial busses, and only if the bus is extremely simple.
This problem would also impact FASTA too, arguably even moreso because there is more data being processed.
Lastly, a program cannot tell if the sequence was RNA or DNA, as this format keeps no metadata. It is assumed that the program reading the file knows this.
Finally, if the sequence length is not a multiple of 4, the sequence will end with up to 3 false 'A' nucleotides. Again, the program should deal with this.
This is still better than extra G's or C's, as these more significantly impact the properties (temperature) of short sequences like primers.
There are a few ways to mitigate this, but the best solution would be that the length is provided as metadata somehow.
"""
import sys
from argparse import ArgumentParser as AP
from argparse import FileType

parser = AP(description='Converts FASTA sequences to ACGT sequences')
parser.add_argument('input', type=FileType('r'))
parser.add_argument('output', type=FileType('wb'))

args = parser.parse_args()
fin = args.input
fout = args.output

def fasta_nucleotides(f):
	map = {
		'A': 0,
		'C': 1,
		'G': 2,
		'T': 3,
		'U': 3
	}
	tmp = '?'
	while tmp:
		tmp = f.read(1)
		if tmp == '>':
			f.readline()
			continue
		if tmp.isspace():
			continue
		if tmp.upper() in map:
			yield map[tmp.upper()]
			continue
		if tmp.isnumeric():
			# sequence numbers?
			continue

def byte_collector(gen):
	still_run = True
	while still_run:
		a = 0
		b = 0
		c = 0
		d = 0
		try:
			a = gen.__next__()
			b = gen.__next__()
			c = gen.__next__()
			d = gen.__next__()
		except StopIteration:
			still_run = False
		finally:
			x = 0
			x |= a << 6
			x |= b << 4
			x |= c << 2
			x |= d << 0
			yield bytes([x])

def convert_file(fin, fout):
	# TODO: support filenames
	gen = fasta_nucleotides(fin)
	for b in byte_collector(gen):
		# windows is garbage and doesn't do this properly
		#sys.stdout.buffer.write(b)
		fout.write(b)

convert_file(fin, fout)
fin.close()
fout.close()