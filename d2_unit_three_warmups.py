def add_one(number):
    number += 1
    print("number in function is", number)


def main():
    number = 5
    add_one(number)
    print("number in main is", number)  # I think it will print 5


main()
