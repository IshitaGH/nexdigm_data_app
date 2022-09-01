#!/usr/bin/python3

def test_3(num):
    num1 = -num
    print(f"running test_3: {num1}\n")
    return num1

def main():
    test_3(num1)
    test_3(num2)

if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     print(test_3(4))