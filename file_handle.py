
import os
 
print("YOU ARE HERE FOR WHICH FILE")

a=input("File Name:- ") # excepts a file name presnt or not in your folder 

if os.path.exists(a): #check that your file exist or not 
    print("exist")
    print("WHAT WOULD YOU LIKE TO DO WITH THIS FILE:- read , write or append")

    b=input("tell your response:-")

    if b == 'read':
        try:
            with open(a,'r') as file:
                c=file.read()
                print(c)
                print("FILE READ SUCCESSFULLY")

        except Exception as err:
            print(f"there is an error as {err}")

    elif b=='write':
        try:
            with open(a,'r') as file :
                c=file.read()
                print(f"CURRENT FILE DATA:- {c}") #this show the the data present in the file before overwrite 

        except Exception as err:
            print(f"there is an error as {err}")

        data=input("enter data you want to write:-") 

        try:
            with open (a,'w') as file:
                c=file.write(data)
                print(c)
                print("FILE WRITE SUCCESSFULLY")  #this show the data in the file aftr overwite 

        except Exception as err:
            print(f"there is an error as {err}")


    elif b=='append':
        try:
            with open(a,'r') as file :
                c=file.read()
                print(f"CURRENT FILE DATA:- {c}") #this show the data in the file before appending

        except Exception as err:
            print(f"there is an error as {err}")

        data=input("enter data you want to append:-")

        try:
            with open (a,'a') as file:
                c=file.write(data)
                
                print("FILE APPEND SUCCESSFULLY")  #thi hsow the data in the file after appending 

        except Exception as err:
            print(f"there is an error as {err}")

else:
    print("not exist") #this works if your file didn't exist in your folder 
    print("WOULD YOU LIKE TO CREATE THIS FILE") #ask to create that file or not 
    d=input("tell your response Y/N:-")

    if d.upper() == 'Y':
        try:
            with open(a, 'w') as file:
                data = input("What would you like to write in the new file:-")
                file.write(data)
            print("FILE CREATED AND DATA WRITTEN SUCCESSFULLY")

        except Exception as err:
            print(f"there is an error as {err}")
    else:
        print("File not created.")
    