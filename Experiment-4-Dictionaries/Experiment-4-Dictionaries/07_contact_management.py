contacts={}
while True:
    print("\nCONTACT MANAGEMENT SYSTEM")
    print("1.Add Contact")
    print("2.Search Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Display Contacts")
    print("6.Exit")
    choice=int(input("Enter Choice : "))

    if choice==1:
        name=input("Enter Name : ")
        phone=input("Enter Phone : ")
        contacts[name]=phone
        print("Contact Added Successfully")
    elif choice==2:
        name=input("Enter Name : ")
        if name in contacts:
            print("Phone :",contacts[name])
        else:
            print("Contact Not Found")
    elif choice==3:
        name=input("Enter Name : ")
        if name in contacts:
            phone=input("Enter New Phone : ")
            contacts[name]=phone
            print("Updated Successfully")
        else:
            print("Contact Not Found")
    elif choice==4:
        name=input("Enter Name : ")
        if name in contacts:
            del contacts[name]
            print("Deleted Successfully")
        else:
            print("Contact Not Found")
    elif choice==5:
        print("\nCONTACT LIST")
        for name,phone in contacts.items():
            print(name,"\t",phone)
    elif choice==6:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
