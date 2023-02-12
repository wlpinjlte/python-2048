import random
import time
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.config import Config
from kivy.animation import Animation
from kivy.graphics import Color
from kivy.graphics import Canvas
from kivy.graphics import Rectangle
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'resizable', '0')
Config.write()

# Game BackEnd
class Game:
    def __init__(self):
        self.board=[[0 for i in range(4)]for j in range(4)]
        self.board[1][2]=2
        self.board[2][1]=2
        self.isMarge=[[False for j in range(4)]for i in range(4)]

    def getBoard(self):
        return self.board

    def updateFiledToFill(self):
        freeField = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    freeField.append((i, j))

        if len(freeField) == 0:
            return

        fieldToChoose = random.randint(0, len(freeField) - 1)
        self.board[freeField[fieldToChoose][0]][freeField[fieldToChoose][1]] = 2

    def endGame(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j]==0:
                    return False
        for i in range(len(self.board)-1):
            for j in range(len(self.board)-1):
                if self.board[i][j]==self.board[i+1][j] or self.board[i][j]==self.board[i][j+1]:
                    return False
        for i in range(len(self.board)-1,0,-1):
            for j in range(len(self.board)-1,0,-1):
                if self.board[i][j]==self.board[i-1][j] or self.board[i][j]==self.board[i][j-1]:
                    return False
        return True
    def getIsMarge(self):
        return self.isMarge

    def move(self, direction):
        isMarge = [[False for i in range(len(self.board[0]))] for j in range(len(self.board))]
        maxX = len(self.board) - 1
        maxY = len(self.board) - 1
        if (direction == 'left'):
            for x in range(len(self.board)):
                firstIteam = 0
                positonToPlaceIteam = 0
                while firstIteam < len(self.board[0]) and self.board[x][firstIteam] == 0:
                    firstIteam += 1
                if firstIteam == len(self.board):
                    continue
                for i in range(len(self.board) - firstIteam):
                    if (self.board[x][firstIteam + i] == 0):
                        continue
                    temp = self.board[x][firstIteam + i]
                    self.board[x][firstIteam + i] = 0
                    self.board[x][positonToPlaceIteam] = temp

                    if positonToPlaceIteam > 0 and isMarge[x][positonToPlaceIteam - 1] == False and self.board[x][
                        positonToPlaceIteam - 1] == self.board[x][positonToPlaceIteam]:
                        self.board[x][positonToPlaceIteam - 1] = self.board[x][positonToPlaceIteam - 1] * 2
                        self.board[x][positonToPlaceIteam] = 0
                        isMarge[x][positonToPlaceIteam - 1] = True
                    else:
                        positonToPlaceIteam += 1

        elif (direction == 'right'):
            for x in range(len(self.board)):
                firstIteam = maxY
                positonToPlaceIteam = maxY
                while firstIteam > -1 and self.board[x][firstIteam] == 0:
                    firstIteam -= 1
                if firstIteam == -1:
                    continue
                for i in range(firstIteam + 1):
                    if (self.board[x][firstIteam - i] == 0):
                        continue
                    temp = self.board[x][firstIteam - i]
                    self.board[x][firstIteam - i] = 0
                    self.board[x][positonToPlaceIteam] = temp

                    if positonToPlaceIteam < maxY and isMarge[x][positonToPlaceIteam + 1] == False and self.board[x][
                        positonToPlaceIteam + 1] == self.board[x][positonToPlaceIteam]:
                        self.board[x][positonToPlaceIteam + 1] = self.board[x][positonToPlaceIteam + 1] * 2
                        self.board[x][positonToPlaceIteam] = 0
                        isMarge[x][positonToPlaceIteam + 1] = True
                    else:
                        positonToPlaceIteam -= 1
        elif (direction == 'up'):
            for y in range(len(self.board)):
                firstIteam = 0
                positonToPlaceIteam = 0
                while firstIteam < len(self.board) and self.board[firstIteam][y] == 0:
                    firstIteam += 1
                if firstIteam == len(self.board):
                    continue
                for i in range(len(self.board) - firstIteam):
                    if (self.board[firstIteam + i][y] == 0):
                        continue
                    temp = self.board[firstIteam + i][y]
                    self.board[firstIteam + i][y] = 0
                    self.board[positonToPlaceIteam][y] = temp

                    if positonToPlaceIteam > 0 and isMarge[positonToPlaceIteam - 1][y] == False and \
                            self.board[positonToPlaceIteam - 1][y] == self.board[positonToPlaceIteam][y]:
                        self.board[positonToPlaceIteam - 1][y] = self.board[positonToPlaceIteam - 1][y] * 2
                        self.board[positonToPlaceIteam][y] = 0
                        isMarge[positonToPlaceIteam - 1][y] = True
                    else:
                        positonToPlaceIteam += 1
        elif (direction == 'down'):
            for y in range(len(self.board)):
                firstIteam = maxX
                positonToPlaceIteam = maxX
                while firstIteam > -1 and self.board[firstIteam][y] == 0:
                    firstIteam -= 1
                if firstIteam == -1:
                    continue
                for i in range(firstIteam + 1):
                    if (self.board[firstIteam - i][y] == 0):
                        continue
                    temp = self.board[firstIteam - i][y]
                    self.board[firstIteam - i][y] = 0
                    self.board[positonToPlaceIteam][y] = temp

                    if positonToPlaceIteam < maxY and isMarge[positonToPlaceIteam + 1][y] == False and \
                            self.board[positonToPlaceIteam + 1][y] == self.board[positonToPlaceIteam][y]:
                        self.board[positonToPlaceIteam + 1][y] = self.board[positonToPlaceIteam + 1][y] * 2
                        self.board[positonToPlaceIteam][y] = 0
                        isMarge[positonToPlaceIteam + 1][y] = True
                    else:
                        positonToPlaceIteam -= 1
        self.isMarge=isMarge


# Game FrontEnd(Gui)
def setImage(image,vaule,isAnimation):
    pathToImageToSet=None
    if(vaule>128 or vaule==0):
        pathToImageToSet='./assets/image/empty.PNG'
    elif(vaule==2):
        pathToImageToSet = './assets/image/2.PNG'
    elif (vaule == 4):
        pathToImageToSet = './assets/image/4.PNG'
    elif (vaule == 8):
        pathToImageToSet = './assets/image/8.PNG'
    elif (vaule == 16):
        pathToImageToSet = './assets/image/16.PNG'
    elif (vaule == 32):
        pathToImageToSet = './assets/image/32.PNG'
    elif (vaule == 64):
        pathToImageToSet = './assets/image/64.PNG'
    elif (vaule == 128):
        pathToImageToSet = './assets/image/128.PNG'
    if(image==None):
        return Image(source=pathToImageToSet,size_hint=(100,100))
    elif(image.source==pathToImageToSet):
        return
    image.source=pathToImageToSet
    if(isAnimation):
        animation=Animation(size_hint=(110,110),size=(110,110),duration=0.1)
        animation+=Animation(size_hint=(100,100),size=(100,100),duration=0.2)
        animation.start(image)

class Template(Widget):
    mainGrid = ObjectProperty(None)
    gameOver = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.game=Game()
        board = self.game.getBoard()
        self.flag=True
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self.guiBoard = GridLayout(cols=4)
        self.fields = [[None for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                image = setImage(None,board[i][j],False)
                self.guiBoard.add_widget(image)
                self.fields[i][j] = image
        self.mainGrid.add_widget(self.guiBoard)
    def updateMap(self):
        self.board=self.game.getBoard()
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                setImage(self.fields[i][j],self.board[i][j],self.game.getIsMarge()[i][j])

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.game.move(keycode[1])
        self.game.updateFiledToFill()
        self.updateMap()
        print(self.game.endGame())
        if(self.game.endGame() and self.flag==True):
            self.flag=False
            with self.canvas.after:
                Color(1,1,1,0.3,mode='rgba')
                Rectangle(size= (400, 400),pos=self.pos)
            self.gameOver.text="[b][color=7e746a]GameOver[/color][/b]"


        return True


class MainApp(App):
    def build(self):
        from kivy.base import runTouchApp
        return runTouchApp(Template())


if __name__ == "__main__":
    MainApp().run()
