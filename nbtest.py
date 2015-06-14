import unittest
import subprocess

class TestFull(unittest.TestCase):
    
    def test01(self):
        proc = subprocess.Popen(["python", "nb.py"], stdout=subprocess.PIPE)
        out = proc.communicate()[0]
        mystr1="('Score(crypto):', 25239.08993198242)\n"
        mystr2="('Score(dino):', 2601.7664705783586)\n"
        self.assertEqual(out,mystr1+mystr2)


if __name__ == '__main__':
    unittest.main()
