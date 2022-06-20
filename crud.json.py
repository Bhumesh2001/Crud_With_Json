
import json
print('\033[35m',"WELCOME TO CRUD OPERATION",'\033[0m')
while True:
    try:
        print()
        print('\033[33m',"press 1 for create \n press 2 for read \n press 3 for update \n press 4 for delete \n press 5 for exit",'\033[0m')
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
                        print('\033[36m'," your info created successfully ",'\033[0m')
            else:
                print()
                print('\033[31m',"please enter valid mo.number: ",'\033[0m')
                create()
        def read():
            mo = (input("enter your mo.number: "))
            if len(mo) == 10:
                with open("crud.json","r") as red:
                    lo = json.load(red)
                    if mo in lo:
                        print()
                        print(lo[mo])
                    else:
                        print()
                        print('\033[34m',"number does not exist: ",'\033[0m')
                        read()
            else:
                print()
                print('\033[38m',"number is not valid: : ")
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
                            print('\033[32m',"updated successfully.......",'\033[0m')
                    else:
                        print()
                        print('\033[35m',"your mo.number does not exist",'\033[0m')
                        update()
            else:
                print()
                print('\033[33m',"please enter valid mo.number",'\033[0m')
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
                        print('\033[31m',"successfully deleted",'\033[0m')
                else:
                    print()
                    print('\033[34m',"Number does not exist: ",'\033[0m')
                    delete()
            else:
                print()
                print('\033[37m',"please enter valid mo.number",'\033[0m')
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
        print('\033[37m',"your mobail number does not exist",'\033[0m')
