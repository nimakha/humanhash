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

API
---

~~~~~
python setup.py install
import hhlib
h = hhlib.HH(msg = message, algorithm = "sha512")
h.update(message)
h.paragraph(length)
~~~~~

LICENSE
-------

Copyright © 2012 by Nima Khazaei.

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
