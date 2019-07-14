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
## What version of python is this?
Python 3.
## Which Python 3?
The latest will probably work.
## Can I hear you rant about why you chose the MIT license?
You sure can! See README.LICENSE.md at the root of this repo.
## Can you add Python 2 support?
Unless someone contributes it, or a lot of people want Python 2 support, probably not.

I know Python 3 much better than Python 2, and 3 is much better IMHO.
## Contributing
All contributions are greatly appreciated. Pull requests are extremely helpful, but issues are definitely welcomed too.
