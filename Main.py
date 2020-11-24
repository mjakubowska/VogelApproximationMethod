import sys
import checkData.FileErrors as fe


def main():
    if len(sys.argv) > 1:
        filePath = sys.argv[1]
        print(filePath)
    fe.load_data("sample.txt")


if __name__ == "__main__":
    main()
