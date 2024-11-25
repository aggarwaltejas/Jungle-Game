# print("Jungle Game")
# print("There are 2 turns in the jungle : Left and Right")
# num=int(input("Enter Number : "))
# if(num==1):
#     print("The guy took left turn")
#     num=int(input("Enter Numer : "))
#     if(num==3):
#         print("The guy again took left turn")
#         print("Tiger came and killed the person \nGame over")
#     elif(num==4):
#         print("The guy took right turn")
#         print("A shooter shot the guy \nGame Over")
#     else:
#         print("Wrong input")


# elif(num==2):
#     print("The guy took right turn")
#     num=int(input("Enter Numer : "))
#     if(num==5):
#         print("The guy again took right turn")
#         print("A ditch came in front of the guy and the guy fell in that ditch \nGame Over")
#     elif(num==6):
#         print("The guy took left turn")
#         print("The guy met a stranger at this point")
#         word=input("Take help from the stranger no help : ")
#         if(word=="help"):
#             print("The guy reached the destination")
#         elif(word=="no help"):
#             print("The guy met some adivasis there and the adivasis took him away \nGame over")
#         else:
#             print("Wrong input")
#     else:
#         print("Wrong input")
# else:
#     print("Wrong input")


print("Jungle Game")
print("There are 2 turns in the jungle : Left and Right")
Turn=input("Left / Right : ")
if(Turn=="Left"):
    print("The guy took left turn")
    print("There are again 2 turns in the jungle : Left and Right")
    Turn=input("Left / Right : ")
    if(Turn=="Left"):
        print("The guy again took left turn")
        print("Tiger came and killed the person \nGame over")
    elif(Turn=="Right"):
        print("The guy took right turn")
        print("A shooter shot the guy \nGame Over")
    else:
        print("Wrong input")
    


elif(Turn=="Right"):
    print("The guy took right turn")
    print("There are again 2 turns in the jungle : Left and Right")
    Turn=input("Left / Right : ")
    if(Turn=="Right"):
        print("The guy again took right turn")
        print("A ditch came in front of the guy and the guy fell in that ditch \nGame Over")
    elif(Turn=="Left"):
        print("The guy took left turn")
        print("The guy met a stranger at this point")
        word=input("Take help from the stranger no help : ")
        if(word=="help"):
            print("The guy reached the destination")
        elif(word=="no help"):
            print("The guy met some adivasis there and the adivasis took him away \nGame over")
        else:
            print("Wrong input")
    else:
        print("Wrong input")
else:
    print("Wrong input")