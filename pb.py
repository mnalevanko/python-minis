import csv

f = open("sample-sales.csv",'rt')
reader = csv.reader(f)
shoes = set()
belts = set()
shirts = set()

for row in reader:
    customer = (row[0],row[1])
    category = row[3]
    if category == "Shoes":
        shoes.add(customer)
    if category == "Belt":
        belts.add(customer)
    if category == "Shirt":
        shirts.add(customer)

f.close()

print("%s customers have purchased shoes" % len(shoes))
print("%s customers have purchased belts" % len(belts))
print("%s customers have purchased shoes but not belts" % len(shoes - belts))
print("%s customers have purchased shoes and belts" % len(shoes & belts))
print("%s customers have purchases shoes and shirts" % len(shoes & shirts))
print("%s customers have purchased shoes, belts and shirts" % len(shoes & belts & shirts))
print("The following customers are our most valued. They have purchased shoes & belts & shirts:")

for customer in shoes & belts & shirts:
    print(customer)
