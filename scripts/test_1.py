#!/usr/bin/python3

import sys
sys.path.append('/Users/IshitaGhosh/Desktop/nexdigm/nexdigm_data_app/')

# import django #might have to delete these two lines later
# django.setup()

from table.models import Post


def test_1():
    current_entry.add = current_entry.num1 + current_entry.num2
    current_entry.save()
    # print(f"running test_1: {current_entry.add}\n")

def main():
    test_1()

if __name__ == "__main__":
    main()