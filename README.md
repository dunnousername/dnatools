# dnatools
I watched a video on genetic engineering and thought it was really cool. I decided to make some simple tools to work with DNA sequences for fun.
## What is ACGT format?
I invented this format (it probably already existed, since it is basically the naive solution for what I'm trying to do).

FASTA is the standard format for these things, but it requires a byte per nucleotide; I reduced this to 2 bits per nucleotide.
This has a few caveats, explained in more detail in dnatools/fasta2acgt.py.

However, it offers a lot of benefits; for example, uncompressed, it is (less than, due to FASTA metadata) a quarter of the size of a FASTA nucleotide file.

This makes it, in theory, faster to process. (Although these tools are implemented in python, and this would apply moreso to native code.)

It also makes it extremely easy to, for example, find the complement of a DNA strand (IIRC, RNA produced during transcription is usually the complement of the DNA strand): because of how it is designed, you just flip every bit in the sequence.

I provide programs for converting ACGT to and from FASTA, as well as complementing an ACGT sequence.

There is also a program for converting FASTA amino sequences to FASTA RNA sequences, as well as some test files you can play with.
## Contributing
All contributions are greatly appreciated. Pull requests are extremely helpful, but issues are definitely welcomed too.
