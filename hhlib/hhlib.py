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
    def __init__(self, msg = None, algorithm = None, struct = None):
    
        if algorithm == None:
            self.h = hashlib.new("sha512")
        elif algorithm == "ident":
            self.h = IdentHash()
        else:
            self.h = hashlib.new(algorithm)

        if msg != None:
            self.update(msg)

        if struct == None:
            self.struct = [[Noun, Adjective, Verb_3rd, Noun], [Noun, Verb_3rd, Noun]]
        else:
            self.struct = struct

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

    def _sentence(self, num_in, struct = None):
        if struct == None:
            struct = self.struct
        i = 0
        while num_in > 0:
            self.l = []
            for unit in struct[i]:
                if num_in > 0:
                    self.l.append(unit.word(int(num_in % unit.length())))
                    num_in = num_in / unit.length()
            self.l.reverse()
            yield self.l[0][0].capitalize() + " ".join(self.l)[1:] + "."
            i = (i + 1) % len(struct)

    def sentence(self, struct = None):
        return self._sentence(self._hex_to_int(self.hexdigest()), struct)

    def paragraph(self, length = None, struct = None):
        paragraph = []
        self.s = self.sentence(struct = struct)
        while length > 0 or length == None:
            try:
                paragraph.append(self.s.next())
            except StopIteration:
                break
            if length != None: length -= 1
        return "\n".join(paragraph)
