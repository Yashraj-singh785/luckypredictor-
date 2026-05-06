"""Generate funny names by randomly combining names from 2 separate lists."""
import sys
import random


def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print("Welcome to the Lucky predictor 'Funny name picker.'\n")
    print("A name which is more funny and creative:\n\n")

    first = ('Shiva', 'Divyansh', 'Dishant', 'Ayush', 'Hardik')
    last = ('Yadav', 'Shukla', 'Prajapati', 'Trigger', 'Shekawat')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        print("\n\n")
        # Trick IDLE by using stderr to print name in red
        print(f"{first_name} {last_name}", file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()