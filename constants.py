import pygame

pygame.init()

# HERE ARE THE COLORS

GAME_WIDTH = 800
GAME_HEIGHT = 600
CELL_WIDTH = 32
CELL_HEIGHT = 32

# TEMPORARY FPS LIMIT
GAME_FPS = 60

CLASSROOM_WIDTH = 30
CLASSROOM_HEIGHT = 30

COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)
COLOR_BLUE = (0, 0, 255)

#SPRITES
S_PLAYER = pygame.image.load("data/cheems.png")
S_WALL = pygame.image.load("data/other.png")
S_FLOOR = pygame.image.load("data/floor.png")
#S_CLASSMATE = pygame.image.load(classmate.sprite)
#pygame.image.load(S_CLASSMATE)

# FONT
FONT_MESSAGE = pygame.font.Font('data/Roboto-Black.ttf', 20)

# Classmate properties
names = ["Sophia", "Isabella", "Emma", "Olivia", "Ava", "Emily", "Abigial", "Ella",
"Addison", "Avery", "Lillian", "Lilith", "Bella", "Charlotte", "Aubrey", "Mariah",
"Eva", "Genesis", "Scarlett", "Madelyn", "Molly", "Faith", "Harper", "Autumn", "Kaylee",
"Lauren", "Allison", "Sarah", "Jacob", "Isaac", "Andrew", "Ryan", "Zachary", "Diego",
"Jaden", "Kevin", "Xavier", "Ian", "Chase", "Ayden", "Carson", "Adam", "Thomas", "Jose",
"Robert", "Dylan", "Joseph", "Caleb", "Elijah", "Evan", "Eli", "Luis"]
gradyear = ["2020", "2021", "2022", "2023", "2024"]
traits1 = ["hardworking", "laidback", "a party animal"]
traits2 = ["knowledgable", "resourceful", "clueless"]
traits3 = ["a pancake lover", "will eat anything", "a waffle lover"]
image_base = ["3d.png", 'blue.png', 'bread.png', 'dabbing.png', 'deal.png', 'doge.PNG',
'dogecoin.png', 'headphone.png', 'helmet.png', 'kid.jpg', 'pixel.png', 'sandwich.png',
'shout.png', 'smug.png', 'animu.png', 'plush.jpeg', 'poof.jpg', 'sad.jpg', 'shibaflower.jpg',
'smile.jpg', 'yawn.jpeg', 'pot.jpeg',]
