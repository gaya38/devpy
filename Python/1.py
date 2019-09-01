try: 
    x = 5*[5]
    y = x[5] 
    print("End")
except IndexError: 
    print("Index out of bound")
else: 
    print("Nothing is wrong") 
finally: 
    print("Finally we are here")
