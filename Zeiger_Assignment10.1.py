
import os

def main():
    directory = input("Please, Enter the name of the directory where you want to save the file : ") 
    file = input("Please, create a filename : ")
    name = input("Please, enter your name : ") 
    address = input("Please, enter your address : ")
    phone = input("Please, enter your phone number : ") 
    
 
    if os.path.isdir(directory):#checkdirectory

        writeFile = open(os.path.join(directory,file),'w') #opendirectory 
        writeFile.write(name+','+address+','+phone+'\n') #writedata
    
        writeFile.close() #closedirectory
        print("File contents:")
#reading the file for proof of storing
        readFile = open(os.path.join(directory,file),'r')
        for line in readFile:
            print(line)
        readFile.close()
    else:
        print("Sorry, this Directory does not exist...")

main()