import re
import os
import sys
import json

files = []

def get_help():
    help = \
    """
    LINES OF CODE COUNT

    Usage:
        python3 lines_of_code <path>
        python3 lines_of_code -h | --help

    Options:
        -h --help           Show this screen.
        -a --all            View supported languages

    Examples:
        python3 lines_of_code ~/main/assignments/
        python3 lines_of_code ~/main/assignments/random_cpp_file.cpp
    """
    print(help)

def get_languages():
    print("Languages supported : ")
    json_data = open('langs.json').read()
    language_packs = json.loads(json_data)
    i = 1
    for pack in language_packs:
        print(i,"\b. ",language_packs[pack]['language']," ",language_packs[pack]['extension'])
        i+=1

def read_args():
    """ Parse command-line arguments """
    number_of_arguments = len(sys.argv)

    if(number_of_arguments != 2):
        print("***INVALID NUMBER OF ARGUMENTS***")
        print("Run \"python3 lines_of_code -h\" for help")
        sys.exit(0)
    else:
        pass

    if sys.argv[1] in ['--help','-h']:
        get_help()
    elif sys.argv[1] in ['--all','-a']:
        get_languages()
    elif not (os.path.isdir(sys.argv[1]) or os.path.isfile(sys.argv[1])):
        print("***PATH DOES NOT EXIST***\nPass a valid path")
        sys.exit(0)
    else:
        loc = LinesOfCode(sys.argv[1])
        loc.filter_files()
        loc.count_all()


class LinesOfCode():
    """
    Calculate the number of lines of code in a path.
    lines_of_code = total_number_of_lines - ( multiline comments + comment lines + blank lines )
    """

    ALLOWED_EXTENSIONS = []
    files = []
    files_with_extensions = []
    language_packs = []

    def __init__(self, input_path):

        self.collect_extensions()

        path = os.path.abspath(input_path)

        if(os.path.isdir(path)):
            for root, directories, filenames in os.walk(path):
                for fname in filenames:
                    self.files.append((os.path.join(root,fname)))
        elif(os.path.isfile(path)):
            self.files.append(path)
        print("Found ", len(self.files), " file(s)")

    def filter_files(self):
        self.files = list(filter(self.is_suitable_extension,self.files))

        if(len(self.files) == 0):
            print("No suitable files found")
            sys.exit()
        elif(len(self.files) == 1):
            print("Found ", 1, " suitable file")
        else:
            print("Found ", len(self.files), " suitable files" )
        self.get_files_extensions()


    def is_suitable_extension(self, filename):
        basename = os.path.basename(filename)
        try:
            extension = basename.split('.')[-1]
            if(extension in self.ALLOWED_EXTENSIONS):
                return True
        except IndexError:
            return False

    def count_all(self):
        for file in self.files:
            self.count_loc(file)

    def count_loc(self, file):

        basename = os.path.basename(file)
        extension = basename.split('.')[-1]
        lan_pack = self.language_packs[extension]
        # print(lan_pack)

        content = open(file,'r').read()
        lines = content.split('\n')
        single_line_comments = 0
        blank_lines = 0

        for line in lines:

            if(lan_pack['single_comments']):
                if(line.strip().startswith(lan_pack['single_comments_trigger'])):
                    single_line_comments += 1;

            if(line.strip()==''):
                # print("blnk found")
                blank_lines += 1

        # if(lan_pack['multi_comments']):
        #     start = content.find(lan_pack['multi_comment_start'])
        #     end = content.find(lan_pack['multi_comment_end'])
        #     print(start)
        #     print(end)

        # print(lan_pack['multi_comment_start'])
        multi_starts = list(re.finditer(lan_pack['multi_comment_start'], content))

        multi_ends = list(re.finditer(lan_pack['multi_comment_end'], content))
        # print(multi_ends)
        a = []
        b = []
        for i in multi_starts:
            a.append(i.start())
        for i in multi_ends:
            b.append(i.start())
        # print(a)
        # print(b)
        if(a==b):
            similar_comments = True
        else:
            similar_comments = False
        effective_comment_lines = 0

        while(len(b)>0):
            if(similar_comments):a = list(filter(lambda x:x>=b[0], a))
            comment_start = a.pop(0)
            b = list(filter(lambda x:x>comment_start, b))
            comment_end = b.pop(0)
            # print("st = ", comment_start, " en = ", comment_end)

            comment_segment = content[comment_start:comment_end+1]
            comment_lines = comment_segment.split('\n')
            total_comment_lines = len(comment_lines)
            # print("commentlines :",comment_lines)

            blank_comment_lines = 0
            singles = 0
            for line in comment_lines:
                if(lan_pack['single_comments']):
                    if(line.strip().startswith(lan_pack['single_comments_trigger'])):
                        singles += 1;
                if(line.strip()==''):
                    blank_comment_lines += 1

            effective_comment_lines += len(comment_lines) - blank_comment_lines - singles

        # print("effective comment lines = ",effective_comment_lines)
        # # print(content.count('//'))
        # print("Multi start occurences = ", a)
        # print("Multi end occurences = ", b)

        final_loc = len(lines) - single_line_comments - blank_lines - effective_comment_lines

        print()
        print("Filename : ", file)
        print("Total lines = ", len(lines))
        print("Blank lines = ", blank_lines)
        print("Single line comment lines = ", single_line_comments)
        print("Effective multiple line comments = ", effective_comment_lines)
        print("Lines of Code = ", final_loc)
        print()


    def collect_extensions(self):
        json_data = open('langs.json').read()
        self.language_packs = json.loads(json_data)
        self.ALLOWED_EXTENSIONS = list(self.language_packs.keys())
        # print(self.ALLOWED_EXTENSIONS)

    def get_files_extensions(self):
        extensions = []
        for f in self.files:
            basename = os.path.basename(f)
            extensions.append(basename.split('.')[-1])
        self.files_with_extensions = list(zip(self.files, extensions))
        # print(self.files_with_extensions)


read_args();
