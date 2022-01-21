import sys
import pygments
from pygments.lexers import PythonLexer

def generate_scale(file_name):
    scale = []
    return scale

def main(input_file, output_file):
    temp_code = "from pygments.lexers import PythonLexer"
    pl = PythonLexer()
    yoyo = pygments.lex(temp_code, pl)
    for elem in yoyo:
        print(elem)

def print_help():
    print("""Usage: pybeatcoder [INPUT FILE] [OUTPUT FILE]""")

if __name__ == '__main__':
    if len(sys.argv)==2:
        if sys.argv[1] in ["-h", "--help"]:
            print_help()
    else :
        main(sys.argv[1], sys.argv[2])