#!/usr/bin/python3

import runpy
import sys
sys.path.append('/Users/IshitaGhosh/Desktop/nexdigm/nexdigm_data_app/')

import django
django.setup()

from table.models import Post

global_vars = {
    "current_entry": current_entry,
}

# global_vars["num1"] = 
def fn1():
    runpy.run_path(path_name=r"scripts/test_1.py", init_globals=global_vars, run_name='__main__')

def fn2():
    runpy.run_path(path_name=r"scripts/test_2.py", init_globals=global_vars, run_name='__main__')

def fn3():
    runpy.run_path(path_name=r"scripts/test_3.py", init_globals=global_vars, run_name='__main__')

def main():
    fn1()
    fn2()
    fn3()
    # print(global_vars.items())

if __name__ == '__main__':
    main()