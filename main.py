from grid import Grid


def main():
    w, h = input("Enter board dimensions (width,height): ").split(",")
    grid = Grid(int(w), int(h))

    while not grid.is_game_over():
        grid.draw()
        print("Enter coordinates (x,y) to reveal, or 'f' to flag")
        choice = input("> ").split(",")
        if choice == ["f"]:
            x, y = input("Flag coordinates (x,y): ").split(",")
            grid.flag(int(x), int(y))
        else:
            x, y = choice
            grid.guess(int(x), int(y))

        if grid.all_bombs_flagged():
            grid.draw()
            print("You found all the bombs!")
            grid.end_game()

    print(f"Game over. Score: {grid.get_score()}")


if __name__ == "__main__":
    main()
