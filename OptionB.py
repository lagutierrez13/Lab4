# Author: Luis Gutierrez
# Professor: Diego Aguirre CS 2302
# TA: Saha Pravakar
# Purpose: The purpose of this lab is to work with a hash table to find the number of anagrams
#          in a list of words. The program prompts the user to choose from a menu of options
#          to use to find the number of anagrams for each word on the list.
#          It then prompts the user to select from 2 options on operations to do using the hash table
#          This program will also compute the load factor of the hash table and also the average
#          number of comparisons made to perform a retrieve operation.

# Import used to close program
import sys


class Node:
    # Constructor with a word parameter creates the Node object.
    def __init__(self, word, next):
        self.word = word
        self.next = next


# This function contains the primary menu used to prompt the user
def print_main_menu():
    print("-----MENU-----")
    print("Chose the data structure or quit")
    print("1.) Hash Table")
    print("2.) Quit")
    print("--------------")


# This function contains the secondary menu used to prompt the user
def print_secondary_menu():
    print("-----MENU-----")
    print("What do you want to do?")
    print("1.) Find number of anagrams of a certain word")
    print("2.) Use my own file to see what word has the most anagrams")
    print("3.) Find table's load factor")
    print("4.) Compute average number of comparisons for retrieve function")
    print("5.) Quit")
    print("--------------")


# This hash function will sort the words in the hash table based on the first letter's ASCII value
# Hash table size of 94
def hash_function_1(word):
    # Get the first character from the line and the ASCII value for that character (32-126)
    first_letter = word[0:1]
    first_letter_value = ord(first_letter)
    # K is the value of the first character in the string
    return first_letter_value - 32


# This hash function will sort the words by the sum of the ASCII values of the characters
# Anagrams should be grouped in the same linked list
# Hash table size of 6000
def hash_function_2(word):
    sum_char_values = 0
    for char in word:  # Traverse through word and sum the values of each character
        sum_char_values += ord(char)
    return sum_char_values


# def hash_function_3(word):

# This function receives the name of a file and creates a Hash Table from its contents and returns it,
def create_hash_table_1(file):
    # Open the given file
    file1 = open(file)
    print("Creating Hash Table from file...")
    # Create Hash Table and insert the lines in the file as nodes using the hash function and taking care of collisions

    # Empty Hash Table of size 6000
    hash_table = [None] * 6000

    for line in file1:
        # Get location in Hash Table using the hash function
        location = hash_function_2(line)

        # Add the node to the linked list within the corresponding index in the hash table
        hash_table[location] = Node(line.strip(), hash_table[location])

    print("Hash Table finished")
    return hash_table


# Function that computes the load factor of a Hash Table
# The function receives a Hash Table as parameter
def compute_load_factor(hash_table):
    if hash_table is None:
        return None
    count = 0
    for head in hash_table:
        current = head
        while current is not None:
            count += 1
            current = current.next
    return int(count / len(hash_table))


# Function that computes the average number of comparisons made for successful retrieve operation on the hash table
def retrieve_average_number_of_comparisons(hash_table):
    if hash_table is None:
        return None
    master_count = 0
    for head in hash_table:
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        master_count = master_count + (count // 2)
    return master_count // len(hash_table)


# Used for testing purposes
# Function prints the contents of the tree in-order
# The root of the tree is passed into the function
def print_hash_table(hash_table):
    for head in hash_table:
        current = head
        while current is not None:
            print(current.word)
            current = current.next


# Function that receives the root of a tree, a word and a prefix and computes the permutations of word
# It looks for the permutations in the tree and sees if they are a valid word
# The function returns the number of permutations that are a valid word
def count_anagrams(hash_table, word, prefix=""):
    # Base case
    if len(word) <= 1:
        string = prefix + word

        # Traverse the tree to look for word ***************
        in_tree = False
        # Using the hash function get the the index where the words with that first character are stored
        current = hash_table[hash_function_2(word)]
        while current is not None:
            if current.word.lower() == string.lower():
                in_tree = True  # The string is in the tree
                current = None  # End the loop because you have found the string in the tree
            current = current.next

        # If the word has been found in the tree... print the word with the prefix added
        if in_tree:
            return 1
        else:
            return 0
    else:
        # If the word is larger than 1 letter...
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur
            if cur not in before:  # Check if permutations of cur have not been generated.
                return 1 + count_anagrams(hash_table, before + after, prefix + cur)


# Function that returns the word in a file that contains the most anagrams
# The function's parameters are the file with the words to compare and the tree with all the english words
def most_anagrams(file, hash_table):
    # File to get words from to make anagrams and compare how many each have to get the max
    file1 = open(file)
    max_anagrams = 0
    max_anagrams_word = ""
    # Traverse through the file's words and count the anagrams in each word and find the word with
    # the largest number of anagrams
    for line in file1:
        count = count_anagrams(hash_table, line)
        if count > max_anagrams:
            max_anagrams = count
            max_anagrams_word = line
    return max_anagrams_word


# Function used for testing specific parts of the code
# Some examples are shown
# ***************************************
def test():
    # Create the hash table
    table = create_hash_table_1("words.txt")
    print_hash_table(table)
    # print(count_anagrams(table, "something"))
    # print(most_anagrams("MyTest.txt", table))
    # print(retrieve_average_number_of_comparisons(table))


def main():
    print_main_menu()
    answer = input()

    # Ensure the answer is of valid type integer and one of the options
    while answer.isdigit() is False or (int(answer) != 1 and int(answer) != 2):
        if not answer.isdigit():
            answer = input("TYPE ERROR on input. Try again: \n")
        else:
            answer = input("INVALID NUMBER. Try again: \n")

    # Depending on selection do something

    # If 1 create a hash table
    if int(answer) == 1:
        my_table = create_hash_table_1("words.txt")

        print_secondary_menu()
        answer = input()

        # Ensure the answer is of valid type integer and one of the options
        while answer.isdigit() is False or (
                int(answer) != 1 and int(answer) != 2 and int(answer) != 3 and int(answer) != 4 and int(answer) != 5):
            if not answer.isdigit():
                answer = input("TYPE ERROR on input. Try again: \n")
            else:
                answer = input("INVALID NUMBER. Try again: \n")

        # Repeat the second menu until the user quits
        while int(answer) != 5:
            # If 1 ask for the word to find number of anagrams for
            if int(answer) == 1:
                print("Enter the word you want to use")
                word_answer = input()

                while word_answer.isdigit():
                    word_answer = input("TYPE ERROR. Enter a valid word: \n")

                anagrams = count_anagrams(my_table, word_answer)
                print(word_answer + " has " + str(anagrams) + " anagrams")
            # If 2 ask for the name of the file to use
            elif int(answer) == 2:
                print("Enter the name of the file you want to use")
                word_answer = input()

                try:
                    return_word = most_anagrams(word_answer, my_table)
                    print("The word with the most anagrams is: " + return_word)
                except FileNotFoundError:
                    print("File could not be found")
                    sys.exit("CLOSING PROGRAM")
            # If 3 compute the load factor of the table
            elif int(answer) == 3:
                print("The load factor for this table is: ", compute_load_factor(my_table))
            # If 4 compute the average number of comparisons for the table
            elif int(answer) == 4:
                print("The average number of comparisons is: ", retrieve_average_number_of_comparisons(my_table))

            print_secondary_menu()
            answer = input()

            # Ensure the answer is of valid type integer and one of the options
            while answer.isdigit() is False or (
                    int(answer) != 1 and int(answer) != 2 and int(answer) != 3 and int(answer) != 4 and int(
                answer) != 5):
                if not answer.isdigit():
                    answer = input("TYPE ERROR on input. Try again: \n")
                else:
                    answer = input("INVALID NUMBER. Try again: \n")
        sys.exit("CLOSING PROGRAM")

    # If 2 quit
    elif int(answer) == 2:
        sys.exit("CLOSING PROGRAM")


# test()
main()
