import tables
import re
import yaml
from collections import namedtuple

class MakeCorpusKeyaki():

    def __init__(self, yaml_file=""):
        self.re_express = re.compile("\(.* ")
        self.char = ""
        try:
            with open(yaml_file, encoding="utf-8") as yf:
                import yaml
                e = yaml.load(yf)
                self.corpus_list = e["corpus_list"]
                self.tree_bank_word_label = e["tree_bank_word_label"]
                self.tree_bank_phrase_label = e["tree_bank_phrase_label"]
                self.tree_bank_phrase_add_label = e["tree_bank_phrase_add_label"]
                self.tree_bank_special_label = e["tree_bank_special_label"]
                self.tree_bank_list = [self.tree_bank_word_label, self.tree_bank_phrase_label,
                                       self.tree_bank_phrase_add_label, self.tree_bank_special_label]

        except Exception as ex:
            raise Exception("ICML yaml is not set. please confirm ICML2011.yaml on your root or environment variables")

    def remake_corpus(self):
        concate_data = ""
        f_list = open(self.corpus_list, "r")
        for f in f_list:
            file = open(f.strip(), "r")
            for data in file:
                if "ID " in data:
                    self.char = self.__replace_symbol(concate_data)
                    print(self.char)
                    concate_data = ""
                else:
                    concate_data = concate_data + " " + data.strip()

    def __replace_symbol(self, concate_data):
        for data in self.tree_bank_list:
            for k in data.keys():
                if k in concate_data:
                    replace_char = "(" + str(data[k]) + " "
                    pattern = re.compile(r"\(%s " % k)
                    concate_data = re.sub(pattern, replace_char, concate_data)
        return concate_data

