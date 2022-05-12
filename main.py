import itertools
from colorama import Fore, Style, init

init()


def win():
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Horizontal win
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally (-)")
            return True

    # Diagonal Win
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/)")
        return True

    diags = []
    for ix in range(len(game)):  # ix is index
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (\) ")
        return True

    # Vertical win
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is the winner vertically (|) ")
            return True

        return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print(Fore.RED + 'This position has been already played in! Choose another!' + Style.RESET_ALL)
            return game_map, False
        print("   " + "  ".join([str(i) for i in range(len(game_map))]))  # old is: print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
            print(count, colored_row)
        return game_map, True

    # error handling
    except IndexError as e:
        print(Fore.RED + 'Error: make sure you inout column as 0 1 or 2,', e + Style.RESET_ALL)
        return game_map, False

    except Exception as e:
        print(Fore.RED + 'Something went very wrong!', e + Style.RESET_ALL)
        return game_map, False


play = True
players = [1, 2]
while play:
    while True:
        check_game_size = input("What size do you want for your xo game? ex: 2, 3, 4: ")
        # take only numbers greater than 1
        if check_game_size.isdigit() and int(check_game_size) > 1:
            game_size = int(check_game_size)
            break
        else:
            print(Fore.YELLOW + 'Please enter a number greater than 1!' + Style.RESET_ALL)

    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        if current_player == 1:
            current_player_colored = Fore.GREEN + 'X' + Style.RESET_ALL
        elif current_player == 2:
            current_player_colored = Fore.MAGENTA + 'O' + Style.RESET_ALL
        print(f"Current Player: {current_player_colored}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? "))
            row_choice = int(input("What row do you want to play? "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win():
            game_won = True
            again = input("The game is over, would you like to play again? (y/n): ")
            if again.lower() == "y":
                print("YES SIR!, just let me restart the game for you.")
            elif again.lower() == "n":
                print("Game closed")
                play = False
            else:
                print("Not a valid answer, so...see you later.")
                play = False
