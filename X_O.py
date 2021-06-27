#!/usr/bin/env python
# coding: utf-8

# In[4]:


def Start_game():
    a = ""
    n = 0
    i = list(range(1,10))
    print ("Chose ur role\n")
    win_combo = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

    while True:
        one = str.upper(input())
        if one == "X":
            two = "O"
        elif one == "O":
            two = "X"
        else :
            print("\nTake other chose") 
            continue
        break

    if one == "X" or one == "O":

        print("\nFirst player play --", one)
        print("Second player play --", two)


    print("-------------")
    for b in range(3):
        print ("|", i[0+b*3], "|", i[1+b*3], "|", i[2+b*3], "|")
        print("-------------")


    while True:
        print ("Chose ur number: ")
        point = int(input())

        if not int(point) in [1,2,3,4,5,6,7,8,9]:
            print("\nWrong chose\n")
            continue

        for number in i:
            if number == point:
                i[point-1] = one
                one,two = two,one


        print("-------------")
        for b in range(3):
            print ("|", i[0+b*3], "|", i[1+b*3], "|", i[2+b*3], "|")
            print("-------------")

        for check_win in win_combo:
            if (i[check_win[n]-1] == i[check_win[n+1]-1] == i[check_win[n+2]-1]):
                a = "win" 
                print("{} win".format(two))

        if a == "win":
            break
        else: 
            continue

if __name__ == "__main__":
    Start_game()


# 
# 
