def get_time():
    import datetime
    return datetime.datetime.now()

def log():
    act = input("Food/ Exercise \n f for Food \t e for Exercise \n")
    act = act.lower()
    if act == "f":
        name1 = input("Your name?")
        name1 = name1.lower()
        act == act + name1
        with open (f"{act}_{name1}.txt","a") as l1:
            lst1 = []
            while True:
                food = input("What have you eaten? ")
                entry1 = f"{food} {get_time()}"
                lst1.append(entry1)
                qn = input("Add more? \n y for Yes \t n for No \n").lower()
                if qn == "y":
                    continue
                elif qn == "n":
                    break
            l1.writelines(lst1)

    elif act == "e":
        name2 = input("Your name?")
        name2 = name2.lower()
        act == act + name2
        with open (f"{act} {name2}.txt","a") as l2:
            lst2 = []
            while True:
                ex = input("Which exercise did you do? ")
                entry2 = f"{ex}{get_time()}"
                lst2.append(entry2)
                qn = input("Add more? \n y for Yes \t n for No \n").lower()
                if qn == "y":
                    continue
                elif qn == "n":
                    break
            l2.writelines(lst2)
    else:
        pass      


def retrieve():
    act = input("Food/ Exercise \n f for Food \t e for Exercise \n")
    act = act.lower()
    if act == "f":
        name1 = input("Your name?")
        name1 = name1.lower()
        act == act + name1
        with open (f"{act}_{name1}.txt","a+") as r1:
            rf1 = r1.readlines()
            if rf1 == []:
                print("You haven't logged in anything yet!")
            else:
                print("\n", rf1)

    elif act == "e":
        name2 = input("Your name?")
        name2 = name2.lower()
        act == act + name2
        with open (f"{act} {name2}.txt","a+") as r2:
            re2 = r2.readlines()
            if re2 == []:
                print("You haven't logged in yet!")
            else:
                print("\n", re2)
    else:
        pass

process = input("\t \t Welcome to Health Management System \t \t \n Log/Retrieve \n l for Log \t r for Retrieve")
process = process.lower()
if process == "l":
    log()
elif process == "r":
    retrieve()
else:
    pass