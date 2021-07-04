from itertools import groupby
a=[1,2,3,4]
person=[{'name':'Tim','age':'25'},{'name':'raj','age':'27'},{'name':'shreya','age':'21'},{'name':'utkarsh','age':'21'}]# we can group diff datattypes like dictionory also
# def smaller_than_3(x):
#     return x<3

# grp_obj=groupby(a,key=smaller_than_3) 
grp_obj=groupby(a,key=lambda x:x<3)#we can use lambda func also
for key,value in grp_obj:
    print(key,list(value))

grp_obj=groupby(person,key=lambda x:x['age'])#we can use lambda func also
for key,value in grp_obj:
    print(key,list(value))


