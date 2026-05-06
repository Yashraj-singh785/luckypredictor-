import sys,random
print ("welcome to the Lucky predictor 'Funny name picker .'\n")
print("A name  which is more funnier and creative :\n\n")

first = ('Shiva', 'Divyansh' , 'Dishant' , 'Ayush' , 'Hardik' ,)
last = ('Yadav','Shukla','Prajapati','Trigger','Shekawat')

while True :
    firstName = random.choice(first)
    lastName = random.choice(last)
    print("\n\n")
    print("{}{}".format(firstName, lastName) ,file =sys.stderr)
    print("\n\n")

    try_again =input("\n\nTry again?(Press Enter else n to quit)\n ")
    if try_again.lower() == "n":
        break
    input("\nPress Enter to exit.")