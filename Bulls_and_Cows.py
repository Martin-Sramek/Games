import random
import time

def generate_secret_number():
   """
   Generates the 4-digit "secret number".
   The "secret number" is in fact a list which contains 4 numbers (0-9) and which must be guessed by the player.
   Returns a list with 4 numbers (numbers are in form of a string) which are all different.
   """
   list_of_numbers = []

   while len(list_of_numbers) != 4:
       random_number = str(random.randint(0, 9))
       if random_number in list_of_numbers:
           continue
       else:
           list_of_numbers.append(random_number)

   return list_of_numbers


def player_guess():
   """
   Processes the input entered by the player and converts the 4-digit number entered by the player
   to a list which contains 4 numbers (0-9).
   Returns a list with 4 numbers (numbers are in form of a string) which are all different.
   """
   valid_guess = False

   while not valid_guess:
       list_of_numbers = list(input("Enter a 4-digit number. The digits must be all different and the number can start with 0.\n"))

       if len(set(list_of_numbers)) != 4:
           continue

       for element in list_of_numbers:
           if not element.isdigit() or int(element) > 9 or int(element) < 0:
               break
       else:
           valid_guess = True

   return list_of_numbers


def end_of_game(secret_number, player_number):
   """
   Compares whether the player has guessed the "secret number".
   Compares two lists - one created by computer and the second
   which is created from the number entered by the player.
   """
   if secret_number == player_number:
       return True
   else:
       return False


def high_score_table(player_name, total_time, high_score):
   """
   Prints, sorts and saves game statistics - player names and time of individual games.
   When the player finishes playing, the statistics are not stored.
   """
   high_score[player_name] = total_time
   longest_name = 6

   for name in high_score.keys():
       if len(name) > longest_name:
           longest_name = len(name)

   table_width = longest_name + 22
   separator = table_width * "-"
   print("{0:^{1}}".format("***** HIGH SCORES *****", table_width))
   print(separator)
   print("| {0:^{1}} | Time in seconds |".format("Player", longest_name))
   print(separator)
   sorted_high_score = sorted(high_score.items(), key = lambda item : item[1])
   for value in sorted_high_score:
       print("| {0:^{2}} | {1:^15} |".format(value[0], value[1], longest_name))
       print(separator)


def compare(secret_number):
   """
   Compares the "secret number" with the number entered by the player until the player guess the "secret number".
   Shows how many bulls and cows the player has gained after each attempt or if the playert has guessed the "secret
   number" and win.
   """
   while True:
       bulls_and_cows = {"bulls": 0, "cows": 0}
       player_number = player_guess()

       for i, num in enumerate(player_number):
           if num == secret_number[i]:
               bulls_and_cows["bulls"] = bulls_and_cows.get("bulls") + 1
           elif num != secret_number[i] and num in secret_number:
               bulls_and_cows["cows"] = bulls_and_cows.get("cows") + 1

       if end_of_game(secret_number, player_number):
           break

       print("-" * 16)
       print("{} bulls | {} cows".format(bulls_and_cows["bulls"], bulls_and_cows["cows"]))
       print("-" * 16)

   print("-" * 51)
   print("CONGRATULATION! You guessed the secret number {}.".format("".join(secret_number)))
   print("-" * 51 + "\n")


def another_play():
    """
    Asks the player if he wants to play another game.
    """
    while True:
       play_again = input("Do you want to play again? Enter y for yes or n for no: ")

       if len(play_again) != 1 or not play_again.isalpha():
           continue
       elif play_again.lower() == "y":
           return True
       elif play_again.lower() == "n":
           return False


def main():
   print("=" * 76)
   print("""Welcome! Let's play Bulls and Cows.

Description of the game:
1) The computer thinks of a secret 4-digit number and you try to guess it.

2) At each turn you enter a 4-digit number, and the computer says how close
  your number is to the secret number by giving:
   - the number of bulls - digits correct in the right position
   - the number of cows - digits correct but in the wrong position

Example: if the secret number is: 1234
                and you entered: 3204 - then you will get 2 bulls and 1 cow

Try to guess the secret number in the shortest time possible!""")
   print("=" * 76)

   high_score = {}
   playing = True

   while playing:
       secret_number = generate_secret_number()
       print()
       player_name = input("Enter your name: ")
       start_time =  time.time()
       compare(secret_number)
       total_time = round(time.time() - start_time, 1)
       high_score_table(player_name, total_time, high_score)
       print()
       playing = another_play()


if __name__ == "__main__":
   main()