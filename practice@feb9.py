# mydictionary = {'name':'nagendra','branch':'cse','programming language':'python'}
# print('give the query:')

# for k,v in mydictionary.items():
#     print(k+":"+v)
    
# programmers =[
#                    {
#                     'name':'nagendra',
#                     'programming language':'python'
#                    },
#                    {
#                     'name':'vamsi',
#                     'programming language':'python'
#                    },
#                    {
#                     'name':'shashank',
#                     'programming language':'python',
#                    },
#                    {
#                      'name':'Namratha',
#                      'programming language':'java'
#                    },
#                    {
#                     'name':'Preeti',
#                     'programming language':'java'
#                    },
#                    {
#                     'name':'Keerthi',
#                     'programming language':'C++'
#                    }
            
#             ]
# for programmer in programmers:
#     print(programmer["name"])

# programmers= {
#                 'vamsi':'python',
#                 'shashank':'python',
#                 'nagendra':'python',
#                 'namratha':'java',
#                 'preeti':'java',
#                 'keerthi':'C++'
#             }
# for value in set(programmers.values()):
#     languages = list(value)
#     count = programmers.values().count(languages)
#     print("{count} people are interested in {value}")

# programmers = {'vamsi':'python',
#         'shashank':'java',
#         'venkatesh':'C++',
#         'Harshath':'python',
#         'Likitha':'Java',
#         'Namratha':'Java',
#         'Preeti':'python',
#         'Bhavya':'Java',
#         'Madhuri':'C',
#         'Vyshali':'python',
#         'keerthi':'C++'
#        }

# for values in set(programmers.values()):
#     count = list(programmers.values()).count(values)
#     print(f"{count} people are interested in {values}")
# print(count)

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input() 
#     for k,v in student_marks.items():
#         if query_name==k:
#             sum = 0
#             for marks in v:
#                 sum += marks
#             percentage = sum/3

#     print("{:.2f}".format(percentage))


# print('enter no of students:')
# n = int(input())
# st_details = {}
# for _ in range(n):
#     name,*line = input().split()
#     score = list(map(float,line))
#     st_details[name] = score 
# print('enter the student name:')
# query = input()
# for k,v in st_details.items():
#     if query == k:
#         sum = 0
#         for marks in v:
#             sum += marks
#         percentage = sum/3
# print("the average marks are: {:.2f}".format(percentage))

# myarry = input("enter the values").split()
# values = list(map(int,myarry))
# maxelement = values[0]

# for value in values:
#     if value>maxelement:
#         maxelement = value

# print(maxelement)


# msg = 'hello my name is nagendra and im from cse final year'
# msg_l = len(msg)
# for i in range(msg_l):
#     if (msg[i].islower()):
#         msg[i].upper()
#     else:
#         msg[i].lower()
# print(msg)
    
# # for i in 

# # def swap_case(s):
# #     length = len(s)
# #     for i in range(length):
# #         if s[i].islower():
# #             s[i].upper()
# #         else:
# #             s[i].lower()
# #     return s

# # if __name__ == '__main__':
# #     s = input()
# #     result = swap_case(s)
# #     print(result)

# def count_substring(string, sub_string):
#    S_list = list(string)
#    S_length = len(S_list)
#    Sub_list = list(sub_string)
#    Sub_length  = len(Sub_list)
#    pattern = 0
#    for i in range(S_length):
#     for j in range(Sub_length):
#         if S_list[i]==Sub_list[j]:
            
            
            
#    print(pattern)

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
   