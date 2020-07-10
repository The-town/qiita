from operate_file_1 import all_files
import configparser
import re
import linecache


class Todo:
    def __init__(self):

        self.rule_file = configparser.ConfigParser()
        self.rule_file.read("./config.ini", "UTF-8")

        self.dir_name_keys = list(self.rule_file["Dir_names"].keys())
        self.dir_names = [self.rule_file["Dir_names"][key] for key in self.rule_file["Dir_names"].keys()]
        self.patterns = [self.rule_file["File_names"][key] for key in self.rule_file["File_names"].keys()]

    def search_file(self):
        paths = []
        for dir_name in self.dir_names:
            paths.extend(list(all_files(dir_name, ";".join(self.patterns))))
        return paths

    def limit_search_file(self, dir_name_key):
        paths = list(all_files(self.rule_file["Dir_names"][dir_name_key], ";".join(self.patterns)))
        return paths

    def search_importance(self, file_name):
        result = self.judge_importance(file_name)
        if result is None:
            return self.rule_file["Importance_color"]["default"]
        else:
            return self.rule_file["Importance_color"][result.group()[1]]

    def search_meta_data(self, path):
        linecache.clearcache()
        first_line = linecache.getline(path, 1)
        if "#" == first_line[0]:
            metadata_list = first_line[1:].split(" ")[:len(self.rule_file["Meta_data"].keys())]
            display_metadata_list = []
            for i, metadata in enumerate(metadata_list):
                if metadata != "":
                    display_metadata_list.append(":".join([self.rule_file["Meta_data"][str(i+1)], metadata]))
            return display_metadata_list
        else:
            return [""]

    def sort_todo(self, paths, method):
        if method == "importance":
            return self.sort_importance(paths)
        elif method == "limit":
            return self.sort_todo_limit(paths)

    def sort_importance(self, paths):
        path_dicts = []
        for path in paths:
            path_dict = {}
            file_name = path.split("\\")[-1].split(".")[0]
            result = self.judge_importance(file_name)
            if result is None:
                path_dict["importance"] = "z"
            else:
                path_dict["importance"] = result.group()[1]
            path_dict["path"] = path
            path_dicts.append(path_dict)

        sorted_path_dicts = sorted(path_dicts, key=lambda x: x["importance"])
        sorted_paths = [sorted_path_dict["path"] for sorted_path_dict in sorted_path_dicts]
        return sorted_paths

    def sort_todo_limit(self, paths):
        path_dicts = []
        for path in paths:
            path_dict = {}
            first_metadata = self.search_meta_data(path)[0]
            if self.rule_file["Meta_data"]["1"] in first_metadata:
                path_dict["metadata_todo_limit"] = first_metadata.split(":")[-1]
            else:
                path_dict["metadata_todo_limit"] = "9999/12/31"
            path_dict["path"] = path
            path_dicts.append(path_dict)

        sorted_path_dicts = sorted(path_dicts, key=lambda x: x["metadata_todo_limit"])
        sorted_paths = [sorted_path_dict["path"] for sorted_path_dict in sorted_path_dicts]
        return sorted_paths

    def judge_importance(self, file_name):
        pattern = r"\[[{0}]\]".format(
            "|".join(
                [key.upper() for key in self.rule_file["Importance_color"].keys()]
            )
        )
        re_pattern = re.compile(pattern)
        result = re_pattern.search(file_name)
        return result

    def get_dir_name_keys(self):
        return self.dir_name_keys