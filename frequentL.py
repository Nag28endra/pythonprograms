myList = ['nagendra','vamsi','preeti','keerthi','namratha','nagendra']
frequent = max(dict.fromkeys(myList),key =myList.count)
print(f'the most frequent repeated name is {frequent}')