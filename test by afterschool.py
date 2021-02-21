from simpled import *

database = esential(unhide = False, dbname="db.txt")
database.add("bagas","nama","bagas")
database.add("bagas","email","stgbgs@gmail.com")
database.add("jonathan","nama","jonathan")
database.add("jonathan","email","stgbgs@gmail.com")

# w = database.deleteByS("bagas")
# database.show()


# database.deleteByL("bagas")
# database.show()

x = database.takeAll()
print(x)

# database.deleteAll()
# x = database.takeByL("Bagas")
# print(x)
# x = database.takeByL("bagas")
# print(x)


# x = database.takeByL("bagas")
# print(x)


# x = []
# y = []
# y1 = []
# y1.append("Bagas")
# y1.append("Minum")
# y2 = []
# y2.append("Jonathan")
# y2.append("Minum")
# y.append(y1)
# y.append(y2)
# x.append(y)
# z = []
# z.append("Sitanggang")
# z.append("Minum")
# x.append(z)

# print(x)
# print(x[0][1][0])

