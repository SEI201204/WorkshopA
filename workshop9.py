#9. จงเขียนโปรแกรมPython ของโปรแกรมค านวณค่าคอมมิชชั นของพนักงานขาย โดยป้อนรหัสพนักงาน ชื อพนักงาน 
#และจ านวนเงินซึ งเป็นยอดขายของพนักงาน จากผู้ใช้ทางแป้นพิมพ์ และค านวณค่าคอมมิชชั น จากเงื อนไข ดังนี้
#ขายของได้ไม่เกิน 1000 บาท ค่าคอมมิชชั น เป็น0.0 บาท
#ขายของได้ตั้งแต่ 1001 –2000  บาท ค่าคอมมิชชั นคิด 1% 
#จากยอดขายขายของได้ตั้งแต่ 2001 –3000  บาท ค่าคอมมิชชั นคิด 3% 
#จากยอดขายขายของได้ตั้งแต่ 3001  บาท ขึ้นไป ค่าคอมมิชชั นคิด 5% จากยอดขาย
#1.รับข้อมูลจากพนักงานขาย 2.คำนวณค่าคอมมิชชั่น 3.แสดงผลการคำนวณทางหน้าจอ 4.แสดงชื่อโปรแกรมทางหน้าจอ

def inputData( ) :
    idWork = input('โปรดป้อนรหัสพนักงาน : ')
    name = input('โปรดป้อนชื่อของคุณ : ')
    totalSellingPrice = float(input('โปรดใส่จำนวนเงินยอดขาย : '))
    return idWork,name,totalSellingPrice

def calBonus(totalSellingPrice) :
    if totalSellingPrice <=1000:
        bonus=totalSellingPrice
    elif totalSellingPrice >1000 and totalSellingPrice <=2000 :
        bonus=totalSellingPrice+totalSellingPrice*1/100
    elif totalSellingPrice >2000 and totalSellingPrice <=3000 :
        bonus=totalSellingPrice+totalSellingPrice*3/100
    else :
        bonus=totalSellingPrice+totalSellingPrice*5/100
    return bonus

def showCalBonus( ) :
    print(f'รหัสพนักงานของคุณ {idWork}')
    print(f'ชื่อของพนักงานคือ {name}')
    print(f'ยอดขายของคุณคือ {totalSellingPrice} บาท')
    print(f'ค่าคอมมิชซันของคุณคือ {bonus}')
    print('**----------------------------------------------------**')

def showProgramName( ) :
    print('**----------------------------------------------------**')
    print('**--------------โปรแกรมคำนวณค่าคอมมิชซัน----------------**')
    print('**----------------------------------------------------**')

idWork,name,totalSellingPrice=inputData( )
bonus=calBonus(totalSellingPrice)
showProgramName( )
showCalBonus( )
