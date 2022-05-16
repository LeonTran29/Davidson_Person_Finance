lst = []
text = [1,2,3]
for i in text:
    try:
        int(i)
        lst.append(int(i))
    except:
        continue
_dict = {}
for i in lst:
    _dict[i] = i**3
    
print(_dict)