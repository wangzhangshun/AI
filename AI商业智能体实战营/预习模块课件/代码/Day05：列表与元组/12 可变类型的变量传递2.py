l1 = [1, 2, 3]
l2 = [l1, 4, 5]  # l2[0] =  l1

# print(id(l1))
# print(id(l2[0]))

# l1.append(4)
# print(l1)
# print(l2[0])

# l2[0][2] = 300
# print(l1)
# print(l2[0])

# l1 = 1000
# print(id(l1))
# print(id(l2[0]))


l2[0] = 1000
# print(l1)
# print(l2)  # [1000,4,5]
l1[2] = 3000
print(l1)
print(l2)
