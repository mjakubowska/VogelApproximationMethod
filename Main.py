import sys
from checkData import FileErrors
import checkData.FileErrors as fe


def main():
    if len(sys.argv) > 1:
        filePath = sys.argv[1]
        print(filePath)
    fe.check_syntax("sample.txt")


if __name__ == "__main__":
    main()
