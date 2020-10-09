'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):

    zero_counter = 0

    for i in range(len(arr) - 1):
        if arr[i] == 0:
            zero_counter += 1
    #loop through arr,
    # if i equals 0, then swap with the right
    while zero_counter != 0:
        for i in range(len(arr) - 1):
            if arr[i] == 0:
                print(arr)
                arr[i], arr[i+1] = arr[i+1], arr[i]
        zero_counter -= 1


    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
