from os import path
from datetime import datetime


def log(*args):
    main_dir = path.dirname(path.dirname(path.abspath(__file__)))
    file = open(f'{main_dir}/log.txt', 'a')
    msg = f'[{datetime.now()}] {" ".join(args)}\n'
    file.write(msg)
