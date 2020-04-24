# cities=["delhi","Kolkata","london","Bnagalore"]
#
# with open("D:\pythonWrite","w") as city_files:
#     for city in cities:
#         print(city,file=city_files)

# cities=[]
# with open("D:\QaClickGit\MobileAutomationAppium\Reports\htmlreport.html",'r') as city_files:
#     for city in city_files:
#         cities.append(city.strip('\n'))
# print(cities)
# for city in cities:
#     print(city)


# with open("binary","bw") as bin_file:
#     for i in range(17):
#         bin_file.write(bytes(range(17)))
#
#
# with open("binary","br") as binfile:
#     for b in binfile:
#         print(b)


a = 65534
b = 65535
c = 665336
x = 2998302

with open("binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))
