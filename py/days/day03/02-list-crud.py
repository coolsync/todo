A = ["bob", "mark", "jerry"]

print('-------append elem to list A, before-------')
for v in A:
    print(v)

tmp = input('please input name: ')

A.append(tmp)

print('-------append elem to list A, after-------')
for v in A:
    print(v)

# modify
A[1] = "hello"

print(A)