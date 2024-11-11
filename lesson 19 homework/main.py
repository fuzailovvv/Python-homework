# Masala 1
# list = [1 , 2 , 3 , 8 , 5 , 6 , 7 , 8 , 9 ]
# son = int (input("sonni kirting : "))

# i = 0
# find = 0
# while(i<len(list)) :
#     if list[i]==son :
#         find = list[i]
#     i+=1 

# if (find==son) :
#     print("True")
# else :
#     print("False")


# Masala 2
# i = 100 
# while i<=999 :
#     b = i%10 
#     o = i//10%10
#     y = i//100%10
#     if (b+o+y>5 and b+o+y<8) :
#         print(i)
#     i+=1


# Masala 
# son = int (input("Sonni kirting : "))

# if son<0 :
#     son=-son

# xonalr_soni = 0 

# while son > 0 :
#     son//=10
#     xonalr_soni+=1

# if xonalr_soni==0 :
#     xonalr_soni =1 

# print(xonalr_soni)


# Masala 4
# son = int (input("Sonni  uzunligini kiriting : "))

# summa = 0
# i = 0
# while i<son:
#     a = int (input("Sonni kirit : ")) 
#     summa += a 
#     i+=1

# print(summa)

son = int (input("Son uzunligini kirting : "))

i = 0 
katta =  y = int (input("Sonni kirting : "))
while i<son-1 :
    y = int (input("Sonni kirting : "))
    if y<katta :
        katta = y
    
print(katta)