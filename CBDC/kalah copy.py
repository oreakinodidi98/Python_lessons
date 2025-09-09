"""
A Kalah game simulator that:
- Reads game setup and moves from a file
- Validates file format and rules
- Plays out the game step by step
- Prints final scores or error messages exactly as specified
"""

# Import to read the file name from the command line and print errors
import sys


# Error handling: print error and stop program
def error(message):
    """Print error and stop program."""
    print(f"kalah: error: {message}", file=sys.stderr)
    sys.exit(1)

# Parsing Function: header and body parsing
def read_header(line):
    """Read and validate header: m houses per player, n seeds per house."""
    parts = line.split()
    if len(parts) != 2:
        # Check for exactly 2 numbers
        error("expected two values in header line")
    try:
        m = int(parts[0])
        n = int(parts[1])
    except ValueError:
        # check for valid integers
        error("invalid value in header line")
    if m <= 0 or n <= 0:
        # check for positive values
        error("invalid value in header line")
    # return to build game
    return m, n

def read_move(line, m):
    """Read and validate a move: must be between 1 and m (house you want to play). Every move line has one number"""
    parts = line.split()
    if len(parts) != 1:
        # Expected one value in body line
        error("expected one value in body line")
    try:
        move = int(parts[0])
        # get house number
    except ValueError:
        # check for valid integers
        error("invalid value in body line")
    if move < 1 or move > m:
        # check for valid house number between 1 and m
        error("invalid value in body line")
    # return valid move
    return move

# Game Logic Functions
def game_finished(p1_houses, p2_houses):
    """Return True if either side of houses is empty."""
    # Check if either player's houses are empty
    return all(h == 0 for h in p1_houses) or all(h == 0 for h in p2_houses)

def show_winner(p1_store, p2_store):
    """Print the winner result."""
    if p1_store > p2_store:
        print(f"1 {p1_store} {p2_store}")
        # If Player 1 has more, print 1 score1 score2
    elif p2_store > p1_store:
        print(f"2 {p1_store} {p2_store}")
        # If Player 2 has more, print 2 score1 score2
    else:
        print(f"0 {p1_store} {p2_store}")
        # If it's a tie, print 0 score1 score2


def play_move(p1_houses, p2_houses, p1_store, p2_store, current_player, chosen_house, m):
    """
    One full turn of Kalah:
    - Pick seeds from chosen house
    - Sow them around the board
    - Apply capture and extra turn rules
    Returns updated board and next player.
    """

    # Choose correct side: check if Player 1 or Player 2 is playing
    if current_player == 1:
        houses = p1_houses
        opponent_houses = p2_houses
        my_store = p1_store
        opponent_store = p2_store
    else:
        houses = p2_houses
        opponent_houses = p1_houses
        my_store = p2_store
        opponent_store = p1_store

    # code to pick a house and the number of seeds from that house
    idx = chosen_house - 1  # Convert to 0-index
    if houses[idx] == 0:
        error("invalid move house is empty")

    seeds = houses[idx]
    houses[idx] = 0  # Empty chosen house
    position = ("house", idx, "self")  # Start from this house

    # code to sprinkle seeds, go to each house one step at a time
    while seeds > 0:
        # Move to the next spot in the sowing path
        position = next_position(position, current_player, m)
        if position == ("store", "opponent"):  # Skip opponent's store
            position = next_position(position, current_player, m)

        # Place a seed
        if position[0] == "house":
            if position[1] < m:
                if position[2] == "self":
                    houses[position[1]] += 1
                else:
                    opponent_houses[position[1]] += 1
        elif position == ("store", "self"):
            my_store += 1
        seeds -= 1

    # After sowing, check last position for rules
    extra_turn = False
    if position == ("store", "self"):
        # Landed in own store -> extra turn
        extra_turn = True
    elif position[0] == "house" and position[2] == "self":
        # Landed in own house
        last_idx = position[1]
        if houses[last_idx] == 1:  # It was empty before placing
            opposite_idx = m - 1 - last_idx
            captured = opponent_houses[opposite_idx]
            if captured > 0:
                # Capture seeds
                my_store += captured + houses[last_idx]
                houses[last_idx] = 0
                opponent_houses[opposite_idx] = 0

    # Update stores back to original variables
    if current_player == 1:
        p1_store, p2_store = my_store, opponent_store
    else:
        p2_store, p1_store = my_store, opponent_store

    # Switch turn if no extra turn
    if not extra_turn:
        current_player = 2 if current_player == 1 else 1

    return p1_houses, p2_houses, p1_store, p2_store, current_player


def next_position(position, player, m):
    """
    Given the current position, find the next position for sowing.
    Positions are represented as:
    - ("house", index, "self" or "opp")
    - ("store", "self") or ("store", "opponent")
    """
    if position[0] == "house":
        idx = position[1]
        side = position[2]
        if side == "self":
            if player == 1:
                # Player 1: move left → right across own row
                if idx < m - 1:
                    return ("house", idx + 1, "self")
                else:
                    # After last house, go to own store
                    return ("store", "self")
            else:
                # Player 2: move right → left across own row
                if idx > 0:
                    return ("house", idx - 1, "self")
                else:
                    return ("store", "self")

        else:  # opponent side
            if player == 1:
                # P1 is sowing across opponent row (P2), right → left
                if idx > 0:
                    return ("house", idx - 1, "opp")
                else:
                    return ("store", "opponent")
            else:
                # P2 is sowing across opponent row (P1), left → right
                if idx < m - 1:
                    return ("house", idx + 1, "opp")
                else:
                    return ("store", "opponent")

    elif position == ("store", "self"):
        # After own store, jump to opponent houses
        if player == 1:
            return ("house", m - 1, "opp")  # start at P2 h(m)
        else:
            return ("house", 0, "opp")      # start at P1 h1

    elif position == ("store", "opponent"):
        # After opponent store, back to your houses
        if player == 1:
            return ("house", 0, "self")     # start again at P1 h1
        else:
            return ("house", m - 1, "self") # start again at P2 h(m)
    #         # If not at end of your houses, go to next house
    #         if idx < m - 1:
    #             return ("house", idx + 1, "self")
    #         else:
    #             # After last house, go to own store
    #             return ("store", "self")
    #     else:  # opponent side
    #         if idx > 0:
    #             return ("house", idx - 1, "opp")
    #         else:
    #             # After first opponent house, go to opponent store
    #             return ("store", "opponent")
    # elif position == ("store", "self"):
    #     # After your store, start opponent houses (rightmost first)
    #     return ("house", m - 1, "opp")
    # elif position == ("store", "opponent"):
    #     # After opponent store, start your houses (leftmost first)
    #     return ("house", 0, "self")

# main program
def main():
    #  main code logic here
    try:
        # Check for one file name
        if len(sys.argv) == 1:
            error("no input file")
        if len(sys.argv) > 2:
            error("too many arguments")

        filename = sys.argv[1]

        # open file
        try:
            with open(filename, "r") as file:
                lines = [line.strip() for line in file if line.strip()]
        except OSError:
            error("could not open file")

        # Get the first line (header)
        if not lines:
            error("expected two values in header line")

        m, n = read_header(lines[0])  # houses per player, seeds per house

        # Set up the board
        p1_houses = [n] * m
        p2_houses = [n] * m
        p1_store = 0
        p2_store = 0
        current_player = 1

        # Get the moves (rest of the file)
        moves = [read_move(line, m) for line in lines[1:]]

        # Play each move
        for chosen_house in moves:
            (p1_houses, p2_houses, p1_store, p2_store, current_player) = \
                play_move(p1_houses, p2_houses, p1_store, p2_store, current_player, chosen_house, m)

            if game_finished(p1_houses, p2_houses):
                # Collect seeds
                p1_store += sum(p1_houses)
                p2_store += sum(p2_houses)
                p1_houses = [0] * m
                p2_houses = [0] * m
                show_winner(p1_store, p2_store)
                return

        # If we ran out of moves but game not over
        error("insufficient moves")

    except SystemExit:
        # End when error() is called
        pass

if __name__ == "__main__":
    main()