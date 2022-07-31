
import json,os
print('\033[1m','\033[91m',"WELCOME TO CRUD OPERATION",'\033[0m')
while True:
    try:
        print()
        print('\033[33m',"press 1 for create \n press 2 for read \n press 3 for update \n press 4 for delete \n press 5 for exit",'\033[0m')
        print()
        def create():
            a = input("Enter your no.number: ")
            if len(a) == 10:
                if os.path.exists("crud.json"):
                    with open("crud.json","r") as obj1:
                        if obj1.read() == "":
                            d1 ={}
                        else:
                            obj1.seek(0)
                            d1 = json.load(obj1)
                        d1[a]=({"name":input("Enter your name: "),
                                "email":input("Enter your email: "),"address":input("Enter your address: ")})
                        with open("crud.json","w") as obj1:
                            json.dump(d1,obj1,indent=4)
                            print()
                            print('\033[35m'," Your info created successfully ",'\033[0m')
                else:
                    with open('crud.json','w'):
                        create()
            else:
                print()
                print('\033[35m',"Please enter valid mo.number: ",'\033[0m')
                create()
        def read():
            mo = (input("Enter your mo.number: "))
            if len(mo) == 10:
                with open("crud.json","r") as red:
                    lo = json.load(red)
                    if mo in lo:
                        print()
                        print(lo[mo])
                    else:
                        print()
                        print('\033[1m','\033[91m',"Number does not exist: ",'\033[0m')
                        read()
            else:
                print()
                print('\033[1m','\033[91m',"Number is  invalid: ",'\033[0m')
                read()
        def update():
            v = (input('Which mo.number of data do you want to update: '))
            if len(v) == 10:
                with open("crud.json","r") as obj3:
                    data = json.load(obj3)
                    if v in data:
                        a = {"name":input("Enter your name: "),"email":input("Enter your email: "),
                             "address":input("Enter your address: ")}
                        data[v] = a
                        with open("crud.json","w") as obj4:
                            json.dump(data,obj4,indent=4)
                            print()
                            print('\033[37m',"Updated Successfully.......",'\033[0m')
                    else:
                        print()
                        print('\033[37m',"Your mo.number does not exist",'\033[0m')
                        update()
            else:
                print()
                print('\033[37m',"Please enter valid mo.number",'\033[0m')
                update()
        def delete():
            with open("crud.json","r") as data:
                d1 = json.load(data)
            m = (input("Which mo.number of data do you want to delete: "))
            if len(m) == 10:
                if m in d1:
                    d1.pop(m)
                    with open("crud.json","w") as obj5:
                        json.dump(d1,obj5,indent=4)
                        print()
                        print('\033[36m',"Successfully Deleted",'\033[0m')
                else:
                    print()
                    print('\033[36m',"Number does not exist: ",'\033[0m')
                    delete()
            else:
                print()
                print('\033[36m',"Please enter valid mo.number",'\033[0m')
                delete()
        choice = int(input("Enter your choice: "))
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
        print('\033[37m',"Your mobail number does not exist",'\033[0m')
