'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    arr.sort()
    for i, x in enumerate(arr):
        if i + 1 == len(arr):
            if arr[i-1] != x:
                return x
        if i == 0:
            if arr[i+1] != x:
                return x
        if arr[i-1] != x and arr[i+1] != x:
            return x


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")