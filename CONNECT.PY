import numpy as np
import pygame as pygame
import sys
import math
ROW_COUNT=6
COLUMN_COUNT=7
BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)
SQUARE=100
RADIUS=int(SQUARE/2-5)
width=COLUMN_COUNT*SQUARE        
height=ROW_COUNT*SQUARE   
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board,row,col,piece):
    board[row][col]=piece
def is_valid_locator(board, col):
    return board[5][col] == 0
def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r
def print_board(board):
    print(np.flip(board,0))
def winning(board,piece):
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BLUE,(c*SQUARE,r*SQUARE+SQUARE,SQUARE,SQUARE))
            pygame.draw.circle(screen,BLACK,(int(c*SQUARE+SQUARE/2),int(r*SQUARE+SQUARE*(3/2))),RADIUS)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c]==1: 
                pygame.draw.circle(screen,RED,(int(c*SQUARE+SQUARE/2),height-int(r*SQUARE+SQUARE*(1/2))),RADIUS)
            elif board[r][c]==2: 
                pygame.draw.circle(screen,YELLOW,(int(c*SQUARE+SQUARE/2),height-int(r*SQUARE+SQUARE*(1/2))),RADIUS)
            
    pygame.display.update()

board = create_board()
pygame.init()
myFont=pygame.font.SysFont("monospace",75)
size=(width,height)
screen=pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

game_over = False
turn = 0
while not game_over:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            pygame.draw.rect(screen,BLACK,(0,0,width,SQUARE))
            posx=event.pos[0]
            if turn==0:
                pygame.draw.circle(screen,RED,(posx,int(SQUARE/2)),RADIUS)
            elif turn==1:   
                pygame.draw.circle(screen,YELLOW,(posx,int(SQUARE/2)),RADIUS)
            pygame.display.update()

        if event.type==pygame.MOUSEBUTTONDOWN:    
            if turn == 0:
                posx=event.pos[0]
                col=int(math.floor(posx/SQUARE))
                if is_valid_locator(board,col):
                    row=get_next_open_row(board,col)
                    drop_piece(board,row,col,1)
            if turn == 1:
                posx=event.pos[0]
                col=int(math.floor(posx/SQUARE))
                if is_valid_locator(board,col):
                    row=get_next_open_row(board,col)
                    drop_piece(board,row,col,2)
            if winning(board,turn+1):
                label=myFont.render("Player "+str(turn+1)+" Won",1,BLUE)
                screen.blit(label,(40,10))
                game_over=True        
            print_board(board)
            draw_board(board)
            turn += 1
            turn %= 2
            if game_over:
                pygame.time.wait(3000)
