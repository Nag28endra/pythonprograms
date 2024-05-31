# def myFunction():
#     """ this is the function body that is used for writing a block of code"""
#     print('Welcome to the functions concept')

# myFunction()

# """ line 1 is the 'function definiton' and the line 5 is a 'function call'.
#     These are the two most important parts of the entire program.
#     Function defintion: holds the block of code to be executed
#     Function call: it will call the function that was defined
# """

# def myFavouriteBook(book): # book is a parameter
#     """ passing parameters to the function. 
#         sometimes these are called arguments
#     """
#     print(f"{book} is my favourite of all time")

# myFavouriteBook('Harry Potter')#passing string value

def myFavouriteBook(book,character):
    """using key-value pair to match the parameters with those of 
       the function parameters.
    """
    print(f"{character.title()} is my favourite character in {book.title()} book")

myFavouriteBook(book='harry potter', character="professor snape")
# NOTE: the keys used in the function call should be same as those given in function 

