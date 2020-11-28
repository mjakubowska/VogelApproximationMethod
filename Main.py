import sys
from checkData.Loader import Loader
from alg.Vogl import Vogl, find_2min_diff
from model.Contract import Contract


def main():
    if len(sys.argv) > 1:
        filePath = sys.argv[1]
        print(filePath)
    loader = Loader()
    loader.load_data("sample.txt")
    vogl = Vogl(loader)
    print(vogl.find_max_mins())


if __name__ == "__main__":
    main()
