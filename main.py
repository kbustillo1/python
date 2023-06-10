print("hello world!")
y = input("give me a number ")
print(type(y))
for x in range(-10, 11):
    if x % 2 == 0:
        print(x / int(y))
my_list = [1, 2, 3, 4, 5]
print(type(my_list))
my_dict = {
    "a": "b",
    "c": my_list
}
print(type(my_dict))
print(my_dict["c"][0])
print(type(my_dict["c"][0]))
