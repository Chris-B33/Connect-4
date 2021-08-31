def print_board(mtx):
    for r in mtx:
        print("      |", " ".join(r), "|")
    print("      |---------------|")
    print("      | 1 2 3 4 5 6 7 |")


class Connect4:

    def __init__(self):

        self.player1_turn = True
        self.grid = [
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"]
        ]

    def reset_grid(self):

        self.grid = [
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"]
        ]

    def check_win(self, mtx):

        for y in range(5, 0, -1):
            for x in range(7):

                # Make sure tile isn't empty
                tile = mtx[y][x]
                if tile == "-":
                    continue

                # Check cols
                if y - 3 > 0:
                    for i in range(4):
                        if not mtx[y - i][x] == tile:
                            break
                    else:
                        return 1 if self.player1_turn else 2

                # Check rows
                if x + 3 < len(self.grid[0]):
                    for i in range(4):
                        if not mtx[y][x + i] == tile:
                            break
                    else:
                        return 1 if self.player1_turn else 2

                # Check diagonal up
                if x + 3 < len(self.grid[0]) and y - 3 > 0:
                    for i in range(4):
                        if not mtx[y - i][x + i] == tile:
                            break
                    else:
                        return 1 if self.player1_turn else 2

                # Check diagonals down
                if x + 3 < len(self.grid[0]) and y + 3 < len(self.grid):
                    for i in range(4):
                        print(y+i, x+i)
                        if not mtx[y + i][x + i] == tile:
                            break
                    else:
                        return 1 if self.player1_turn else 2
        return 0

    def start(self):

        while True:
            # Take input
            print_board(self.grid)
            col = int(input(f"What column will Player {1 if self.player1_turn else 2} place in?: ")) - 1
            print("\n")

            # Place piece
            for row in range(len(self.grid) - 1, -1, -1):
                if self.grid[row][col] == "-":
                    self.grid[row][col] = "R" if self.player1_turn else "B"
                    break

            else:
                print("Can't place there! Choose again.")
                continue

            # Check win conditions
            con = self.check_win(self.grid)
            if con != 0:
                print_board(self.grid)
                print(f"        Player {con} wins!")
                break

            # Repeat
            self.player1_turn = False if self.player1_turn else True
        return 1 if self.player1_turn else 2


game = Connect4()
score = [0, 0]

while True:
    game.reset_grid()
    win = game.start()
    score[win - 1] += 1

    print(str(score[0]), "|", str(score[1]))
    play = input("Play again? (Y/N): ")
    if play.lower() == "y":
        continue
    else:
        print("Okay, fuck you pal.")
        break
