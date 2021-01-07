import pyfiglet
class WordGen:
	def __init__(self,wordlist):
		self.wordlist=wordlist
		self.length=len(wordlist)
		self.newlist=[]
		print(self.length," Words entered")
		print("processing...")
	def gen(self,t1,t2):
		t3=[]
		for i in t2:
			for j in t1:
				t3.append(i+j)
		return t3
	def generate(self):
		wordlist2=self.wordlist
		file=open("wordlist.txt","w")
		templist=[]
		for item in self.wordlist:
			file.write(str(item)+"\n")
		for item in self.wordlist:
			for item2 in self.wordlist:
				templist.append(item+item2)
				file.write(str(item+item2)+"\n")
		for i in range(self.length-2):
			t4=self.gen(self.wordlist,templist)
			for i in t4:
				file.write(str(i)+"\n")
			templist=t4
		print("Word Generated")
		#print(self.newlist)
		#print(len(self.newlist))
		print("Saved as wordlist.txt")
		
		
def main():
	ascii_banner = pyfiglet.figlet_format("WordGen")
	print(ascii_banner)
	input_string = input("Enter words separated by comma : ")
	word_list  = input_string.split(",")
	wordgen=WordGen(word_list)
	wordgen.generate()

if __name__ == '__main__':
	main()