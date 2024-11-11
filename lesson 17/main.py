# son = int (input("Sonni kirting : "))
# daraja = int(input("DArajani kirting : "))

# kv = 1
# d = daraja
# while daraja>0 :
#     print(son)
#     kv*=son
#     daraja-=1


# print(f"{son} ning {d} darajasi : {kv}")


son = 100
while son<999 :
    print(son)
    son+=1

print(son)

num = 0
while (True) : 
    b = son%10
    o = son//10%10
    y= son //100%10

    yigindi = b+o+y 
    if (yigindi%2==0):
        print(yigindi)
    if (yigindi==27) :
        break 

