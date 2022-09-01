#!/usr/bin/python3

global add

def test_1(num1, num2):
    add = num1 + num2
    num1 = add
    print(f"running test_1: {num1}, {num2}\n")
    return add

def main():
    return test_1(num1, num2)

if __name__ == "__main__":
    main()