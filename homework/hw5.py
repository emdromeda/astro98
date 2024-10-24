import numpy as np

# 1 the odd ones out

arr=np.array([[1,2,3],[5,7,9],[2,4,6],[7,7,7]])
def only_odd(array):
    odd_rows=np.array([], dtype=int)
    n=0
    for row in array:
        check=[]
        for i in row:
            if i%2==1:
                check.append(True)
            else:
                check.append(False)
        if all(check):
            odd_rows = np.append(odd_rows,row)
            n=n+1
        odd_rows = odd_rows.reshape((n, arr.shape[1]))
    return odd_rows

print(only_odd(arr))

# 2 lets play checkers

# 2.1-2.3
def checkerboard():
    board = np.zeros([8,8], dtype=int)
    for n in range(board.shape[0]):
        if n%2==0:
            for m in range(board.shape[1]):
                if m%2==0:
                    board[n][m]=1
    for n in range(board.shape[0]):
        if n%2==1:
            for m in range(board.shape[1]):
                if m%2==1:
                    board[n][m]=1
    return board

print(checkerboard())

# 2.4 
def reverse_checkerboard():
    board = np.zeros([8,8], dtype=int)
    for n in range(board.shape[0]):
        if n%2==1:
            for m in range(board.shape[1]):
                if m%2==0:
                    board[n][m]=1
    for n in range(board.shape[0]):
        if n%2==0:
            for m in range(board.shape[1]):
                if m%2==1:
                    board[n][m]=1
    return board

print(reverse_checkerboard())

# 3 the expanding universe
universe = np.array(['galaxy', 'clusters'])
def expansion(arr, n):
    expanded_arr=np.array([])
    for word in arr:
        expanded_word=""
        m=0
        p=len(word)-1
        while m < p:
            expanded_letter = word[m]+n*" "
            expanded_word = expanded_word+expanded_letter
            m=m+1
        expanded_word = expanded_word+word[-1]
        expanded_arr = np.append(expanded_arr, expanded_word)
    return expanded_arr

print(expansion(universe, 3))

# 4 
planets = np.random.randint(100, 1000, (5, 5))
def second_largest(array):
    second_largest_planets=np.array([], dtype=int)
    ordered_array=np.transpose(array)
    ordered_array = np.sort(ordered_array)
    for row in ordered_array:
        second_largest_planets=np.append(second_largest_planets, row[-2])
    return second_largest_planets

print(second_largest(planets))


