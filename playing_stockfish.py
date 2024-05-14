'''
import chess
import chess.engine

def play_chess():
    # Set up the chess board
    board = chess.Board()

    # Set up the Stockfish engine
    stockfish_path = "/home/stockfish/stockfish/stockfish-ubuntu-x86-64-avx2"  # Update this with the path to your Stockfish binary
    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        while not board.is_game_over():
            # Display the current board
            print(board)

            # Get the FEN of the current position
            fen = board.fen()

            # Make a move using Stockfish
            result = engine.play(board, chess.engine.Limit(time=1.0))  # Adjust time limit as needed
            best_move = result.move

            # Make the move on the board
            board.push(best_move)

            # Wait for user input (you can replace this with an AI player)
            input("Press Enter for the opponent's move...")

    # Display the final board
    print("Game Over")
    print(board)

if __name__ == "__main__":
    play_chess()
'''
print(chr(104))
l=[1,2,3,4]
l=l[:4]
print(l)
l=[[] for i in range(16) ]
print(l)
class test:
    def __init__(self):
        self.hi=1
        self.wow=2
        self.bye=3
        self.l=[self.hi,self.wow,self.bye]
    def do_one(self):
        print("hello")
        return
    def do_two(self):
        print("hi")
        return
    def func_list(self):
        l=[self.do_one,self.do_two]
        return l
o=test()
print(o.func_list()[0]())
print(chr(97))
print(chr(104))