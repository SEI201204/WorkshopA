#2. จงเขียนโปรแกรมPython ของโปรแกรมคำนวณหาค่าเฉลี่ยของคะแนนจากการสอบ 3 ครั้ง
#   โดยรับค่า รหัสนักเรียน ชื่อนักเรียน และคะแนนสอบแต่ละครั้งรวม 3 ครั้งทางแป้นพิมพ์ 
#   แล้วแสดงผลค่าเฉลี่ยที่คำนวณได้ทางหน้าจอ

def showProgramName() :
    print('*--โปรแกรมคำนวณค่าเฉลี่ยของคะแนนจากการสอบ 3 ครั้ง--*')

def inputData( ) :
    std_id = input('ป้อนรหัสนักศึกษา : ')
    std_name = input('ป้อนชื่อนักศึกษา : ')
    return std_id, std_name

def inputnumber() :
    num1 = int(input('คะแนนสอบครั้งที่ 1 : '))
    num2 = int(input('คะแนนสอบครั้งที่ 2 : '))
    num3 = int(input('คะแนนสอบครั้งที่ 3 : '))
    return num1, num2, num3

def Sumofnumber(num1, num2, num3) :
    Sumofnumber = (num1+ num2+ num3)
    return Sumofnumber

def Averageofnumber(num1, num2, num3):
    Averageofnumber = ((num1+ num2+ num3)/3)
    return Averageofnumber

def show(num1, num2, num3, Sumofnumber, Averageofnumber) :
    print(f'ผลรวมของคะแนนสอบทั้ง 3 ครั้ง : {Sumofnumber:.4f} ')
    print(f'ค่าเฉลี่ยของคะแนนสอบทั้ง 3 ครั้ง : {Averageofnumber:.4f} ')


print('---------------------------------------------------')
showProgramName() 
print('---------------------------------------------------')
std_id, std_name = inputData( )
print('---------------------------------------------------')
num1, num2, num3 = inputnumber( )
print('---------------------------------------------------')
Sumofnumber = Sumofnumber(num1, num2, num3)

Averageofnumber = Averageofnumber(num1, num2, num3)

show(num1, num2, num3,Sumofnumber,Averageofnumber)
print('---------------------------------------------------')