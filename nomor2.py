
def counter(x):
    hasil = list(map(list, zip(*x)))[::-1]
    print("", hasil[0], '\n', hasil[1], '\n', hasil[2])
    return hasil
    

A = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

B = [[9, 8, 7],
[6, 5, 4],
[3, 2, 1]]

counter(A)
print("="*50)
counter(B)


