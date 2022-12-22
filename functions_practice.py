def hello():
    print("Hello user")

def pack(one, two, three):
    return[one, two, three]

def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(lunch_list)):
            if i == 0:
                print(f"First I eat {lunch_list[0]}")
            else: 
                print(f"Next I eat {lunch_list[i]}")

hello()
print(pack("one","two","three"))
eat_lunch(["sandwich", "chips", "orange"])
eat_lunch([])