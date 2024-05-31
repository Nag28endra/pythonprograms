def mapping(value):
    return value**2

if __name__ == "__main__":
    myList = [12,23,34,54,65]
    AList = list(map(mapping,myList))
    print(AList)