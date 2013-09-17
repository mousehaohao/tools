import hashlib
import sys,os
import time
import shutil

def help():
	print "Usage: python HashIt.py [HashFolder] [Copy2Folder]"

def _getContent(hashFolder):
	if not os.path.exists(hashFolder):  
		print "%s doesn't exist!" %fromFolder
		return
 	
	files = os.listdir(hashFolder)  
	for file in files:
		filePath = os.path.join(hashFolder, file)
		fileContent = ""
		if os.path.isfile(filePath):
			fp = open(filePath, 'rb')
			try:
			     fileContent = fp.read()
			finally:
			     fp.close()
		yield filePath, fileContent

def _copy2(renamedFile, copy2Folder):
	if not os.path.exists(copy2Folder):
		os.mkdir(copy2Folder)
	shutil.copy(renamedFile, copy2Folder)

def _renameIt(filePath, MD5Path):
	if not os.path.exists(MD5Path) and os.path.exists(filePath):
		print "Now hashing %s to %s ..........." %(filePath, MD5Path)
		os.rename(filePath, MD5Path)
		return MD5Path
	return
		

def hashIt(hashFolder, copy2Folder):
	for filePath, content in _getContent(hashFolder):
		MD5Name = (hashlib.md5(content).hexdigest().lower())
		MD5Path = os.path.join(hashFolder, MD5Name)
 		#time.sleep(1)
		renamedFile = _renameIt(filePath, MD5Path)
		if None != renamedFile:
			_copy2(renamedFile, copy2Folder)

if __name__ == "__main__":
	if 3 != len(sys.argv):
		help()
		sys.exit()

	hashFolder = sys.argv[1]
	copy2Folder = sys.argv[2]
	hashIt(hashFolder, copy2Folder)
