from data.node import Node
from data.tube import Tube


# puzzles
def get_puzzle(puzzle_id: int):
    for puzzle in PUZZLES:
        if puzzle.num_id == puzzle_id:
            return puzzle
    return None


puzzle_id = 0


def add_puzzle(puz: Node):
    global puzzle_id
    puz.num_id = puzzle_id
    PUZZLES.append(puz)
    puzzle_id += 1

PUZZLES = []

# 1 - 10
# add_puzzle(Node([
#         Tube(['ORANGE', 'ORANGE']),
#         Tube(['ORANGE', 'ORANGE'])
#     ], 2, 2))

# add_puzzle(Node([
#         Tube(['ORANGE', 'ORANGE', 'BROWN', 'RED']),
#         Tube(['BEIGE', 'MINT_GREEN', 'MINT_GREEN', 'BROWN']),
#         Tube(['ORANGE', 'RED', 'MINT_GREEN', 'MINT_GREEN']),
#         Tube(['BEIGE', 'RED', 'RED', 'BEIGE']),
#         Tube(['BROWN', 'ORANGE', 'BEIGE', 'BROWN']),
#         Tube([]),
#         Tube([])
#     ], 7, 2))

# # todo: move this puzzle to like 50 when more get added
# add_puzzle(Node([
#         Tube(['MINT_GREEN', 'GRAY', 'ORANGE', 'YELLOW']),
#         Tube(['RED', 'PURPLE', 'GREEN', 'CYAN']),
#         Tube(['GREEN', 'PINK', 'MINT_GREEN', 'PURPLE']),
#         Tube(['YELLOW', 'PINK', 'RED', 'BROWN']),
#         Tube(['GREEN', 'VIOLET', 'BROWN', 'PURPLE']),
#         Tube(['GREEN', 'GRAY', 'PURPLE', 'YELLOW']),
#         Tube(['ORANGE', 'GRAY', 'CYAN', 'DARK_GREEN']),
#         Tube(['RED', 'DARK_GREEN', 'CYAN', 'PINK']),
#         Tube(['VIOLET', 'VIOLET', 'CYAN', 'MINT_GREEN']),
#         Tube(['DARK_GREEN', 'BROWN', 'PINK', 'ORANGE']),
#         Tube(['GRAY', 'MINT_GREEN', 'YELLOW', 'ORANGE']),
#         Tube(['RED', 'BROWN', 'DARK_GREEN', 'VIOLET']),
#         Tube([]),
#         Tube([])
#     ], 14, 2))

# offset bat dau tu 0
#level 1
add_puzzle(Node([
        Tube(['ORANGE', 'ORANGE', 'BLUE', 'BLUE']),
        Tube(['BLUE', 'BLUE', 'ORANGE', 'ORANGE']),
        Tube([])
    ], 3, 1))

#level 2
add_puzzle(Node([
        Tube(['ORANGE', 'BLUE', 'ORANGE', 'BLUE']),
        Tube(['BLUE', 'ORANGE', 'BLUE', 'ORANGE']),
        Tube([])
    ], 3, 1))

#level 3
add_puzzle(Node([
        Tube(['BLUE', 'RED', 'ORANGE', 'ORANGE']),
        Tube(['BLUE', 'RED', 'ORANGE', 'BLUE']),
        Tube(['RED', 'ORANGE', 'BLUE', 'RED']),
        Tube([]),
        Tube([])
    ], 5, 2))

#level 4
add_puzzle(Node([
        Tube(['ORANGE', 'RED', 'BLUE', 'ORANGE']),
        Tube(['ORANGE', 'ORANGE', 'RED', 'BLUE']),
        Tube(['RED', 'BLUE', 'RED', 'BLUE']),
        Tube([]),
        Tube([])
    ], 5, 2))

#level 5
add_puzzle(Node([
        Tube(['PINK', 'BLUE', 'CYAN', 'ORANGE']),
        Tube(['RED', 'ORANGE', 'RED', 'PINK']),
        Tube(['BLUE', 'RED', 'CYAN', 'CYAN']),
        Tube(['PINK', 'BLUE', 'ORANGE', 'CYAN']),
        Tube(['BLUE', 'RED', 'PINK', 'ORANGE']),
        Tube([]),
        Tube([])
    ], 5, 2))

#level 6
add_puzzle(Node([
        Tube(['CYAN', 'CYAN', 'PINK', 'BLUE']),
        Tube(['CYAN', 'RED', 'ORANGE', 'BLUE']),
        Tube(['BLUE', 'PINK', 'BLUE', 'ORANGE']),
        Tube(['PINK', 'RED', 'ORANGE', 'RED']),
        Tube(['PINK', 'RED', 'CYAN', 'ORANGE']),
        Tube([]),
        Tube([])
    ], 5, 2))



