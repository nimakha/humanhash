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
