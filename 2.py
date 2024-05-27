def new_member():
    name = input("enter your name :")
    age = input("age :")
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            ages = self.age
        def myfunc(self):
            #print("name : " + self.name + " , age :" +self.age)
            names = open("names.txt","a")
            names.write("name :"+self.name + " , age : "+self.age +"\n")
            names.close()
    p1 = Person(name,age)
    p1.myfunc()
    srch = input("what name do you want to search fot ? :")
    word = srch
    with open(r"names.txt", 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        for line in lines:
            # check if string present on a current line
            if line.find(word) != -1:
                print(word, 'string exists in file')
                print('Line Number:', lines.index(line))
                print('Line:', line)
            else:
                print('string does not exist in a file') 
    

def mon(age):
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
w = input("choose :")    
if w =="1":
   mon(age)
elif w == "2":
   new_member()   


