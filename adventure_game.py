



#imports
import math 
import time 
import random

#lists
bag_items = ['500 Exso coins','Bronze Sword (5 damage)','Rope (10 feet)','(8)Health potion(s)']
health_levels = [100]
levels = [1]
armors = ['Bronze(100E)','Silver(500E)','Gold(3000E)','Dimond(20,000E)','Dracium(500,000E)','Silfisteium(777,777,777)']
weight = [5]
potions = ['Health potion(100E)','Mana potion(110E)','Strength potion(150E)','Speed potion(100E)',]
weapons = ['Bronze Sword(100E)','Silver Sword(500E)','Gold Sword(3000E)','Dimond Sword(20,000E)','Dracium Sword(500,000E)','Silfisteium Sword(777,777,777)']
#simplify
underline = "{:s}\n{:s}\n".format("", len(range(150)) * "-")



#first text
print('This is my adventure game!')
time.sleep(2)


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
             if choice3 ==1:
                print('You go out on a quest for...')
                time.sleep(2)
                print('Slimes!')
                time.sleep(1)
                print('but..')
                time.sleep(2)
                print('Sorry this is the end of the Demo, Thanks for playing!')
                break
             if choice3 == 2:
                print('oh...')
                time.sleep(1)
                print('Your to weak...')
                time.sleep(1)
                print('You leave and go train to get stronger')
                time.sleep(2)
                print('Demo over, thank you for playing the demo of my game!')
                break
             if choice3 == 3:
                print('oh...')
                time.sleep(1)
                print('Your to weak...')
                time.sleep(1)
                print('You leave and go train to get stronger')
                time.sleep(2)
                print('Demo over, thank you for playing the demo of my game!')
                break
             else:
                print('Invalid input!')
                break
    #leave
          if choice2 == 2:
              print('Thanks for playing!')
              time.sleep(2)
              print(f'Goodbye!')
              break
          else:
            print('Invalid menu choice! please enter a number between 1 and 4 only.')
            break
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
               if choice4 == 1:
                  print('Item stored...')
                  time.sleep(2)
                  print('Bag updated!')
                  time.sleep(2)
                  bag_items.append('chest-piece')
                  print('Demo over, thank you for playing the demo of my game!')
                  break
               if choice4 == 2:
                  print('You leave the piece of armor and live another day...')
                  time.sleep(2)
                  print('Demo over, thank you for playing the demo of my game!')
                  break
               else:
                  print('Invalid input!')
                  break
             if choice3 == 2:
      # talk
              print('He wobbles up to you...')
              time.sleep(2)
              print('He swarms you with a bunch of his friends...')
              time.sleep(2)
              print('He eats you...')
              time.sleep(1)
              print('Thanks for playing!')
              break
             if choice3 == 3:
      # go around
              print('You go around the slime and you live another day')
              time.sleep(2)
              print('Thanks for playing!')
              break
           else:
              print('Invalid menu choice! please enter a number between 1 and 4 only.')
              break
    #leave dungeon
           if choice2 == 2:
              print(f'Thank you for playing my game...')
              time.sleep(2)
              print(f'Goodbye!')
              break
           else:
            print('Invalid menu choice! please enter a number between 1 and 4 only.')
            break
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
          #armor
              if choice3==1: 
                 print('You browse there armors...')
                 time.sleep(1)
                 print('They have...')
                 time.sleep(1)
                 print(underline)
                 print(armors)
                 print(underline)
                 print('This is the end of the demo, Thanks for playing!')
                 break
          #potions
              if choice3==2:
                 print('You browse there potions...')
                 time.sleep(1)
                 print('They have...')
                 time.sleep(1)
                 print(underline)
                 print(potions)
                 print(underline)
                 print('This is the end of the demo, Thanks for playing!')
                 break
          #weapons
              if choice3==3:
                 print('You browse there weapons...')
                 time.sleep(1)
                 print('They have...')
                 time.sleep(1)
                 print(underline)
                 print(weapons)
                 print(underline)
                 print('This is the end of the demo, Thanks for playing!')
                 break
              else:
                 print('Invalid input')
            if choice2 == 2:
              print(f'Thank you for playing my game...')
              time.sleep(2)
              print(f'Goodbye!')
              break
            else:
             print('Invalid menu choice! please enter a number between 1 and 4 only.')
             break
  #bag
       elif choice ==4:
            print('Checking bag...')
            time.sleep(2)
            print(f'this is in your bag...')
            time.sleep(2)
            print(underline)
            print(f'{bag_items}')
            print(underline)
            time.sleep(2)
       else:
        print('Invalid menu choice! please enter a number between 1 and 4 only.')
   


if __name__ == '__main__':
    main()