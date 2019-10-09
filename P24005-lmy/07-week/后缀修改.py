# 写一个脚本实现找到/tmp目录及其子目录下的以.htm结尾的文件，把其后缀名改为.html
from pathlib import Path

p = Path('Temp')

def fn(p):
    for x in p.iterdir():
        if x.is_dir():
            p = p.joinpath(x.name)
            fn(p)
            p = p.parent
        else:
            if x.match('*.tmp'):
                x.rename(x.with_suffix('.html'))

fn(p)

