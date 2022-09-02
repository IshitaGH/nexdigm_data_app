#!/usr/bin/python3

import sys
sys.path.append('/Users/IshitaGhosh/Desktop/nexdigm/nexdigm_data_app/')

# import django #might have to delete these two lines later
# django.setup()

from table.models import Post

def test_2():
    current_entry.square = current_entry.add * current_entry.add
    current_entry.save()
    # print(f"running test_2: {current_entry.square}\n")

def main():
    test_2()

if __name__ == "__main__":
    main()