# Partner_finder_final.py
"""
The Softdes Partner Finder
- Players create a character, and then will talk to other characters
in the classroom to find their perfect softdes partner.
- Each character will be saved into a database that will then use
those characters as the students in subsequent playthroughs.

Created by: Jason Lin and Regan Mah
"""
import pygame
import random
from constants import names, traits1, traits2, traits3, S_CLASSMATE
from partner_finder_controller import obj_Actor, ai_Test
# from partner_finder_controller import obj_Actor

white=(255,255,255)


'''
 ____ _____ ____  _   _  ____ _____ _   _ ____  _____ ____
/ ___|_   _|  _ \| | | |/ ___|_   _| | | |  _ \| ____/ ___|
\___ \ | | | |_) | | | | |     | | | | | | |_) |  _| \___ \
 ___) || | |  _ <| |_| | |___  | | | |_| |  _ <| |___ ___) |
|____/ |_| |_| \_\\___/ \____| |_|  \___/|_| \_\_____|____/  '''


class struc_Tile:
    def __init__(self, block_path):
        self.block_path = block_path


'''
  ____ ___  __  __ ____   ___  _   _ _____ _   _ _____ ____
 / ___/ _ \|  \/  |  _ \ / _ \| \ | | ____| \ | |_   _/ ___|
| |  | | | | |\/| | |_) | | | |  \| |  _| |  \| | | | \___ \
| |__| |_| | |  | |  __/| |_| | |\  | |___| |\  | | |  ___) |
 \____\___/|_|  |_|_|    \___/|_| \_|_____|_| \_| |_| |____/  '''


class com_Classmate:
    '''
    classmates can move around and be interacted with
    '''
    #GIVE AI
    def __init__(self, name_instance):

        self.name_instance = name_instance


    # Generates classmates: TODO could put this into its function
    # define a variable n representing number of classmates to generate
    # for i in n
    # randomly choose a name from constants, and traits
    # create object from obj_Actor class passing into it the name and traits




def generate_student():

    students = []

    classmate_number = 20

    for n in range(classmate_number):
        students.append(obj_Actor(random.randint(1, 23), random.randint(1, 17),
                                    random.choice(names), random.choice(traits1),
                                    random.choice(traits2), random.choice(traits3),
                                    S_CLASSMATE, ai = ai_Test()))

    return students
























# class Menu:
#     """
#     A class used for the startup menus and the endgame menus, as
#     well as the teacher menu (?)
#     """
#     def __init__():
#         pass
#
# class Prof(Menu):
#     """
#     Prof will basically be like a save point/ends game when you
#     select your Partner.
#     Not sure if this falls under the menu class or not
#     """
#
#     def end_result():
#         '''
#         When character chooses a partner, a final result will
#         be posted stating the outcome of the game.
#         '''
#         pass
#     pass
#
# class Student:
#
#     def __init__(self, name, gradyear, trait1, trait2, trait3, x, y):
#         self.name = name
#         self.gradyear = gradyear
#         self.trait1 = trait1
#         self.trait2 = trait2
#         self.trait3 = trait3
#         self.x = x
#         self.y = y
#
    def generate_student():

        students = []

        names = ["Sophia", "Isabella", "Emma", "Olivia", "Ava", "Emily", "Abigial", "Ella",
        "Addison", "Avery", "Lillian", "Lilith", "Bella", "Charlotte", "Aubrey", "Mariah",
        "Eva", "Genesis", "Scarlett", "Madelyn", "Molly", "Faith", "Harper", "Autumn", "Kaylee",
        "Lauren", "Allison", "Sarah", "Jacob", "Isaac", "Andrew", "Ryan", "Zachary", "Diego",
        "Jaden", "Kevin", "Xavier", "Ian", "Chase", "Ayden", "Carson", "Adam", "Thomas", "Jose",
        "Robert", "Dylan", "Joseph", "Caleb", "Elijah", "Evan", "Eli", "Luis"]
        gradyear = ["2020", "2021", "2022", "2023", "2024"]
        traits1 = ["hardworking", "laidback", "useless"]
        traits2 = ["knowledgable", "resourceful", "clueless"]
        traits3 = ["pancake_lover", "eats_anything", "waffle_lover"]

        while i <= 40:
            students.append(Student(i, random.choice(names), random.choice(gradyear), random.choice(traits1), random.choice(traits2), random.choice(traits3), x, y))
#
#     def draw(self):
#         window.blit(self.image(self.x, self.y))
#
#
# class PlayerCharacter(Student):
#
#     def create_student(name, gradyear):
#         #Takes player input to create a character with a name
#         #and their gradyear
#         name = input("What is your name?")
#         year = input("What year are you in?")
#         trait1, trait2, trait3 = define_traits()
#
#     def define_traits():
#         #Asks the player several questions that will define the traits
#         #of the player character. These traits will then be used to
#         #see if the player character and their parter are compatible.
#         question1 = input("How would you describe your working style?\nA) If it needs to be done, it better be done well\nB) Meh it'll happen one way or another\nC) Work? What's work?")
#         question2 = input("Coding experience?\nA) I know everything I need to know\nB) I know enough to get by\nC) Coding? What's coding?")
#         question3 = input("Do you like pancakes?\nA) I eat pancakes and nothing else\nB) Meh I'll eat them if they're put in front of me\nC) I will only eat waffles and nothing else")
#
#         if question1 == 'A' or question1 == 'a':
#             trait1 = "hardworking"
#             return trait1
#         elif question1 == 'B' or question1 == 'b':
#             trait1 = "laidback"
#             return trait1
#         elif question1 == 'C' or question1 == 'c':
#             trait1 = "useless"
#             return trait1
#
#         if question2 == 'A' or question2 == 'a':
#             trait2 = "knowledgable"
#             return trait2
#         elif question2 == 'B' or question2 == 'b':
#             trait2 = "resourceful"
#             return trait2
#         elif question2 == 'C' or question2 == 'c':
#             trait2 = "clueless"
#             return trait2
#
#         if question3 == 'A' or question3 == 'a':
#             trait3 = "pancake_lover"
#             return trait3
#         elif question3 == 'B' or question3 == 'b':
#             trait3 = "eats_anything"
#             return trait3
#         if question3 == 'C' or question3 == 'c':
#             trait3 = "waffle_lover"
#             return trait3
#
#         return trait1, trait2, trait3
#
#     def store_student():
#         """
#         Stores student in a list that will be used to select
#         which students populate the class at random.
#         """
#         created_students = []
#         created_students.append(self.create_student())
#
#         return created_students