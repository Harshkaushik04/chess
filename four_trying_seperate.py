import copy

from one_chess_board_setup import chess_player
def force_generate_move(player_one,player_two,move):
    player_one_copied=copy.copy(player_one)
    player_two_copied=copy.copy(player_two)
    if len(move) == 5 and (move[3:] not in player_one_copied.co_ordinates):
        piece=move[0]
        initial_position=move[1:3]
        final_position=move[3:]
        if piece.lower() == "p" or piece.lower()=="b" or piece.lower()=="n" or piece.lower()=="r" or piece.lower()=="q" or piece.lower()=="k":
            flag=False
            for i in range(len(player_one_copied.co_ordinates)):
                if initial_position==player_one_copied.co_ordinates[i] and 105 > ord(final_position[0]) > 96 and 9 > int(final_position[1]) > 0:
                    player_one_copied.co_ordinates[i]=final_position
                    player_one_copied.moves[i].append(final_position)
                    flag=True
                    break
            if flag==False:
                print("position not possible")
    return [player_one_copied,player_two_copied]


def pawn_one(player_one, player_two):
    pawn_moves = []
    final_position = player_one.co_ordinates[0][0] + str(int(player_one.co_ordinates[0][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position not in player_two.co_ordinates and (int(player_one.co_ordinates[0][1]) + 1 < 9) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[0]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[0][0]) + 1) + str(int(player_one.co_ordinates[0][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[0]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[0][0]) - 1) + str(int(player_one.co_ordinates[0][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[0]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = player_one.co_ordinates[0][0] + str(int(player_one.co_ordinates[0][1]) + 2)
    intermediate_position = player_one.co_ordinates[0][0] + str(int(player_one.co_ordinates[0][1]) + 1)
    if (len(player_one.moves[0]) == 1) and (
            intermediate_position not in player_two.co_ordinates) and (
            final_position not in player_two.co_ordinates) and (
            intermediate_position not in player_one.co_ordinates and intermediate_position not in player_two.co_ordinates) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[0]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    return pawn_moves
def pawn_two(player_one, player_two):
    pawn_moves = []
    final_position = player_one.co_ordinates[1][0] + str(int(player_one.co_ordinates[1][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position not in player_two.co_ordinates and (
            int(player_one.co_ordinates[1][1]) + 1 < 9) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[1]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[1][0]) + 1) + str(int(player_one.co_ordinates[1][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[1]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[1][0]) - 1) + str(int(player_one.co_ordinates[1][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[1]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = player_one.co_ordinates[1][0] + str(int(player_one.co_ordinates[1][1]) + 2)
    intermediate_position = player_one.co_ordinates[1][0] + str(int(player_one.co_ordinates[1][1]) + 1)
    if (len(player_one.moves[0]) == 1) and (
            intermediate_position not in player_two.co_ordinates) and (
            final_position not in player_two.co_ordinates) and (
            intermediate_position not in player_one.co_ordinates and intermediate_position not in player_two.co_ordinates) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[1]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    return pawn_moves

def pawn_three(player_one, player_two):
    pawn_moves = []
    final_position = player_one.co_ordinates[2][0] + str(int(player_one.co_ordinates[2][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position not in player_two.co_ordinates and (
            int(player_one.co_ordinates[2][1]) + 1 < 9) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[2]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[2][0]) + 1) + str(int(player_one.co_ordinates[2][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[2]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[2][0]) - 1) + str(int(player_one.co_ordinates[2][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[2]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = player_one.co_ordinates[2][0] + str(int(player_one.co_ordinates[2][1]) + 2)
    intermediate_position = player_one.co_ordinates[2][0] + str(int(player_one.co_ordinates[2][1]) + 1)
    if (len(player_one.moves[0]) == 1) and (
            intermediate_position not in player_two.co_ordinates) and (
            final_position not in player_two.co_ordinates) and (
            intermediate_position not in player_one.co_ordinates and intermediate_position not in player_two.co_ordinates) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[2]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    return pawn_moves

def pawn_four(player_one, player_two):
    pawn_moves = []
    final_position = player_one.co_ordinates[1][0] + str(int(player_one.co_ordinates[3][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position not in player_two.co_ordinates and (
            int(player_one.co_ordinates[3][1]) + 1 < 9) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[3]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[3][0]) + 1) + str(int(player_one.co_ordinates[3][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[3]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[3][0]) - 1) + str(int(player_one.co_ordinates[3][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[3]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = player_one.co_ordinates[3][0] + str(int(player_one.co_ordinates[3][1]) + 2)
    intermediate_position = player_one.co_ordinates[3][0] + str(int(player_one.co_ordinates[3][1]) + 1)
    if (len(player_one.moves[0]) == 1) and (
            intermediate_position not in player_two.co_ordinates) and (
            final_position not in player_two.co_ordinates) and (
            intermediate_position not in player_one.co_ordinates and intermediate_position not in player_two.co_ordinates) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[3]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    return pawn_moves

def pawn_five(player_one, player_two):
    pawn_moves = []
    final_position = player_one.co_ordinates[4][0] + str(int(player_one.co_ordinates[4][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position not in player_two.co_ordinates and (
            int(player_one.co_ordinates[4][1]) + 1 < 9) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[4]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[4][0]) + 1) + str(int(player_one.co_ordinates[4][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[4]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[4][0]) - 1) + str(int(player_one.co_ordinates[4][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[4]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = player_one.co_ordinates[4][0] + str(int(player_one.co_ordinates[4][1]) + 2)
    intermediate_position = player_one.co_ordinates[4][0] + str(int(player_one.co_ordinates[4][1]) + 1)
    if (len(player_one.moves[0]) == 1) and (
            intermediate_position not in player_two.co_ordinates) and (
            final_position not in player_two.co_ordinates) and (
            intermediate_position not in player_one.co_ordinates and intermediate_position not in player_two.co_ordinates) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[4]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    return pawn_moves

def pawn_six(player_one, player_two):
    pawn_moves = []
    final_position = player_one.co_ordinates[5][0] + str(int(player_one.co_ordinates[5][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position not in player_two.co_ordinates and (
            int(player_one.co_ordinates[5][1]) + 1 < 9) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[5]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[5][0]) + 1) + str(int(player_one.co_ordinates[5][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[5]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[5][0]) - 1) + str(int(player_one.co_ordinates[5][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[5]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = player_one.co_ordinates[5][0] + str(int(player_one.co_ordinates[5][1]) + 2)
    intermediate_position = player_one.co_ordinates[5][0] + str(int(player_one.co_ordinates[5][1]) + 1)
    if (len(player_one.moves[0]) == 1) and (
            intermediate_position not in player_two.co_ordinates) and (
            final_position not in player_two.co_ordinates) and (
            intermediate_position not in player_one.co_ordinates and intermediate_position not in player_two.co_ordinates) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[5]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    return pawn_moves

def pawn_seven(player_one, player_two):
    pawn_moves = []
    final_position = player_one.co_ordinates[6][0] + str(int(player_one.co_ordinates[6][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position not in player_two.co_ordinates and (
            int(player_one.co_ordinates[6][1]) + 1 < 9) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[6]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[6][0]) + 1) + str(int(player_one.co_ordinates[6][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[6]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[6][0]) - 1) + str(int(player_one.co_ordinates[6][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[6]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = player_one.co_ordinates[6][0] + str(int(player_one.co_ordinates[6][1]) + 2)
    intermediate_position = player_one.co_ordinates[6][0] + str(int(player_one.co_ordinates[6][1]) + 1)
    if (len(player_one.moves[0]) == 1) and (
            intermediate_position not in player_two.co_ordinates) and (
            final_position not in player_two.co_ordinates) and (
            intermediate_position not in player_one.co_ordinates and intermediate_position not in player_two.co_ordinates) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[6]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    return pawn_moves

def pawn_eight(player_one, player_two):
    pawn_moves = []
    final_position = player_one.co_ordinates[7][0] + str(int(player_one.co_ordinates[7][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position not in player_two.co_ordinates and (
            int(player_one.co_ordinates[7][1]) + 1 < 9) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[7]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[7][0]) + 1) + str(int(player_one.co_ordinates[7][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[7]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = chr(ord(player_one.co_ordinates[7][0]) - 1) + str(int(player_one.co_ordinates[7][1]) + 1)
    if final_position not in player_one.co_ordinates and final_position in player_two.co_ordinates and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[7]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    final_position = player_one.co_ordinates[7][0] + str(int(player_one.co_ordinates[7][1]) + 2)
    intermediate_position = player_one.co_ordinates[7][0] + str(int(player_one.co_ordinates[7][1]) + 1)
    if (len(player_one.moves[0]) == 1) and (
            intermediate_position not in player_two.co_ordinates) and (
            final_position not in player_two.co_ordinates) and (
            intermediate_position not in player_one.co_ordinates and intermediate_position not in player_two.co_ordinates) and force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[7]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
        pawn_moves.append(final_position)
    return pawn_moves

def bishop_dark(player_one, player_two):
    bishop_d_one = []
    bishop_d_two = []
    bishop_d_three = []
    bishop_d_four = []

    # d_one
    i = 1
    while (ord(player_one.co_ordinates[10][0]) + i < 105) and (ord(player_one.co_ordinates[10][0]) + i > 96) and (
            int(player_one.co_ordinates[10][1]) + i < 9) and (int(player_one.co_ordinates[10][1]) + i > 0):
        final_position = chr(ord(player_one.co_ordinates[10][0]) + i) + str(
            int(player_one.co_ordinates[10][1]) + i)
        if force_generate_move(player_one,player_two,"p"+player_one.co_ordinates[10]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one):
            bishop_d_one.append(final_position)
        i += 1

    # d_two
    i = 1
    while (ord(player_one.co_ordinates[10][0]) - i < 105) and (ord(player_one.co_ordinates[10][0]) - i > 96) and (
            int(player_one.co_ordinates[10][1]) + i < 9) and (int(player_one.co_ordinates[10][1]) + i > 0):
        final_position = chr(ord(player_one.co_ordinates[10][0]) - i) + str(
            int(player_one.co_ordinates[10][1]) + i)
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[10] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            bishop_d_two.append(final_position)
        i += 1

    # d_three
    i = 1
    while (ord(player_one.co_ordinates[10][0]) - i < 105) and (ord(player_one.co_ordinates[10][0]) - i > 96) and (
            int(player_one.co_ordinates[10][1]) - i < 9) and (int(player_one.co_ordinates[10][1]) - i > 0):
        final_position = chr(ord(player_one.co_ordinates[10][0]) - i) + str(
            int(player_one.co_ordinates[10][1]) - i)
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[10] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            bishop_d_three.append(final_position)
        i += 1

    # d_four
    i = 1
    while (ord(player_one.co_ordinates[10][0]) + i < 105) and (ord(player_one.co_ordinates[10][0]) + i > 96) and (
            int(player_one.co_ordinates[10][1]) - i < 9) and (int(player_one.co_ordinates[10][1]) - i > 0):
        final_position = chr(ord(player_one.co_ordinates[10][0]) + i) + str(
            int(player_one.co_ordinates[10][1]) - i)
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[10] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            bishop_d_four.append(final_position)
        i += 1

    for i in range(len(bishop_d_one)):
        if bishop_d_one[i] in player_one.co_ordinates:
            bishop_d_one = bishop_d_one[:i]
            break
        if bishop_d_one[i] in player_two.co_ordinates:
            bishop_d_one = bishop_d_one[:i + 1]
            break

    for i in range(len(bishop_d_two)):
        if bishop_d_two[i] in player_one.co_ordinates:
            bishop_d_two = bishop_d_two[:i]
            break
        if bishop_d_two[i] in player_two.co_ordinates:
            bishop_d_two = bishop_d_two[:i + 1]
            break

    for i in range(len(bishop_d_three)):
        if bishop_d_three[i] in player_one.co_ordinates:
            bishop_d_three = bishop_d_three[:i]
            break
        if bishop_d_three[i] in player_two.co_ordinates:
            bishop_d_three = bishop_d_three[:i + 1]
            break

    for i in range(len(bishop_d_four)):
        if bishop_d_four[i] in player_one.co_ordinates:
            bishop_d_four = bishop_d_four[:i]
            break
        if bishop_d_four[i] in player_two.co_ordinates:
            bishop_d_four = bishop_d_four[:i + 1]
            break

    bishop_dark_moves = bishop_d_one + bishop_d_two + bishop_d_three + bishop_d_four
    return bishop_dark_moves

def bishop_light(player_one, player_two):
    bishop_d_one = []
    bishop_d_two = []
    bishop_d_three = []
    bishop_d_four = []

    # d_one
    i = 1
    while (ord(player_one.co_ordinates[13][0]) + i < 105) and (ord(player_one.co_ordinates[13][0]) + i > 96) and (
            int(player_one.co_ordinates[13][1]) + i < 9) and (int(player_one.co_ordinates[13][1]) + i > 0):
        final_position = chr(ord(player_one.co_ordinates[13][0]) + i) + str(
            int(player_one.co_ordinates[13][1]) + i)
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[13] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            bishop_d_one.append(final_position)
        i += 1

    # d_two
    i = 1
    while (ord(player_one.co_ordinates[13][0]) - i < 105) and (ord(player_one.co_ordinates[13][0]) - i > 96) and (
            int(player_one.co_ordinates[13][1]) + i < 9) and (int(player_one.co_ordinates[13][1]) + i > 0):
        final_position = chr(ord(player_one.co_ordinates[13][0]) - i) + str(
            int(player_one.co_ordinates[13][1]) + i)
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[13] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            bishop_d_two.append(final_position)
        i += 1

    # d_three
    i = 1
    while (ord(player_one.co_ordinates[13][0]) - i < 105) and (ord(player_one.co_ordinates[13][0]) - i > 96) and (
            int(player_one.co_ordinates[13][1]) - i < 9) and (int(player_one.co_ordinates[13][1]) - i > 0):
        final_position = chr(ord(player_one.co_ordinates[13][0]) - i) + str(
            int(player_one.co_ordinates[13][1]) - i)
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[13] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            bishop_d_three.append(final_position)
        i += 1

    # d_four
    i = 1
    while (ord(player_one.co_ordinates[13][0]) + i < 105) and (ord(player_one.co_ordinates[13][0]) + i > 96) and (
            int(player_one.co_ordinates[13][1]) - i < 9) and (int(player_one.co_ordinates[13][1]) - i > 0):
        final_position = chr(ord(player_one.co_ordinates[13][0]) + i) + str(
            int(player_one.co_ordinates[13][1]) - i)
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[13] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            bishop_d_one.append(final_position)
        i += 1

    for i in range(len(bishop_d_one)):
        if bishop_d_one[i] in player_one.co_ordinates:
            bishop_d_one = bishop_d_one[:i]
            break
        if bishop_d_one[i] in player_two.co_ordinates:
            bishop_d_one = bishop_d_one[:i + 1]
            break

    for i in range(len(bishop_d_two)):
        if bishop_d_two[i] in player_one.co_ordinates:
            bishop_d_two = bishop_d_two[:i]
            break
        if bishop_d_two[i] in player_two.co_ordinates:
            bishop_d_two = bishop_d_two[:i + 1]
            break

    for i in range(len(bishop_d_three)):
        if bishop_d_three[i] in player_one.co_ordinates:
            bishop_d_three = bishop_d_three[:i]
            break
        if bishop_d_three[i] in player_two.co_ordinates:
            bishop_d_three = bishop_d_three[:i + 1]
            break

    for i in range(len(bishop_d_four)):
        if bishop_d_four[i] in player_one.co_ordinates:
            bishop_d_four = bishop_d_four[:i]
            break
        if bishop_d_four[i] in player_two.co_ordinates:
            bishop_d_four = bishop_d_four[:i + 1]
            break

    bishop_light_moves = bishop_d_one + bishop_d_two + bishop_d_three + bishop_d_four
    return bishop_light_moves

def rook_one(player_one, player_two):
    rook_d_one = []
    rook_d_two = []
    rook_d_three = []
    rook_d_four = []
    # d_one
    i = 1
    while (ord(player_one.co_ordinates[8][0]) + i < 105) and (ord(player_one.co_ordinates[8][0]) + i > 96):
        final_position = chr(ord(player_one.co_ordinates[8][0]) + i) + player_one.co_ordinates[8][1]
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[8] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            rook_d_one.append(final_position)
        i += 1
    # d_two
    i = 1
    while (int(player_one.co_ordinates[8][1]) + i < 9) and (int(player_one.co_ordinates[8][1]) + i > 0):
        final_position = player_one.co_ordinates[8][0] + str(int(player_one.co_ordinates[8][1]) + i)
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[8] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            rook_d_two.append(final_position)
        i += 1
    # d_three
    i = 1
    while (ord(player_one.co_ordinates[8][0]) - i < 105) and (ord(player_one.co_ordinates[8][0]) - i > 96):
        final_position = chr(ord(player_one.co_ordinates[8][0]) - i) + (player_one.co_ordinates[8][1])
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[8] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            rook_d_three.append(final_position)
        i += 1
    # d_four
    i = 1
    while (int(player_one.co_ordinates[8][1]) - i < 9) and (int(player_one.co_ordinates[8][1]) - i > 0):
        final_position = chr(ord(player_one.co_ordinates[8][0])) + str(int(player_one.co_ordinates[8][1]) - i)
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[8] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            rook_d_four.append(final_position)
        i += 1
    for i in range(len(rook_d_one)):
        if rook_d_one[i] in player_one.co_ordinates:
            rook_d_one = rook_d_one[:i]
            break
        if rook_d_one[i] in player_two.co_ordinates:
            rook_d_one = rook_d_one[: i + 1]
            break
    for i in range(len(rook_d_two)):
        if rook_d_two[i] in player_one.co_ordinates:
            rook_d_two = rook_d_two[:i]
            break
        if rook_d_two[i] in player_two.co_ordinates:
            rook_d_two = rook_d_two[: i + 1]
            break
    for i in range(len(rook_d_three)):
        if rook_d_three[i] in player_one.co_ordinates:
            rook_d_three = rook_d_three[:i]
            break
        if rook_d_three[i] in player_two.co_ordinates:
            rook_d_three = rook_d_three[: i + 1]
            break
    for i in range(len(rook_d_four)):
        if rook_d_four[i] in player_one.co_ordinates:
            rook_d_four = rook_d_four[:i]
            break
        if rook_d_four[i] in player_two.co_ordinates:
            rook_d_four = rook_d_four[: i + 1]
            break
    rook_one_moves = rook_d_one + rook_d_two + rook_d_three + rook_d_four
    return rook_one_moves

def rook_two(player_one, player_two):
    rook_d_one = []
    rook_d_two = []
    rook_d_three = []
    rook_d_four = []
    # d_one
    i = 1
    while (ord(player_one.co_ordinates[15][0]) + i < 105) and (ord(player_one.co_ordinates[15][0]) + i > 96):
        final_position = chr(ord(player_one.co_ordinates[15][0]) + i) + player_one.co_ordinates[15][1]
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[15] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            rook_d_one.append(final_position)
        i += 1
    # d_two
    i = 1
    while (int(player_one.co_ordinates[15][1]) + i < 9) and (int(player_one.co_ordinates[15][1]) + i > 0):
        final_position = player_one.co_ordinates[15][0] + str(int(player_one.co_ordinates[15][1]) + i)
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[15] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            rook_d_two.append(final_position)
        i += 1
    # d_three
    i = 1
    while (ord(player_one.co_ordinates[15][0]) - i < 105) and (ord(player_one.co_ordinates[15][0]) - i > 96):
        final_position = chr(ord(player_one.co_ordinates[15][0]) - i) + (player_one.co_ordinates[15][1])
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[15] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            rook_d_three.append(final_position)
        i += 1
    # d_four
    i = 1
    while (int(player_one.co_ordinates[15][1]) - i < 9) and (int(player_one.co_ordinates[15][1]) - i > 0):
        final_position = chr(ord(player_one.co_ordinates[15][0])) + str(
            int(player_one.co_ordinates[15][1]) - i)
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[15] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            rook_d_four.append(final_position)
        i += 1
    for i in range(len(rook_d_one)):
        if rook_d_one[i] in player_one.co_ordinates:
            rook_d_one = rook_d_one[:i]
            break
        if rook_d_one[i] in player_two.co_ordinates:
            rook_d_one = rook_d_one[: i + 1]
            break
    for i in range(len(rook_d_two)):
        if rook_d_two[i] in player_one.co_ordinates:
            rook_d_two = rook_d_two[:i]
            break
        if rook_d_two[i] in player_two.co_ordinates:
            rook_d_two = rook_d_two[: i + 1]
            break
    for i in range(len(rook_d_three)):
        if rook_d_three[i] in player_one.co_ordinates:
            rook_d_three = rook_d_three[:i]
            break
        if rook_d_three[i] in player_two.co_ordinates:
            rook_d_three = rook_d_three[: i + 1]
            break
    for i in range(len(rook_d_four)):
        if rook_d_four[i] in player_one.co_ordinates:
            rook_d_four = rook_d_four[:i]
            break
        if rook_d_four[i] in player_two.co_ordinates:
            rook_d_four = rook_d_four[: i + 1]
            break
    rook_two_moves = rook_d_one + rook_d_two + rook_d_three + rook_d_four
    return rook_two_moves

def queen(player_one, player_two):
    bishop_d_one = []
    bishop_d_two = []
    bishop_d_three = []
    bishop_d_four = []
    rook_d_one = []
    rook_d_two = []
    rook_d_three = []
    rook_d_four = []

    # Bishop moves
    # d_one
    i = 1
    while ((ord(player_one.co_ordinates[11][0]) + i < 105)
            and (ord(player_one.co_ordinates[11][0]) + i > 96)
            and (int(player_one.co_ordinates[11][1]) + i < 9)
            and (int(player_one.co_ordinates[11][1]) + i > 0)):
        final_position = (chr(ord(player_one.co_ordinates[11][0]) + i) + str(
            int(player_one.co_ordinates[11][1]) + i))
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[11] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            bishop_d_one.append(final_position)
        i += 1
    # d_two
    i = 1
    while ((ord(player_one.co_ordinates[11][0]) - i < 105)
            and (ord(player_one.co_ordinates[11][0]) - i > 96)
            and (int(player_one.co_ordinates[11][1]) + i < 9)
            and (int(player_one.co_ordinates[11][1]) + i > 0)):
        final_position = (chr(ord(player_one.co_ordinates[11][0]) - i) + str(
            int(player_one.co_ordinates[11][1]) + i))
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[11] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            bishop_d_two.append(final_position)
        i += 1
    # d_three
    i = 1
    while ((ord(player_one.co_ordinates[11][0]) - i < 105)
            and (ord(player_one.co_ordinates[11][0]) - i > 96)
            and (int(player_one.co_ordinates[11][1]) - i < 9)
            and (int(player_one.co_ordinates[11][1]) - i > 0)):
        final_position = (chr(ord(player_one.co_ordinates[11][0]) - i) + str(
            int(player_one.co_ordinates[11][1]) - i))
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[11] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            bishop_d_three.append(final_position)
        i += 1
    # d_four
    i = 1
    while ((ord(player_one.co_ordinates[11][0]) + i < 105)
            and (ord(player_one.co_ordinates[11][0]) + i > 96)
            and (int(player_one.co_ordinates[11][1]) - i < 9)
            and (int(player_one.co_ordinates[11][1]) - i > 0)):
        final_position = (chr(ord(player_one.co_ordinates[11][0]) + i) + str(
            int(player_one.co_ordinates[11][1]) - i))
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[11] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            bishop_d_four.append(final_position)
        i += 1

    for i in range(len(bishop_d_one)):
        if bishop_d_one[i] in player_one.co_ordinates:
            bishop_d_one = bishop_d_one[:i]
            break
        if bishop_d_one[i] in player_two.co_ordinates:
            bishop_d_one = bishop_d_one[:i + 1]
            break
    for i in range(len(bishop_d_two)):
        if bishop_d_two[i] in player_one.co_ordinates:
            bishop_d_two = bishop_d_two[:i]
            break
        if bishop_d_two[i] in player_two.co_ordinates:
            bishop_d_two = bishop_d_two[:i + 1]
            break
    for i in range(len(bishop_d_three)):
        if bishop_d_three[i] in player_one.co_ordinates:
            bishop_d_three = bishop_d_three[:i]
            break
        if bishop_d_three[i] in player_two.co_ordinates:
            bishop_d_three = bishop_d_three[:i + 1]
            break
    for i in range(len(bishop_d_four)):
        if bishop_d_four[i] in player_one.co_ordinates:
            bishop_d_four = bishop_d_four[:i]
            break
        if bishop_d_four[i] in player_two.co_ordinates:
            bishop_d_four = bishop_d_four[:i + 1]
            break

    bishop_moves = bishop_d_one + bishop_d_two + bishop_d_three + bishop_d_four

    # Rook moves
    # d_one
    i = 1
    while ((ord(player_one.co_ordinates[11][0]) + i < 105)
            and (ord(player_one.co_ordinates[11][0]) + i > 96)):
        final_position = (chr(ord(player_one.co_ordinates[11][0]) + i) +
                          player_one.co_ordinates[11][1])
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[11] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            rook_d_one.append(final_position)
        i += 1
    # d_two
    i = 1
    while ((int(player_one.co_ordinates[11][1]) + i < 9)
            and (int(player_one.co_ordinates[11][1]) + i > 0)):
        final_position = (player_one.co_ordinates[11][0] +
                          str(int(player_one.co_ordinates[11][1]) + i))
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[11] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            rook_d_two.append(final_position)
        i += 1
    # d_three
    i = 1
    while ((ord(player_one.co_ordinates[11][0]) - i < 105)
            and (ord(player_one.co_ordinates[11][0]) - i > 96)):
        final_position = (chr(ord(player_one.co_ordinates[11][0]) - i) +
                          (player_one.co_ordinates[11][1]))
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[11] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            rook_d_three.append(final_position)
        i += 1
    # d_four
    i = 1
    while ((int(player_one.co_ordinates[11][1]) - i < 9)
            and (int(player_one.co_ordinates[11][1]) - i > 0)):
        final_position = (chr(ord(player_one.co_ordinates[11][0])) +
                          str(int(player_one.co_ordinates[11][1]) - i))
        if force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[11] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one):
            rook_d_four.append(final_position)
        i += 1

    for i in range(len(rook_d_one)):
        if rook_d_one[i] in player_one.co_ordinates:
            rook_d_one = rook_d_one[:i]
            break
        if rook_d_one[i] in player_two.co_ordinates:
            rook_d_one = rook_d_one[:i + 1]
            break
    for i in range(len(rook_d_two)):
        if rook_d_two[i] in player_one.co_ordinates:
            rook_d_two = rook_d_two[:i]
            break
        if rook_d_two[i] in player_two.co_ordinates:
            rook_d_two = rook_d_two[:i + 1]
            break
    for i in range(len(rook_d_three)):
        if rook_d_three[i] in player_one.co_ordinates:
            rook_d_three = rook_d_three[:i]
            break
        if rook_d_three[i] in player_two.co_ordinates:
            rook_d_three = rook_d_three[:i + 1]
            break
    for i in range(len(rook_d_four)):
        if rook_d_four[i] in player_one.co_ordinates:
            rook_d_four = rook_d_four[:i]
            break
        if rook_d_four[i] in player_two.co_ordinates:
            rook_d_four = rook_d_four[:i + 1]
            break

    rook_moves = rook_d_one + rook_d_two + rook_d_three + rook_d_four
    queen_moves = bishop_moves + rook_moves
    return queen_moves

def knight_one(player_one, player_two):
    knight_moves = []
    moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    for x, y in moves:
        final_position = (
            chr(ord(player_one.co_ordinates[9][0]) + x) +
            str(int(player_one.co_ordinates[9][1]) + y)
        )
        if (
            96 < ord(player_one.co_ordinates[9][0]) + x < 105
            and 0 < int(player_one.co_ordinates[9][1]) + y < 9
            and final_position not in player_one.co_ordinates and force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[11] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one)
        ):
            knight_moves.append(final_position)

    return knight_moves


def knight_two(player_one, player_two):
    knight_moves = []
    moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    for x, y in moves:
        final_position = (
            chr(ord(player_one.co_ordinates[14][0]) + x) +
            str(int(player_one.co_ordinates[14][1]) + y)
        )
        if (
            96 < ord(player_one.co_ordinates[14][0]) + x < 105
            and 0 < int(player_one.co_ordinates[14][1]) + y < 9
            and final_position not in player_one.co_ordinates and force_generate_move(player_one, player_two, "p" + player_one.co_ordinates[11] + final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two, player_one)
        ):
            knight_moves.append(final_position)

    return knight_moves

def king(player_one,player_two):
    king_moves = []
    moves=[[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
    for x,y in moves:
        final_position = (chr(ord(player_one.co_ordinates[12][0]) + x) + str(int(player_one.co_ordinates[12][1]) + y))
        #force_generate_move(player_one,player_two)
        if (96 < ord(player_one.co_ordinates[12][0]) + x < 105 and 0 < int(player_one.co_ordinates[12][1]) + y < 9 and (final_position not in player_one.co_ordinates) and force_generate_move(player_one,player_two,"k"+player_one.co_ordinates[12]+final_position)[0].co_ordinates[12] not in all_possible_except_king(player_two,player_one)):
            king_moves.append(final_position)
        return king_moves

def func_list():
    func=[pawn_one,pawn_two,pawn_three,pawn_four,pawn_five,pawn_six,pawn_seven,pawn_eight,rook_one,knight_one,bishop_dark,queen,king,bishop_light,knight_two,rook_two]
    return func

def all_possible_except_king(player_one,player_two):
    possible = pawn_one(player_one,player_two) + pawn_two(player_one,player_two) + pawn_three(player_one,player_two) + pawn_four(player_one,player_two) + pawn_five(player_one,player_two) + pawn_six(player_one,player_two) + pawn_seven(player_one,player_two) + pawn_eight(player_one,player_two) + rook_one(player_one,player_two) + rook_two(player_one,player_two) + bishop_light(player_one,player_two) + bishop_dark(player_one,player_two) + knight_one(player_one,player_two) + knight_two(player_one,player_two)
    return possible
