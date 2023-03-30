#I M P O R T I N G
import sys,subprocess
import time 
import math
import webbrowser as wb
import random as rd

subprocess.run('cls',shell=True)
#main menu
menu = '''1. ODI
2. T20
3. TEST'''

for menu in menu:
    time.sleep(0.028)
    print(menu,end='')

menu_format = int(input())

player_name_list = []

#scoring for odi
for i in range (1,12):
    player_name= str(i),'.', input("Enter the ")
    player_name_list.append(player_name)

global s
global sn
s = 0
sn = 0

striker = list[s]
non_striker = list[sn]
print("opener:",striker,non_striker)

for over in range (50):
    for ball in range (1,7):
        print("Enter the score for the",ball,"th ball:")
        score_ball = input()
        if score_ball.isalpha:
            pass