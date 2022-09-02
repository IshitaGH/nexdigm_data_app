#!/usr/bin/python3

import sys
sys.path.append('/Users/IshitaGhosh/Desktop/nexdigm/nexdigm_data_app/')

# import django #might have to delete these two lines later
# django.setup()

from table.models import Post


def test_3():
    current_entry.neg = -current_entry.square
    current_entry.save()
    # print(f"running test_3: {current_entry.neg}\n")

def main():
    test_3()

if __name__ == "__main__":
    main()