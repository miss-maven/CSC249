# csc-249 Binary search 
# Jane Martin
# 2/05/2024
# Silver 
# 2.3.2 code inspo to create a binary search
def binary_search(arr, key):
  low = 0
  high = len(arr) - 1
  while high >= low: 
    mid = (high + low) // 2
    if arr[mid] < key:
      low = mid + 1
    elif arr[mid] > key:
      high = mid - 1
    else: 
      return mid

def guess_game():
  low = 0
  high = 99 #user can choose a integer from 0-99
  tries = 0
  print("Pick a whole number from 0 - 99: ")
  # using tries to keep track
  while tries < 5:
    guess = (high + low) // 2
    response = input ("Is your number {}?".format(guess))
    #print("(please enter < less than, greater than >, or = equals)")
    if response == '<':
      high = guess - 1
    elif response == '>' :
      low = guess + 1
    elif response == '=' : 
      print("I guessed your number in {} tries".format(tries + 1))
      return #break
    else: 
      print("Invalid input please enter <, >, or = ")
      continue


    tries += 1
    print("Did not guess your number in five tries..")
def main(): 
  numbers = [2, 4, 7, 10, 32, 45, 87]

  while True: 
    print("Menu ")
    print("1 - Binary Search")
    print("2 - Guess Number Game")
    print("3 - Exit ")
    user_choice = (input("Enter your choice: "))
    if user_choice == '1':
      key = int(input("Enter an integer value: "))
      key_index = binary_search(numbers, key)
      if key_index == -1:
        print('{} was not found sowwy'.format(key))
      else: 
        print('Found the {} at index {}'.format(key, key_index))
    elif user_choice == '2':
      guess_game()
    elif user_choice == '3': 
      print("Goodbye.")
    else: 
      print("Invalid input attempt please enter 1,2, or 3")

if __name__ == "__main__":
  main()

