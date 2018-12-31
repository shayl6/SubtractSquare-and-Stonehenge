"""
An implementation of game and state for Stonehenge.
"""
from typing import Any
from game import Game
from game_state import GameState


class StonehengeGame(Game):
    """
    StonehengeGame to be played with two players.
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this StonehengeGame, using p1_starts to find
        who the first player is.
        """
        side = ''
        while not (side.isdigit() and 6 > int(side) > 0):
            side = input("Enter the side length of board:")
        side = int(side)
        self.current_state = StonehengeState(p1_starts, side)

    def get_instructions(self) -> str:
        """
        Return the instructions for this StonehengeGame.
        """
        return "Players take turns claiming cells. When a Player captures at " \
               "least half of the cells in a ley-line, then the player" \
               "captures that ley-line. The first player to capture at " \
               "least half of the ley-lines is the winner"

    def is_over(self, state: 'StonehengeState') -> bool:
        """
        Return whether or not this game is over at state.
        """
        p1 = 0
        p2 = 0
        for i in state.ley_line:
            if i == '1':
                p1 += 1
            elif i == '2':
                p2 += 1
        return (2 * p1 >= len(state.ley_line)
                or 2 * p2 >= len(state.ley_line) or
                state.get_possible_moves() == [])

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.
        """
        p1 = 0
        p2 = 0
        for i in self.current_state.ley_line:
            if i == '1':
                p1 += 1
            elif i == '2':
                p2 += 1
        if (p1 * 2) >= len(self.current_state.ley_line):
            return player == 'p1' and self.is_over(self.current_state)
        return player == 'p2' and self.is_over(self.current_state)

    def str_to_move(self, string: str) -> Any:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        """
        if string.isalpha() and string.isupper():
            return string
        return 1


class StonehengeState(GameState):
    """
        The state of a game at a certain point in time.

        WIN - score if player is in a winning position
        LOSE - score if player is in a losing position
        DRAW - score if player is in a tied position
        p1_turn - whether it is p1's turn or not
        """
    WIN: int = 1
    LOSE: int = -1
    DRAW: int = 0
    p1_turn: bool
    side_length = int
    lines: list
    ley_line: list

    def __init__(self, is_p1_turn: bool, side_length: int) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        >>> a = StonehengeState(True, 1)
        >>> a.lines == ['AB', 'C']
        True
        >>> a.ley_line == ['@'] * 6
        True
        """
        self.p1_turn = is_p1_turn
        self.side_length = side_length
        if side_length == 1:
            self.lines = ['AB', 'C']
        elif side_length == 2:
            self.lines = ['AB', 'CDE', 'FG']
        elif side_length == 3:
            self.lines = ['AB', 'CDE', 'FGHI', 'JKL']
        elif side_length == 4:
            self.lines = ['AB', 'CDE', 'FGHI', 'JKLMN', 'OPQR']
        elif side_length == 5:
            self.lines = ['AB', 'CDE', 'FGHI', 'JKLMN',
                          'OPQRST', 'UVWXY']
        self.ley_line = ['@'] * 3 * (side_length + 1)

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        if self.side_length == 1:
            r1 = '      {}   {}\n'
            r3 = '{}  {}  {}\n'
            r5 = '  {}  {}   {}\n'
            r7 = '        {}'
            tem = r1 + r3 + r5 + r7
            sol = tem.format(self.ley_line[2], self.ley_line[3],
                             self.ley_line[0], self.lines[0][0],
                             self.lines[0][1], self.ley_line[1],
                             self.lines[1][0], self.ley_line[5],
                             self.ley_line[4])
            return sol
        elif self.side_length == 2:
            r1 = ' {} {}\n'
            r2 = '{} {} {} {}\n'
            r3 = '{} {} {} {}\n'
            r4 = '{} {} {} {}\n'
            r5 = ' {} {}'
            tem = r1 + r2 + r3 + r4 + r5
            sol = tem.format(self.ley_line[3], self.ley_line[4],
                             self.ley_line[0], self.lines[0][0],
                             self.lines[0][1], self.ley_line[5],
                             self.ley_line[1], self.lines[1][0],
                             self.lines[1][1], self.lines[1][2],
                             self.ley_line[2], self.lines[2][0],
                             self.lines[2][1], self.ley_line[8],
                             self.ley_line[6], self.ley_line[7])
            return sol
        elif self.side_length == 3:
            r1 = ' {} {}\n'
            r2 = '{} {} {} {}\n'
            r3 = '{} {} {} {} {}\n'
            r4 = '{} {} {} {} {}\n'
            r5 = '{} {} {} {} {}\n'
            r6 = ' {} {} {}'
            tem = r1 + r2 + r3 + r4 + r5 + r6
            sol = tem.format(self.ley_line[4], self.ley_line[5],
                             self.ley_line[0], self.lines[0][0],
                             self.lines[0][1], self.ley_line[6],
                             self.ley_line[1], self.lines[1][0],
                             self.lines[1][1], self.lines[1][2],
                             self.ley_line[7], self.ley_line[2],
                             self.lines[2][0], self.lines[2][1],
                             self.lines[2][2], self.lines[2][3],
                             self.ley_line[3], self.lines[3][0],
                             self.lines[3][1], self.lines[3][2],
                             self.ley_line[11], self.ley_line[8],
                             self.ley_line[9], self.ley_line[10])
            return sol
        elif self.side_length == 4:
            r1 = ' {} {}\n'
            r2 = '{} {} {} {}\n'
            r3 = '{} {} {} {} {}\n'
            r4 = '{} {} {} {} {} {}\n'
            r5 = '{} {} {} {} {} {}\n'
            r6 = '{} {} {} {} {} {}\n'
            r7 = ' {} {} {} {}'
            tem = r1 + r2 + r3 + r4 + r5 + r6 + r7
            sol = tem.format(self.ley_line[5], self.ley_line[6],
                             self.ley_line[0], self.lines[0][0],
                             self.lines[0][1], self.ley_line[7],
                             self.ley_line[1], self.lines[1][0],
                             self.lines[1][1], self.lines[1][2],
                             self.ley_line[8], self.ley_line[2],
                             self.lines[2][0], self.lines[2][1],
                             self.lines[2][2], self.lines[2][3],
                             self.ley_line[9], self.ley_line[3],
                             self.lines[3][0], self.lines[3][1],
                             self.lines[3][2], self.lines[3][3],
                             self.lines[3][4], self.ley_line[4],
                             self.lines[4][0], self.lines[4][1],
                             self.lines[4][2], self.lines[4][3],
                             self.ley_line[14], self.ley_line[10],
                             self.ley_line[11], self.ley_line[12],
                             self.ley_line[13])
            return sol
        elif self.side_length == 5:
            r1 = ' {} {}\n'
            r2 = '{} {} {} {}\n'
            r3 = '{} {} {} {} {}\n'
            r4 = '{} {} {} {} {} {}\n'
            r5 = '{} {} {} {} {} {} {}\n'
            r6 = '{} {} {} {} {} {} {}\n'
            r7 = '{} {} {} {} {} {} {}\n'
            r8 = ' {} {} {} {} {}'
            tem = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8
            sol = tem.format(self.ley_line[6], self.ley_line[7],
                             self.ley_line[0], self.lines[0][0],
                             self.lines[0][1], self.ley_line[8],
                             self.ley_line[1], self.lines[1][0],
                             self.lines[1][1], self.lines[1][2],
                             self.ley_line[9], self.ley_line[2],
                             self.lines[2][0], self.lines[2][1],
                             self.lines[2][2], self.lines[2][3],
                             self.ley_line[10], self.ley_line[3],
                             self.lines[3][0], self.lines[3][1],
                             self.lines[3][2], self.lines[3][3],
                             self.lines[3][4], self.ley_line[11],
                             self.ley_line[4], self.lines[4][0],
                             self.lines[4][1], self.lines[4][2],
                             self.lines[4][3], self.lines[4][4],
                             self.lines[4][5], self.ley_line[5],
                             self.lines[5][0], self.lines[5][1],
                             self.lines[5][2], self.lines[5][3],
                             self.lines[5][4], self.ley_line[17],
                             self.ley_line[12], self.ley_line[13],
                             self.ley_line[14], self.ley_line[15],
                             self.ley_line[16])
            return sol
        return 'game'

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.

        >>> a = StonehengeState(True, 1)
        >>> a.get_possible_moves()
        ['A', 'B', 'C']
        """
        if self.state_over():
            return []
        result = []
        for line in self.lines:
            for point in line:
                if point != '1' and point != '2':
                    result.append(point)
        return result

    def get_current_player_name(self) -> str:
        """
        Return 'p1' if the current player is Player 1, and 'p2' if the current
        player is Player 2.

        >>> a = StonehengeState(True, 1)
        >>> a.get_current_player_name()
        'p1'
        """
        if self.p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move: Any) -> 'StonehengeState':
        """
        Return the StonehengeState that results from applying move
        to this StonehengeState.

        >>> a = StonehengeState(True, 1)
        >>> b = a.make_move('A')
        >>> b.lines == ['1B', 'C']
        True
        """
        new_state = StonehengeState(not self.p1_turn, self.side_length)
        new_state.lines = []
        new_state.ley_line = []
        for line in self.lines:
            nline = ''
            for point in line:
                if point != move:
                    nline += point
                elif self.p1_turn:
                    nline += '1'
                else:
                    nline += '2'
            new_state.lines.append(nline)
        new_state.ley_line = self.help_complete_ley_mark(new_state.lines)
        return new_state

    def help_complete_ley_mark(self, lines: list) -> list:
        """
        Return the ley-lines marker when the board is like lines.

        >>> a = StonehengeState(True, 1)
        >>> b = a.make_move('A')
        >>> a.help_complete_ley_mark(b.lines)
        ['1', '@', '1', '@', '1', '@']
        """
        complete = []
        complete = self.help_add_ley_mark(lines, 0)
        ley_right = lines[:]
        ley_right[-1] = ' ' + ley_right[-1]
        ley_rights = []
        for a in range(self.side_length + 1):
            rn = ''
            for l in ley_right:
                if a <= len(l) - 1:
                    rn += l[a]
            ley_rights.append(rn.strip())
        complete.extend(self.help_add_ley_mark(ley_rights, 1))
        ley_left = lines[:]
        for b in range(self.side_length + 1):
            ley_left[b] = ' ' * (self.side_length - 1 - b) + ley_left[b]
        ley_left[-1] += ' '
        ley_lefts = []
        for c in range(self.side_length + 1):
            ln = ''
            for n in ley_left:
                ln += n[c]
            ley_lefts.append(ln.strip())
        complete.extend(self.help_add_ley_mark(ley_lefts, 2))
        return complete

    def help_add_ley_mark(self, situation: list, num: int) -> list:
        """
        Return a list of ley-line markers at range num based on situation.

        >>> a = StonehengeState(True, 1)
        >>> b = a.make_move('A')
        >>> a.help_add_ley_mark(b.lines, 0)
        ['1', '@']
        """
        new_ley_mark = []
        for line in range(self.side_length + 1):
            p1 = 0
            p2 = 0
            for cell in situation[line]:
                if cell == '1':
                    p1 += 1
                elif cell == '2':
                    p2 += 1
            if self.ley_line[line + num * (self.side_length + 1)] == '1':
                new_ley_mark.append('1')
            elif self.ley_line[line + num * (self.side_length + 1)] == '2':
                new_ley_mark.append('2')
            elif (p1 * 2) >= len(situation[line].strip()):
                new_ley_mark.append('1')
            elif (p2 * 2) >= len(situation[line].strip()):
                new_ley_mark.append('2')
            else:
                new_ley_mark.append('@')
        return new_ley_mark

    def is_valid_move(self, move: Any) -> bool:
        """
        Return whether move is a valid move for this GameState.

        >>> a = StonehengeState(True, 1)
        >>> a.is_valid_move('A')
        True
        """
        return move in self.get_possible_moves()

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        a = 'p1turn: {}, side length: {}, lines: {}, ley-lines: {}'
        return a.format(self.p1_turn,
                        self.side_length, self.lines, self.ley_line)

    def state_over(self) -> bool:
        """
        Return whether or not this game is over at state.

        >>> a = StonehengeState(True, 1)
        >>> b = a.make_move('A')
        >>> b.state_over()
        True
        """
        p1 = 0
        p2 = 0
        for i in self.ley_line:
            if i == '1':
                p1 += 1
            elif i == '2':
                p2 += 1
        return (2 * p1 >= len(self.ley_line) or
                2 * p2 >= len(self.ley_line))

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.

        >>> a = StonehengeState(True, 1)
        >>> a.rough_outcome()
        1
        """
        if self.state_over():
            return self.LOSE
        new = [self.make_move(c) for c in self.get_possible_moves()]
        if any([d.state_over() for d in new]):
            return self.WIN
        else:
            result = []
            for e in new:
                last = [e.make_move(f) for f in e.get_possible_moves()]
                if any([g.state_over() for g in last]):
                    result.append(False)
                else:
                    result.append(True)
            if any(result):
                return self.DRAW
            return self.LOSE


if __name__ == "__main__":
    from python_ta import check_all
    # import doctest
    # doctest.testmod()
    check_all(config="a2_pyta.txt")
