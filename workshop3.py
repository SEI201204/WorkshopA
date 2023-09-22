# คำนวณภาษี ณ ที่ จ่ายของสินค้า โดยรับชื่อสินค้า และราคาสินค้า ทางแป้นพิมพ์
# แสดงผลภาษีที่ คำนวณได้ทางหน้าจอ ทั้งนี้ภาษีคิดที ร้อยละ 7 ของราคาสินค้า

def showProgramName() :
    print('โปรแกรมคำนวณหาสินค้ารวมภาษี')

def inputData( ) :
    product_name = input('ป้อนชื่อสินค้า : ')
    product_cost = int(input('ป้อนราคาสินค้า : '))
    return product_name, product_cost

def calVat(product_cost ) :
    vat = product_cost*(7/100)
    return vat

def calProductSale( product_cost, vat) :
    product_sale = product_cost + vat
    return product_sale

def showProductSale( product_name, product_cost, vat, product_sale ) :
    print(f'ชื่อสินค้า {product_name}')
    print(f'ราคาสินค้า (ต้นทุน) {product_cost:.2f} บาท')
    print(f'ภาษีมูลค่าเพิ่ม {vat:.2f} บาท')
    print(f'ราคาสินค้า {product_sale:.2f} บาท')
   
print('----------------------------------------------------------------')
showProgramName()
product_name, product_cost = inputData( )
print('----------------------------------------------------------------')
vat = calVat(product_cost )
product_sale = calProductSale( product_cost, vat)
showProductSale(product_name,product_cost,vat,product_sale )
print('----------------------------------------------------------------')