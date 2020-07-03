from operate_file_1 import all_files
import os
import linecache
import configparser


class Todo:
    def __init__(self):

        rule_file = configparser.ConfigParser()
        rule_file.read("./config.ini", "UTF-8")

        self.dir_name_keys = list(rule_file["Dir_names"].keys())
        self.dir_names = [rule_file["Dir_names"][key] for key in rule_file["Dir_names"].keys()]
        self.patterns = [rule_file["File_names"][key] for key in rule_file["File_names"].keys()]

    def search_file(self):
        paths = {}
        for index, dir_name in enumerate(self.dir_names):
            paths[self.dir_name_keys[index]] = list(all_files(dir_name, ";".join(self.patterns)))
        return paths

"""    
            
        for path in paths:

            #ファイル名記入
            line_list.append("File Name : ")
            line_list.append(path)
            line_list.append("\n")

            for line in range(line_number):
                line_list.append(linecache.getline(path, line + 1))
            line_list.append("\n")
            line_list.append("================================================")
            line_list.append("\n")

        file_object = open("list.txt", "w")
        file_object.writelines(line_list)
        file_object.close()
"""