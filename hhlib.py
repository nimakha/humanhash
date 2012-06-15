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
