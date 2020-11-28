import sys
from checkData.Loader import Loader
from transportationProblem.Vogl import Vogl, find_2min_diff
from model.Contract import Contract


def main():
    try:
        file_input = sys.argv[1]
    except IndexError:
        print("brak argumentu wywołania")
        sys.exit(1)
    try:
        file = open(file_input, 'r')
        loader = Loader()
        loader.load_data(file)
    except OSError as e:
        print(f"Błędny argument wywołania, nie można otworzyć pliku {sys.argv[1]}")
        sys.exit(2)
    # vogl = Vogl(loader)
    #print(vogl.find_max_mins())


if __name__ == "__main__":
    main()
