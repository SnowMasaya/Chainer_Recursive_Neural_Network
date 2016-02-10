import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))


class TestExtractData(unittest.TestCase):

    def test_extract_data(self):
        from extract_data import ExtractData
        e = ExtractData(yaml_file="../ICML2011.yaml")
        e.extract_data()


if __name__ == '__main__':
    unittest.main()
