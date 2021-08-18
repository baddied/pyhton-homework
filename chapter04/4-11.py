'''
pizza_list = ['red pizze','yellow pizza','green pizza']
friend_pizzas = pizza_list[:]

pizza_list.append('blue pizza')
friend_pizzas.append('black pizza')

print("My pizza:")
print(pizza_list)
print("\n Friend pizza:")
print(friend_pizzas)

for myp in pizza_list:
    print(myp)

for frp in friend_pizzas:
    print(frp)
'''

pizzas=['hawaii',"hotdong",'spicy']
friend_pizzas=pizzas[:]
pizzas.append('cheese')
friend_pizzas.append('mango')
print("My favorite pizzas are:")
for p in pizzas:
    print(p)
print()
print("My friend's favorite pizzas are:")
for fp in friend_pizzas:
    print(fp)



