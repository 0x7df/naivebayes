"""Unit testing driver for naive Bayes classifier."""

import unittest
import subprocess
import nbutil


def tstfun(infile, cryptoscore, dinoscore):
    """Utility function for the first 3 tests."""
    proc = subprocess.Popen(["python", "nb.py", infile],
                            stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    mystr1 = "('Score(crypto):', "+cryptoscore+")\n"
    mystr2 = "('Score(dino):', "+dinoscore+")\n"
    return out, mystr1+mystr2


class TestFull(unittest.TestCase):

    """Required class for unittest.

    See https://docs.python.org/2.7/library/unittest.html#basic-example.
    """

    def test01(self):
        """Single-document - test against original code."""
        (out, mystr) = tstfun("test01_input.yml", "25239.08993198242",
                              "2601.7664705783586")
        self.assertEqual(out, mystr)

    def test02(self):
        """Single document - test against original code."""
        (out, mystr) = tstfun("test02_input.yml", "1617656.2932267354",
                              "1.7777297062779534e+26")
        self.assertEqual(out, mystr)

    def test03(self):
        """Single document - test against original code."""
        (out, mystr) = tstfun("test03_input.yml", "832.0706697339581",
                              "5482.325210726829")
        self.assertEqual(out, mystr)

    def test_count_words(self):
        """Unit test of count_words function."""
        s = "Hello my name, is Greg. My favorite food is pizza."
        wc = nbutil.count_words(nbutil.tokenize(s))
        self.assertEqual(wc, {'favorite': 1.0, 'food': 1.0, 'greg': 1.0,
                              'hello': 1.0, 'is': 2.0, 'my': 2.0,
                              'name': 1.0, 'pizza': 1.0})

    def test09(self):
        """Multiple docs - test against self.

        Tests run over several documents against concatenation of
        results from multiple runs over same documents.
        """
        proc = subprocess.Popen(["python", "nb.py", "test09_input.yml"],
                                stdout=subprocess.PIPE)
        allout = proc.communicate()[0]
        refout = ""
        proc = subprocess.Popen(["python", "nb.py", "test04_input.yml"],
                                stdout=subprocess.PIPE)
        refout += proc.communicate()[0]
        proc = subprocess.Popen(["python", "nb.py", "test05_input.yml"],
                                stdout=subprocess.PIPE)
        refout += proc.communicate()[0]
        proc = subprocess.Popen(["python", "nb.py", "test06_input.yml"],
                                stdout=subprocess.PIPE)
        refout += proc.communicate()[0]
        proc = subprocess.Popen(["python", "nb.py", "test07_input.yml"],
                                stdout=subprocess.PIPE)
        refout += proc.communicate()[0]
        self.assertEqual(refout, allout)


if __name__ == '__main__':
    unittest.main()
