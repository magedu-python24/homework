# 实现cat命令（支持查看内容和-n参数功能即可）
import argparse

parser = argparse.ArgumentParser(prog='cat',
                                 description='concatenate file(s), or standard input, to standard output.',
                                 add_help=False
                                 )
parser.add_argument('file',
                    nargs='?',
                    help='files name'
                    )
parser.add_argument('-n', '--number',
                    action='store_true',
                    dest='num',
                    help='number all output lines'
                    )

args = parser.parse_args()

def show_cat(file:str, num=False):
    if file:
        with open(file, encoding='utf-8') as f:
            for n, line in enumerate(f, 1):
                if num:
                    print(n, line, end='')
                else:
                    print(line, end='')
    else:
        print(input('<<<<'))

if __name__ == '__main__':
    show_cat(args.file, args.num)