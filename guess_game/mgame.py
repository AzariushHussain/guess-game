import random

def guess():
        random_number=random.randint(1,100)
        
        print("Welcome to guessing game....!!!")
        print("enter the number")
        attempts=0
        z=True
        num=0
        while (random_number!=num ) :
            attempts+=1
            num=int(input(''))
            if num >random_number:
                print("enter a smaller number")
            elif num< random_number:
                print("enter a larger number")
            elif num==random_number:
                return attempts

