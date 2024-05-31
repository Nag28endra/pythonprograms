# dict_1 = {'name':'nagendra','language':'python'}
# dict_2 = {'name':'vamsi','language':'java'}
# myList =[dict_1,dict_2]
# for i in myList:
#     print(i)

# details = { 'nagendra': ['python','c','sql','dsa'],
#              'vamsi': ['java','python']
#             }
# for keys,values in details.items():
#     print(f'the language of {keys} are:')
#     for language in values:
#         print(language.split())

dictionary = {'name':'Sita','branch':'cse'}
def fun(name,branch):
    print(name,branch)
fun(**dictionary)