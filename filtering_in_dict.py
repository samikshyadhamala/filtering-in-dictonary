                   #dictonary
empty=dict()
empty.update({"name":"samikshya"})
empty["age"]=17
empty["name_c"]=1
# print((empty["age"]))
empty["age"]=empty["age"]+2  #we can also add value  
empty["name_c"]=empty["name_c"]+1  #similarly we can count no
print(empty)
print("subject" in empty)  #to check whether the key is there or not
           #we have a list of names and empty dict now we have to do is filter how mangy names and put it in dict
name_count=dict()#empty dict
names=["ram","sita","hari","ram","hari","ram"]
for r_n in names:
    name_count[r_n]=name_count.get(r_n,0)+1 #or 1 line 
    # if r_n not in name_count:
    #     name_count[r_n]=1
    # else:
    #     name_count[r_n]=name_count[r_n]+1
print(name_count)
    
