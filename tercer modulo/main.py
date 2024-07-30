def potencia(base, exp=False):
    if exp:
        results = base ** exp
    else:
        results = base ** 2
    return results


def main():
    print(potencia(8, ))


if __name__ == "__main__":
    main()