def myFilter(value):
    if value > 20:
        return value

if __name__ == "__main__":
    myList = [12,23,27,67,90,56,87]
    AList = list(filter(myFilter,myList))
    print(f' the filtered list elements are {AList}')

