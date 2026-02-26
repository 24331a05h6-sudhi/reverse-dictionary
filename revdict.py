def reverse_lookup(data,target):
    results=[]
    for k,v in data.items():
        if v==target:
            results.append(k)
    return results
my_dict={"siraj":"73","virat":"18","iyer":"96" }
print(reverse_lookup(my_dict,"96"))