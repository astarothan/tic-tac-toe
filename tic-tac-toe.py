# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:17:43 2022

@author: ahmet
"""

A=[["*","*","*"],["*","*","*"],["*","*","*"]]

def xox(x,y,d):
    global A
    A[x][y]=d
    
def showtable():
    for k in range (3):
        for j in range(3):
            print(A[k][j],end=' ')
        print('')
        
    
def checkwin(x):
    global win
    win=0
    b=0
    for y in range(3):
        if A[y][0] !='*' and A[y][0]==A[y][1]==A[y][2]:                         
                win=1
                return win
    for m in range(3):
        if A[0][m] !='*':
            if A[0][m]==A[1][m]==A[2][m]:
                win=1
                return win
    if A[0][0]!="*" and A[0][0]==A[1][1]==A[2][2]:
        win=1
        return win
    if A[0][2]!="*" and A[0][2]==A[1][1]==A[2][0]:
        win=1
        return win
    if win!=1:
        for l in range(3):                
            for g in range(3):
                if A[l][g]=="*":
                    b+=1
            if b!=0:
                break
        if b==0:
            win=2
    
          
            
            
            
u=0 
while u==0:
    while True:
        x,y=input("Please enter for X ((1-3) (1-3)): ").split()
        x=int(x)-1
        y=int(y)-1
        d='X'
        if x>=0 and x<=2 and y>=0 and y<=2:
            if A[x][y] !="*":
                print("You cannot this place please enter again")
                continue
            else:
                xox(x,y,d)
                showtable()
                checkwin(d)
                if win!=0:
                    if win==1:
                        u=1
                        print("X win")
                        break
                    if win==2:
                        u=1
                        print("It's tie ")
                        break
                    
        else:
            print("You cannot enter this number")
        break
    if u==1:
        break
    while True:
        x,y=input("Please enter for O ((1-3) (1-3)): ").split()
        x=int(x)-1
        y=int(y)-1
        d='O'
        if x>=0 and x<=2 and y>=0 and y<=2:
            if A[x][y] !="*":
                print("You cannot this place please enter again")
                continue
            else:
                xox(x,y,d)
                showtable()
                checkwin(d)
                if win!=0:
                    if win==1:
                        print("O win")
                        u=1
                        break
                    if win==2:
                        u=1
                        print("It's tie ")
                        break
        else:
            print("You cannot enter this number")
            continue
        break
    if u==1:
        break
        
   
        
        
