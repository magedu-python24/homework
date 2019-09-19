import argparse
from pathlib import Path

parser = argparse.ArgumentParser(prog='cat',add_help=True,description='concatenate files and print on the standard output')
parser.add_argument('file',help='file help')
parser.add_argument('-n',action='store_true',help='number all output lines')

if __name__ == '__main__':
    args = parser.parse_args()
    p = Path(args.file)
    if p.is_file():
        with p.open('r') as f:
            for i,line in enumerate(f.readlines(),1):
                print('{}  {}'.format(i,line) if args.n else line,end='')
    else:
        print('file does not exist')
