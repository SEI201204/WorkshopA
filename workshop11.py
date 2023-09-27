def calculate_phone_cost(minutes):
    if minutes <= 15:
        cost = minutes * 5
    elif minutes <= 30:
        cost = 15 * 5 + (minutes - 15) * 3
    else:
        cost = 15 * 5 + 15 * 3 + (minutes - 30) * 1.50
    return cost

def inputData():
    name = input('โปรดใส่ชื่อผู้ใช้โทรศัพท์ของคุณ: ')
    phone_number = input('โปรดป้อนหมายเลขโทรศัพท์ของคุณ: ')
    minutes = int(input('โปรดป้อนจำนวนนาทีที่ใช้โทร: '))

    cost = calculate_phone_cost(minutes)

    print('**------------------------------------**')
    print(f'ชื่อผู้ใช้โทรศัพท์ของคุณคือ {name}')
    print(f'หมายเลขโทรศัพท์ของคุณคือ {phone_number}')
    print(f'จำนวนนาทีที่ใช้โทร: {minutes} นาที')
    print(f'ค่าโทรสำหรับ {minutes} นาทีคือ: {cost} บาท')
    print('**------------------------------------**')

if __name__ == "__main__":
    inputData()