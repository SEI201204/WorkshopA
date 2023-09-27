# โปรแกรมแสดงข้อความต้อนรับนักศึกษา โดยรับชั้นปีทางแป้นพิมพ์แล้วแสดงข้อความต้อนรับ ดังนี้
# กรณีป้อน 1 แสดงข้อความ "Welcome Freshman"
# กรณีป้อน 2 แสดงข้อความ "Welcome Sophomore"
# กรณีป้อน 3 แสดงข้อความ "Welcome Junior"
# กรณีป้อน 4 แสดงข้อความ "Welcome Senior"
#1.รับค่าข้อมูลนักศึกษาทางแป้นพิมพ์ 2.ตรวจสอบข้อมูล 3.แสดงผลทางหน้าจอ 4.แสดงชื่อโปรแกรมหน้าจอ

def inputData( ) :
    years = int(input('โปรดใส่ชั้นปีของคุณ (1-4): '))
    return years

def cheakYear(years) :
    if years == 1 :
        return('Welcome Freshman')
    elif years == 2 :
        return('Welcome Sophomore')
    elif years == 3 :
        return('Welcome Junior')
    elif years == 4 :
        return('Welcome Senior')
    else :
        return('ไม่รู้จักชั้นปีที่ระบุ')
    
def showCheakYear(years) :
    print(f'ชั้นปีของคุณคือ ปี{years}')
    print(cheakYear(years))
    print('**--------------------------------**')

def showProgramName( ) :
    print('**--------------------------------**')
    print('**------โปรแกรมต้อนรับนักศึกษา-------**')
    print('**--------------------------------**')

years=inputData( )
showProgramName( )
showCheakYear(years)
