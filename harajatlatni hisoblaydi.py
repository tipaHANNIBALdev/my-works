expenses=[]
def add_expense():
    a=input('xarajatning nomini kiriting:\n>>>')
    b=float(input('summani kiriting:\n>>>'))
    expenses.append((a,b))
    print("harajat muaffaqiyatli qo'shildi")
def view_expenses():
    total=0
    if not expenses:
        print("sizda hozircha harajatlar yo'q ")
    else:
        print("sizning harajatlaringiz")
        for a,b in expenses:
            print(f"{a}:{b}")
            total+=b
        print(f"harajatlar summasi {total}")
while True:
    print("\nTanlang")
    print("1.harajat qo'shish")
    print("2.harajatni ko'rish")
    print("3.chiqish")


    tanlov=input("harakat raqamini tanlang:")

    if tanlov =='1':
        add_expense()
    elif tanlov =='2':
        view_expenses()
    elif tanlov =='3':
        break
    else:
        print("noto'g'ri tanlov")
