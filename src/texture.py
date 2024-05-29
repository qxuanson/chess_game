import pygame

white_pawn = pygame.image.load("./images/wp.png")
white_bishop = pygame.image.load("./images/wB.png")
white_knight = pygame.image.load("./images/wN.png")
white_rook = pygame.image.load("./images/wR.png")
white_queen = pygame.image.load("./images/wQ.png")
white_king = pygame.image.load("./images/wK.png")

black_pawn = pygame.image.load("./images/bp.png")
black_bishop = pygame.image.load("./images/bB.png")
black_knight = pygame.image.load("./images/bN.png")
black_rook = pygame.image.load("./images/bR.png")
black_queen = pygame.image.load("./images/bQ.png")
black_king = pygame.image.load("./images/bK.png")
elements = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']

def GetSprite(piece):
    sprite = None
    if piece == 'wp':
        sprite = white_pawn
    elif piece == 'wR':
        sprite = white_rook
    elif piece == 'wN':
        sprite = white_knight
    elif piece == 'wB':
        sprite = white_bishop
    elif piece == 'wK':
        sprite = white_king
    elif piece == 'wQ':
        sprite = white_queen
    elif piece == 'bp':
        sprite = black_pawn
    elif piece == 'bR':
        sprite = black_rook
    elif piece == 'bN':
        sprite = black_knight
    elif piece == 'bB':
        sprite = black_bishop
    elif piece == 'bK':
        sprite = black_king
    elif piece == 'bQ':
        sprite = black_queen
    transformed = pygame.transform.smoothscale(sprite, (100, 100))
    return transformed