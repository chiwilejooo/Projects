def fibonachi(n):
    if n <= 1:
        return 1
    return fibonachi(n-1) + fibonachi(n-2)


def main():
    for a in range(10):
        print(fibonachi(a))


if __name__ == '__main__':
    main()