def calculate_tour_cost(group_size):
    if group_size >= 1 and group_size <= 2:
        return 300 * group_size
    elif group_size >= 3 and group_size <= 5:
        return 250 * group_size
    elif group_size >= 6 and group_size <= 10:
        return 210 * group_size
    elif group_size >= 11:
        return 150 * group_size

def main():
    tour_leader_name = input('โปรดใส่ชื่อหัวหน้ากรุ๊ปทัวร์: ')
    contact_number = input('โปรดป้อนเบอร์โทรศัพท์ติดต่อกลับของหัวหน้ากรุ๊ปทัวร์: ')
    group_size = int(input('โปรดป้อนจำนวนคนที่จะไปทัวร์: '))

    tour_cost = calculate_tour_cost(group_size)

    print('**------------------------------------**')
    print(f'ชื่อหัวหน้ากรุ๊ปทัวร์: {tour_leader_name}')
    print(f'เบอร์โทรศัพท์ติดต่อกลับ: {contact_number}')
    print(f'จำนวนคนที่จะไปทัวร์: {group_size} คน')
    print(f'ค่าใช้จ่ายในการซื้อแพ็กเกจท่องเที่ยว: {tour_cost} บาท')
    print('**------------------------------------**')

if __name__ == "__main__":
    main()