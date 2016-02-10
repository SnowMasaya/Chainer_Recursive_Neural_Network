import tables
import re
import yaml
from collections import namedtuple

class ExtractData():

    def __init__(self, yaml_file=""):
        self.re_express = re.compile("feat2|adj|segLabels|segs2|labels")
        #self.re_express = re.compile("adj")
        try:
            with open(yaml_file, encoding="utf-8") as yf:
                import yaml
                e = yaml.load(yf)
                self.train_data = e["train_data"]

        except Exception as ex:
            raise Exception("ICML yaml is not set. please confirm ICML2011.yaml on your root or environment variables")

    def extract_data(self):
        f = tables.openFile(self.train_data)
        for items in f.walk_nodes("/#refs#/"):
            split_item = str(items).split(" ")
            print(items)
            if type(items) is not tables.group.Group and self.re_express.search(split_item[0]) :
                 print(split_item[0])
                 print(f.get_node(split_item[0]).read())
                 print(len(f.get_node(split_item[0]).read()))
                 print(len(f.get_node(split_item[0]).read()[0]))
