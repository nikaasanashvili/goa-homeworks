#პრეზენტაციის თემა banki 

# შესავალი
print("Hello to GOA bank:")
print("BANK PROGRAM")

# ოპერაციის ნომრები (არჩევითია): 
print("1.deposit")
print("2.deposit to someone")
print("3.show balance")
print("4.creat credit card")
print("5.exsit")

# ოპერაციის არჩევა
operation_number=int(input("Choose the operation number you want: "))

# დეპოზიტი (1)
if operation_number==1:
    print("Hello")
    # უნდა თუ არა მომხმარებელს ოპერაციის განხორციელება: 
    operation=input("Are you sure to perform the operation? ")
    if operation=="yes":
        # დეპოზიტი
        money=int(input("How much do you want to deposit in your account?: "))
        if money>0:
            # ვალუტის არჩევა ლარი ან დოლარი
            cource=input("It's USD or GEL: ")
            # თუ ვალუტა არის დოლარი
            if cource=="USD":
                print("Now in your account you have "+str(money)+"$")
                add=input("Do you want add another $?: ")
                # ფულის დამატება დოლარში
                if add=="yes":
                    new_deposit=int(input("Enter: "))
                    print("Now you have "+str(money+new_deposit)+cource+", have a good day")
                elif add=="no":
                    print("thanks for using GOA BANK, goodbay")
                else:
                    print("ERROR")
            # თუ ვალუტა არის ლარი
            elif cource=="GEL":
                print("Now inn your account you have "+str(money)+"₾")
                add=input("Do you want add another ?: ")
                # ფულის დამატება ლარში
                if add=="yes":
                    new_deposit=int(input("Enter: "))
                    print("Now you have "+str(money+new_deposit)+cource+", have a good day. thanks for using GOA BANK")
                elif add=="no":
                    print("thanks for using GOA BANK, goodbay")
                else:
                    print("ERROR")
            else:
                print("Sorry, but you cannot deposit the amount of this course.")
        # დეპოზიტის სხვა შემთხევები
        elif money<=0:
            print("The operation cannot be performed")
        else:
            print("ERROR")
    # თუ უარი თქვა მომხმარებელმა ოპერაციის განხორციელებაზე, ან სხვა...
    elif operation=="no":
        print("thanks for using GOA BANK, goodbye")
    else:
        print("ERROR")
    # დეპოზიტი საკუთართავთან დასრულდა.

# გადარიცხვა სხვასთან არჩევის შემთხვევაში (2)
elif operation_number==2:

    # ვეკითხებით მომხმარებელს input-ის საშვალებით  სურს თუ არა სხვასთან დეპოზიტი 
    print("do you want to deposit with someone else?")
    user=input("do you? (yes or no): ")

    # yes არჩევის შემთხვევაში
    if user=="yes":
        name=input("persone name: ")
        last_name=input("persone lastname: ")
        money=int(input("How many do you want to depozit: "))
        
        # ვალუტის არჩევა და ფულის პირობები
        if money >0:
            cource=input("GEL or USD: ")
            # თუ GEL აირჩია
            if cource=="GEL":
                perm=input("Are you sure you want to transfer "+str(money)+" "+ "₾ "+"to "+name+" "+last_name+"? " )
                if perm=="yes":
                    x=int(input("enter your card code: "))
                    print("Registration completed, thanks for using GOA BANK")
                if perm=="no":
                    print("goodbye")
            # თუ USD აირჩია
            elif cource=="USD":
                perm=input("Are you sure you want to transfer "+str(money)+" "+ "$ to"+name +" " + last_name+"? "  )
                if perm=="yes":
                    x=int(input("enter your card code: "))
                    print("Registration completed, thanks for using GOA BANK")
                if perm=="no":
                    print("thanks for using GOA BANK, goodbye")
        else:
            print("ERROR")
    elif user=="no":
        print("thanks for using GOA BANK, goodbye")
    else:
        print("ERROR")

# ბალანსის ჩვენება (3)
elif operation_number==3:
    user=input("do you want to show balsans? ")
    # თუ მომხმარებელი თანახმა არის
    if user=="yes":
        balance =0
        print(f"your balance is {balance:.2f} GEL")
    # თუ არ არის მომხმარებელი თანახმა
    elif user=="no":
        print("Thanks for using GOA bank")

    
# credit card-ის შექმნა (4)
elif operation_number==4:
    #ვეკითხებით მომხმარებელს უნდა თუ არა შექმნას საკრედითო ბარათი
    print("hello welcome to GOA BANK ")
    print("You want to make credit card")
    user=input("do you?: ")
    # თუ მომხმარებელი თანახმა არის
    if user=="yes":
        #ვეკითხებით მონაცემებს
        name=input("enter your name: ")
        lastname=input("enter your lastname: ")
        # ასაკის პირობები
        print("how old are you")
        age=int(input("enter your age: "))
        if age < 18:
            print("you are not adult ")
        elif age>=18:
            print("enter your birtday")
            year=input("year: ")
            month=input("month: ")
            day=input("day: ")
            print("credit card created, thanks for using GOA BANK")
        else:
            print("ERROR")
    # თუ მომხმარებელმა გადაიფიქრა
    elif user=="no":
        print("thanks for using GOA BANK, goodbye")
    else:
        print("ERROR")

# exit (5)
elif operation_number==5:
    print("Goodbye, thanks for using GOA BANK")

# სხვა..
else:
    print("ERROR")