# squares = []
# for i in range(1,11):
#     square = i**2
#     squares.append(square)
# print(squares)

# squares = [i**2 for i in range(1,11)]
# print(squares)

# list = [['master',2021],['bigil',2019],['sarkar',2018],['mersal',2017]]

# for i in list:
#     for j in i:
#         print(i)
# aliens = []
# for alien in range(20):
#     new_alien = {'color':'red','points':5}
#     aliens.append(new_alien)

# for i in aliens[:5]:
#     print(i)
 

# dict ={'name':'nagendra','languages':'python','goal':'AI and ML engineer'}
# for value in dict.values():
#     print(value)

details = {
                "mvnb":{
                            'first':'nagendra',
                            'last':'marisetti',
                            'location':'bcm'
                       },
                'bvamsi':{
                           'first':'vamsi',
                           'last':'bandi',
                           'location':'raghavapuram'
                }
          }
for username,useinfo in details.items():
    print(f'username:{username}')
    print(f"fullname: {useinfo['first']} {useinfo['last']}")
    print(f'location: {useinfo["location"]}')