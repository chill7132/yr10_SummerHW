def Timestable():
    num = int(input("Which timestable would you like to see?>>>"))#Asks user for an input of a number
    if num <= 12:#Checks if the number is less or equal to 12
        for i in range(1,13):
           print(num,'x',i,'=',num*i)#Prints all the timestable for the chosen number
    else:
        print("A number between 1 and 12 please")#Tells the user they need to pick a number between 1 and 12
        Timestable()#Replays the function so that the user can enter a number between 1 and 12

Timestable()#Starts the function when the code is run instead of typing in the function name to get it to run
 here
