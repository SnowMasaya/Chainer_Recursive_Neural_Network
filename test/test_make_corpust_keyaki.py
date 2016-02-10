import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))


class TestMakeCorpusKeyaki(unittest.TestCase):

    def test_make_corpus(self):
        from make_corpus_keyaki import MakeCorpusKeyaki
        e = MakeCorpusKeyaki(yaml_file="ICML2011.yaml")
        e.remake_corpus()

if __name__ == '__main__':
    unittest.main()
