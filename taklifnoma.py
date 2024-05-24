ismlar=[]
b=int(input('taflif qilmoqchi bolgan odamlarni sonini kiriting:'))
cc=input("qanday to'y qilmoqchisiz (nikoh) yoki (xatna):\n>>>")
vv=input("qaysi vaqtga (nahorgi) yoki (kechki):\n>>>")
tt=input("familiyangizni kiriting:\n>>>")
for a in range (b):
    ismlar.append(input(f"Taklif qilishni hohlagan {a+1}-do'stingizni ismini kiriting:\n>>>"))
for b in ismlar:
    print(f"assalomu alaykum hurmatli {b.upper()} sizni va oila azolaringizni farzandimizning {cc.upper()} to'yi munosabati bilan sizni va oila azolaringizni  {vv.upper()} yoziladigon dasturhonga lutfan taklif qilamiz hurmat bilan {tt.upper()}lar oilasi")
