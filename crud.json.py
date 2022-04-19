import json
d1 = {}
print("WELCOME TO CRUD OPERATION")
while True:
    try:
        print()
        print("press 1 for create\npress 2 for read\npress 3 for update\npress 4 for delete\npress 5 for exit")
        print()
        def create():
            a = input("enter your mo.number: ")
            if len(a) == 10:
                with open("crud.json","w") as obj1:
                    d1[a]=({"name":input("enter your name: "),
                    "email":input("enter your email: "),"address":input("enter your address: ")})
                    json.dump(d1,obj1,indent=6)
                    print()
                    print("your info created successfully")
            else:
                print()
                print("please enter valid mo.number: ")
        def read():
            mo = (input("enter your mo.number: "))
            if len(mo) == 10:
                if mo in d1:
                    with open("crud.json","r") as obj2:
                        r  = json.load(obj2)
                        print()
                        print(r)
                else:
                    if mo in d1:
                        pass
                        print()
                    else:
                        print()
                        print("your mo.number does not exist")
                    for i in d1:
                        g = i
                        while mo != g:
                            mo = (input("enter  your mo. number1: "))
                            print()
                            if len(mo) == 10:
                                if mo in d1:
                                    with open("crud.json","r") as obj2:
                                        r  = json.load(obj2)
                                        print()
                                        print(r)
                                    print()
                                    print("operation successful....")
                                else:
                                    print("your mo.number does not exist")
                            else:
                                print("please enter valid mo.number")
            else:
                print()
                print("please enter valid mo.number")
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
                        if v in data:
                            print("your enter mo.number is wrong\nplease try again")
                            for j in data:
                                m = j
                                while v != m:
                                    v = input("which mo.number of data do you want to update: ")
                                    print()
                                    if v != m :
                                        print("your enter mo.number is wrong\nplease try again")
                                print("operation successfully....")
                                print()
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
            else:
                print()
                print("please enter valid mo.number")
        def delete():
            m = (input("which mo.number of data do you want to delete: "))
            if len(m) == 10:
                if m in d1:
                    d1.pop(m)
                    with open("crud.json","w") as obj5:
                        json.dump(d1,obj5,indent=6)
                        print()
                        print("successfully deleted")
                else:
                    if m in d1:
                        pass
                        print()
                    else:
                        print()
                        print("your entered mo.number does not exist")
                    for i in d1:
                        n = i
                        while m != n:
                            m = (input("which mo.number of data do you want to delete: "))
                            if m != n:
                                print("your enter mo.number is wrong\nplease try again")
                        print()
                        print("operation successful....")
            else:
                print()
                print("please enter valid mo.number")
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
        print("please first enter your choice")