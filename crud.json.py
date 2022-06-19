
import json
print("WELCOME TO CRUD OPERATION")
while True:
    try:
        print()
        print("press 1 for create\npress 2 for read\npress 3 for update\npress 4 for delete\npress 5 for exit")
        print()
        def create():
            a = input("enter your mo.number: ")
            if len(a) == 10:
                with open("crud.json","r") as obj1:
                    if obj1.read() == "":
                        d1 ={}
                    else:
                        obj1.seek(0)
                        d1 = json.load(obj1)
                    d1[a]=({"name":input("enter your name: "),
                            "email":input("enter your email: "),"address":input("enter your address: ")})
                    with open("crud.json","w") as obj1:
                        json.dump(d1,obj1,indent=6)
                        print()
                        print("your info created successfully")
            else:
                print()
                print("please enter valid mo.number: ")
                create()
        def read():
            mo = (input("enter your mo.number: "))
            if len(mo) == 10:
                with open("crud.json","r") as red:
                    lo = json.load(red)
                    if mo in lo:
                        print(lo[mo])
                    else:
                        print()
                        print("number does not exist: ")
                        read()
            else:
                print()
                print("number is not valid: : ")
                read()
        def update():
            v = (input('which mo.number of data do you want to update: '))
            if len(v) == 10:
                with open("crud.json","r") as obj3:
                    data = json.load(obj3)
                    if v in data:
                        a = {"name":input("enter your name: "),"email":input("enter your email: "),
                             "address":input("enter your address: ")}
                        data[v] = a
                        with open("crud.json","w") as obj4:
                            json.dump(data,obj4,indent=6)
                            print()
                            print("updated successfully.......")
                    else:
                        print()
                        print("your mo.number does not exist")
                        update()
            else:
                print()
                print("please enter valid mo.number")
                update()
        def delete():
            with open("crud.json","r") as data:
                d1 = json.load(data)
            m = (input("which mo.number of data do you want to delete: "))
            if len(m) == 10:
                if m in d1:
                    d1.pop(m)
                    with open("crud.json","w") as obj5:
                        json.dump(d1,obj5,indent=6)
                        print()
                        print("successfully deleted")
                else:
                    print()
                    print("Number does not exist: ")
                    delete()
            else:
                print()
                print("please enter valid mo.number")
                delete()
        choice = int(input("enter your choice: "))
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        else:
            break
    except:
        print()
        print("your mobail number does not exist")
