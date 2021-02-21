class esential():
	# CREATE
	def __init__(self, dbname, unhide = True):
		self.dbname = dbname
		try:
			file = open(self.dbname, "r")
			file.close()
		except:
			file = open(self.dbname, "w")
			file.close()
		if unhide:
			print("THE PATTERN OF THE DATABASE IS [LISTNAME]identifier:value\nadd False in second argument or 'dbname = ... ,unhide = False' when initializing database object\nto hide this writing")
		# self.id = 0,

	def add(self, lists, name, value):
		file = open(self.dbname, "a")
		# ids = str(self.id)		
		file.write("["+lists+"]"+name+":"+value+"\n")
		# self.id+=1
		file.close()

	# READ
	def takeByL(self, lists):
		listed = "["+lists+"]"
		file = open(self.dbname, "r")
		text = file.readlines()
		amount = len(text)
		if amount == 0:
			return []
		texts = []
		texts.append(lists)
		for i in range(0, amount):
			if listed in text[i]:
				take = text[i]
				take = take.replace(listed,"")				
				take = take.replace("\n","")
				take = take.split(":")
				texts.append(take)
		
		return texts

	def takeAll(self):
		file = open(self.dbname, "r")
		oldText = file.readlines()
		text = []
		texts = []
		for i in range(0, len(oldText)):
			edited = oldText[i]
			edited = edited.replace("\n", "")
			text.append(edited)
		for i in range(0, len(text)):
			takes = text[i]
			takes = takes.split("[",)
			takes = takes.pop(1)
			takes = takes.split("]",)
			takes[1] = takes[1].split(":")
			texts.append(takes)
		return texts

	def show(self):
		x = self.takeAll()
		for i in range(0, len(x)):
			print("["+x[i][0]+"]"+x[i][1][0]+":"+x[i][1][1])

	# DELETE
	def deleteByL(self, lists):
		listed = "["+lists+"]"
		file = open(self.dbname, "r")
		text = file.readlines()
		file.close()
		amount = len(text)
		texts = []
		for i in range(0, amount):
		 	if listed in text[i]:
		 		continue
		 	else:
		 		texts.append(text[i])
		file2 = open(self.dbname, "w")
		for i in range(0, len(texts)):
			file2.write(texts[i])
		file2.close()

	def deleteByS(self, value):
		file = open(self.dbname, "r")
		text = file.readlines()
		file.close()
		amount = len(text)
		texts = []
		for i in range(0, amount):
		 	if value in text[i]:
		 		continue
		 	else:
		 		texts.append(text[i])
		file2 = open(self.dbname, "w")
		for i in range(0, len(texts)):
			file2.write(texts[i])
		file2.close()
		
	def deleteAll(self):
		file = open(self.dbname, "w")
		file.write("")
		file.close()