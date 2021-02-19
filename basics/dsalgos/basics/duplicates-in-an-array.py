def find_duplicates(numbers):

    for num in numbers:
        if (numbers[abs(num)]>0):
             numbers[abs(num)]=-numbers[abs(num)]
        else:
            print("Duplicate found %s" % abs(num))



if __name__ == '__main__':

    numbers =[1, 2, 3, 2, 1, 4]

    print(find_duplicates(numbers))
