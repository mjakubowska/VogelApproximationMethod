import sys
from checkData.Loader import Loader
from alg.Vogl import Vogl


def main():
    if len(sys.argv) > 1:
        filePath = sys.argv[1]
        print(filePath)
    loader = Loader()
    loader.load_data("sample.txt")
    vogl = Vogl(loader)
    vogl.print_matrix()


if __name__ == "__main__":
    main()
