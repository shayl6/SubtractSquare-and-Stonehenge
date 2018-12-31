"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
from game_state import GameState

# TODO: Adjust the type annotation as needed.


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def recursive_minimax_strategy(game: Any) -> Any:
    """
    Return a move that minimizes the possible loss for a player recursively.
    """
    state = game.current_state
    list_score = [help_recu_min(game, state.make_move(c)) * -1
                  for c in state.get_possible_moves()]
    highest_score = max(list_score)
    move = list_score.index(highest_score)
    return game.current_state.get_possible_moves()[move]


def help_recu_min(game: Any, state: GameState)-> int:
    """
    Return the highest guaranteed score for the state.
    """
    old_state = game.current_state
    if game.is_over(state):
        game.current_state = state
        if game.is_winner(state.get_current_player_name()):
            game.current_state = old_state
            return state.WIN
        elif game.is_winner('p1') or game.is_winner('p2'):
            game.current_state = old_state
            return state.LOSE
        game.current_state = old_state
        return state.DRAW
    else:
        new_state = [state.make_move(c) for c in state.get_possible_moves()]
        return max([help_recu_min(game, s) * -1 for s in new_state])


class Equip:
    """
    A Equip that containers information like state, score and children.
    """
    state: GameState
    score: int
    children: list

    def __init__(self, state: GameState, score: int = None,
                 children: list = None):
        """
        Create a new Equip self which has state, score and children.
        """
        self.state = state
        self.score = score
        self.children = children.copy() if children else []


def iterative_minimax_strategy(game: Any) -> Any:
    """
    Return a move that minimizes the possible loss for a player iteratively.
    """
    old_state = game.current_state
    start = Equip(game.current_state)
    process = [start]
    while process:
        deal = process.pop()
        if deal.children:
            deal.score = max([s.score * -1 for s in deal.children])
        elif game.is_over(deal.state):
            game.current_state = deal.state
            if game.is_winner(deal.state.get_current_player_name()):
                game.current_state = old_state
                deal.score = deal.state.WIN
            elif (not game.is_winner('p1')) and (not game.is_winner('p2')):
                game.current_state = old_state
                deal.score = deal.state.DRAW
            else:
                game.current_state = old_state
                deal.score = deal.state.LOSE
        else:
            new_state = [Equip(deal.state.make_move(c))
                         for c in deal.state.get_possible_moves()]
            process.append(deal)
            for a in new_state:
                deal.children.append(a)
                process.append(a)
    choies = [c.score * -1 for c in start.children]
    move = choies.index(max(choies))
    return game.current_state.get_possible_moves()[move]


# TODO: Implement a recursive version of the minimax strategy.

# TODO: Implement an iterative version of the minimax strategy.

if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")

    # game = SubtractSquareGame(True)
    # move_chosen = recursive_minimax_strategy(game)
    # print(move_chosen)
