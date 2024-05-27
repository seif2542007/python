def new_name(name , age):
    names = open("names.txt","a")
    names.write("name :"+name+ " , money : "+age+ "K"+"\n")
    names.close()
    return name , age

name_age = new_name("seif","17")
with open(r"names.txt", 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        print(lines)
print("Done !")            




def mon():
    replace_text = input("how much do you want to add ? :") 

    changed_age = int(age) + int(replace_text)

    search_text = age
    with open(r'names.txt', 'r') as file:
        
    
        data = file.read()
        
        
        data = data.replace(str(search_text), str(changed_age))
        
    with open(r'names.txt', 'w') as file:
    
        
        file.write(data)
    
    #Printing Text replaced
    print("Text replaced")