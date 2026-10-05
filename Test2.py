orders_amount = [100,200,None,"Ajab",300,100.25]
orders_amount_int = [100,900,300,100,2000,45,9800,23.45,0,-1,-300,9800]

orders_amount_tup = (100,200,None,"Ajab",300,100.25)
i = 0
sum = 0
# for i in orders_amount:
#     if type(i)==int or type(i)==float:
#         sum = sum+i
# print(sum)

# while i < len(orders_amount):
#     if type(orders_amount[i])==int or type(orders_amount[i])==float:
#         sum = sum + orders_amount[i]
#     i+=1
# print(sum)

# while True:
#     if type(orders_amount[i])==int or type(orders_amount[i])==float:
#         sum = sum + orders_amount[i]
#     i+=1
#     if i == len(orders_amount):
#         break
# print(sum)

print(orders_amount.index("Ajab"))
print(orders_amount_tup.index("Ajab"))



orders_amount_int.sort()

print(orders_amount_int)

orders_amount_int.reverse()

print(orders_amount_int)

orders_amount_cp = orders_amount.copy()

print(orders_amount_cp)

orders_amount[0]="Changed"

print(orders_amount_cp)

order_amount_pointer = orders_amount

orders_amount[0]="Changed"

print(order_amount_pointer)

orders_amount_set = set(orders_amount_int)

print(orders_amount_set)

orders_amount_list = list(orders_amount_set)

print(orders_amount_list)