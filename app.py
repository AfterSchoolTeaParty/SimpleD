from simpled import *
import os
lists = ["=======================================",
"This is a simple console for SimpleD Database CRUD",
"LIST OF COMMAND", 
"- exit : to exit the app", 
"- help : to get the information",
"- cls : to clear the screen",
"- status : to show your status",
"- create : to create database e.g: 'create db' db is the database name\n WARN: BECAREFUL CREATING AN EXIST DB WILL REWRITE THE OLD ONE",
"- open : to open an exist database e.g: 'open db' where db is the databasename"
"- show : to show your database",
"- add l-i-v : 'l' is your listname,\n 'i' is the identifier of the value,\n 'v' is the value",
"- delete -a : to delete all data in your database",
"- delete -l : to delete data based on the list ",
"- delete -s : to delete data based on name or list",
"- delete -b : to delete the last inputed line of data"
"======================================="]
print("If this your first time of using.\n Try to use 'help' and open the example database")
Play = True
while Play:
	try:
		inputed = input(">>>")
		
		# NON DATABASE INPUT
		if inputed == "exit" :
			Play = False
		elif inputed =="help":
			for i in range(0, len(lists)):
				print(lists[i])
		elif inputed  == "cls":
			os.system("cls")
		elif inputed == "status":
			try: 
				print("current database :",database.dbname)
				countLine = len(database.takeAll())
				print("Lines : ", countLine)
			except:
				print("You are not in a database. Try to enter or create a new one :)")

		# DATABASE THING INPUT
		elif 'open' in inputed:
			command = inputed.replace('open ', '')
			try:
				file = open(command+'.txt', "r")
				file.close()
				choice = input("File is exist do you want to load the file? [y|n]:")
				Choosing = True
				while Choosing:
					if choice == 'y':
						currentDB = esential(unhide=False, dbname=command+'.txt')
						database = currentDB
						break
					elif choice == 'n':
						Choosing = False
						continue
					else:
						continue
			except:
				print("The file is not exist, try to create a new one :)")
		elif "create" in inputed:
			command = inputed.replace("create ","")
			print("Database '"+command+"' has been created")
			database = esential(unhide = False, dbname=command+".txt")
		elif "add" in inputed:
			command = inputed.replace("add ", "")
			command = command.split("-")
			database.add(command[0], command[1], command[2])
		elif "show" in inputed:
			database.show()
		elif "delete -a" in inputed:
			database.deleteAll()
		elif "delete -l:" in inputed:
			command = inputed.replace("delete -l:", "")
			database.deleteByL(command)
		elif "delete -s:" in inputed:
			command = inputed.replace("delete -s:", "")
			database.deleteByS(command)
		elif "delete -b" in inputed:
			datax = database.takeAll()
			count = len(datax)-1
			datax = datax[count]
			delete = "["+datax[0]+"]"+datax[1][0]+":"+datax[1][1]
			database.deleteByS(delete)
			print(delete, "is deleted")
		else:
			print("Your input is UNKNOWN do 'help' for more information")
	except:
		print("ERROR")