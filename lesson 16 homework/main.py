# Masala 1 
# a = int (input("A ni kirting : "))
# b = int (input("B ni kirting : "))

# count = 0 
# while a >= b :
#     a-=b
#     count+=1

# print(count)

# Masala 2
# a = int (input("A ni kirting : "))
# b = int (input("B ni kirting : "))


# while a >= b :
#     a-=b

# print(a)

# Masala 3
# n = int (input("N ni kirting : "))
# k = int (input("K ni kirting : "))


# while n >= k :
#     n-=k

# print(n)


# Masala 4
# n = int(input("n: "))
# x = 1
# while x < n:
#     x *= 3
# if x == n:
#     print("3 - ning darajasi")
# else:
#     print("3 - ning darajasi emas")

# Masala 5
# n = int(input("n: "))
# x = 1
# while x < n:
#     x *= 2
# if x == n:
#     print("2 - ning darajasi")
# else:
#     print("2 - ning darajasi emas")

# Masala 6
# n = int(input("n: "))
# result = 1
# i = n
# while i > 1:
#     result *= i
#     i -= 2
# print(result)

# Masala 7
# n = int(input("n: "))
# k = 1
# while k * k <= n:
#     k += 1
# print(k - 1)

# Masala 8
# n = int(input("n: "))
# k = 1
# while k * k < n:
#     k += 1
# print(k)

# Masala 9
# n = int(input("n: "))
# k = 0
# while 3  k <= n:
#     k += 1
# print(k)

# Masala 10
# n = int(input("n: "))
# k = 0
# while 3  k < n:
#     k += 1
# print(k)

# Masala 11
# n = int(input("n: "))
# k = 0
# sum_ = 0
# while sum_ < n:
#     k += 1
#     sum_ += k
# print(k, sum_)

# Masala 12
# n = int(input("n: "))
# k = 0
# sum_ = 0
# while sum_ + k + 1 <= n:
#     k += 1
#     sum_ += k
# print(k, sum_)

# Masala 13
# a = float(input("a: "))
# sum_ = 0.0
# k = 0
# while sum_ < a:
#     k += 1
#     sum_ += 1 / k
# print(k, sum_)

# Masala 14
# a = float(input("a: "))
# sum_ = 0.0
# k = 0
# while sum_ + 1 / (k + 1) <= a:
#     k += 1
#     sum_ += 1 / k
# print(k, sum_)




# Masala 
son = int(input("Enter a number: "))
start = pow(10,(son-1))
finish = pow(10,son) - 1

while start <= finish:
    print(start)
    start += 1
