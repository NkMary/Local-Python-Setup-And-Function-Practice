def print_hello():
    print("hello, User!")
print_hello()

def print_pack(city, state, zipcode):
    print(city, state, zipcode)
print_pack(city="West Hempstead", state="New York", zipcode="11552")

def eat_lunch():
    lunchbox = ['rice', 'plantain', 'chicken', 'salad']
    if len(lunchbox) == 0:
        print("My lunchbox is empty!")
    else:
        print(f"first I eat {lunchbox[0]}")
        for i in range(1, len(lunchbox)):
            print(f"Next I eat {lunchbox[i]}")

eat_lunch([])
eat_lunch(['rice'])
eat_lunch(['rice', 'plantain', 'chicken', 'salad'])