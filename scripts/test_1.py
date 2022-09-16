#!/usr/bin/python3

#dummy test to demonstrate nesting
import sys
sys.path.append('/Users/IshitaGhosh/Desktop/nexdigm/nexdigm_data_app/')


from table.models import Post


def test_1():
    current_entry.add = current_entry.num1 + current_entry.num2
    current_entry.save()

def main():
    test_1()

if __name__ == "__main__":
    main()