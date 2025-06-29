import unittest
from main import concatenate_wow

class TestConcatenateWow(unittest.TestCase):
  def test_concatenate_wow(self):
    self.assertEqual(concatenate_wow("Hello, "), "Hello, WOW!")
    self.assertEqual(concatenate_wow(""), "WOW!")
    self.assertEqual(concatenate_wow("Jules "), "Jules WOW!")
    self.assertEqual(concatenate_wow("abc", "def"), "abcWOW!defWOW!")
    self.assertEqual(concatenate_wow("A", "B", "C"), "AWOW!BWOW!CWOW!")
    self.assertEqual(concatenate_wow(), "")

if __name__ == "__main__":
  unittest.main()
