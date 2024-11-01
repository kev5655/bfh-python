#!/usr/bin/python3

# to be able to access to the command line parameters
import sys

# to be able to specify type annotations and static type checker mypy
from typing import List, Any, Set, Dict, Tuple, Optional


def append(file_name_1: str, file_name_2: str, file_name_output: str) -> None:
    """
    Appends two files into a third one. Copy the first file in the third one then
    copy the second file to the third one (append).
    :param file_name_1 : name of the first input file
    :param file_name_2 : name of the second input file
    :param file_name_ouput : name of the resulting file
    """

    f1 = open(file_name_1, "r")
    f2 = open(file_name_2, "r")
    f3 = open(file_name_output, "w")

    f3.write(f1.read())
    f3.write(f2.read())

    f1.close()
    f2.close()
    f3.close()
    
    
if __name__ == "__main__":
    """
    argv[0] is the command 
    argv[1] is the first parameter
    argv[2] is the first parameter
    ...
    """
    append(sys.argv[1], sys.argv[2], sys.argv[3]) 
