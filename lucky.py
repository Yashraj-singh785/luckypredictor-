"""Generate funny names by randomly combining names from 2 seprate lists."""
import sys
import random

def main():
    """Choose names at random from 2 tuples of names and print to scren ."""
    print ("welcome to the Lucky predictor 'Funny name picker .'\n")
    print("A name  which is more funnier and creative :\n\n")

    first = ('Shiva', 'Divyansh' , 'Dishant' , 'Ayush' , 'Hardik' ,)
    last = ('Yadav','Shukla','Prajapati','Trigger','Shekawat')

    while True :
        first_Name = random.choice(first)
        last_Name = random.choice(last)
        print("\n\n")
        # Trick IDLE by using "fatal error"setting to print name in red .
        print("{} {}".format(first_Name, last_Name) ,file =sys.stderr)
        print("\n\n")

        try_again =input("\n\nTry again?(Press Enter else n to quit)\n ")
        # converting every N TO n 
        if try_again.lower() == "n":
            break
    
    input("\nPress Enter to exit.")
      

