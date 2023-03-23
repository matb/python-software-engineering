class TowersOfHanoi:
    def __init__(self, n, left='A', center='B', right='C'):
        self.n = n
        self.left = left
        self.center = center
        self.right = right
        

    def solve(self):
        self.move_disks(self.n, self.left, self.right, self.center)

    def move_disks(self, n, left, right, center):
        if n == 1:
            print("Move disk 1 from", left, "to", right)
            return
        self.move_disks(n-1, left, center, right)
        print("Move disk", n, "from", left, "to", right)
        self.move_disks(n-1, center, right, left)


def main() -> None:
    game = TowersOfHanoi(3)
    game.solve()


if __name__ == '__main__':
    main()
