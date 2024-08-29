import collections
from collections import defaultdict
class HashAlgos:

    def __init__(self):
        pass
    # input : ["eat","tea","tan","ate","nat","bat"]
    # output : [["bat"],["nat","tan"],["ate","eat","tea"]]
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return groups.values()

    def ransomeNoteAndMagazine(self, ransome, mag) -> bool:
        def counter(s):
            dict = {}
            for i in range(len(s)):
                dict[s[i]] = dict.get(s[i], 0) + 1
            return dict
        ransome_counter = counter(ransome)
        mag_counter = counter(mag)
        res = True
        for k,v in ransome_counter.items():
            if k in mag_counter.keys() and ransome_counter[k] > mag_counter[k]:
                return False
            elif k not in mag_counter.keys():
                return False
            else:
                continue
        return res

    def findJewelsAndStones(self, stones:str, jewels:str) -> int:
        def counter(s):
            d = collections.defaultdict(int)
            for i in s:
                d[i] += 1
            return d
        stones_counter = counter(stones)
        ans = sum(stones_counter[jewel] for jewel in jewels if jewel in stones_counter)
        return ans

    def lengthOfLongestSubstring(self, s):
        dynamic_window = []
        max_length = 0

        for x in s:
            if x in dynamic_window:
                dynamic_window = dynamic_window[dynamic_window.index(x) + 1:] # resize the window based on the index from the val

            dynamic_window.append(x)
            max_length = max(max_length, len(dynamic_window))

        return max_length

hash_algos = HashAlgos()
# res = hash_algos.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# res = hash_algos.ransomeNoteAndMagazine("aa", "aaba")
# res = hash_algos.findJewelsAndStones("aAAbbbb","aAb")
res = hash_algos.lengthOfLongestSubstring("bbbbb")
print(res)