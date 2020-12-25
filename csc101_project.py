list=[]
def remove_new_line_char_from_list(list):

    i=0
    ls=list
    count=0
    for i in ls:
        if i=="\n":
            count+=1

    for i in range(count):
        j=0
        while j<len(ls):
            if ls[j]=="\n":
                ls.pop(j)
            j+=1
    list=ls
    print(list)


def modify_animal_names(li):
    ls=li
    for i in range(len(ls)):
        t=ls[i]
        ls[i]=t.capitalize()
    list=ls
    print(list)

def find_replace_name(li,n):
    for i in range(len(li)):
      if (li[i]=="cow") or(li[i]=="Cow") or (li[i]=="cow\n") or (li[i]=="Cow\n"):
          li[i]=n
    print(li)

try:
    #this will throw an exception if the file doesn't exist.
    fileptr = open("info.txt","r")
except IOError:
    print("File not found")
#Read the data from the file using readlines method
list=fileptr.readlines()
#closing the file
fileptr.close()
print(list)
remove_new_line_char_from_list(list)
modify_animal_names(list)
name=str(input("Enter your name:"))
find_replace_name(list,name)



