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

def fasta_complement(f):
	# NOTE: converts A to U (which would be done in RNA). Change U to T if you want it to switch to T instead.
	map = {
		'A': 'U',
		'G': 'C',
		'C': 'G',
		'T': 'A',
		'U': 'A'
	}
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
		if tmp.upper() in map:
			yield map[tmp.upper()]

def convert_file(fin, fout):
	gen = fasta_complement(fin)
	fout.write('> sequence complemented with fastacomplement.py\n')
	for idx, nucleotide in enumerate(gen):
		fout.write(nucleotide)
		if idx and not (idx % 32):
			fout.write('\n')
	fout.write('\n')
convert_file(fin, fout)
fin.close()
fout.close()