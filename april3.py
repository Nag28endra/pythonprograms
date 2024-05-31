# def duplicate_count(s):
#     """
#     Returns the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in
#     the input string.
#     """
#     char_count = {}
#     for char in s:
#         char = char.lower()
#         if char.isalnum():
#             if char in char_count:
#                 char_count[char] += 1
#             else:
#                 char_count[char] = 1
#     return sum(1 for count in char_count.values() if count > 1)

# duplicate_count('Indivisibilities')

# def delete_nth(order,max_e):
#     result = []
#     counts = {}
#     for x in order:
#         if x not in counts:
#             counts[x] = 0
#         if counts[x] <max_e:
#             result.append(x)
#             counts[x] += 1
#     return result


# print(delete_nth([1,1,3,3,7,2,2,2,2], 3))
def order(string):
    if not string:
        return ""
    
    words = string.split()
    sorted_words = [""] * len(words)
    
    for word in words:
        index = int(''.join(filter(str.isdigit, word))) - 1
        sorted_words[index] = word
        
    return ' '.join(sorted_words)
order("is2 Thi1s T4est 3a")