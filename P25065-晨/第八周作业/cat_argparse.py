import argparse

parser = argparse.ArgumentParser(prog='cat', description='Concatenate FILE(s) to standard output.', add_help=True)
parser.add_argument('file', nargs='?', help='file name')
parser.add_argument('-n', dest='num', action='store_true', help='number all output lines')
args = parser.parse_args()

def show_file(file:str, number=False):
    with open(file) as f:
        c = 0
        for line in f:
            if line == '\n':
                continue
            if number:
                c += 1
                yield c, line.rstrip('\n')
            else:
                yield line.rstrip('\n')

for x in show_file(args.file, args.num):
    print(x)
