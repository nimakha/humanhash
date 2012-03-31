import humanhash
import unittest

class TestHHFunctions(unittest.TestCase):

  def setUp(self):
    self.msg = ""

  def test_hexdigest(self):
    self.h = humanhash.HumanHash()
    self.assertEqual(self.h.hexdigest(), "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e")
    self.h.update("The quick brown fox jumps over the lazy dog.")
    self.assertEqual(self.h.hexdigest(), "91ea1245f20d46ae9a037a989f54f1f790f0a47607eeb8a14d12890cea77a1bbc6c7ed9cf205e67b7f2b8fd4c7dfd3a7a8617e45f3c463d481c7e586c39ac1ed")

  def test_hex_to_int(self):
    self.empty_sha512_hex = "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e"
    self.qbf_sha512_hex = "91ea1245f20d46ae9a037a989f54f1f790f0a47607eeb8a14d12890cea77a1bbc6c7ed9cf205e67b7f2b8fd4c7dfd3a7a8617e45f3c463d481c7e586c39ac1ed"

    self.empty_sha512_int = 10868450558671247443152026947160338505683745266658651051718065983487878962987857602829315249215796444208488632888003673539585986066311769564391053988452926L
    self.qbf_sha512_int = 7642154151329160362837211161587045664414440157266416477977960063987610751319471890049388589735903591731492541815879910385812692600527820944081072741335533L

    self.h = humanhash.HumanHash()

    self.assertEqual(self.h._hex_to_int(self.empty_sha512_hex), self.empty_sha512_int)
    self.assertEqual(self.h._hex_to_int(self.qbf_sha512_hex), self.qbf_sha512_int)

  def test_rebase(self):
    self.empty_sha512 = 10868450558671247443152026947160338505683745266658651051718065983487878962987857602829315249215796444208488632888003673539585986066311769564391053988452926L
    self.qbf_sha512 = 7642154151329160362837211161587045664414440157266416477977960063987610751319471890049388589735903591731492541815879910385812692600527820944081072741335533L

    self.empty_sha512_n_adj_v = [369, 115, 27, 59, 74, 62, 181, 30, 53, 351, 32, 49, 356, 29, 59, 285, 55, 24, 382, 97, 0, 372, 28, 6, 105, 85, 32, 264, 68, 18, 186, 7, 46, 257, 97, 26, 323, 30, 14, 268, 11, 28, 384, 96, 54, 51, 46, 33, 346, 71, 45, 135, 108, 18, 205, 47, 70, 10, 1, 46, 393, 68, 11, 27, 23, 45, 127, 47, 36, 156, 3]
    self.qbf_sha512_n_adj_v = [19, 87, 37, 87, 69, 57, 90, 63, 60, 204, 54, 52, 282, 17, 62, 370, 93, 54, 0, 71, 54, 42, 56, 13, 204, 86, 15, 155, 14, 70, 223, 73, 28, 142, 22, 25, 352, 120, 63, 327, 13, 52, 168, 107, 44, 85, 104, 22, 370, 55, 36, 53, 91, 50, 159, 27, 8, 175, 38, 30, 29, 110, 4, 197, 79, 71, 389, 21, 69, 153, 2]

    self.h = humanhash.HumanHash()

    self.empty_sha512_rebase_output = list(self.h._rebase(self.empty_sha512))
    self.qbf_sha512_rebase_output = list(self.h._rebase(self.qbf_sha512))

    self.assertEqual(self.empty_sha512_rebase_output, self.empty_sha512_n_adj_v)
    self.assertEqual(self.qbf_sha512_rebase_output, self.qbf_sha512_n_adj_v)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestHHFunctions)
  unittest.TextTestRunner(verbosity=2).run(suite)
