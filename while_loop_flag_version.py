
def get_starting_number():
    while True:
        num = input("How many bottles of beer on the wall? ")
        if num.isdigit():
            num = int(num)
            if num > 0:
                return num
            else:
                print("Please enter a number that is euqal or greater than 1.")
        else:
            print("Please enter a valid positive integer.")

def sing(starting_bottles):
    bottles = starting_bottles
    singing = True
    while singing:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles-1} {'bottles' if bottles-1 > 1 else 'bottle'} of beer on the wall.\n")
            bottles -= 1
        elif bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
            singing = False