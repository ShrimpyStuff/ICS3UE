x = 10
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def twod_search(outer_list, value):
    appears = False
    for inner in outer_list:
        if value in inner:
            appears = True
    return appears

print(twod_search(board, x))