def avg_mp_gallon(gallons, miles):
    g = 0
    m = 0
    for gallon in gallons:
        g += gallon
    for mile in miles:
        m += mile 
    avg = m/g
    print("The overall average miles/gallon was", avg)

gallons = []
miles = []
mile_p_gallon = []

while True:
    gallon = float(input("Enter the Gallons used (-1 to end): "))
    if gallon == -1:
        break
    mile = int(input("Enter the miles driven: "))   
    miles.append(mile)
    gallons.append(gallon)
    mp_gallon = mile / gallon
    mile_p_gallon.append(mp_gallon)
    print("The miles / gallon for this tank was", mp_gallon)
    # print("The overall average miles/gallon was", )

avg_mp_gallon(gallons, miles)



