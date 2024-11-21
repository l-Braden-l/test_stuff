



#imports
import math 
import time 
import random

#lists
bag_items = ['500 gold coins','Bronze Sword (5 damage)','Rope (10 feet)','(8)Health potion(s)']
health_levels = [100]
levels = [1]
armors = ['Bronze','Silver','Gold','Dimond','Dracium','Silfisteium']

#first text
print('This is my adventure game!')
time.sleep(2)


def display_menu():
    print('''         Menu:
        1. Go into town
        2. Walk through the forest
        3. Go to the shop
        4. check bag
      ''')

#part 2 
def main():
    while True:
       display_menu()
       choice = float(input('Enter your adventure choice (1-4 only):\n'))
#Town
       if choice == 1:
          print(f'You walk into town and see a adventure guild...')
          time.sleep(2)
          choice2 = float(input('''\nwhat do you do?
  1.Enter the guild
  2.stop
                \n'''))
          if choice2 == 1:
             print(f'You walk into the guild and see a quest board, you take a quest...')
             time.sleep(2)
             choice3 = float(input('''\nwhat quest do you take?
  1.E-level quest (easy)
  2.C-level quest (medium)
  3.S-level quest (Imposible)
                \n'''))
          if choice2 == 2:
              print(f'Thank you for playing my game...')
              time.sleep(2)
              print(f'Goodbye!')
              break
          else:
            print('Invalid menu choice! please enter a number between 1 and 4 only.')

#Forest
       elif choice == 2:
           print(f'you walk into the forest and see a dungeon...')
           time.sleep(2)
           choice2 = float(input('''\nwhat do you do?
  1.Enter the dungeon
  2.stop
                \n'''))
           if choice2 == 1:
             print(f'You walk into the dungeon and see a slime...')
             time.sleep(2)
             choice3 = float(input('''\nwhat do you do?
  1. Attack it 
  2. try to talk to it 
  3. go around it
                \n'''))
           if choice2 == 2:
              print(f'Thank you for playing my game...')
              time.sleep(2)
              print(f'Goodbye!')
              break
           else:
            print('Invalid menu choice! please enter a number between 1 and 4 only.')
 #Shop
       elif choice == 3:
            print(f'You walk into the shop and look around...')
            time.sleep(2)
            choice2 = float(input(('''\ndo you want to see what they have
  1.yes
  2.no
                  \n''')))
            if choice2 == 1:
              print(f'You see many things to buy...')
              time.sleep(2)
              choice3 = float(input('''\nwhere do you look?
  1. Armors
  2. potions
  3. weapons
                \n'''))
            if choice2 == 2:
              print(f'Thank you for playing my game...')
              time.sleep(2)
              print(f'Goodbye!')
              break
            else:
             print('Invalid menu choice! please enter a number between 1 and 4 only.')
#bag
       elif choice ==4:
            print('Checking bag...')
            time.sleep(2)
            print(f'this is in your bag...')
            time.sleep(2)
            print("{:s}\n{:s}\n".format("", len(range(150)) * "-"))
            print(f'{bag_items}')
            print("{:s}\n{:s}\n".format("", len(range(150)) * "-"))
            time.sleep(2)
       else:
        print('Invalid menu choice! please enter a number between 1 and 4 only.')

if __name__ == '__main__':
    main()