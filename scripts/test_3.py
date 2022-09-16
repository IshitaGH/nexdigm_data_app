#!/usr/bin/python3

#dummy test to demonstrate nesting

import sys
sys.path.append('/Users/IshitaGhosh/Desktop/nexdigm/nexdigm_data_app/')

from table.models import Post


def test_3():
    current_entry.neg = -current_entry.square
    current_entry.save()

def main():
    test_3()

if __name__ == "__main__":
    main()