class Dictionary:

    def convert_lst_dict(self,keys,values):
        result = {}
        for i in range (len(keys)):
            if i < len(values):
                result[keys[i]] = values[i]
            else:
                result[keys[i]] = "Null"
        return result
    
    def count_string(self,string):
        freq = {}
        for i in string:
            freq[i] = freq.get(i,0) + 1
        return freq
    
    def key_max_value(self,dict1):
        max_key = max(dict1, key=dict1.get)
        return max_key
    
    def merge_two_dict(self,dict1,dict2):
        dict1.update(dict2)
        return dict1
    
    def remove_key_dict(self,dict1):
        dict1.pop("b")
        return dict1
    
    def sort_by_value(self,dict1):
        sorted_item = dict(sorted(dict1.items(), key = lambda x:x[1])) 
        return sorted_item