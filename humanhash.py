import sys

class HumanHash(object):
  def __init__(self, msg = None, digestmod = None):
    if digestmod == None:
      import hashlib
      digestmod = hashlib.sha512

    if hasattr(digestmod, '__call__'):
      self.digest_cons = digestmod
    else:
      self.digest_cons = lambda d='': digestmod.new(d)
    
    self.h = self.digest_cons()

    if msg != None:
      self.update(msg)

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

def main():
  h = HumanHash()
  print list(h._rebase(h._hex_to_int(h.hexdigest())))

if __name__ == "__main__":
  sys.exit(main())
