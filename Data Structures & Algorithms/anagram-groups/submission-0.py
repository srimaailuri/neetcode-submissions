class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map={}
        for i in strs:
            sorted_i=sorted(i)
            sorted_string = "".join(sorted_i) 
            if sorted_string in hash_map:
                value_list=hash_map[sorted_string]
                value_list.append(i)
                hash_map[sorted_string]=value_list
            else:
                hash_map[sorted_string]=[i]
        return list(hash_map.values())
        