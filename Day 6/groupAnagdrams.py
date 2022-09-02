import collections
anagrams=['me','em','surya','uryas','dict','cidt','vijay']
temp=collections.defaultdict(list)
for i in anagrams:
    item=[char for char in i]
    item.sort()
    temp[''.join(item)].append(i)
print(len(temp.values()))
