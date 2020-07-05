from operate_file_1 import all_files
import os
import linecache
import configparser


class Todo:
    def __init__(self):

        self.rule_file = configparser.ConfigParser()
        self.rule_file.read("./config.ini", "UTF-8")

        self.dir_name_keys = list(self.rule_file["Dir_names"].keys())
        self.dir_names = [self.rule_file["Dir_names"][key] for key in self.rule_file["Dir_names"].keys()]
        self.patterns = [self.rule_file["File_names"][key] for key in self.rule_file["File_names"].keys()]

    def search_file(self):
        paths = {}
        for index, dir_name in enumerate(self.dir_names):
            paths[self.dir_name_keys[index]] = list(all_files(dir_name, ";".join(self.patterns)))
        return paths

    def limit_search_file(self, dir_name_key):
        paths = {}
        paths[dir_name_key] = list(all_files(self.rule_file["Dir_names"][dir_name_key], ";".join(self.patterns)))
        return paths

    def get_dir_name_keys(self):
        return self.dir_name_keys