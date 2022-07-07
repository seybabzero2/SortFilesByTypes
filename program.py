import os
import shutil

def main():
    listDir = os.listdir(path=".")
    PrintDirectory(listDir)
    CreateDirectory(listDir)

def PrintDirectory(directory):
	for i in range(len(directory)):
		print("f: PRINT " + directory[i]);

def CreateDirectory(directory):
	splitDir = []
	for i in range(len(directory)):
		splitDir = directory[i].split('.')
		if not os.path.exists('.' + splitDir[len(splitDir)-1]):
			os.mkdir('.' + splitDir[len(splitDir)-1])
			print("f: TYPE " + splitDir[len(splitDir)-1])
		MoveFiles(directory, splitDir)

def MoveFiles(directory, splitDirectory):
	shutil.move(os.getcwd() + r"\\" + ".".join(splitDirectory), os.getcwd() + r"\\" + '.' + splitDirectory[len(splitDirectory)-1])

if __name__== "__main__" :
	main()