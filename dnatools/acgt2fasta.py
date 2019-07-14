#!/usr/bin/python3
"""
See fasta2acgt.py for more general info.
Assumes DNA.
"""
import sys
from argparse import ArgumentParser as AP
from argparse import FileType

parser = AP(description='Converts ACGT sequences to FASTA sequences')
parser.add_argument('input', type=FileType('rb'))
parser.add_argument('output', type=FileType('w'))

args = parser.parse_args()
fin = args.input
fout = args.output

def acgt_nucleotides(f):
	map = ['A', 'C', 'G', 'T']
	
	#with open('test.acgt', 'rb') as f:
	tmp = b'?'
	while tmp:
		tmp = f.read(1)
		if len(tmp):
			x = int.from_bytes(tmp, 'big')
			a = (x >> 6) & 3
			b = (x >> 4) & 3
			c = (x >> 2) & 3
			d = (x >> 0) & 3
			yield map[a]
			yield map[b]
			yield map[c]
			yield map[d]

def convert_file(fin, fout):
	gen = acgt_nucleotides(fin)
	fout.write('> generated from acgt2fasta.py from ACGT format.\n')
	for idx, nucleotide in enumerate(gen):
		fout.write(nucleotide)
		if idx and not (idx % 32):
			fout.write('\n')
	fout.write('\n')

convert_file(fin, fout)
fin.close()
fout.close()