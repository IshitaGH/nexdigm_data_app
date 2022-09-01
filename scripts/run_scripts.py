#!/usr/bin/python3

import runpy
from ../table/models.py import Post

global_vars = {
    "entry": Post.objects.last()
    "num1": entry.num1,
    "num2": entry.num2
}

# global_vars["num1"] = 
def fn1():
    runpy.run_path(path_name=r"test_1.py", init_globals=global_vars, run_name='test_1')

def fn2():
    runpy.run_path(path_name=r"test_2.py", init_globals=global_vars, run_name='__main__')

def fn3():
    runpy.run_path(path_name=r"test_3.py", init_globals=global_vars, run_name='__main__')

def main():
    fn1()
    fn2()
    fn3()
    print(global_vars.items())

if __name__ == '__main__':
    main()