#!/usr/bin/python3
"""
Complements the ACGT sequence.
"""

from argparse import ArgumentParser as AP
from argparse import FileType

parser = AP(description='Complements an ACGT sequence')
parser.add_argument('input', type=FileType('rb'))
parser.add_argument('output', type=FileType('wb'))

args = parser.parse_args()
fin = args.input
fout = args.output

tmp = fin.read(1)
while tmp:
	fout.write(bytes(
		[0xff - tmp[0]]
	))
	tmp = fin.read(1)

fin.close()
fout.close()