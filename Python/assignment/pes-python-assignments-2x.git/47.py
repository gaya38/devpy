def ext(tup,lst):
    lst=tuple(lst)
    tupl=tup+lst
    return tupl
tup=(10,20,30,40,50)
lst=[60,70,80,90,100]
i=ext(tup,lst)
print i
