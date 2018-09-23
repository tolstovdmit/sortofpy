import os
from collections import defaultdict

def greet():
	print("Hi! I will sort your files.")

def currentDir():
	return os.getcwd()

def currentDirOrInputDir():
	cd = currentDir()
	print(f"You want current directory {cd} or different dir?")
	print("Ok, current directory")
	return cd

def getExtsInDir(files):
	exts = defaultdict(list)
	for filename in files:
		if not os.path.isdir(filename):
			ext = os.path.splitext(filename)[1]
			exts[ext.lower()].append(filename)
	return exts

def dirIsEmpty(directory):
	return not os.listdir(directory)

FileTypes = {
	'Archive': {
		'exts': ['.7z', '.zip', '.tar.gz', '.rar'],
		'defaultFolderName': 'Archives'
	},
	'Picture': {
		'exts': ['.jpg', '.jpeg', '.tiff', '.gif', '.png', '.ai', '.psd'],
		'defaultFolderName': 'Pictures'
	},
	'Movie': {
		'exts': ['.mp4', '.mov'],
		'defaultFolderName': 'Movies'
	},
	'Torrent': {
		'exts': ['.torrent'],
		'defaultFolderName': 'Torrents'
	},
	'Documents': {
		'exts': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.djvu', '.ppt', '.pptx'],
		'defaultFolderName': 'Docs'
	},
	'Audio': {
		'exts': ['.mp3', '.ogg', '.wav', '.opus'],
		'defaultFolderName': 'Audios'
	},
	'Documents': {
		'exts': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.djvu', '.ppt', '.pptx'],
		'defaultFolderName': 'Docs'
	},
	'Dmg': {
		'exts': ['.dmg'],
		'defaultFolderName': 'Dmgs'
	}
}


def moveFilesByClass(fileTypeParams, wdirpath, filesByExt):
	pdir = wdirpath + '/' + fileTypeParams['defaultFolderName']
	
	if not os.path.isdir(pdir):
		os.mkdir(pdir)

	if dirIsEmpty(pdir) or True:
		for ext in fileTypeParams['exts']:
			files = filesByExt[ext]
			for file in files:
				src = wdirpath + '/' + file
				dest = wdirpath + '/' + fileTypeParams['defaultFolderName'] + '/' + file 
				print(src)
				print(dest)
				os.rename(src, dest) 


def main():
	greet()
	wdirpath = currentDirOrInputDir()

	wdirfiles = os.listdir(wdirpath)
	filesByExt = getExtsInDir(wdirfiles)
	
	for ft in FileTypes:
		moveFilesByClass(FileTypes[ft], wdirpath, filesByExt)



if __name__ == '__main__':
	main()