
class Word:
	def __init__(self,wordlist):
		self.wordlist=wordlist
		self.length=len(wordlist)
		self.newlist=[]
		print(self.length)
	def gen(self,t1,t2):
		t3=[]
		for i in t2:
			for j in t1:
				t3.append(i+j)
		return t3
	def generate(self):
		wordlist2=self.wordlist
		file=open("wordist.txt","w")
		templist=[]
		for item in self.wordlist:
			self.newlist.append(item)
			file.write(str(item)+"\n")
		for item in self.wordlist:
			for item2 in self.wordlist:
				templist.append(item+item2)
				self.newlist.append(item+item2)
				file.write(str(item+item2)+"\n")
		for i in range(self.length-2):
			t4=self.gen(self.wordlist,templist)
			for i in t4:
				self.newlist.append(i)
				file.write(str(i)+"\n")
			templist=t4
		print("Word Generated")
		print(self.newlist)
		print(len(self.newlist))

		
		
def main():
	input_string = input("Enter words separated by comma : ")
	word_list  = input_string.split(",")
	word=Word(word_list)
	word.generate()

if __name__ == '__main__':
	main()