from typing import List
import copy

class ChessPiece:
    def __init__(self,name:str,color:str,position:str):
        self.name=name
        self.color=color
        self.position=position
    
    def display(self):
        print(f"{self.color} {self.name} has position {self.position}")
    
    
        

class ChessBoard:
    def __init__(self):
        self.pieces:List[ChessPiece]=[]
    
    def add_piece(self,piece:ChessPiece):
        self.pieces.append(piece)
    
    def display_board(self):
        for piece in self.pieces:
            piece.display()
        
    def clone(self):
        return copy.deepcopy(self)   

piece1=ChessPiece("King","Black","d5")
piece2=ChessPiece("King","White","d6")
piece3=ChessPiece("Queen","Black","d8")
piece4=ChessPiece("Queen","Black","d1")

board=ChessBoard()
board.add_piece(piece1)
board.add_piece(piece2)
board.add_piece(piece3)
board.add_piece(piece4)

board.display_board()

##now copying the new board for the new itertion 
new_chess_board=board.clone()
new_piece=ChessPiece('soldier','white','d9')
new_chess_board.add_piece(new_piece)

print("----------------------------")
new_chess_board.display_board()