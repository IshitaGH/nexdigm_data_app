#!/usr/bin/python3

def test_2(num):
    num1 = num*num
    print(f"running test_2: {num1}\n")
    return num1

def main():
    test_2(num1)
    test_2(num2)

if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     print(test_2(2))