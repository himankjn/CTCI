from collections import defaultdict
#O(wlogw*n)
def groupanagrams(L):
    
    strdic=defaultdict(list)

    for s in L:
        strdic["".join(sorted(s))].append(s)
    fin=[]
    for k,v in strdic.items():
        fin.extend(v)
    return fin

print(groupanagrams(["abc","def","cba","bca","fed"]))