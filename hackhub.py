Dict = {"fish taco": [0, 1, 1, 1, 2, 2, 1, 4], "chicken taco": [1, 0, 1, 1, 2, 2, 1, 4],"veg taco": [0, 0, 1, 1, 3, 3, 1, 4]}
L=["chicken", "fish", "tortilla", "salsa", "tomatoes", "onion", "guacamole", "jalapeno"]
import time
from time import sleep
import webbrowser
import csv
def Order():
    while True:
        p=0
        file=open('poggers.csv','r')
        file2=open('pogger.csv','r')
        reader=csv.reader(file)
        reader2=csv.reader(file2)
        x=[]
        for i in reader2:
            for j in i:
                x.append(int(j))
        l=[]
        print("Enter food to be ordered: ")
        inp=int(input("1-Fish Taco\n2-Chicken Taco\n3-Veg Taco\nEnter: "))
        maal=int(input("Enter amount to be ordered: "))
        for row in reader:
            if row[0].isdigit():
                if inp==1:
                    b=1
                    for j in range(len(row)):
                        a=int(row[j])-maal*Dict["fish taco"][j]
                        if a<=x[j] and a>=0:
                            print("\n")
                            print("WARNING!")
                            sleep(.5)
                            print("Your current stock of ", L[j],"is",a)
                            print("\n")
                        elif a<0:
                            print("\n")
                            print("YOU'RE OUT OF STOCK!")
                            sleep(.5)
                            print("Your current stock of ", L[j], "is", row[j])
                            print("Your required amount is ",maal*Dict["fish taco"][j])
                            print("\n\n")   
                            b+=1
                            p+=1
                        row[j]=str(a)
                    if b==1:
                        l.append(row)
                    else:
                        for j in range(len(row)):
                            a=int(row[j])+maal*Dict["fish taco"][j]
                            row[j]=str(a)
                        l.append(row)
                elif inp==2:
                    b=1
                    for j in range(len(row)):
                        a=int(row[j])-maal*Dict["chicken taco"][j]
                        if a<=x[j] and a>=0:
                            print("\n")
                            print("WARNING!")
                            sleep(.5)
                            print("Your current stock of ", L[j],"is",a)
                            print("\n")
                        elif a<0:
                            print("\n")
                            print("YOU'RE OUT OF STOCK!")
                            sleep(.5)
                            print("Your current stock of ", L[j], "is", row[j])
                            print("Your required amount is ",maal*Dict["chicken taco"][j])
                            print("\n")
                            b+=1
                            p+=1
                        row[j]=str(a)
                    if b==1:
                        l.append(row)
                    else:
                        for j in range(len(row)):
                            a=int(row[j])+maal*Dict["chicken taco"][j]
                            row[j]=str(a)
                        l.append(row)
               
                elif inp==3:
                    b=1
                    for j in range(len(row)):
                        a=int(row[j])-maal*Dict["veg taco"][j]
                        if a<=x[j] and a>=0:
                            print("\n")
                            print("WARNING!")
                            sleep(.5)
                            print("Your current stock of ", L[j],"is",a)
                            print("\n")
                        elif a<0:
                            print("\n")
                            print("YOU'RE OUT OF STOCK!")
                            sleep(.5)
                            print("Your current stock of ", L[j], "is", row[j])
                            print("Your required amount is ",maal*Dict["veg taco"][j])
                            print("\n")
                            b+=1
                            p+=1
                        row[j]=str(a)
                    if b==1:
                        l.append(row)
                    else:
                        for j in range(len(row)):
                            a=int(row[j])+maal*Dict["veg taco"][j]
                            row[j]=str(a)
                        l.append(row)            
        file.close()
        file=open('poggers.csv','w+',newline='')
        writer=csv.writer(file)
        writer.writerow(["chicken", "fish", "tortilla", "salsa", "tomatoes", "onion", "guacamole", "jalapeno"])
        writer.writerows(l)
        file.seek(0)
        rreader=csv.reader(file)
        search()
        if p==0:
            print("\nOrder Successfully Placed\n")
        oo=(input('Enter y to order more or n to exit:'))
        if oo in 'nN':
            break

    
def Add():
    while True:
        file=open('poggers.csv','r')
        reader=csv.reader(file)
        l=[]
        print("Enter new food to be added : ")
        inp=int(input("1-chicken\n2-fish\n3-tortilla\n4-salsa\n5-tomatoes\n6-onions\n7-guacamole\n8-jalapeno\nEnter:"))
        maal=int(input("Enter amount to be added : "))
        for row in reader:
            if row[0].isdigit():
                a=int(row[inp-1])+maal
                row[inp-1]=str(a)
            l.append(row)
        file.close()
        file=open('poggers.csv','w+',newline='')
        writer=csv.writer(file)
        writer.writerows(l)
        file.seek(0)
        rreader=csv.reader(file)
        search()
        print("\nAdded successfully\n")
        oo=(input('enter y to add more or n to exit: '))
        if oo in 'nN':
            break

def warning():
    with open("pogger.csv", "w", newline="") as cf:
        cw = csv.writer(cf)
        print("Enter amount at which you would like to receive the warning at-\n")
        chicken = int(input("Enter amount of chicken: "))
        fish = int(input("Enter amount of fish: "))
        tortilla = int(input("Enter amount of tortilla: "))
        salsa = int(input("Enter amount of salsa: "))
        tomatoes = int(input("Enter amount of tomatoes: "))
        onion = int(input("Enter amount of onion: "))
        guacamole = int(input("Enter amount of guacamole: "))
        jalapeno = int(input("Enter amount of jalapeno: "))
        l=[chicken, fish, tortilla, salsa, tomatoes, onion, guacamole, jalapeno]
        cw.writerow(l)
        return l

def ing():
    with open("poggers.csv", "w", newline="") as cf:
        cw = csv.writer(cf)
        cw.writerow(["Chicken", "fish", "tortilla", "salsa", "tomatoes", "onion", "guacamole", "jalapeno"])
        print("Enter details now-\n")
        chicken = int(input("Enter amount of chicken in storage: "))
        fish = int(input("Enter amount of fish in storage: "))
        tortilla = int(input("Enter amount of tortilla in storage: "))
        salsa = int(input("Enter amount of salsa in storage: "))
        tomatoes = int(input("Enter amount of tomatoes in storage: "))
        onion = int(input("Enter amount of onion in storage: "))
        guacamole = int(input("Enter amount of guacamole in storage: "))
        jalapeno = int(input("Enter amount of jalapeno in storage: "))
        l = [chicken, fish, tortilla, salsa, tomatoes, onion, guacamole, jalapeno]
        cw.writerow(l)


def search():
    with open("poggers.csv","r") as cF:
        cR=csv.reader(cF)
        view=list(cR)
        print("\n")
        print("Your current inventory:\n")
        for i in range(8):
            print(view[0][i],":",view[1][i])     
        print("\n")
            
def browser():
    while True:
        print("Enter the material you would like to order:\n")
        l = ['chicken', 'fish', 'tortilla', 'salsa', 'tomatoes', 'onion', 'guacamole', 'jalapeno']
        inp=int(input("1-chicken\n2-fish\n3-tortilla\n4-salsa\n5-tomatoes\n6-onions\n7-guacamole\n8-jalapeno\nEnter:"))
        a="https://www.bigbasket.com/ps/?q="+l[inp-1]
        webbrowser.open(a)
      
        q=input("do you wish to order more? (y/n): ")
        if q in 'nN':
                break
            
def menu():
    while True:
        print("*"*115)
        sleep(.5)               
        print('WELCOME TO POGGERS'.center(115))
        sleep(1)
        print("1. Enter Materials(first time)".center(114))
        print("2. Enter the Warning".center(114))
        print("3. Add More Materials".center(114))
        print("4. Place An Order".center(114))
        print("5. View Inventory".center(114))
        print("6. Order Materials".center(114))
        print("7. EXIT".center(114))
        sleep(.5)
        print("*"*115)
        ch=int(input())
        if ch==1:
            ing()
        elif ch==2:
            warning()
        elif ch==3:
            Add()
        elif ch==4:
            Order()
        elif ch==5:
            search()
        elif ch==6:
            browser()
        elif ch==7:
            print("thank you for pogging UwU")
            break
menu()
