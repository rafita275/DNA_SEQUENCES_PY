from DNA_script import *

# Test function for substrings of size 2
def test_size_2():
    string = "ATTTGGATT"
    k = 2
    actual_output = count_observed_substrings(string,k)
    expected_output = 5
    assert actual_output == expected_output
test_size_2()

# Test function for substrings of size 3
def test_size_3():
    string = "ATTTGGATT"
    k = 3
    actual_output = count_observed_substrings(string,k)
    expected_output = 6
    assert actual_output == expected_output
test_size_2()

# Test function for sequences with different letters
def test_dif_letter():
    string = "ATTTGGATTE"
    k = 3
    actual_output = count_observed_substrings(string,k)
    expected_output = "The sequence must be in capital letters and all the letters must be A,C,G, or T"
    assert actual_output == expected_output
test_dif_letter()

# Test function for sequences that contain lower case letters
def test_lower_case():
    string = "ATTTGGATTa"
    k = 3
    actual_output = count_observed_substrings(string,k)
    expected_output = "The sequence must be in capital letters and all the letters must be A,C,G, or T"
    assert actual_output == expected_output
test_lower_case()

# Test function for possible substrings of size 3 in a sequence 
def test_size_3_pos():
    string = "ATTTGGATT"
    k = 3
    actual_output = count_possible_substrings(string,k)
    expected_output = 7
    assert actual_output == expected_output
test_size_3_pos()

# Test function to check the linguistic complexity of a sequence
def test_complexity():
    string = "ATTTGGATT"
    actual_output = calculate_linguistic_complexity(string)
    expected_output = 0.875
    assert actual_output == expected_output
test_complexity()