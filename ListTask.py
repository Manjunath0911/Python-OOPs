# sum of all elements in a list
class List:
    
    def sum_list(self,lst):
        total = 0
        for i in lst:
            total  += i
        return total
    
    def max_lst(self,lst):
        print( max(lst))
    
    def count_even_odd(self,lst):
        odd = even = 0
        for i in lst:
            if i %  2 == 0:
                even += i
            else:
                odd += i
        print(f'even = {even}\nodd = {odd}') 

    def reverse_lst(self,string):
        reversed = string[::-1]
        print(f'reversed list : {reversed}')

    def remove_duplicate(self,lst):
        unique = []
        for i in lst:
            if i not in unique:
                unique.append(i)
        # print(f'unique list is : {unique}') 
        return unique

    def second_larget(self,unique):
        unique.sort()
        if len(unique) >= 2: 
            print(f'second largest element in a list is : {unique[-2]}')
        else:
            print(f'length of the list is only: {len(unique)}')
        
    def common_element(self,lst1,lst2):
        common = []
        common_unique =  []
        for i in lst1:
            if i in lst2:
                common.append(i)

        for i in common:
            if  i not in common_unique:
                common_unique.append(i)

        print(f'common elements in two list is : {common_unique}')
    
    def binary_search(self,search_lst, target):
        n = len(search_lst)
        left = 0
        right = n-1

        while left <= right:
            mid = (left+right)//2
            
            if search_lst[mid] == target:
                return mid
            elif search_lst[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def lowest_element(self,lst):
        for i in range(len(lst)):
            if lst[i] < lst[i+1]:
                return lst[i] 
            
    def rotate_lst(self,lst,key):
        key = key % len(lst)
        rotate = lst[key:] + lst[:key]
        return rotate
    
    def frequency(self,lst):
        freq = {} 
        for i in lst:
            freq[i] = freq.get(i,0) + 1
        print(freq)

    def even(self,n):
        if n % 2 == 0:
            return True
        else:
            False





# data
target = 10
search_lst = [2,3,6,8,12,13,16,18]

lst1 = [2,4,1,4,8,3]
lst2 = [4,6,9,8,1,0]
string = "manjunath"
lst = [1,2,3,7,12,7,12,3,8,2,3]
obj1 = List()
# result = obj1.binary_search(search_lst, target)
# if result != -1:
#     print("element found at index : ",result)
# else:
#     print("element not found")
# print(obj1.rotate_lst(lst))
