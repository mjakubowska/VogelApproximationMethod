import sys
from checkData.Loader import Loader
from transportationProblem.Vogel import Vogel


def main():
    if len(sys.argv) < 1:
        print(f"brak argumentu wywołania")
        sys.exit(-1)
    for i in range(1, len(sys.argv)):
        try:
            file_input = sys.argv[i]
        except IndexError:
            print(f"nie można otworzyć pliku {file_input}")
            sys.exit(1)
        try:
            file = open(file_input, 'r')
            loader = Loader(file_input + '_result')
            loader.load_data(file)
            vogel = Vogel(loader)
            vogel.create_configuration()
            file_name = file_input[:-4] + '-result.txt'
            vogel.solution.write_to_file(file_name)
        except OSError:
            print(f"Błędny argument wywołania, nie można wczytać pliku {sys.argv[i]}")


if __name__ == "__main__":
    main()
