# Main driver file
import pygame as p
import ChessEngine
from pygame import mixer

gs = ChessEngine.GameState()
board = gs.board
WIDTH = HEIGHT = 512
DIMENSION = 8 # มิติ
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

p.init()
# title
p.display.set_caption('Chess')
# icon
icon = p.image.load('images/ChessIcon.png')
p.display.set_icon(icon)

wtf = p.image.load('images/wQ.png')

# Load images
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK','wp2','bp2']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))

def gameIntro():
    intro = True
    screen = p.display.set_mode((800, 700))
    while intro:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()

        # image
        background = p.image.load('images/bg4.jpg')
        background_new = p.transform.scale(background, (1366, 768))
        screen.blit(background_new, (0, 0))

        icon = p.image.load('images/iconIntro.png')
        icon_new = p.transform.scale(icon, (362-100, 512-100))
        screen.blit(icon_new, (280, 20))

        # button
        button("PLAY", 300, 400, 220, 80, (92, 145, 101), (255, 160, 122), main)
        button("INFO", 300, 500, 220, 80, (92, 145, 101), (255, 160, 122), gameInfo)
        p.display.update()

def gameInfo():
    info = True
    screen = p.display.set_mode((800, 600))
    while info:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()
        # image
        infobg = p.image.load('images/infobg.png')
        infobgnew = p.transform.scale(infobg, (800, 600))
        screen.blit(infobgnew, (0, 0))
        #button
        button("BACK",50,530,150,60, (92, 145, 101), (255,215,0), gameIntro)
        p.display.update()

def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    board = gs.board
    possibleMoves = gs.getAllPossibleMoves()
    moveMade = False # flag variable for whan a move is made
    animate =  False # flag variable for when we should animate move
    musicOn = False
    loadImages()
    running = True
    sqSelected = () # no square is selected(keep of the last  click of the user(turple: (row, col))
    playerClicks = [] # keep track of player click (two turples: [(6, 4, (4, 4])
    gameOver = False
    choose = False
    gamePause = False
    undoMove = True
    # promosion
    Queen = p.transform.scale(p.image.load('images/' + 'queen' + '.png'), (100,100))
    Rook = p.transform.scale(p.image.load('images/' + 'rook' + '.png'), (100,100))
    Knight = p.transform.scale(p.image.load('images/' + 'knight' + '.png'), (100,100))
    Bishop = p.transform.scale(p.image.load('images/' + 'bishop' + '.png'), (100,100))
    rectQ = p.Rect((100,150), (100,100))
    rectR = p.Rect((100, 300), (100, 100))
    rectN = p.Rect((300, 150), (100, 100))
    rectB = p.Rect((300, 300), (100, 100))
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                p.quit()
                quit()
            #mouse handle
            elif e.type == p.MOUSEBUTTONDOWN:
                if not gameOver and not gamePause:
                    location = p.mouse.get_pos() # (x, y) location of mouse
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    if sqSelected == (row, col): # the user click the same square twice
                        sqSelected = () # delected
                        playerClicks = [] # clear player clicks
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected) # append of 1st and 2nd clicks
                    if len(playerClicks) == 2: # after 2nd click
                        move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                        print(move.getChessNotation())
                        for i in range(len(validMoves)):
                            if move == validMoves[i]:
                                gs.makeMove(validMoves[i])
                                moveMade = True
                                animate = True
                                sqSelected = () # reset user clicks
                                playerClicks = []
                        if not moveMade:
                            playerClicks = [sqSelected]
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z and not gameOver:  # undo move when pressed 'z'
                    gs.undoMove()
                    moveMade = True
                    animate = False
                    gamePause = False
                    choose = False
                elif e.key == p.K_r: # reset the game when press 'r'
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelected = ()
                    playerClicks = []
                    moveMade = False
                    animate = False
                    gameOver = False
                    gamePause = False
                    choose = False
                    main()
        if moveMade:
            if animate:
                animateMove(gs.moveLog[-1], screen, gs.board, clock)
            validMoves = gs.getValidMoves()
            if not gs.inCheck():
                playSound('move.mp3', 0)
            moveMade = False
            animate = False
        drawGameState(screen, gs, validMoves, sqSelected)
        if gs.checkMate:
            if not musicOn:
                playSound('checkMate.mp3', 0)
            if gs.whiteToMove:
                drawText(screen, 'Black win')
            else:
                drawText(screen, 'White win')
            musicOn = True
            gameOver = True
        elif gs.staleMate:
            gameOver = True
            drawText(screen, 'Stalemate')
        elif gs.inCheck():
            isCheck(screen, board, gs)
            if not musicOn:
                playSound('check.mp3', 0)
            musicOn = True
        elif not gs.checkMate or not gs.inCheck():
            musicOn = False
        if len(gs.moveLog) != 0:
            check = ((move.pieceMoved == 'wp' and move.endRow == 0) or (move.pieceMoved == 'bp' and move.endRow == 7))
            if not check:
                choose = False
            elif (gs.moveLog[-1].isPawnPromotion and not choose) and check:
                gamePause = True
                hightLight(WIDTH, HEIGHT, 100, 'white', screen, 0, 0)
                screen.blit(Queen, rectQ)
                screen.blit(Rook, rectR)
                screen.blit(Knight, rectN)
                screen.blit(Bishop, rectB)
                if e.type == p.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        if rectQ.collidepoint(e.pos):
                            board[move.endRow][move.endCol] = move.pieceMoved[0] + 'Q'
                            choose = True
                            gamePause = False
                        elif rectR.collidepoint(e.pos):
                            board[move.endRow][move.endCol] = move.pieceMoved[0] + 'R'
                            choose = True
                            gamePause = False
                        elif rectN.collidepoint(e.pos):
                            board[move.endRow][move.endCol] = move.pieceMoved[0] + 'N'
                            choose = True
                            gamePause = False
                        elif rectB.collidepoint(e.pos):
                            board[move.endRow][move.endCol] = move.pieceMoved[0] + 'B'
                            choose = True
                            gamePause = False
        clock.tick(MAX_FPS)
        p.display.update()

# Hightlight square selected and moves for piece selected
def hightlightSquares(screen, gs, validMoves, sqSelected):
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'): #sqSelected is a piece that can be move
            # hightlight select square
            s = p.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(120) # transperancy value > 0 transparent; 255 opeaque
            s.fill(p.Color('yellow'))
            screen.blit(s, (c*SQ_SIZE, r*SQ_SIZE))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    #print(move.startRow, move.startCol)
                    if gs.board[move.endRow][move.endCol][0] == 'b' or gs.board[move.endRow][move.endCol][0] == 'w':
                        screen.blit(s, (move.endCol * SQ_SIZE, move.endRow * SQ_SIZE))
                    if screen.get_at((move.endCol * SQ_SIZE + 33, move.endRow * SQ_SIZE + 33)) == p.Color(238, 238, 210):
                        p.draw.circle(screen, p.Color(214, 214, 189), (move.endCol * SQ_SIZE + 33, move.endRow * SQ_SIZE + 33), 10)
                    elif screen.get_at((move.endCol * SQ_SIZE + 33, move.endRow * SQ_SIZE + 33)) == p.Color(118, 150, 86):
                        p.draw.circle(screen, p.Color(106, 135, 77), (move.endCol * SQ_SIZE + 33, move.endRow * SQ_SIZE + 33), 10)
                    #elif screen.get_at((move.endCol * SQ_SIZE + 33, move.endRow * SQ_SIZE + 33)) == p.Color(118, 150, 86):
                    # pass
                    #     #(238, 238, 210)
                    # print((move.endCol * SQ_SIZE+30, move.endRow * SQ_SIZE))
                    #print('color',screen.get_at_mapped((move.endCol * SQ_SIZE+30, move.endRow * SQ_SIZE +20)))
                    #print('size',(move.endCol * SQ_SIZE, move.endRow * SQ_SIZE))
                    # print()
                    #print('color', screen.get_at((98, 102)))
                    #p.draw.circle(screen, (214, 214, 189), (move.endCol * SQ_SIZE + 33, move.endRow * SQ_SIZE + 33), 15)
                    #screen.blit(s, (move.endCol * SQ_SIZE, move.endRow * SQ_SIZE))


# Responsoble for all graphic with a current game state
def drawGameState(screen, gs, validMoves, sqSelected):
    drawBoard(screen) # draw square on the board
    hightlightSquares(screen, gs, validMoves, sqSelected)
    drawPieces(screen, gs.board) # draw pieces on top of those square

# draw square on board // The top left square always light
def drawBoard(screen):
    global colors
    colors = [p.Color(238, 238, 210), p.Color(118, 150, 86)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

# draw the pieces on board using GameState.board
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--': # not empty square
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Animating a move
def animateMove(move, screen, board, clock):
    global colors
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol
    framesPerSquare = 10 #frames to move one square
    frameCount = (abs(dR) + abs(dC)) * framesPerSquare
    for frame in range(frameCount + 1):
        r,c = (move.startRow + dR*frame/frameCount, move.startCol + dC*frame/frameCount)
        drawBoard(screen)
        drawPieces(screen, board)
        # erease the piece moved from its ending square
        color = colors[(move.endRow + move.endCol) % 2]
        endSquare = p.Rect(move.endCol*SQ_SIZE, move.endRow*SQ_SIZE, SQ_SIZE, SQ_SIZE)
        p.draw.rect(screen, color, endSquare)
        # draw capture piece onto rectangle
        if move.pieceCaptured != '--':
            screen.blit(IMAGES[move.pieceCaptured], endSquare)
        # draw moving piece
        screen.blit(IMAGES[move.pieceMoved], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
        p.display.flip()
        clock.tick(360)

def drawText(screen, text):
    font = p.font.Font('8-BIT WONDER.TTF', 50)
    if text == 'Black win':
        hightLight(WIDTH, HEIGHT, 100, 'white', screen, 0, 0)
        textObject = font.render(text, 0, p.Color('black'))
    else:
        hightLight(WIDTH, HEIGHT, 100, 'black', screen, 0, 0)
        textObject = font.render(text, 0, p.Color('white'))
    textLocation = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - textObject.get_width()/2, HEIGHT/2 - textObject.get_height()/2)
    screen.blit(textObject, textLocation)

    button("MAIN MENU", 156, 320, 220, 40, (250, 128, 114), (255, 160, 122), gameIntro)
    button("PLAY AGAIN", 156, 380, 220, 40, (250, 128, 114), (255, 160, 122), main)

def text_objects(text, font):
    textSurface = font.render(text, True, p.Color('white'))
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = p.mouse.get_pos()
    click = p.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        p.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        p.draw.rect(screen, ic, (x, y, w, h))

    smallText = p.font.Font('8-BIT WONDER.TTF', 20)  # ----- change from freesansbold.ttf to None
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)

def isCheck(screen, board, gs):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if gs.whiteToMove:
                if board[r][c][0] == 'w' and board[r][c][1] == 'K':
                   return hightLight(SQ_SIZE, SQ_SIZE, 100, 'red', screen, r, c)
            else:
                if board[r][c][0] == 'b' and board[r][c][1] == 'K':
                   return hightLight(SQ_SIZE, SQ_SIZE, 100, 'red',screen, r, c)

def hightLight(surfaceX, surfaceY, transperancy, color, screen, r, c):
    s = p.Surface((surfaceX, surfaceY))
    s.set_alpha(transperancy)  # transperancy value > 0 transparent; 255 opeaque
    s.fill(p.Color(color))
    screen.blit(s, (c * surfaceX, r * surfaceY))

def playSound(url, sec):
    mixer.music.load(f'sound effect\{url}')
    mixer.music.play(sec)

if __name__ == "__main__":
    screen = p.display.set_mode((WIDTH, HEIGHT))
    gameIntro()
