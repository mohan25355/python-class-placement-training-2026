fruit=["apple","mango","orange","banana"]
# newlist=[x if x=="banana" else "orange" for x in fruit]
# newlist=["orange" if x=="banana" else x for x in fruit]
newlist=[x if x!="banana" else "orange" for x in fruit]
print(newlist)