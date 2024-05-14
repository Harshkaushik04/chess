from one_chess_board_setup import chess_player
class possible_moves:
    def __init__(self,player_one,player_two):
        self.player_one=player_one
        self.player_two=player_two
        #self.possible_moves_two=possible_moves(player_two,player_one) #will this work or not?
    def pawn_one(self):
        pawn_moves = []
        if self.player_one.color=="white":
            final_position = self.player_one.co_ordinates[0][0] + str(int(self.player_one.co_ordinates[0][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates  and (int(self.player_one.co_ordinates[0][1]) + 1 < 9):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[0][0]) + 1) + str(int(self.player_one.co_ordinates[0][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[0][0]) - 1) + str(int(self.player_one.co_ordinates[0][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position= self.player_one.co_ordinates[0][0] + str(int(self.player_one.co_ordinates[0][1]) + 2)
            intermediate_position=self.player_one.co_ordinates[0][0] + str(int(self.player_one.co_ordinates[0][1]) + 1)
            if (len(self.player_one.moves[0])==1) and (intermediate_position not in self.player_two.co_ordinates) and (final_position not in self.player_two.co_ordinates) and (intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        elif self.player_one.color=="black":
            final_position = self.player_one.co_ordinates[0][0] + str(int(self.player_one.co_ordinates[0][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[0][1]) - 1 >0):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[0][0]) + 1) + str(int(self.player_one.co_ordinates[0][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[0][0]) - 1) + str(int(self.player_one.co_ordinates[0][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position= self.player_one.co_ordinates[0][0] + str(int(self.player_one.co_ordinates[0][1]) - 2)
            intermediate_position=self.player_one.co_ordinates[0][0] + str(int(self.player_one.co_ordinates[0][1]) - 1)
            if (len(self.player_one.moves[0])==1) and (intermediate_position not in self.player_two.co_ordinates) and (final_position not in self.player_two.co_ordinates) and (intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        return pawn_moves
    def pawn_two(self):
        pawn_moves = []
        if self.player_one.color=="white":
            final_position = self.player_one.co_ordinates[1][0] + str(int(self.player_one.co_ordinates[1][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[1][1]) + 1 < 9):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[1][0]) + 1) + str(
                int(self.player_one.co_ordinates[1][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[1][0]) - 1) + str(
                int(self.player_one.co_ordinates[1][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[1][0] + str(int(self.player_one.co_ordinates[1][1]) + 2)
            intermediate_position = self.player_one.co_ordinates[1][0] + str(
                int(self.player_one.co_ordinates[1][1]) + 1)
            if (len(self.player_one.moves[1]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        elif self.player_one.color=="black":
            final_position = self.player_one.co_ordinates[1][0] + str(int(self.player_one.co_ordinates[1][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[1][1]) - 1 >0):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[1][0]) + 1) + str(
                int(self.player_one.co_ordinates[1][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[1][0]) - 1) + str(
                int(self.player_one.co_ordinates[1][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[1][0] + str(int(self.player_one.co_ordinates[1][1]) - 2)
            intermediate_position = self.player_one.co_ordinates[1][0] + str(
                int(self.player_one.co_ordinates[1][1]) - 1)
            if (len(self.player_one.moves[1]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        return pawn_moves
    def pawn_three(self):
        pawn_moves = []
        if self.player_one.color=="white":
            final_position = self.player_one.co_ordinates[2][0] + str(int(self.player_one.co_ordinates[2][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[2][1]) + 1 < 9):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[2][0]) + 1) + str(
                int(self.player_one.co_ordinates[2][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[2][0]) - 1) + str(
                int(self.player_one.co_ordinates[2][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[2][0] + str(int(self.player_one.co_ordinates[2][1]) + 2)
            intermediate_position = self.player_one.co_ordinates[2][0] + str(
                int(self.player_one.co_ordinates[2][1]) + 1)
            if (len(self.player_one.moves[2]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        elif self.player_one.color=="black":
            final_position = self.player_one.co_ordinates[2][0] + str(int(self.player_one.co_ordinates[2][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[2][1]) - 1 >0):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[2][0]) + 1) + str(
                int(self.player_one.co_ordinates[2][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[2][0]) - 1) + str(
                int(self.player_one.co_ordinates[2][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[2][0] + str(int(self.player_one.co_ordinates[2][1]) - 2)
            intermediate_position = self.player_one.co_ordinates[2][0] + str(
                int(self.player_one.co_ordinates[2][1]) - 1)
            if (len(self.player_one.moves[2]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        return pawn_moves
    def pawn_four(self):
        pawn_moves = []
        if self.player_one.color=="white":
            final_position = self.player_one.co_ordinates[3][0] + str(int(self.player_one.co_ordinates[3][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[3][1]) + 1 < 9):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[3][0]) + 1) + str(
                int(self.player_one.co_ordinates[3][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[3][0]) - 1) + str(
                int(self.player_one.co_ordinates[3][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[3][0] + str(int(self.player_one.co_ordinates[3][1]) + 2)
            intermediate_position = self.player_one.co_ordinates[3][0] + str(
                int(self.player_one.co_ordinates[3][1]) + 1)
            if (len(self.player_one.moves[3]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        elif self.player_one.color=="black":
            final_position = self.player_one.co_ordinates[3][0] + str(int(self.player_one.co_ordinates[3][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[3][1]) - 1 >0):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[3][0]) + 1) + str(
                int(self.player_one.co_ordinates[3][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[3][0]) - 1) + str(
                int(self.player_one.co_ordinates[3][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[3][0] + str(int(self.player_one.co_ordinates[3][1]) - 2)
            intermediate_position = self.player_one.co_ordinates[3][0] + str(
                int(self.player_one.co_ordinates[3][1]) - 1)
            if (len(self.player_one.moves[3]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        return pawn_moves
    def pawn_five(self):
        pawn_moves = []
        if self.player_one.color=="white":
            final_position = self.player_one.co_ordinates[4][0] + str(int(self.player_one.co_ordinates[4][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[4][1]) + 1 < 9):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[4][0]) + 1) + str(
                int(self.player_one.co_ordinates[4][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[4][0]) - 1) + str(
                int(self.player_one.co_ordinates[4][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[4][0] + str(int(self.player_one.co_ordinates[4][1]) + 2)
            intermediate_position = self.player_one.co_ordinates[4][0] + str(
                int(self.player_one.co_ordinates[4][1]) + 1)
            if (len(self.player_one.moves[4]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        elif self.player_one.color=="black":
            final_position = self.player_one.co_ordinates[4][0] + str(int(self.player_one.co_ordinates[4][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[4][1]) - 1 >0):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[4][0]) + 1) + str(
                int(self.player_one.co_ordinates[4][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[4][0]) - 1) + str(
                int(self.player_one.co_ordinates[4][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[4][0] + str(int(self.player_one.co_ordinates[4][1]) - 2)
            intermediate_position = self.player_one.co_ordinates[4][0] + str(
                int(self.player_one.co_ordinates[4][1]) - 1)
            if (len(self.player_one.moves[4]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        return pawn_moves
    def pawn_six(self):
        pawn_moves = []
        if self.player_one.color=="white":
            final_position = self.player_one.co_ordinates[5][0] + str(int(self.player_one.co_ordinates[5][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[5][1]) + 1 < 9):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[5][0]) + 1) + str(
                int(self.player_one.co_ordinates[5][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[5][0]) - 1) + str(
                int(self.player_one.co_ordinates[5][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[5][0] + str(int(self.player_one.co_ordinates[5][1]) + 2)
            intermediate_position = self.player_one.co_ordinates[5][0] + str(
                int(self.player_one.co_ordinates[5][1]) + 1)
            if (len(self.player_one.moves[5]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        elif self.player_one.color=="black":
            final_position = self.player_one.co_ordinates[5][0] + str(int(self.player_one.co_ordinates[5][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[5][1]) - 1 >0):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[5][0]) + 1) + str(
                int(self.player_one.co_ordinates[5][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[5][0]) - 1) + str(
                int(self.player_one.co_ordinates[5][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[5][0] + str(int(self.player_one.co_ordinates[5][1]) - 2)
            intermediate_position = self.player_one.co_ordinates[5][0] + str(
                int(self.player_one.co_ordinates[5][1]) - 1)
            if (len(self.player_one.moves[5]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        return pawn_moves
    def pawn_seven(self):
        pawn_moves = []
        if self.player_one.color=="white":
            final_position = self.player_one.co_ordinates[6][0] + str(int(self.player_one.co_ordinates[6][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[6][1]) + 1 < 9):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[6][0]) + 1) + str(
                int(self.player_one.co_ordinates[6][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[6][0]) - 1) + str(
                int(self.player_one.co_ordinates[6][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[6][0] + str(int(self.player_one.co_ordinates[6][1]) + 2)
            intermediate_position = self.player_one.co_ordinates[6][0] + str(
                int(self.player_one.co_ordinates[6][1]) + 1)
            if (len(self.player_one.moves[6]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        elif self.player_one.color=="black":
            final_position = self.player_one.co_ordinates[6][0] + str(int(self.player_one.co_ordinates[6][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[6][1]) - 1 >0):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[6][0]) + 1) + str(
                int(self.player_one.co_ordinates[6][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[6][0]) - 1) + str(
                int(self.player_one.co_ordinates[6][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[6][0] + str(int(self.player_one.co_ordinates[6][1]) - 2)
            intermediate_position = self.player_one.co_ordinates[6][0] + str(
                int(self.player_one.co_ordinates[6][1]) - 1)
            if (len(self.player_one.moves[6]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        return pawn_moves
    def pawn_eight(self):
        pawn_moves = []
        if self.player_one.color=="white":
            final_position = self.player_one.co_ordinates[7][0] + str(int(self.player_one.co_ordinates[7][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[7][1]) + 1 < 9):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[7][0]) + 1) + str(
                int(self.player_one.co_ordinates[7][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[7][0]) - 1) + str(
                int(self.player_one.co_ordinates[7][1]) + 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[7][0] + str(int(self.player_one.co_ordinates[7][1]) + 2)
            intermediate_position = self.player_one.co_ordinates[7][0] + str(
                int(self.player_one.co_ordinates[7][1]) + 1)
            if (len(self.player_one.moves[7]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        elif self.player_one.color=="black":
            final_position = self.player_one.co_ordinates[7][0] + str(int(self.player_one.co_ordinates[7][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position not in self.player_two.co_ordinates and (int(self.player_one.co_ordinates[7][1]) - 1 >0):
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[7][0]) + 1) + str(
                int(self.player_one.co_ordinates[7][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = chr(ord(self.player_one.co_ordinates[7][0]) - 1) + str(
                int(self.player_one.co_ordinates[7][1]) - 1)
            if final_position not in self.player_one.co_ordinates and final_position in self.player_two.co_ordinates:
                pawn_moves.append(final_position)
            final_position = self.player_one.co_ordinates[7][0] + str(int(self.player_one.co_ordinates[7][1]) - 2)
            intermediate_position = self.player_one.co_ordinates[7][0] + str(
                int(self.player_one.co_ordinates[7][1]) - 1)
            if (len(self.player_one.moves[7]) == 1) and (
                    intermediate_position not in self.player_two.co_ordinates) and (
                    final_position not in self.player_two.co_ordinates) and (
                    intermediate_position not in self.player_one.co_ordinates and intermediate_position not in self.player_two.co_ordinates):
                pawn_moves.append(final_position)
        return pawn_moves
    def bishop_dark(self):
        bishop_d_one=[]
        bishop_d_two = []
        bishop_d_three = []
        bishop_d_four = []
        #d_one
        i=1
        while (ord(self.player_one.co_ordinates[10][0])+i<105) and (ord(self.player_one.co_ordinates[10][0])+i>96) and (int(self.player_one.co_ordinates[10][1])+i<9) and (int(self.player_one.co_ordinates[10][1])+i>0):
            final_position=chr(ord(self.player_one.co_ordinates[10][0])+i)+str(int(self.player_one.co_ordinates[10][1])+i)
            bishop_d_one.append(final_position)
            i+=1
        #d_two
        i = 1
        while (ord(self.player_one.co_ordinates[10][0]) - i < 105) and (ord(self.player_one.co_ordinates[10][0]) - i > 96) and (int(self.player_one.co_ordinates[10][1]) + i < 9) and (int(self.player_one.co_ordinates[10][1]) + i > 0):
            final_position = chr(ord(self.player_one.co_ordinates[10][0]) - i) + str(int(self.player_one.co_ordinates[10][1]) + i)
            bishop_d_two.append(final_position)
            i += 1
        #d_three
        i = 1
        while (ord(self.player_one.co_ordinates[10][0]) - i < 105) and (ord(self.player_one.co_ordinates[10][0]) - i > 96) and (int(self.player_one.co_ordinates[10][1]) - i < 9) and (int(self.player_one.co_ordinates[10][1]) - i > 0):
            final_position = chr(ord(self.player_one.co_ordinates[10][0]) - i) + str(int(self.player_one.co_ordinates[10][1]) - i)
            bishop_d_three.append(final_position)
            i += 1
        #d_four
        i = 1
        while (ord(self.player_one.co_ordinates[10][0]) + i < 105) and (ord(self.player_one.co_ordinates[10][0]) + i > 96) and (int(self.player_one.co_ordinates[10][1]) - i < 9) and (int(self.player_one.co_ordinates[10][1]) - i > 0):
            final_position = chr(ord(self.player_one.co_ordinates[10][0]) + i) + str(int(self.player_one.co_ordinates[10][1]) - i)
            bishop_d_four.append(final_position)
            i += 1
        for i in range(len(bishop_d_one)):
            if bishop_d_one[i] in self.player_one.co_ordinates:
                bishop_d_one=bishop_d_one[:i]
                break
            if bishop_d_one[i] in self.player_two.co_ordinates:
                bishop_d_one=bishop_d_one[:i+1]
                break
        for i in range(len(bishop_d_two)):
            if bishop_d_two[i] in self.player_one.co_ordinates:
                bishop_d_two=bishop_d_two[:i]
                break
            if bishop_d_two[i] in self.player_two.co_ordinates:
                bishop_d_two=bishop_d_two[:i+1]
                break
        for i in range(len(bishop_d_three)):
            if bishop_d_three[i] in self.player_one.co_ordinates:
                bishop_d_three=bishop_d_three[:i]
                break
            if bishop_d_three[i] in self.player_two.co_ordinates:
                bishop_d_three=bishop_d_three[:i+1]
                break
        for i in range(len(bishop_d_four)):
            if bishop_d_four[i] in self.player_one.co_ordinates:
                bishop_d_four=bishop_d_four[:i]
                break
            if bishop_d_four[i] in self.player_two.co_ordinates:
                bishop_d_four=bishop_d_four[:i+1]
                break
        bishop_dark_moves=bishop_d_one+bishop_d_two+bishop_d_three+bishop_d_four
        return bishop_dark_moves
    def bishop_light(self):
        bishop_d_one = []
        bishop_d_two = []
        bishop_d_three = []
        bishop_d_four = []
        #d_one
        i=1
        while (ord(self.player_one.co_ordinates[13][0])+i<105) and (ord(self.player_one.co_ordinates[13][0])+i>96) and (int(self.player_one.co_ordinates[13][1])+i<9) and (int(self.player_one.co_ordinates[13][1])+i>0):
            final_position=chr(ord(self.player_one.co_ordinates[13][0])+i)+str(int(self.player_one.co_ordinates[13][1])+i)
            bishop_d_one.append(final_position)
            i+=1
        #d_two
        i = 1
        while (ord(self.player_one.co_ordinates[13][0]) - i < 105) and (ord(self.player_one.co_ordinates[13][0]) - i > 96) and (int(self.player_one.co_ordinates[13][1]) + i < 9) and (int(self.player_one.co_ordinates[13][1]) + i > 0):
            final_position = chr(ord(self.player_one.co_ordinates[13][0]) - i) + str(int(self.player_one.co_ordinates[13][1]) + i)
            bishop_d_two.append(final_position)
            i += 1
        #d_three
        i = 1
        while (ord(self.player_one.co_ordinates[13][0]) - i < 105) and (ord(self.player_one.co_ordinates[13][0]) - i > 96) and (int(self.player_one.co_ordinates[13][1]) - i < 9) and (int(self.player_one.co_ordinates[13][1]) - i > 0):
            final_position = chr(ord(self.player_one.co_ordinates[13][0]) - i) + str(int(self.player_one.co_ordinates[13][1]) - i)
            bishop_d_three.append(final_position)
            i += 1
        #d_four
        i = 1
        while (ord(self.player_one.co_ordinates[13][0]) + i < 105) and (ord(self.player_one.co_ordinates[13][0]) + i > 96) and (int(self.player_one.co_ordinates[13][1]) - i < 9) and (int(self.player_one.co_ordinates[13][1]) - i > 0):
            final_position = chr(ord(self.player_one.co_ordinates[13][0]) + i) + str(int(self.player_one.co_ordinates[13][1]) - i)
            bishop_d_four.append(final_position)
            i += 1
        for i in range(len(bishop_d_one)):
            if bishop_d_one[i] in self.player_one.co_ordinates:
                bishop_d_one=bishop_d_one[:i]
                break
            if bishop_d_one[i] in self.player_two.co_ordinates:
                bishop_d_one=bishop_d_one[:i+1]
                break
        for i in range(len(bishop_d_two)):
            if bishop_d_two[i] in self.player_one.co_ordinates:
                bishop_d_two=bishop_d_two[:i]
                break
            if bishop_d_two[i] in self.player_two.co_ordinates:
                bishop_d_two=bishop_d_two[:i+1]
                break
        for i in range(len(bishop_d_three)):
            if bishop_d_three[i] in self.player_one.co_ordinates:
                bishop_d_three=bishop_d_three[:i]
                break
            if bishop_d_three[i] in self.player_two.co_ordinates:
                bishop_d_three=bishop_d_three[:i+1]
                break
        for i in range(len(bishop_d_four)):
            if bishop_d_four[i] in self.player_one.co_ordinates:
                bishop_d_four=bishop_d_four[:i]
                break
            if bishop_d_four[i] in self.player_two.co_ordinates:
                bishop_d_four=bishop_d_four[:i+1]
                break
        bishop_light_moves=bishop_d_one+bishop_d_two+bishop_d_three+bishop_d_four
        return bishop_light_moves
    def rook_one(self):
        rook_d_one = []
        rook_d_two = []
        rook_d_three = []
        rook_d_four = []
        # d_one
        i = 1
        while (ord(self.player_one.co_ordinates[8][0]) + i < 105) and (ord(self.player_one.co_ordinates[8][0]) + i > 96):
            final_position = chr(ord(self.player_one.co_ordinates[8][0]) + i)+ self.player_one.co_ordinates[8][1]
            rook_d_one.append(final_position)
            i += 1
        # d_two
        i = 1
        while (int(self.player_one.co_ordinates[8][1]) + i < 9)and (int(self.player_one.co_ordinates[8][1]) + i > 0):
            final_position = self.player_one.co_ordinates[8][0]+ str(int(self.player_one.co_ordinates[8][1]) + i)
            rook_d_two.append(final_position)
            i += 1
        # d_three
        i = 1
        while (ord(self.player_one.co_ordinates[8][0]) - i < 105)and (ord(self.player_one.co_ordinates[8][0]) - i > 96):
            final_position = chr(ord(self.player_one.co_ordinates[8][0]) - i)+(self.player_one.co_ordinates[8][1])
            rook_d_three.append(final_position)
            i += 1
        # d_four
        i = 1
        while (int(self.player_one.co_ordinates[8][1]) - i < 9) and (int(self.player_one.co_ordinates[8][1]) - i > 0):
            final_position = chr(ord(self.player_one.co_ordinates[8][0]))+ str(int(self.player_one.co_ordinates[8][1]) - i)
            rook_d_four.append(final_position)
            i += 1
        for i in range(len(rook_d_one)):
            if rook_d_one[i] in self.player_one.co_ordinates:
                rook_d_one = rook_d_one[:i]
                break
            if rook_d_one[i] in self.player_two.co_ordinates:
                rook_d_one = rook_d_one[: i + 1]
                break
        for i in range(len(rook_d_two)):
            if rook_d_two[i] in self.player_one.co_ordinates:
                rook_d_two = rook_d_two[:i]
                break
            if rook_d_two[i] in self.player_two.co_ordinates:
                rook_d_two = rook_d_two[: i + 1]
                break
        for i in range(len(rook_d_three)):
            if rook_d_three[i] in self.player_one.co_ordinates:
                rook_d_three = rook_d_three[:i]
                break
            if rook_d_three[i] in self.player_two.co_ordinates:
                rook_d_three = rook_d_three[: i + 1]
                break
        for i in range(len(rook_d_four)):
            if rook_d_four[i] in self.player_one.co_ordinates:
                rook_d_four = rook_d_four[:i]
                break
            if rook_d_four[i] in self.player_two.co_ordinates:
                rook_d_four = rook_d_four[: i + 1]
                break
        rook_one_moves=rook_d_one+rook_d_two+rook_d_three+rook_d_four
        return rook_one_moves
    def rook_two(self):
        rook_d_one = []
        rook_d_two = []
        rook_d_three = []
        rook_d_four = []
        # d_one
        i = 1
        while (ord(self.player_one.co_ordinates[15][0]) + i < 105) and (ord(self.player_one.co_ordinates[15][0]) + i > 96):
            final_position = chr(ord(self.player_one.co_ordinates[15][0]) + i) + self.player_one.co_ordinates[15][1]
            rook_d_one.append(final_position)
            i += 1
        # d_two
        i = 1
        while (int(self.player_one.co_ordinates[15][1]) + i < 9) and (int(self.player_one.co_ordinates[15][1]) + i > 0):
            final_position = self.player_one.co_ordinates[15][0] + str(int(self.player_one.co_ordinates[15][1]) + i)
            rook_d_two.append(final_position)
            i += 1
        # d_three
        i = 1
        while (ord(self.player_one.co_ordinates[15][0]) - i < 105) and (ord(self.player_one.co_ordinates[15][0]) - i > 96):
            final_position = chr(ord(self.player_one.co_ordinates[15][0]) - i) + (self.player_one.co_ordinates[15][1])
            rook_d_three.append(final_position)
            i += 1
        # d_four
        i = 1
        while (int(self.player_one.co_ordinates[15][1]) - i < 9) and (int(self.player_one.co_ordinates[15][1]) - i > 0):
            final_position = chr(ord(self.player_one.co_ordinates[15][0])) + str(
                int(self.player_one.co_ordinates[15][1]) - i)
            rook_d_four.append(final_position)
            i += 1
        for i in range(len(rook_d_one)):
            if rook_d_one[i] in self.player_one.co_ordinates:
                rook_d_one = rook_d_one[:i]
                break
            if rook_d_one[i] in self.player_two.co_ordinates:
                rook_d_one = rook_d_one[: i + 1]
                break
        for i in range(len(rook_d_two)):
            if rook_d_two[i] in self.player_one.co_ordinates:
                rook_d_two = rook_d_two[:i]
                break
            if rook_d_two[i] in self.player_two.co_ordinates:
                rook_d_two = rook_d_two[: i + 1]
                break
        for i in range(len(rook_d_three)):
            if rook_d_three[i] in self.player_one.co_ordinates:
                rook_d_three = rook_d_three[:i]
                break
            if rook_d_three[i] in self.player_two.co_ordinates:
                rook_d_three = rook_d_three[: i + 1]
                break
        for i in range(len(rook_d_four)):
            if rook_d_four[i] in self.player_one.co_ordinates:
                rook_d_four = rook_d_four[:i]
                break
            if rook_d_four[i] in self.player_two.co_ordinates:
                rook_d_four = rook_d_four[: i + 1]
                break
        rook_two_moves = rook_d_one + rook_d_two + rook_d_three + rook_d_four
        return rook_two_moves

    def queen(self):
        bishop_d_one = []
        bishop_d_two = []
        bishop_d_three = []
        bishop_d_four = []
        rook_d_one = []
        rook_d_two = []
        rook_d_three = []
        rook_d_four = []

        # d_one
        i = 1
        while ((ord(self.player_one.co_ordinates[11][0]) + i < 105)
                and (ord(self.player_one.co_ordinates[11][0]) + i > 96)
                and (int(self.player_one.co_ordinates[11][1]) + i < 9)
                and (int(self.player_one.co_ordinates[11][1]) + i > 0)):
            final_position = (chr(ord(self.player_one.co_ordinates[11][0]) + i)+ str(int(self.player_one.co_ordinates[11][1]) + i))
            bishop_d_one.append(final_position)
            i += 1
        # d_two
        i = 1
        while ((ord(self.player_one.co_ordinates[11][0]) - i < 105)
                and (ord(self.player_one.co_ordinates[11][0]) - i > 96)
                and (int(self.player_one.co_ordinates[11][1]) + i < 9)
                and (int(self.player_one.co_ordinates[11][1]) + i > 0)):
            final_position = (chr(ord(self.player_one.co_ordinates[11][0]) - i)+ str(int(self.player_one.co_ordinates[11][1]) + i))
            bishop_d_two.append(final_position)
            i += 1
        # d_three
        i = 1
        while ((ord(self.player_one.co_ordinates[11][0]) - i < 105)
                and (ord(self.player_one.co_ordinates[11][0]) - i > 96)
                and (int(self.player_one.co_ordinates[11][1]) - i < 9)
                and (int(self.player_one.co_ordinates[11][1]) - i > 0)):
            final_position = (chr(ord(self.player_one.co_ordinates[11][0]) - i)+ str(int(self.player_one.co_ordinates[11][1]) - i))
            bishop_d_three.append(final_position)
            i += 1
        # d_four
        i = 1
        while ((ord(self.player_one.co_ordinates[11][0]) + i < 105)
                and (ord(self.player_one.co_ordinates[11][0]) + i > 96)
                and (int(self.player_one.co_ordinates[11][1]) - i < 9)
                and (int(self.player_one.co_ordinates[11][1]) - i > 0)):
            final_position = (chr(ord(self.player_one.co_ordinates[11][0]) + i)+ str(int(self.player_one.co_ordinates[11][1]) - i))
            bishop_d_four.append(final_position)
            i += 1

        for i in range(len(bishop_d_one)):
            if bishop_d_one[i] in self.player_one.co_ordinates:
                bishop_d_one = bishop_d_one[:i]
                break
            if bishop_d_one[i] in self.player_two.co_ordinates:
                bishop_d_one = bishop_d_one[:i + 1]
                break
        for i in range(len(bishop_d_two)):
            if bishop_d_two[i] in self.player_one.co_ordinates:
                bishop_d_two = bishop_d_two[:i]
                break
            if bishop_d_two[i] in self.player_two.co_ordinates:
                bishop_d_two = bishop_d_two[:i + 1]
                break
        for i in range(len(bishop_d_three)):
            if bishop_d_three[i] in self.player_one.co_ordinates:
                bishop_d_three = bishop_d_three[:i]
                break
            if bishop_d_three[i] in self.player_two.co_ordinates:
                bishop_d_three = bishop_d_three[:i + 1]
                break
        for i in range(len(bishop_d_four)):
            if bishop_d_four[i] in self.player_one.co_ordinates:
                bishop_d_four = bishop_d_four[:i]
                break
            if bishop_d_four[i] in self.player_two.co_ordinates:
                bishop_d_four = bishop_d_four[:i + 1]
                break

        bishop_moves = bishop_d_one + bishop_d_two + bishop_d_three + bishop_d_four

        # d_one
        i = 1
        while ((ord(self.player_one.co_ordinates[11][0]) + i < 105)and (ord(self.player_one.co_ordinates[11][0]) + i > 96)):
            final_position = (chr(ord(self.player_one.co_ordinates[11][0]) + i)+ self.player_one.co_ordinates[11][1])
            rook_d_one.append(final_position)
            i += 1
        # d_two
        i = 1
        while ((int(self.player_one.co_ordinates[11][1]) + i < 9)and (int(self.player_one.co_ordinates[11][1]) + i > 0)):
            final_position = (self.player_one.co_ordinates[11][0]+ str(int(self.player_one.co_ordinates[11][1]) + i))
            rook_d_two.append(final_position)
            i += 1
        # d_three
        i = 1
        while ((ord(self.player_one.co_ordinates[11][0]) - i < 105)and (ord(self.player_one.co_ordinates[11][0]) - i > 96)):
            final_position = (chr(ord(self.player_one.co_ordinates[11][0]) - i)+ (self.player_one.co_ordinates[11][1]))
            rook_d_three.append(final_position)
            i += 1
            # d_four
        i = 1
        while ((int(self.player_one.co_ordinates[11][1]) - i < 9)and (int(self.player_one.co_ordinates[11][1]) - i > 0)):
            final_position = (chr(ord(self.player_one.co_ordinates[11][0]))+ str(int(self.player_one.co_ordinates[11][1]) - i))
            rook_d_four.append(final_position)
            i += 1

        for i in range(len(rook_d_one)):
            if rook_d_one[i] in self.player_one.co_ordinates:
                rook_d_one = rook_d_one[:i]
                break
            if rook_d_one[i] in self.player_two.co_ordinates:
                rook_d_one = rook_d_one[: i + 1]
                break
        for i in range(len(rook_d_two)):
            if rook_d_two[i] in self.player_one.co_ordinates:
                rook_d_two = rook_d_two[:i]
                break
            if rook_d_two[i] in self.player_two.co_ordinates:
                rook_d_two = rook_d_two[: i + 1]
                break
        for i in range(len(rook_d_three)):
            if rook_d_three[i] in self.player_one.co_ordinates:
                rook_d_three = rook_d_three[:i]
                break
            if rook_d_three[i] in self.player_two.co_ordinates:
                rook_d_three = rook_d_three[: i + 1]
                break
        for i in range(len(rook_d_four)):
            if rook_d_four[i] in self.player_one.co_ordinates:
                rook_d_four = rook_d_four[:i]
                break
            if rook_d_four[i] in self.player_two.co_ordinates:
                rook_d_four = rook_d_four[: i + 1]
                break

        rook_moves = rook_d_one + rook_d_two + rook_d_three + rook_d_four
        queen_moves = bishop_moves + rook_moves
        return queen_moves
    def knight_one(self):
        knight_moves=[]
        x,y=1,2
        final_position=chr(ord(self.player_one.co_ordinates[9][0]) + x)+str(int(self.player_one.co_ordinates[9][1]) + y)
        if (ord(self.player_one.co_ordinates[9][0]) + x < 105) and (ord(self.player_one.co_ordinates[9][0]) + x > 96) and (int(self.player_one.co_ordinates[9][1]) + y < 9) and (int(self.player_one.co_ordinates[9][1]) + y > 0) and (final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x,y=1,-2
        final_position = chr(ord(self.player_one.co_ordinates[9][0]) + x) + str(
            int(self.player_one.co_ordinates[9][1]) + y)
        if (ord(self.player_one.co_ordinates[9][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[9][0]) + x > 96) and (
                int(self.player_one.co_ordinates[9][1]) + y < 9) and (
                int(self.player_one.co_ordinates[9][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x,y=-1,2
        final_position = chr(ord(self.player_one.co_ordinates[9][0]) + x) + str(
            int(self.player_one.co_ordinates[9][1]) + y)
        if (ord(self.player_one.co_ordinates[9][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[9][0]) + x > 96) and (
                int(self.player_one.co_ordinates[9][1]) + y < 9) and (
                int(self.player_one.co_ordinates[9][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x,y=-1,-2
        final_position = chr(ord(self.player_one.co_ordinates[9][0]) + x) + str(
            int(self.player_one.co_ordinates[9][1]) + y)
        if (ord(self.player_one.co_ordinates[9][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[9][0]) + x > 96) and (
                int(self.player_one.co_ordinates[9][1]) + y < 9) and (
                int(self.player_one.co_ordinates[9][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x,y=2,1
        final_position = chr(ord(self.player_one.co_ordinates[9][0]) + x) + str(
            int(self.player_one.co_ordinates[9][1]) + y)
        if (ord(self.player_one.co_ordinates[9][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[9][0]) + x > 96) and (
                int(self.player_one.co_ordinates[9][1]) + y < 9) and (
                int(self.player_one.co_ordinates[9][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x,y=2,-1
        final_position = chr(ord(self.player_one.co_ordinates[9][0]) + x) + str(
            int(self.player_one.co_ordinates[9][1]) + y)
        if (ord(self.player_one.co_ordinates[9][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[9][0]) + x > 96) and (
                int(self.player_one.co_ordinates[9][1]) + y < 9) and (
                int(self.player_one.co_ordinates[9][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x,y=-2,1
        final_position = chr(ord(self.player_one.co_ordinates[9][0]) + x) + str(
            int(self.player_one.co_ordinates[9][1]) + y)
        if (ord(self.player_one.co_ordinates[9][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[9][0]) + x > 96) and (
                int(self.player_one.co_ordinates[9][1]) + y < 9) and (
                int(self.player_one.co_ordinates[9][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x,y=-2,-1
        final_position = chr(ord(self.player_one.co_ordinates[9][0]) + x) + str(
            int(self.player_one.co_ordinates[9][1]) + y)
        if (ord(self.player_one.co_ordinates[9][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[9][0]) + x > 96) and (
                int(self.player_one.co_ordinates[9][1]) + y < 9) and (
                int(self.player_one.co_ordinates[9][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        return knight_moves

    def knight_two(self):
        knight_moves = []
        x, y = 1, 2
        final_position = chr(ord(self.player_one.co_ordinates[14][0]) + x) + str(
            int(self.player_one.co_ordinates[14][1]) + y)
        if (ord(self.player_one.co_ordinates[14][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[14][0]) + x > 96) and (
                int(self.player_one.co_ordinates[14][1]) + y < 9) and (
                int(self.player_one.co_ordinates[14][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x, y = 1, -2
        final_position = chr(ord(self.player_one.co_ordinates[14][0]) + x) + str(
            int(self.player_one.co_ordinates[14][1]) + y)
        if (ord(self.player_one.co_ordinates[14][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[14][0]) + x > 96) and (
                int(self.player_one.co_ordinates[14][1]) + y < 9) and (
                int(self.player_one.co_ordinates[14][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x, y = -1, 2
        final_position = chr(ord(self.player_one.co_ordinates[14][0]) + x) + str(
            int(self.player_one.co_ordinates[14][1]) + y)
        if (ord(self.player_one.co_ordinates[14][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[14][0]) + x > 96) and (
                int(self.player_one.co_ordinates[14][1]) + y < 9) and (
                int(self.player_one.co_ordinates[14][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x, y = -1, -2
        final_position = chr(ord(self.player_one.co_ordinates[14][0]) + x) + str(
            int(self.player_one.co_ordinates[14][1]) + y)
        if (ord(self.player_one.co_ordinates[14][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[14][0]) + x > 96) and (
                int(self.player_one.co_ordinates[14][1]) + y < 9) and (
                int(self.player_one.co_ordinates[14][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x, y = 2, 1
        final_position = chr(ord(self.player_one.co_ordinates[14][0]) + x) + str(
            int(self.player_one.co_ordinates[14][1]) + y)
        if (ord(self.player_one.co_ordinates[14][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[14][0]) + x > 96) and (
                int(self.player_one.co_ordinates[14][1]) + y < 9) and (
                int(self.player_one.co_ordinates[14][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x, y = 2, -1
        final_position = chr(ord(self.player_one.co_ordinates[14][0]) + x) + str(
            int(self.player_one.co_ordinates[14][1]) + y)
        if (ord(self.player_one.co_ordinates[14][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[14][0]) + x > 96) and (
                int(self.player_one.co_ordinates[14][1]) + y < 9) and (
                int(self.player_one.co_ordinates[14][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x, y = -2, 1
        final_position = chr(ord(self.player_one.co_ordinates[14][0]) + x) + str(
            int(self.player_one.co_ordinates[14][1]) + y)
        if (ord(self.player_one.co_ordinates[14][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[14][0]) + x > 96) and (
                int(self.player_one.co_ordinates[14][1]) + y < 9) and (
                int(self.player_one.co_ordinates[14][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        x, y = -2, -1
        final_position = chr(ord(self.player_one.co_ordinates[14][0]) + x) + str(
            int(self.player_one.co_ordinates[14][1]) + y)
        if (ord(self.player_one.co_ordinates[14][0]) + x < 105) and (
                ord(self.player_one.co_ordinates[14][0]) + x > 96) and (
                int(self.player_one.co_ordinates[14][1]) + y < 9) and (
                int(self.player_one.co_ordinates[14][1]) + y > 0) and (
                final_position not in self.player_one.co_ordinates):
            knight_moves.append(final_position)
        return knight_moves

    def king(self):
        king_moves=[]
        #d1
        player_one_copy=self.player_one.make_copy()
        player_two_copy=self.player_two.make_copy()
        final_position = self.player_one.co_ordinates[12][0] + str(int(self.player_one.co_ordinates[12][1]) + 1)
        generate_position(player_one_copy, player_two_copy,"k"+self.player_one.co_ordinates[12]+final_position)
        player_two_possible_moves=possible_moves(self.player_two,self.player_one)
        player_two_copy_possible_moves=possible_moves(player_two_copy,player_one_copy)
        if (final_position not in self.player_one.co_ordinates) and (final_position not in player_two_possible_moves.all_possible_except_king()) and (player_one_copy.co_ordinates[12] not in player_two_copy_possible_moves.all_possible_except_king()) and ((int(self.player_one.co_ordinates[12][1]) + 1 < 9)):
            king_moves.append(final_position)
        #d2
        player_one_copy = self.player_one.make_copy()
        player_two_copy = self.player_two.make_copy()
        final_position = chr(ord(self.player_one.co_ordinates[12][0])-1) + self.player_one.co_ordinates[12][1]
        generate_position(player_one_copy, player_two_copy, "k" + self.player_one.co_ordinates[12] + final_position)
        player_two_possible_moves = possible_moves(self.player_two, self.player_one)
        player_two_copy_possible_moves = possible_moves(player_two_copy, player_one_copy)
        if (final_position not in self.player_one.co_ordinates) and (final_position not in player_two_possible_moves.all_possible_except_king()) and (player_one_copy.co_ordinates[12] not in player_two_copy_possible_moves.all_possible_except_king()) and (ord(self.player_one.co_ordinates[12][0])-1>96):
            king_moves.append(final_position)
        #d3
        player_one_copy = self.player_one.make_copy()
        player_two_copy = self.player_two.make_copy()
        final_position = self.player_one.co_ordinates[12][0] + str(int(self.player_one.co_ordinates[12][1]) - 1)
        generate_position(player_one_copy, player_two_copy, "k" + self.player_one.co_ordinates[12] + final_position)
        player_two_possible_moves = possible_moves(self.player_two, self.player_one)
        player_two_copy_possible_moves = possible_moves(player_two_copy, player_one_copy)
        if (final_position not in self.player_one.co_ordinates) and (
                final_position not in player_two_possible_moves.all_possible_except_king()) and (
                player_one_copy.co_ordinates[12] not in player_two_copy_possible_moves.all_possible_except_king()) and (
        (int(self.player_one.co_ordinates[12][1])-1 > 0)):
            king_moves.append(final_position)
        #d4
        player_one_copy = self.player_one.make_copy()
        player_two_copy = self.player_two.make_copy()
        final_position = chr(ord(self.player_one.co_ordinates[12][0]) + 1) + self.player_one.co_ordinates[12][1]
        generate_position(player_one_copy, player_two_copy, "k" + self.player_one.co_ordinates[12] + final_position)
        player_two_possible_moves = possible_moves(self.player_two, self.player_one)
        player_two_copy_possible_moves = possible_moves(player_two_copy, player_one_copy)
        if (final_position not in self.player_one.co_ordinates) and (
                final_position not in player_two_possible_moves.all_possible_except_king()) and (
                player_one_copy.co_ordinates[12] not in player_two_copy_possible_moves.all_possible_except_king()) and (
                ord(self.player_one.co_ordinates[12][0]) + 1 < 105):
            king_moves.append(final_position)
        #d5
        player_one_copy = self.player_one.make_copy()
        player_two_copy = self.player_two.make_copy()
        final_position = chr(ord(self.player_one.co_ordinates[12][0]) + 1) + str(int(self.player_one.co_ordinates[12][1])+1)
        generate_position(player_one_copy, player_two_copy, "k" + self.player_one.co_ordinates[12] + final_position)
        player_two_possible_moves = possible_moves(self.player_two, self.player_one)
        player_two_copy_possible_moves = possible_moves(player_two_copy, player_one_copy)
        if (final_position not in self.player_one.co_ordinates) and (
                final_position not in player_two_possible_moves.all_possible_except_king()) and (
                player_one_copy.co_ordinates[12] not in player_two_copy_possible_moves.all_possible_except_king()) and (
                ord(self.player_one.co_ordinates[12][0]) + 1 < 105) and (int(self.player_one.co_ordinates[12][1])+1 < 9) :
            king_moves.append(final_position)
        #d6
        player_one_copy = self.player_one.make_copy()
        player_two_copy = self.player_two.make_copy()
        final_position = chr(ord(self.player_one.co_ordinates[12][0]) - 1) + str(
            int(self.player_one.co_ordinates[12][1]) + 1)
        generate_position(player_one_copy, player_two_copy, "k" + self.player_one.co_ordinates[12] + final_position)
        player_two_possible_moves = possible_moves(self.player_two, self.player_one)
        player_two_copy_possible_moves = possible_moves(player_two_copy, player_one_copy)
        if (final_position not in self.player_one.co_ordinates) and (
                final_position not in player_two_possible_moves.all_possible_except_king()) and (
                player_one_copy.co_ordinates[12] not in player_two_copy_possible_moves.all_possible_except_king()) and (
                ord(self.player_one.co_ordinates[12][0]) - 1 > 96) and (
                int(self.player_one.co_ordinates[12][1]) + 1 < 9):
            king_moves.append(final_position)
        #d7
        player_one_copy = self.player_one.make_copy()
        player_two_copy = self.player_two.make_copy()
        final_position = chr(ord(self.player_one.co_ordinates[12][0]) - 1) + str(
            int(self.player_one.co_ordinates[12][1]) - 1)
        generate_position(player_one_copy, player_two_copy, "k" + self.player_one.co_ordinates[12] + final_position)
        player_two_possible_moves = possible_moves(self.player_two, self.player_one)
        player_two_copy_possible_moves = possible_moves(player_two_copy, player_one_copy)
        if (final_position not in self.player_one.co_ordinates) and (
                final_position not in player_two_possible_moves.all_possible_except_king()) and (
                player_one_copy.co_ordinates[12] not in player_two_copy_possible_moves.all_possible_except_king()) and (
                ord(self.player_one.co_ordinates[12][0]) - 1 > 96) and (
                int(self.player_one.co_ordinates[12][1]) - 1 > 0):
            king_moves.append(final_position)
        #d8
        player_one_copy = self.player_one.make_copy()
        player_two_copy = self.player_two.make_copy()
        final_position = chr(ord(self.player_one.co_ordinates[12][0]) + 1) + str(
            int(self.player_one.co_ordinates[12][1]) - 1)
        generate_position(player_one_copy, player_two_copy, "k" + self.player_one.co_ordinates[12] + final_position)
        player_two_possible_moves = possible_moves(self.player_two, self.player_one)
        player_two_copy_possible_moves = possible_moves(player_two_copy, player_one_copy)
        if (final_position not in self.player_one.co_ordinates) and (
                final_position not in player_two_possible_moves.all_possible_except_king()) and (
                player_one_copy.co_ordinates[12] not in player_two_copy_possible_moves.all_possible_except_king()) and (
                ord(self.player_one.co_ordinates[12][0]) + 1 < 105) and (
                int(self.player_one.co_ordinates[12][1]) - 1 > 0):
            king_moves.append(final_position)
        return king_moves

    def all_possible_except_king(self):
        possible=self.pawn_one()+self.pawn_two()+self.pawn_three()+self.pawn_four()+self.pawn_five()+self.pawn_six()+self.pawn_seven()+self.pawn_eight()+self.rook_one()+self.rook_two()+self.bishop_light()+self.bishop_dark()+self.knight_one()+self.knight_two()
        return possible

    def func_list(self):
        func_l=[self.pawn_one,self.pawn_two,self.pawn_three,self.pawn_four,self.pawn_five,self.pawn_six,self.pawn_seven,self.pawn_eight,self.rook_one,self.knight_one,self.bishop_dark,self.queen,self.king,self.bishop_light,self.knight_two,self.rook_two]
        return func_l

class start_game:
    def __init__(self, white, black):  # white and black are objects of class chess_player
        self.player_one = white
        self.player_two = black
        self.white_moves=None
        self.black_moves=None
    def game(self):  # main content of game
        while True:  # when completed the checkmate condition is completed, write that here
            # didnt check whether the move is legal or not
            white_move = input("White move:")
            '''
            if len(white_move)==2: #pawn move
                #didnt add legal move criteria yet
                final_position=white_move
                first_letters_pawn_co_ordinates = [word[0] for word in self.white.pawns]
                flag = False
                for i in range(len(first_letters_pawn_co_ordinates)):
                    if first_letters_pawn_co_ordinates[i] == final_position[0]:
                        self.white.pawns[i] = white_move
                        flag = True
                        break
                if flag == False:
                    print("move wasnt legal,play move again")
                    continue
            
            if len(white_move) == 4 and white_move[2:] not in self.white.co_ordinates:  # pawn move
                initial_position = white_move[:2]
                final_position = white_move[2:]
                flag = False
                for i in range(len(self.white.pawns)):
                    if initial_position == self.white.pawns[i]:
                        self.white.pawns[i] = white_move[2:]
                        self.white.co_ordinates[i]=white_move[2:]
                        flag = True
                        break
                if flag == False:
                    print("move not legal")
                    continue
                for i in range(len(self.black.co_ordinates)):  # didnt include the black king case
                    if white_move[2:] == self.black.co_ordinates[i]:
                        self.black.co_ordinates[i] = None  # piece captured
            elif len(white_move) == 4 and white_move[2:] in self.white.co_ordinates: #illegal move
                print("move not legal")
                continue
            if len(white_move) == 5 and white_move[3:] not in self.white.co_ordinates:
                if white_move[0].upper()=="B":
                    pass
            '''
            #break



def generate_position(player_one,player_two,move):
    copied_position = player_one.make_copy()
    player_one_possible_moves=possible_moves(player_one,player_two)
    player_two_possible_moves=possible_moves(player_two,player_one)
    if len(move) == 5 and (move[3:] not in player_one.co_ordinates):
        piece=move[0]
        initial_position=move[1:3]
        final_position=move[3:]
        if piece.lower() == "p":
            flag=False
            for i in range(len(player_one.co_ordinates)):
                #print(player_one_possible_moves.func_list()[i]())
                if initial_position == player_one.co_ordinates[i] and (final_position in player_one_possible_moves.func_list()[i]()) and i<8:
                    player_one.moves[i].append(final_position)
                    player_one.co_ordinates[i]=final_position
                    flag=True
                    for j in range(len(player_two.co_ordinates)):
                        if final_position == player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
                    break
            if flag==False:
                print("move not legal")
                #continue ,if we were in game loop,also make seperate game loops for black and white(some condition for exit) and one common
        elif piece.lower()=="r":
            if initial_position == player_one.co_ordinates[8] and (final_position in player_one_possible_moves.func_list()[8]()):
                    player_one_possible_moves.func_list()[8]()
                    player_one.moves[8].append(final_position)
                    player_one.co_ordinates[8]=final_position
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            elif initial_position == player_one.co_ordinates[15] and (final_position in player_one_possible_moves.func_list()[15]()):
                    #print(player_one_possible_moves.func_list()[15]())
                    player_one.moves[15].append(final_position)
                    player_one.co_ordinates[15]=final_position
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            else:
                print("move is not legal")
                # continue ,if we were in game loop,also make seperate game loops for black and white(some condition for exit) and one common
        elif piece.lower()=="b":
            if initial_position == player_one.co_ordinates[10] and (final_position in player_one_possible_moves.func_list()[10]()):
                    player_one_possible_moves.func_list()[10]()
                    player_one.moves[10].append(final_position)
                    player_one.co_ordinates[10]=final_position
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            elif initial_position == player_one.co_ordinates[13] and (final_position in player_one_possible_moves.func_list()[13]()):
                    #print(player_one_possible_moves.func_list()[13]())
                    player_one.moves[13].append(final_position)
                    player_one.co_ordinates[13]=final_position
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            else:
                print("move is not legal")
                # continue ,if we were in game loop,also make seperate game loops for black and white(some condition for exit) and one common
        elif piece.lower()=="n":
            if initial_position == player_one.co_ordinates[9] and (final_position in player_one_possible_moves.func_list()[9]()):
                    player_one_possible_moves.func_list()[9]()
                    player_one.moves[9].append(final_position)
                    player_one.co_ordinates[9]=final_position
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            elif initial_position == player_one.co_ordinates[14] and (final_position in player_one_possible_moves.func_list()[14]()):
                    #print(player_one_possible_moves.func_list()[14]())
                    player_one.moves[14].append(final_position)
                    player_one.co_ordinates[14]=final_position
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            else:
                print("move is not legal")
                # continue ,if we were in game loop,also make seperate game loops for black and white(some condition for exit) and one common
        elif piece.lower()=="q":
            if initial_position == player_one.co_ordinates[11] and (final_position in player_one_possible_moves.func_list()[11]()):
                    player_one_possible_moves.func_list()[11]()
                    player_one.moves[11].append(final_position)
                    player_one.co_ordinates[11]=final_position
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            else:
                print("move is not legal")
                # continue ,if we were in game loop,also make seperate game loops for black and white(some condition for exit) and one common

        elif piece.lower()=="k":
            if initial_position == player_one.co_ordinates[12] and (final_position in player_one_possible_moves.func_list()[12]()):
                    player_one_possible_moves.func_list()[12]()
                    player_one.moves[12].append(final_position)
                    player_one.co_ordinates[12]=final_position
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            else:
                print("move is not legal")
                # continue ,if we were in game loop,also make seperate game loops for black and white(some condition for exit) and one common



def test_game():
    player_one=chess_player("white")
    player_one.setup()
    player_two=chess_player("black")
    player_two.setup()
    game=start_game(player_one,player_two)
    one_possible_moves=possible_moves(player_one,player_two)
    generate_position(player_one,player_two,"pe2e4")
    generate_position(player_two,player_one,"pf7f6")
    generate_position(player_one,player_two,"pg2g3")
    generate_position(player_two,player_one,"pg7g5")
    generate_position(player_one,player_two,"bf1d3")
    generate_position(player_two,player_one,"ph7h6")
    generate_position(player_one,player_two,"ng1f3")
    generate_position(player_two,player_one,"pe7e5")
    generate_position(player_one,player_two,"nf3g5")
    generate_position(player_two,player_one,"pf6g5")
    generate_position(player_one,player_two,"ph2h3")
    generate_position(player_two,player_one,"pb7b5")
    print(player_one.co_ordinates)
    print(player_two.co_ordinates)
    print(player_one.moves)
    print(player_two.moves)
    print(one_possible_moves.bishop_light())
    return
test_game()