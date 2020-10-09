'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Create a dictionary
    frequency = dict()

    # Loop through arr

    for number in arr:
        # If number exists as value, add 1,
        # If not, add key to dictionary
        if number not in frequency:
            frequency[number] = 1
        else:
            frequency[number] += 1

    #loop through dictionary
    for key in frequency:
        #if value equals 1, return integer
        if frequency[key] == 1:
            return key






    return -1



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
