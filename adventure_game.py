



#imports
import math 
import time 
import random

#lists
bag_items = ['500 gold coins','Bronze Sword (5 damage)','Rope (10 feet)','(8)Health potion(s)']
health_levels = [100]
levels = [1]
armors = ['Bronze','Silver','Gold','Dimond','Dracium','Silfisteium']
weight = [5]
#first text
print('This is my adventure game!')
time.sleep(2)

#simplify
invalid_text = print('Invalid menu choice! please enter a number between 1 and 4 only.')
thanks = print('Thank you for playing my game...')
#menu displayed
def display_menu():
    print('''         Menu:
        1. Go into town
        2. Walk through the forest
        3. Go to the shop
        4. check bag
      ''')

#game
def main():
 
  while True:
       display_menu()
       choice = float(input('Enter your adventure choice (1-4 only):\n'))
  #Town
       if choice == 1:
          print(f'You walk into town and see a adventure guild...')
          time.sleep(2)
    #enter guild      
          choice2 = float(input('''\nwhat do you do?
  1.Enter the guild
  2.stop
                \n'''))
          if choice2 == 1:
             print(f'You walk into the guild and see a quest board, you take a quest...')
             time.sleep(2)
      #quests
             choice3 = float(input('''\nwhat quest do you take?
  1.E-level quest (easy)
  2.C-level quest (medium)
  3.S-level quest (Imposible)
                \n'''))
    #leave
          if choice2 == 2:
              print(thanks)
              time.sleep(2)
              print(f'Goodbye!')
              break
          else:
            print(invalid_text)

  #Forest
       elif choice == 2:
           print(f'you walk into the forest and see a dungeon...')
           time.sleep(2)
           choice2 = float(input('''\nwhat do you do?
  1.Enter the dungeon
  2.stop
                \n'''))
           if choice2 == 1:
   # in dungeon
             print(f'You walk into the dungeon and see a slime...')
             time.sleep(2)
             choice3 = float(input('''\nwhat do you do?
  1. Attack it 
  2. try to talk to it 
  3. go around it
                \n'''))
             if choice3 == 1:
      # fight
               print(f'You take out your sword and slash the slime...')
               time.sleep(2)
               print(f'It dies and drops a chest-piece...')
               choice4 = float(input('''\nwhat do you do?
  1. store it in bag
  2. leave it
                \n'''))
             if choice3 == 2:
              print('He wobbles up to you...')
              time.sleep(2)
              print('He swarms you with a bunch of his friends...')
              time.sleep(2)
              print('He eats you...')
              time.sleep(1)
              print(thanks)
              break
             if choice3 == 3:
              print('You go around the slime and you live another day')
              print(thanks)
              break
             else:
              print(invalid_text)


           if choice2 == 2:
              print(f'Thank you for playing my game...')
              time.sleep(2)
              print(f'Goodbye!')
              break
           else:
            print(invalid_text)
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
    #options
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
             print(invalid_text)
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
        print(invalid_text)

if __name__ == '__main__':
    main()