import unittest
import subprocess
import nbutil

def tstfun(infile, cryptoscore, dinoscore):
    proc = subprocess.Popen(["python", "nb.py", infile], stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    mystr1="('Score(crypto):', "+cryptoscore+")\n"
    mystr2="('Score(dino):', "+dinoscore+")\n"
    return out, mystr1+mystr2
        

class TestFull(unittest.TestCase):
 
    def test01(self):
        (out, mystr) = tstfun("test01_input.yaml", "25239.08993198242", "2601.7664705783586")
        self.assertEqual(out,mystr)

    def test02(self):
        (out, mystr) = tstfun("test02_input.yaml", "1617656.2932267354", "1.7777297062779534e+26")
        self.assertEqual(out,mystr)

    def test03(self):
        (out, mystr) = tstfun("test03_input.yaml", "832.0706697339581", "5482.325210726829")
        self.assertEqual(out,mystr)

    def test_count_words(self):
        s = "Hello my name, is Greg. My favorite food is pizza."
        wc = nbutil.count_words(nbutil.tokenize(s))
        self.assertEqual(wc, {'favorite': 1.0, 'food': 1.0, 'greg': 1.0, 'hello': 1.0, 'is': 2.0, 'my': 2.0, 'name': 1.0, 'pizza': 1.0})

    

if __name__ == '__main__':
    unittest.main()
