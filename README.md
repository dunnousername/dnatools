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
## What license does this project use?
It uses the MIT license.
## Why not use GPL?
GPL is awful.
## But it's not!
It is.
## Why are you only giving one line answers?
Not sure.
## Really though, why don't you like the GPL?
I think open-source is about helping society, at least to some extent. And society is made of people.

So, I'd rather give people choices to benefit from this project, even if that means they don't share the changes back.

At least for me, if I download something that someone is offering for free, I don't want them to demand I show them what I did with the code.

If your friend gives you a recipe for a vanilla cake, and you make a much better chocolate cake by modifying the recipe, it would still be really weird if your friend knocks on your door and demands the recipe for the chocolate cake.

## Why not use a public domain license?
I think I remember reading somewhere that "public domain" is ill-defined legally, and so in some places you get less freedom with public domain code than you do with e.g. MIT-licensed code.

But I'm not sure.
## If you're not sure, then make it public domain now!
What benefit do you get from that? Pretty much the only thing the MIT license requires for normal use is that you give attribution.

With the chocolate cake example, I think most people would agree that, if you open a chocolate cake store (bakery... ?) and make millions, the least you could do is put your friend's name in fine print somewhere in the store.

## Can you add Python 2 support?
Unless someone contributes it, or a lot of people want Python 2 support, probably not.

I know Python 3 much better than Python 2, and 3 is much better IMHO.
## Contributing
All contributions are greatly appreciated. Pull requests are extremely helpful, but issues are definitely welcomed too.
