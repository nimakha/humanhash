#!/usr/bin/env python
import sys
from wordlists import Noun, Adjective, Verb_3rd
import hashlib

class IdentHash(object):
    def __init__(self, msg = ""):
        self._digest = msg

    def update(self, msg):
        self._digest += msg

    def hexdigest(self):
        return self._digest


class HH(object):
    def __init__(self, msg = None, algorithm = None, sstruct = None):
    
        if algorithm == None:
            self.h = hashlib.new("sha512")
        elif algorithm == "ident":
            self.h = IdentHash()
        else:
            self.h = hashlib.new(algorithm)

        if msg != None:
            self.update(msg)

        if sstruct == None:
            self.sstruct = [Noun, Adjective, Verb_3rd, Noun]
        else:
            self.sstruct = sstruct

    algorithms = hashlib.algorithms

    def update(self, msg):
        self.h.update(msg)

    def update_from_file(self, f):
        for block in iter(lambda: f.read(self.h.block_size), ''):
            self.h.update(block)

    def digest(self):
        return self.h.digest()

    def hexdigest(self):
        return self.h.hexdigest()

    def _hex_to_int(self, hex_in):
        return int("0x" + hex_in, 16)

    def _sentence(self, num_in, sstruct = None):
        if sstruct == None:
            sstruct = self.sstruct
        while num_in > 0:
            self.l = []
            for unit in sstruct:
                if num_in > 0:
                    self.l.append(unit.word(int(num_in % unit.length())))
                    num_in = num_in / unit.length()
            self.l.reverse()
            yield self.l[0][0].capitalize() + " ".join(self.l)[1:] + "."

    def sentence(self, sstruct = None):
        return self._sentence(self._hex_to_int(self.hexdigest()), sstruct)

    def paragraph(self, length = None, sstruct = None):
        paragraph = []
        self.s = self.sentence(sstruct = sstruct)
        while length > 0 or length == None:
            try:
                paragraph.append(self.s.next())
            except StopIteration:
                break
            if length != None: length -= 1
        return "\n".join(paragraph)

def main():
    import argparse
    parser = argparse.ArgumentParser(description = "Represent cryptographic hashes as English sentences.")
    parser.add_argument("input", type = str, default = None, nargs = "?", 
                        help = "file to read, use '-' or leave unspecified to read from stdin")
    parser.add_argument("-x", "--hex", action = "store_true",
                        help = "specifies that input is in the form of a pre-computed hexadecimal number, rather than a filename")
    parser.add_argument("-n", "--length", type = int, default = None,
                        help = "length, in number of sentences")
    parser.add_argument("-a", "--algorithm", type = str, choices = HumanHash.algorithms, default = "sha512",
                        help = "algorithm used to compute the cryptographic digest, defaults to sha512")
    parser.add_argument("-m", "--mnemonic", action = "store_true",
                        help = "instead of generating a paragraph, produce a two-word mnemonic codename")
    args = parser.parse_args()

    if args.hex:
        h = HH(algorithm = "ident")
        h.update(args.input)
    else:
        h = HH(algorithm = args.algorithm)
        if args.input == "-" or args.input == None:
            h.update_from_file(sys.stdin)
        else:
            with open(args.input, "r") as f:
                h.update_from_file(f)

    if args.mnemonic:
        print h.paragraph(length = 1, sstruct = [Noun, Adjective])
    else:
        print h.paragraph(length = args.length)

if __name__ == "__main__":
    sys.exit(main())
