import factorial
import sys

def main():
    n = int(input())
    print(factorial.factorial(n))

if __name__ == '__main__':
    sys.exit(main() or 0)
