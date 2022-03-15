def demo_zip():
    for a, b in zip(range(5, 10), range(10, 20, 2)):
        print(a, b)


def demo_map():
    print(pow(2, 3))
    for i in map(pow, [2, 3, 4], [7, 5, 3]):
        print(i)


def main():
    # demo_zip()
    demo_map()


if __name__ == "__main__":
    main()
