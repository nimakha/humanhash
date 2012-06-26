HumanHash
========

An algorithm for generating natural-language-based cryptographic hashes.

* * * * *

USAGE
-----

~~~~~
humanhash [-h] [-x] [-n LENGTH]
          [-a {md5,sha1,sha224,sha256,sha384,sha512}] [-m]
          [input]
~~~~~

`-h, --help`
  shows a short help message

`-x, --hex`
  specifies that input is in the form of a pre-computed hexadecimal number, 
  rather than a filename

`-n, --length` *LENGTH*
  length of output, in number of sentences

`-a, --algorithm` *{md5,sha1,sha224,sha256,sha384,sha512}*
  algorithm used to compute the cryptographic digest, defaults to sha512

`-m, --mnemonic`
  instead of generating a paragraph, produces a two-word mnemonic codename

API
---

~~~~~
$ python setup.py install

>>> import hhlib
>>> h = hhlib.HH(msg = message, algorithm = "sha512")
>>> h.update(message)
>>> h.paragraph(length)
~~~~~

HISTORY
-------

The HumanHash algorithm was originally conceived and implemented as 
[All Hands Active](http://allhandsactive.com/), the first hackerspace in Ann 
Arbor, MI, was working on ratifying its first bylaws, around January 2011. 
HumanHash was used as a mechanism to for generating unambiguous, deterministic 
codenames for revisions of the bylaws. See example usage on 
[AHA's mailing list](http://goo.gl/CVF1F).

LICENSE
-------

Copyright © 2011--2012 by Nima Khazaei.

Permission to use, copy, modify, and/or distribute this software for any 
purpose with or without fee is hereby granted, provided that the above 
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH 
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND 
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, 
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM 
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR 
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR 
PERFORMANCE OF THIS SOFTWARE.
