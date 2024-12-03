def read_input_lines(filename: str) -> list[str]:
    with open(filename, 'r') as file:
          return file.read().splitlines()


def read_input_as_string(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()