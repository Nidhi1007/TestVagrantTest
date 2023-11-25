def gst(product, unit_price, gst, quantity):
    if (unit_price>500):
        gst_amount=(gst*unit_price)/100
        total_gst=(gst_amount)*(quantity)
        discount = (unit_price*quantity)*(0.05)
        total_price = unit_price * quantity
        net_amount= total_price-discount
    else:
        gst_amount=(gst*unit_price)/100
        total_gst=(gst_amount)*(quantity)
        net_amount = unit_price * quantity
    return product, net_amount, total_gst


product_name=["leather wallet","umbrella","cigarette","honey"]
price=[1100,900,200,100]
gst_price=[18,12,28,0]
number=[1,4,3,2]

l=[]
for i in range(4):
    l.append(gst(product_name[i], price[i], gst_price[i], number[i]))



for i in range(4):
    max=0
    if (l[i][2])>max:
        p=l[i][0]
        max=l[i][2]

print("maximum gst is paid for product")
print(p)

total=0
for i in range(4):
    total=total+l[i][1]

print("total amount to be paid to shopkeeper is")
print(total)
        



        
        
