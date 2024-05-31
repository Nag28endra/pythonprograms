dict = {'vamsi':'python',
        'shashank':'java',
        'venkatesh':'C++',
        'Harshath':'python',
        'Likitha':'Java',
        'Namratha':'Java',
        'Preeti':'python',
        'Bhavya':'Java',
        'Madhuri':'C',
        'Vyshali':'python',
        'keerthi':'C++'
       }
count = 0
for values in dict.values():
    if values == 'python':
        count +=1
print(f'there are {count} members who are interested in python')