#!/usr/bin/env python3
import sys

# Function to check if the letters used in a sequence are of the list A,C,G, OR T
def ACGT_check(string):
    # Letters that are used on the DNA sequences
    valid_letters = {'A', 'C', 'G', 'T'}
    
    # Check if all the letters in the sequence are A,C,G, OR T 
    for letter in string:
        if letter not in valid_letters:
            return False

    return True

# Function to calculate the observed substrings that are in a specific sequence
def count_observed_substrings(sequence, k):
    # If the sequence contains any lower case or a different letter from A,C,G, OR T
    # the function returns a message of warning.
    if any(char.islower() for char in sequence) or not ACGT_check(sequence):
        return("The sequence must be in capital letters and all the letters must be A,C,G, or T")
    else:       
        # Create an empty set
        substrings = set()
        # For loop that reads in each iteration the first k letters and in the next 
        # iteration moves to the next letter and reads again k more letters.
        for i in range(len(sequence) - k + 1):
            substring = sequence[i:i+k]
            # Adds the substring to the substrings set, ensuring that only unique 
            # elements are stored in the set
            substrings.add(substring)
        return len(substrings)


# Function to calculate the possible substrings that could be in a specific sequence
def count_possible_substrings(sequence, k):
    if k == 1:
        return(4) # Since there are only 4 possible letters(A,C,G,AND T)
    else:
        # The maximum possible theoretical substrings is provided by the number of letters
        # that the sequence contains minus the size of the substrin plus 1.
        return len(sequence) - k + 1
    

# Function to calculate the linguistic complexity of a sequence of DNA    
def calculate_linguistic_complexity(sequence):
    # Intialize the count of both observed and possible substrings
    total_observed = 0
    total_possible = 0
    
    # For loop to add all the observed and possible substring for the range of the sequence
    for k in range(1, len(sequence) + 1):
        observed = count_observed_substrings(sequence, k)
        possible = count_possible_substrings(sequence, k)

        total_observed += observed
        total_possible += possible
    
    # Linguistic complexity formula
    linguistic_complexity = total_observed / total_possible
    return linguistic_complexity

def main():

    # Check if the file path is provided as a command line argument
    if len(sys.argv) < 2:
        print("Please provide the path to the sequence data file.")
        return
    # Assign the first argument provided on the terminal as file_path
    file_path = sys.argv[1]

    try:
        # Opens the file, reads it and splits the string into a list of lines
        with open(file_path, 'r') as file:
            sequences = file.read().splitlines()
        
        # Calculates the linguistic complexity of the sequence with the the previous functions 
        # Prints a message with the sequence and the linguistic complexity
        for i, sequence in enumerate(sequences):
            linguistic_complexity = calculate_linguistic_complexity(sequence)
            print(f"Sequence {i + 1}: Linguistic Complexity = {linguistic_complexity:.3f}")
    
    # If the file provided as an argument after the script name is not found it shows an error
    except FileNotFoundError:
        print(f"File not found: {file_path}")


if __name__ == '__main__':
    main()