def main_func():
    choose = input("what do you want to do :"+"\n"+"1 . add a new member "+"\n"+"2 . add money "+"\n"+"3 . change the name"+"\n"+"4 . search for a name"+"\n"+"5 . nothing"+"\n"+"please choose a number : " )

        #add new 
    if choose =="1":    
        name = input("enter your name :")
        money = input("money  :")
    def new_member():
        name = input("enter the name :")
        
        class Person:
                
                def __init__(self, name, money):
                    self.name = name
                    self.money = money
                if choose == "1":        
                    def myfunc(self):
                            #print("name : " + self.name + " , age :" +self.age)
                        names = open("names.txt","a")
                        names.write("name :"+self.name + " , money : "+self.money + "K"+"\n")
                        names.close()
        money = mon()
        p1 = Person(name,money)
        p1.myfunc()
        return name , money
        #choose = input("what do you want to do :"+"\n"+"1 . add a new member "+"\n"+"2 . add money "+"\n"+"3 . change the name"+"\n"+"4 . search for a name"+"\n"+"5 . nothing"+"\n"+"please choose a number : " )
                
        
    #search
    def search():
        srch = input("what name do you want to search for ? :")
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
        if choose == "2":
            mon()
        return word ,mon()
                   
        


    #add money
    

    def mon():
        name , money = new_member()
        
        replace_age = input("how much do you want to add ? :") 

        changed_age = int(money) + int(replace_age)

        search_text = money
        with open(r'names.txt', 'r') as file:
                
            
                data = file.read()
                
                
                data = data.replace(str(search_text), str(changed_age))
                
        with open(r'names.txt', 'w') as file:
            
            file.write(data)
            print("mission done sucssesfuly without errors !")
        return money    

    #change the name
    def namess():
        name , money = new_member()
        replace_text = input("what is the new name ? :") 

        changed_name =  replace_text

        search_text = name
        with open(r'names.txt', 'r') as file:
            
        
            data = file.read()
            
            
            data = data.replace(str(search_text), str(changed_name))
            
        with open(r'names.txt', 'w') as file:
        
            file.write(data)
        print("mission done sucssesfuly without errors !")


    #delete name
    if choose =="1":
        new_member()

    elif choose == "2" :
        search()
        
        
        print("Done !")
    elif choose == "3" :
        search()
        namess()   
        print("Done !")
    elif choose =="4":
        search()
        print("Done !")
    elif choose == "5":
        print("Done !")         
main_func()