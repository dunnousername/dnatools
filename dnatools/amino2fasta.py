#!/usr/bin/python3
"""
Converts an amino acid fasta sequence to a fasta ***RNA*** sequence.
Run this through complement.py after converting to acgt format to get a DNA sequence.
Default optimizes for as few GC's as possible.
"""
import sys
from argparse import ArgumentParser as AP
from argparse import FileType

parser = AP(description='Converts amino acid FASTA sequences to FASTA RNA sequences')
parser.add_argument('input', type=FileType('r'))
parser.add_argument('output', type=FileType('w'))

args = parser.parse_args()
fin = args.input
fout = args.output

def fasta_aminos(f):
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
		if tmp:
			yield tmp.upper()

def amino_to_nucleotides(aminos):
	map = {
		# if there are any errors with this, PLEASE let me know.
		'A': 'GCA', # alanine
		'B': 'GAU', # aspartate/asparagine
		'C': 'UGU', # cysteine
		'D': 'GAU', # aspartate
		'E': 'GAA', # glutamate
		'F': 'UUU', # phenylalanine
		'G': 'GGA', # glycine
		'H': 'CAU', # histidine
		'I': 'AUU', # isoleucine
		'K': 'AAA', # lysine
		'L': 'UUA', # leucine
		'M': 'AUG', # methionine
		'N': 'AAU', # asparagine
		'P': 'CCU', # proline
		'Q': 'CAA', # glutamine
		'R': 'AGA', # arginine
		'S': 'AGU', # serine
		'T': 'ACA', # threonine
		'U': 'UGA', # selenocysteine # UGA from the wikipedia page for this amino acid
		'V': 'GUU', # valine
		'W': 'UGG', # tryptophan
		'Y': 'UAU', # tyrosine
		'Z': 'GAA', # glutamate/glutamine
		'X': 'AAA', # any # chose lysine because this doesn't seem to matter
		# if you want no stop codon automatically placed, uncomment this and comment the entry below it
		#'*': '' # end of sequence
		'*': 'UAG'  # end of sequence (just picked a random stop codon)
	}
	# comment the following if you don't want to automatically have a start codon
	yield from 'AUG'
	for amino in aminos:
		if amino in map:
			yield from map[amino]
			if amino == '*':
				return
	# the following adds the end of sequence codon if we don't already have one
	yield from map['*']

def convert_file(fin, fout):
	gen = fasta_aminos(fin)
	fout.write('> converted from amino acids to RNA with amino2fasta.py\n')
	for idx, nucleotide in enumerate(amino_to_nucleotides(gen)):
		fout.write(nucleotide)
		if idx and not (idx % 32):
			fout.write('\n')
	fout.write('\n')
convert_file(fin, fout)
fin.close()
fout.close()