from zipfile import ZipFie

# specifying the zip file name

file_name=".zip"

# opening th zip file in READ mode
with  ZipFile(file_name,'r') as zip:
	zip.printdir()
	#extracting all the files
	print('Extracting all the files now...')
	zip.extractall()
	print("Done!")