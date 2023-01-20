import pygame
import os
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui_file import Ui_MainWindow
size = width, height = 1000, 1000
GRAVITY = 2
FPS = 50
pygame.init()
screen = pygame.display.set_mode(size)
pygame.mixer.music.load('муызка_основа.mp3')
sound1 = pygame.mixer.Sound('взрыв бомбы.mp3')
a = []
all_sprites3 = pygame.sprite.Group()
level_time = 0


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.pushButton_1.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)
        self.pushButton_3.clicked.connect(self.run3)
        self.pushButton_4.clicked.connect(self.run4)

    def run1(self):
        global level_time
        load_level(1)
        f = open('data/level1.txt', mode='r')
        a = f.readlines()
        level_time = int(a[0])
        self.close()
#        start_screen()


    def run2(self):
        global level_time
        load_level(2)
        f = open('data/level2.txt', mode='r')
        a = f.readlines()
        level_time = int(a[0])
        self.close()
#        start_screen()

    def run3(self):
        global level_time
        load_level(3)
        f = open('data/level3.txt', mode='r')
        a = f.readlines()
        level_time = int(a[0])
        self.close()
#        start_screen()



    def run4(self):
        global level_time
        load_level(4)
        f = open('data/level4.txt', mode='r')
        a = f.readlines()
        level_time = int(a[0])
        self.close()
#        start_screen()


def load_level(filename):
    # читаем уровень, убирая символы перевода строки
    global a
    try:
        f = open('data/level' + str(filename) + '.txt', mode='r')
        a = f.readlines()
        f.close()
    except:
        print('Cannot load file:', filename)
        raise SystemExit()



def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ИГРА: BOMB DESTROYER",
                  "ПРАВИЛА ИГРЫ:",
                  "ВЗОРВАТЬ ВСЕ БОМБЫ ПУШКОЙ",
                  "ПУШКА СТРЕЛЯЕТ НА ПРОБЕЛ",
                  "ПУЛЯ ЛЕТИТ ИЗ ЦЕНТРА",
                  "ДВИЖЕНИЕ ПУШКИ ПРАВОЙ И ЛЕВОЙ СТРЕЛКАМИ"]

    fon = pygame.transform.scale(load_image('фон.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
#    sys.exit(app.exec_())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # �������� ����
        pygame.display.flip()
        clock.tick(FPS)


def stop_screen_win(t):
    intro_text = ["ТЫ ПРОШЕЛ УРОВЕНЬ", "",
                  "ЗА ВРЕМЯ:", str(t)]

    fon = pygame.transform.scale(load_image('победа.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


def stop_screen_lose(t):
    intro_text = ["ТЫ НЕ ПРОШЕЛ УРОВЕНЬ", "",
                  "ВРЕМЯ ПРЕВЫСИЛО: " + str(a[0]).strip() + ' СЕКУНД']

    fon = pygame.transform.scale(load_image('проигрыш1.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)



def stop_screen_lose1(t):
    intro_text = ["ТЫ НЕ ПРОШЕЛ УРОВЕНЬ", "",
                  "ТЫ СБИЛ НЕ ВСЕ БОМБЫ"]

    fon = pygame.transform.scale(load_image('проигрыш1.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


clock = pygame.time.Clock()

#start_screen()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


...
# для отслеживания улетевших частиц
# удобно использовать пересечение прямоугольников
screen_rect = (0, 0, width, height)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x3, y):
        global all_sprites3
        super().__init__(all_sprites3)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = level_time - 1
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x3, y)
        self.time = 0

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, atime):
        self.time += 1
        if (self.time % 50 == 0):
            self.cur_frame = (self.cur_frame - 1) % level_time
            self.image = self.frames[self.cur_frame]


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy, asprites):
        super().__init__(asprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = GRAVITY

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position, asprites):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers), asprites)


class Gun(pygame.sprite.Sprite):
    image = load_image("images.jpg")
#    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Gun.image
        self.rect = self.image.get_rect()

    def update(self, x, y):
        self.rect = self.rect.move(x, y)


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image1 = load_image("boom.png")
    boomed = False
#    image.set_colorkey((255, 255, 255))

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(104, width - 104)
        self.rect.y = random.randrange(height - 600)

    def update1(self):
        self.image = self.image1
        self.boomed = True

    def get_boomed(self):
        return self.boomed

    def update2(self, x, y):
        if not self.boomed:
            self.rect = self.rect.move(x, y)



class Bullet(pygame.sprite.Sprite):
    image = load_image("bullet.png")
    in_action = False

    def get_inAction(self):
        return self.in_action

    def reset_inAction(self):
        self.rect.x = -50
        self.rect.y = -50
        self.in_action = False

    def set_inAction(self, arect, width):
        if not self.get_inAction():
            self.rect.x = arect.x + width / 2
            self.rect.y = arect.y
            self.in_action = True


    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        # 111
        super().__init__(*group)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.rect.x = -50
        self.rect.y = -50

    def update(self, x, y):
        self.rect = self.rect.move(x, y)
        if self.rect.y <= 0:
            self.reset_inAction()
        #if pygame.sprite.spritecollideany(self, bombs):
            #self.reset_inAction()
        #if pygame.sprite.spritecollideany(self, vertical_borders):
            #self.reset_inAction()

    def update1(self):
        self.reset_inAction()


if __name__ == '__main__':
    start_screen()
    if (len(a) != 0):
        pygame.mixer.music.play(-1)
        # создадим группу, содержащую все спрайты
        all_sprites = pygame.sprite.Group()
        all_sprites1 = pygame.sprite.Group()
        all_sprites2 = pygame.sprite.Group()
        # создадим спрайт
        sprite = Gun(all_sprites)
        bullet = Bullet(all_sprites1)
        number = AnimatedSprite(load_image("цифры.png"), 10, 10, 0, 0)
        running = True
        x_pos = 0
        x = 0
        bombs = []
        ch = 0
        v = 1
        for i in range(int(a[1])):
            bombs.append(Bomb(all_sprites))
        motion = 0
        y_pos = height - sprite.image.get_height()
        all_sprites.update(x_pos, y_pos)
        y_pos = 0
        x_pos1 = 0
        y_pos1 = -15
        t = 0
        b = False
        while running:
            all_sprites3.update(clock.tick())
            if not b and t > int(a[0]):
                running = False
                stop_screen_lose(t)
            screen.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    if ch == len(bombs):
                        stop_screen_win(t)
                        running = False
                    else:
                        stop_screen_lose1(t)
                        running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        motion = 1
                    elif event.key == pygame.K_RIGHT:
                        motion = 2
                    elif event.key == pygame.K_SPACE:
                        bullet.set_inAction(sprite.rect, sprite.image.get_width())
                elif event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT,
                                 pygame.K_RIGHT]:
                        motion = 0
            x_pos = 0
            if motion == 1:
                x_pos = -5
            elif motion == 2:
                x_pos = 5
            if x <= (width - sprite.image.get_width()) and motion == 2:
                x += x_pos
                all_sprites.update(x_pos, y_pos)
            if x >= 0 and motion == 1:
                x += x_pos
                all_sprites.update(x_pos, y_pos)
            if bullet.get_inAction():
                all_sprites1.update(x_pos1, y_pos1)
            for i in range(len(bombs)):
                if bombs[i].get_boomed():
                    continue
                if bullet.rect.x + bullet.image.get_width() // 2 > bombs[i].rect.x\
                        and bullet.rect.x + bullet.image.get_width() // 2 < bombs[i].rect.x + 50\
                        and bullet.rect.y < bombs[i].rect.y:
                    bullet.update1()
                    bombs[i].update1()
                    sound1.play()
                    ch += 1
            if ch == len(bombs):
                create_particles((sprite.rect.x + sprite.image.get_width() // 2, 0), all_sprites2)
                b = True
            if a[2] == 'True':
                for i in range(len(bombs)):
                    x1 = bombs[i].rect.x
                    if x1 == 950 or x1 == -1:
                        v = -v
                    bombs[i].update2(v, y_pos)
                    clock.tick()
            all_sprites2.update()
            all_sprites.draw(screen)
            all_sprites1.draw(screen)
            all_sprites2.draw(screen)
            all_sprites3.draw(screen)
            pygame.display.flip()
            t += clock.tick() / FPS
            clock.tick(200)
            pygame.time.delay(20)
        pygame.quit()
