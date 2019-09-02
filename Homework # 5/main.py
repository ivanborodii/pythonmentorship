from task1 import task1
from task2 import task2

def main():
    tasknum=input('Select the task which you want to run? (1 - Mandatory homework / 2 - Advanced homework): ')
    if tasknum=='1':
        task1()
    elif tasknum=='2':
        task2()
    else:
        print("You've entered invalid character. Please enter 1 or 2.")
        main()

if __name__=='__main__': # Entry point
    play_again = True
    while play_again:
        main()
        play_again = input("Do you want to run the program one more time? (y/n) ").lower() == 'y'
    print("")