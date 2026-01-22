from ListTask import List
from DictTask import Dictionary


dict1 = {"a": 10, "b": 50, "c": 30}
dict2 = {"d": 3, "e": 4}
numbers = [1, 2, 3, 4, 5]
keys =  ["name","age","dept"]
values = ["Manjunath",24]
obj = List()
obj1 = Dictionary()
string = "malayalam"
# print(obj1.convert_lst_dict(keys,values))
search_lst = ["ab","abab","aba","aaaa","aaaaa","aaaaaaaa"]
target = "ab"
print(obj.binary_search(search_lst, target))



