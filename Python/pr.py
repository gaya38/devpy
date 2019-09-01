list_a = [1, 2, 3]
list_b = [10, 20, 30]  
print map(lambda x, y: x + y, list_a, list_b)
a = [1, 2, 3, 4, 5, 6]
print filter(lambda x : x % 2 == 0, a)
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
print filter(lambda x : x['name']=='python',dict_a)
