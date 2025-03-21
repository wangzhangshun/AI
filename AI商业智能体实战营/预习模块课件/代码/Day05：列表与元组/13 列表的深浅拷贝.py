# 案例1

# l1 = [1, 2, 3]
# l2 = l1[:]

# print(id(l1))
# print(id(l2))

# print(id(l1[0]))
# print(id(l2[0]))
# print(id(l1[1]))
# print(id(l2[1]))
# print(id(l1[2]))
# print(id(l2[2]))


# l2 = l1.copy()
# l2 = list(l1)

# l1[0] = 100
# print(l2)
# l2[1] = 200
# print(l1)

# l1[2] = 300

# 案例2

# l1 = [1, 2, 3, [4, 5]]
# l2 = l1[:]

# l1[0] = 100
# print(l2)


# l1[3][0] = 400
# print(l2)

# l2[3][1] = 500
# print(l1)


# 深拷贝实现

import copy

# 浅拷贝
# copy.copy()
l1 = [1, 2, 3, [4, 5]]
l2 = copy.deepcopy(l1)

l2[3][0] = 400
print(l1)



