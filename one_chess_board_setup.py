import copy
class chess_player:
    def __init__(self,color):
        self.color=color
        self.moves=[[] for i in range(16)]
        self.co_ordinates=None
    def setup(self):
        if self.color.lower()=="white":
            #pawn_1,pawn_2,pawn_3,pawn_4,pawn_5,pawn_6,pawn_7,pawn_8,rook_1,knight_1,bishop_dark,queen,king,bishop_light,knight_2,rook_2
            self.moves=[["a2"],["b2"],["c2"],["d2"],["e2"],["f2"],["g2"],["h2"],["a1"],["b1"],["c1"],["d1"],["e1"],["f1"],["g1"],["h1"]]
            self.co_ordinates = ["a2","b2","c2","d2","e2","f2","g2","h2","a1","b1","c1","d1","e1","f1","g1","h1"]
        elif self.color.lower()=="black":
            #pawn_1,pawn_2,pawn_3,pawn_4,pawn_5,pawn_6,pawn_7,pawn_8,rook_1,knight_1,bishop_dark,queen,king,bishop_light,knight_2,rook_2
            self.moves=[["a7"],["b7"],["c7"],["d7"],["e7"],["f7"],["g7"],["h7"],["a8"],["b8"],["c8"],["d8"],["e8"],["f8"],["g8"],["h8"]]
            self.co_ordinates = ["a7","b7","c7","d7","e7","f7","g7","h7","a8","b8","c8","d8","e8","f8","g8","h8"]
        else:
            raise Exception("color not valid")
    def make_copy(self):
        copied_player=copy.copy(self)
        return copied_player





#player_1=chess_player("white")
#player_1.setup()
#print(player_1.co_ordinates)
