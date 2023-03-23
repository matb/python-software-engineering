def towers_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    towers_of_hanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from", source, "to", destination)
    towers_of_hanoi(n-1, auxiliary, destination, source)


def main() -> None:
    towers_of_hanoi(3, 'A', 'C', 'B')


if __name__ == '__main__':
    main()
