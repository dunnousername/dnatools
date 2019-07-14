#!/usr/bin/python3
"""
Converts a fasta ***RNA*** sequence to an amino acid fasta sequence.
"""
import sys
from argparse import ArgumentParser as AP
from argparse import FileType

parser = AP(description='Converts FASTA RNA sequences to FASTA amino acid sequences')
parser.add_argument('input', type=FileType('r'))
parser.add_argument('output', type=FileType('w'))

args = parser.parse_args()
fin = args.input
fout = args.output

def fasta_nucleotides(f):
	allowed = ['U', 'C', 'A', 'G']
	tmp = '?'
	while tmp:
		tmp = f.read(1)
		if tmp == '>':
			f.readline()
			continue
		if tmp.isspace():
			continue
		if tmp.isnumeric():
			# sequence numbers?
			continue
		if tmp.upper() in allowed:
			yield allowed.index(tmp.upper())

def nucleotides_to_amino(nucleotides):
	# pretty sure this is right, let me know if it isn't
	map = 'FFLLLLLLIIIMVVVVSSSSPPPPTTTTAAAAYY**HHQQNNKKDDEECC*WRRRRSSRRGGGG'
	assert len(map) == 64
	while True:
		try:
			a = next(nucleotides)
			b = next(nucleotides)
			c = next(nucleotides)
			yield map[(a << 4) | (b << 2) | (c << 0)]
		except StopIteration:
			return

def convert_file(fin, fout):
	gen = fasta_nucleotides(fin)
	fout.write('> converted from RNA to amino acids with fasta2amino.py\n')
	for idx, nucleotide in enumerate(nucleotides_to_amino(gen)):
		fout.write(nucleotide)
		if idx and not (idx % 32):
			fout.write('\n')
	fout.write('\n')
convert_file(fin, fout)
fin.close()
fout.close()