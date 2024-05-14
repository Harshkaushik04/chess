from one_chess_board_setup import chess_player
from six_new_tryping_seperate import force_generate_move,pawn_one,pawn_two,pawn_three,pawn_four,pawn_five,pawn_six,pawn_seven,pawn_eight,bishop_dark,rook_one,rook_two,knight_one,knight_two,king,queen,bishop_light,all_possible,func_list,possible_moves_list
def generate_position(player_one,player_two,move):
    played_move=False
    if len(move) == 5 and (move[3:] not in player_one.co_ordinates):
        piece=move[0]
        initial_position=move[1:3]
        final_position=move[3:]
        if piece.lower() == "p":
            flag=False
            for i in range(len(player_one.co_ordinates)):
                #print(player_one_possible_moves.func_list()[i]())
                if initial_position == player_one.co_ordinates[i] and (final_position in func_list()[i](player_one,player_two)) and i<8:
                    player_one.moves[i].append(final_position)
                    player_one.co_ordinates[i]=final_position
                    played_move=True
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
            if initial_position == player_one.co_ordinates[8] and (final_position in func_list()[8](player_one,player_two)):
                    player_one.moves[8].append(final_position)
                    player_one.co_ordinates[8]=final_position
                    played_move=True
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            elif initial_position == player_one.co_ordinates[15] and (final_position in func_list()[15](player_one,player_two)):
                    #print(player_one_possible_moves.func_list()[15]())
                    player_one.moves[15].append(final_position)
                    player_one.co_ordinates[15]=final_position
                    played_move=True
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            else:
                print("move is not legal")
                # continue ,if we were in game loop,also make seperate game loops for black and white(some condition for exit) and one common
        elif piece.lower()=="b":
            if initial_position == player_one.co_ordinates[10] and (final_position in func_list()[10](player_one,player_two)):
                    player_one.moves[10].append(final_position)
                    player_one.co_ordinates[10]=final_position
                    played_move=True
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            elif initial_position == player_one.co_ordinates[13] and (final_position in func_list()[13](player_one,player_two)):
                    #print(player_one_possible_moves.func_list()[13]())
                    player_one.moves[13].append(final_position)
                    player_one.co_ordinates[13]=final_position
                    played_move=True
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            else:
                print("move is not legal")
                # continue ,if we were in game loop,also make seperate game loops for black and white(some condition for exit) and one common
        elif piece.lower()=="n":
            if initial_position == player_one.co_ordinates[9] and (final_position in func_list()[9](player_one,player_two)):
                    player_one.moves[9].append(final_position)
                    player_one.co_ordinates[9]=final_position
                    played_move=True
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            elif initial_position == player_one.co_ordinates[14] and (final_position in func_list()[14](player_one,player_two)):
                    #print(player_one_possible_moves.func_list()[14]())
                    player_one.moves[14].append(final_position)
                    player_one.co_ordinates[14]=final_position
                    played_move=True
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            else:
                print("move is not legal")
                # continue ,if we were in game loop,also make seperate game loops for black and white(some condition for exit) and one common
        elif piece.lower()=="q":
            if initial_position == player_one.co_ordinates[11] and (final_position in func_list()[11](player_one,player_two)):
                    player_one.moves[11].append(final_position)
                    player_one.co_ordinates[11]=final_position
                    played_move=True
                    for j in range(len(player_two.co_ordinates)):
                        if final_position==player_two.co_ordinates[j]:
                            player_two.co_ordinates[j]=None
                            break
            else:
                print("move is not legal")
                # continue ,if we were in game loop,also make seperate game loops for black and white(some condition for exit) and one common
        elif piece.lower() == "k":
            if initial_position == player_one.co_ordinates[12] and (
                    final_position in func_list()[12](player_one, player_two)):
                player_one.moves[12].append(final_position)
                player_one.co_ordinates[12] = final_position
                played_move=True
                for j in range(len(player_two.co_ordinates)):
                    if final_position == player_two.co_ordinates[j]:
                        player_two.co_ordinates[j] = None
                        break
            else:
                print("move is not legal")
                # continue ,if we were in game loop,also make seperate game loops for black and white(some condition for exit) and one common
        elif move=="o-o-o" and player_one.color=="white":
            in_between_squares=["b1","c1","d1"]
            if len(player_one.moves[12])==1 and len(player_one.moves[8])==1 and (set(in_between_squares) & set(player_one.co_ordinates)=={}) and (set(in_between_squares+[player_one.co_ordinates[12]])&set(all_possible(player_two,player_one)+player_two.co_ordinates) is {}):
                player_one.co_ordinates[12]="c1"
                player_one.co_ordinates[8]="d1"
                player_one.moves[12].append("c1")
                player_one.moves[8].append("d1")
                played_move=True
            else:
                print("move is not legal")
        elif move=="o-o-o" and player_one.color=="black":
            in_between_squares=["b8","c8","d8"]
            if len(player_one.moves[12])==1 and len(player_one.moves[8])==1 and (set(in_between_squares) & set(player_one.co_ordinates)=={}) and (set(in_between_squares+[player_one.co_ordinates[12]])&set(all_possible(player_two,player_one)+player_two.co_ordinates) is {}):
                player_one.co_ordinates[12]="c8"
                player_one.co_ordinates[8]="d8"
                player_one.moves[12].append("c8")
                player_one.moves[8].append("d8")
                played_move=True
            else:
                print("move is not legal")
        else:
            print("move not legal or maybe bug") #game in developing phase
    elif len(move) == 3:
        if move=="o-o" and player_one.color=="white":
            in_between_squares=["f1","g1"]
            if len(player_one.moves[12])==1 and len(player_one.moves[15])==1 and (set(in_between_squares) & set(player_one.co_ordinates)=={}) and (set(in_between_squares+[player_one.co_ordinates[12]])&set(all_possible(player_two,player_one)+player_two.co_ordinates) is {}):
                player_one.co_ordinates[12]="g1"
                player_one.co_ordinates[8]="f1"
                player_one.moves[12].append("g1")
                player_one.moves[8].append("f1")
                played_move=True
            elif move == "o-o" and player_one.color == "black":
                in_between_squares = ["f8", "g8"]
                if len(player_one.moves[12]) == 1 and len(player_one.moves[15]) == 1 and (
                        set(in_between_squares) & set(player_one.co_ordinates) == {}) and (
                        set(in_between_squares + [player_one.co_ordinates[12]]) & set(
                        all_possible(player_two, player_one) + player_two.co_ordinates) is {}):
                    player_one.co_ordinates[12] = "g8"
                    player_one.co_ordinates[15] = "f8"
                    player_one.moves[12].append("g8")
                    player_one.moves[15].append("f8")
                    played_move = True
            else:
                print("move is not legal")
    else:
        print("move not legal or maybe bug") #game in developing phase
    return played_move
class game:
    def __init__(self, white, black):  # white and black are objects of class chess_player
        self.player_one = white
        self.player_two = black
        self.white_moves=None
        self.black_moves=None
    def start_game(self):
        print("Chess game starts now\nRules:\n(1)To make a move simply write (piece name)+(initial position of piece)+(final position of piece)\nFor example for moving pawn from e2 to e4 simply write pe2e4\n(2)Chess pieces shortforms are:\npawn:p\nking:k\nqueen:q\nrook:r\nbishop:b\nknight:n\n(3)For king side castling: o-o\n   For queen side castling: o-o-o\n(4)if a move is not legal it will be displayed so and you will be promted to play move again")
        print("==================================================================")
        while True:
            played_white_move_bool = False
            while played_white_move_bool is False:
                white_move=input("Enter white's move:")
                played_white_move_bool=generate_position(self.player_one,self.player_two,white_move)
                print("==================================================================")
                print(f"White pieces position:{self.player_one.co_ordinates}\nBlack pieces position:{self.player_two.co_ordinates}")
                print("==================================================================")
                print(f"White places gone till now:{self.player_one.moves}\nBlack places gone till now:{self.player_two.moves}")
                print("==================================================================")
                print(f"White pieces possible moves list:{possible_moves_list(player_one,player_two)}\nBlack pieces possible moves list:{possible_moves_list(player_two,player_one)}")
                print("==================================================================")
            if set(king(self.player_two,self.player_one)+[self.player_two.co_ordinates[12]]).issubset(set(all_possible(self.player_one,self.player_two))) is True:
                print("Black is checkmated")
                print("White won!\nGame ends")
                print("==================================================================")
                break
            played_black_move_bool=False
            while played_black_move_bool is False:
                black_move=input("Enter black's move:")
                played_black_move_bool=generate_position(self.player_two,self.player_one,black_move)
                print("==================================================================")
                print(f"White pieces position:{self.player_one.co_ordinates}\nBlack pieces position:{self.player_two.co_ordinates}")
                print("==================================================================")
                print(f"White places gone till now:{self.player_one.moves}\nBlack places gone till now:{self.player_two.moves}")
                print("==================================================================")
                print(f"White pieces possible moves list:{possible_moves_list(player_one, player_two)}\nBlack pieces possible moves list:{possible_moves_list(player_two, player_one)}")
                print("==================================================================")
            if set(king(self.player_one,self.player_two)+[self.player_one.co_ordinates[12]]).issubset(set(all_possible(self.player_two,self.player_one))) is True:
                print("White is checkmated")
                print("Black won!\nGame ends")
                print("==================================================================")
                break
player_one=chess_player("white")
player_one.setup()
player_two=chess_player("black")
player_two.setup()
first_battle=game(player_one,player_two)
first_battle.start_game()
