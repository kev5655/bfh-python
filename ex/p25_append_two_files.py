import sys
import os

# python ./ex/p25_append_two_files.py  ./ex/p4_even.py  ./ex/p5_circle_area.py  ./rsc/out_p4_and_p5.txt


def read_args() -> tuple[str, str, str]:
    _, f1, f2, f3 = sys.argv
    return (f1, f2, f3)


def check_is_file(f: str):
    if not os.path.isfile(f):
        print(f"file not exists: {f}")
        exit(0)


def folder_not_exists(file: str):
    if not os.path.isdir(os.path.dirname(file)):
        print(f"file has no valid folder {file}")
        exit(0)


def main():
    file1, file2, out_file = read_args()
    # print(readArgs())

    check_is_file(file1)
    check_is_file(file2)
    folder_not_exists(out_file)

    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            with open(out_file, "w") as out:
                out.write(f1.read() + f2.read())


if __name__ == '__main__':
    main()
