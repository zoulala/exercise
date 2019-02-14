import pygame
from pygame.locals import *
import sys

BLACK = (155, 230, 85)
WHITE = (255, 255, 255)

SCREEN_SIZE = [320, 400]
BAR_SIZE = [20, 5]
BALL_SIZE = [15, 15]


class Game(object):
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Simple Game')

        self.ball_pos_x = SCREEN_SIZE[0] // 2 - BALL_SIZE[0] / 2
        self.ball_pos_y = SCREEN_SIZE[1] // 2 - BALL_SIZE[1] / 2
        # ball移动方向
        self.ball_dir_x = -1  # -1 = left 1 = right
        self.ball_dir_y = -1  # -1 = up   1 = down
        self.ball_pos = pygame.Rect(self.ball_pos_x, self.ball_pos_y, BALL_SIZE[0], BALL_SIZE[1])

        self.score = 0
        self.bar_pos_x = SCREEN_SIZE[0] // 2 - BAR_SIZE[0] // 2
        self.bar_pos = pygame.Rect(self.bar_pos_x, SCREEN_SIZE[1] - BAR_SIZE[1], BAR_SIZE[0], BAR_SIZE[1])

    def bar_move_left(self): # 板子左移
        self.bar_pos_x = self.bar_pos_x - 2

    def bar_move_right(self): # 板子右移
        self.bar_pos_x = self.bar_pos_x + 2

    def run(self):
        pygame.mouse.set_visible(0)  # make cursor invisible

        bar_move_left = False
        bar_move_right = False
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 鼠标左键按下(左移)
                    bar_move_left = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # 鼠标左键释放
                    bar_move_left = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # 右键
                    bar_move_right = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                    bar_move_right = False

            if bar_move_left == True and bar_move_right == False:
                self.bar_move_left()
            if bar_move_left == False and bar_move_right == True:
                self.bar_move_right()

            # 板子坐标变更，绘制板子白色
            self.screen.fill(BLACK)
            self.bar_pos.left = self.bar_pos_x
            pygame.draw.rect(self.screen, WHITE, self.bar_pos)

            # 控制球的左右上下移动速度，绘制球白色
            self.ball_pos.left += self.ball_dir_x * 2
            self.ball_pos.bottom += self.ball_dir_y * 3
            pygame.draw.rect(self.screen, WHITE, self.ball_pos)

            # 球碰撞到壁，则反方向运动
            if self.ball_pos.top <= 0 or self.ball_pos.bottom >= (SCREEN_SIZE[1] - BAR_SIZE[1] + 1):
                self.ball_dir_y = self.ball_dir_y * -1
            if self.ball_pos.left <= 0 or self.ball_pos.right >= (SCREEN_SIZE[0]):
                self.ball_dir_x = self.ball_dir_x * -1

            # 板子接住球+1分,没接住 game over
            if self.bar_pos.top <= self.ball_pos.bottom and (
                    self.bar_pos.left < self.ball_pos.right and self.bar_pos.right > self.ball_pos.left):
                self.score += 1
                print("Score: ", self.score, end='\r')
            elif self.bar_pos.top <= self.ball_pos.bottom and (
                    self.bar_pos.left > self.ball_pos.right or self.bar_pos.right < self.ball_pos.left):
                print("Game Over: ", self.score)
                return self.score

            pygame.display.update()
            self.clock.tick(30)  # 设置游戏最大帧率


game = Game()
game.run()
