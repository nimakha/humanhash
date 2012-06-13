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


class HumanHash(object):
    def __init__(self, msg = None, algorithm = "sha512", sstruct = None):
    
        self.h = hashlib.new(algorithm)

        if msg != None:
            self.update(msg)

        if sstruct == None:
            self.sstruct = [Noun, Adjective, Verb_3rd, Noun]
        else:
            self.sstruct = sstruct

    def update(self, msg):
        self.h.update(msg)

    def digest(self):
        return self.h.digest()

    def hexdigest(self):
        return self.h.hexdigest()

    def _hex_to_int(self, hex_in):
        return int("0x" + hex_in, 16)

    def _rebase(self, num_in, radices = [401, 121, 75]):
        self.period = len(radices)
        self.position = 0
        while num_in > 0:
            self.radix = radices[self.position % self.period]
            yield int(num_in % self.radix)
            num_in = num_in / self.radix
            self.position = self.position + 1

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
        
def main():
    h = HumanHash()
    print "\n".join(list(h._sentence(h._hex_to_int(h.hexdigest()))))

if __name__ == "__main__":
    sys.exit(main())
