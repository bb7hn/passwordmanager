import time
import os
import os.path
import random
import colorama
from termcolor import colored
from math import sqrt
import getpass



colorama.init()

# Sifreleme Fonksiyonu
def asciisq(sifre):
	sifrelenmis=""
	for i in sifre:
		rand=random.randint(10,99)
		sifreli = ord(i)*ord(i)
		sifrelenmis=sifrelenmis+str(rand)+str(sifreli)+"++@++"
	return sifrelenmis
#Cozumleme Fonksiyonu
def asciisqd(sifreli):
	cozulmus=""
	sayyac1=0
	sayyac2=0
	for i in sifreli.split(','):
		sayyac1 = sayyac1+1
		for j in i.split('++@++'):
			sayyac2 = sayyac2+1
			cozulecek = j[2:]
			if cozulecek!='':
				cozulmus = cozulmus + chr(int(sqrt(int(cozulecek))))
				
	
	return str(cozulmus)
#dizin kontrolu
encryptfolder=str(os.path.exists('./my_files/to_encrypt'))
decryptfolder=str(os.path.exists('./my_files/to_decrypt'))
decryptedfolder=str(os.path.exists('./my_files/decrypted'))
encryptedfolder=str(os.path.exists('./my_files/encrypted'))
rootfolder=str(os.path.exists('./my_files'))

if rootfolder=="False":
	os.mkdir("my_files")
if encryptfolder=="False":
	os.mkdir("my_files/to_encrypt")
if decryptfolder=="False":
	os.mkdir("my_files/to_decrypt")
if decryptedfolder=="False":
	os.mkdir("my_files/decrypted")
if encryptedfolder=="False":
	os.mkdir("my_files/encrypted")
	
correctkey ='correctkey'
loginkey=getpass.getpass("ENTER THE LOGIN KEY\n")
if loginkey==correctkey:
	a = 1	
	while a == 1:
		print (colored("Welcome to ","green")+ colored("ANONIMA ",'red') + colored("HASH SYSTEM ",'blue')+"\n")
		print("""The List of Commands
		
		1-) Add new platform and password
		
		2-) Show your platforms and their passw
		
		3-) Search a platform
		
		4-) Enycrypt TEXT
		
		5-) Decrypt TEXT
		
		6-) Create an encrypted file
		
		7-) Read an encrypted file
		
		8-) Delete a file
		
		9-) Enycrypt file

		10-) Decrypt file
		
		c-) Clear the screen
		
		e-) Exit the program
		""")
		islem=input("Command:")
		if islem=="1":
			print('\n 1...\n')
			time.sleep(2)
			filepath='log.4N0N'
			f = open(filepath,'a+')
			kadi = asciisq(input("\n Username:"))
			sifre = asciisq(getpass.getpass("\n Pass:"))
			link = asciisq(input("\n Link or name of platform:"))
			f.write(','+kadi+","+sifre+","+link+"\n")
			f.close()
			os.system('cls' if os.name=='nt' else 'clear')
		elif islem=="2":
			os.system('cls' if os.name=='nt' else 'clear')
			print('\n 2...\n')
			time.sleep(2)
			filepath='log.4N0N'
			f = open(filepath,'r')
			b=1
			sayac = 0
			log=""
			null =''
			while b==1 :
				sayac= sayac+1
				new = f.readline()
				log = log + new
				if new==null:
					b=0
			f.close()
			sayac2=0
			sayac3=0
			if log[0]==',':
				log = log[1:]
			for i in log:	
				if sayac2 == ((sayac-1)*3):
					break
				if sayac3==0:
					print(colored("-",'green')*20)
					
					print(colored("USER:",'blue')+ asciisqd((log.split(",")[sayac2])))
					
				elif sayac3==1:
					print(colored("PASS:",'red')+ asciisqd((log.split(",")[sayac2])))
					
				elif sayac3==2:
					print(colored("PLATFORM:",'green')+asciisqd(log.split(",")[sayac2]))
					
					print(colored("-",'green')*20)
					print(colored("-",'green')*20)
				sayac3+=1	
				if sayac3>2:
					sayac3=0
				sayac2=sayac2+1
			input("press any key to continue")
			os.system('cls' if os.name=='nt' else 'clear')
		elif islem=="3":
			userofplat=''
			passofplat=''
			plat=''
			print('\n ...3')
			time.sleep(1)
			os.system('cls' if os.name=='nt' else 'clear')
			searching_key = input("Platform Name:")
			filepath2='log.4N0N'
			f2 = open(filepath2,'r')
			c=1
			sayac = 0
			log2=""
			null2 =''
			while c==1 :
				sayac= sayac+1
				new2 = f2.readline()
				log2 = log2 + new2
				if new2==null2:
					c=0
			f2.close()
			sayac2=0
			sayac3=0
			if log2[0]==',':
				log2 = log2[1:]
			for i in log2:	
				if sayac2 == ((sayac-1)*3):
					break
				if sayac3==0:
					 userofplat=asciisqd((log2.split(",")[sayac2]))
				elif sayac3==1:
					passofplat= asciisqd((log2.split(",")[sayac2]))
				elif sayac3==2:
					plat =asciisqd(log2.split(",")[sayac2])
					if searching_key.lower() == plat.lower():
						os.system('cls' if os.name=='nt' else 'clear')
						print (colored("Platform : ",'green')+ plat)
						print (colored("User : ",'blue')+ userofplat)
						print (colored("Pass : ",'red')+ passofplat)
						break
					else:
						plat=''
						userofplat=''
						passofplat=''
				sayac3+=1	
				if sayac3>2:
					sayac3=0
				sayac2=sayac2+1
			if(userofplat==''):
				print(colored("There is no match",'red'))
				time.sleep(2)
			else:
				input("press any key to continue")
				os.system('cls' if os.name=='nt' else 'clear')
				
		elif islem=="4":
			print('\n ...4')
			sifrelenecek = input("\n Enter the Text You Want To Enycrypt\n")
			print(colored("------"*10,'green'))
			print("\n")
			print (asciisq(sifrelenecek)+"\n\n")
			print(colored("------"*10,'green'))
			print("\n")
			input("press any key to continue")
			os.system('cls' if os.name=='nt' else 'clear')
		elif islem=="5":
			print('\n ...5')
			sifrelenecek = input("\n Enter the Text You Want To Decrypt\n")
			print(colored("------"*10,'green'))
			print("\n")
			print (asciisqd(sifrelenecek)+"\n\n")
			print(colored("------"*10,'green'))
			print("\n")
			input("press any key to continue")
			os.system('cls' if os.name=='nt' else 'clear')
		elif islem=="6":
			filename = input("Filename: ")
			filepath='my_files/'+filename+'.4N0N'
			f = open(filepath,'a+')
			cc=1
			log=''
			null=''
			while cc==1 :
				new = f.readline()
				log = log + new
				if new==null:
					cc=0
			f.close()
			os.system('cls' if os.name=='nt' else 'clear')
			print(colored("You can free to write anything it will be encrypted when it is saving...",'blue')+"\n"+colored(" Press Enter To Save",'green')+"\n\n")
			print(log)
			save_TEXT = input("")
			filepath='my_files/'+filename+'.4N0N'
			f = open(filepath,'a+')
			f.write(asciisq(save_TEXT))
			f.close()
			os.system('cls' if os.name=='nt' else 'clear')
			print(filename+".4N0N"+colored(" Saved",'green'))
			time.sleep(2)
			os.system('cls' if os.name=='nt' else 'clear')
		elif islem=="7":
			os.system('cls' if os.name=='nt' else 'clear')
			print("File List:\n\n")
			dosyalar = os.listdir("./my_files/")
			sayici=0
			filenum=[]
			for dosya in dosyalar:
				
				if dosya.endswith(".4N0N"):
					sayici+=1
					print(dosya + "  --->>  "+ colored(str(sayici),'green'))
					filenum.insert(sayici,dosya)
			file_num=input("\nThe number of file which will open: ")
			filepath='my_files/'+filenum.pop(int(file_num)-1)
			f = open(filepath,'r')
			c=1
			log=''
			while c==1 :
				new = f.readline()
				log = log + new
				if new=='':
					c=0
			f.close()
			os.system('cls' if os.name=='nt' else 'clear')
			print(colored(asciisqd(log),'green'))
			while a==1:
				closeinp=input("\n Write c to close : ")
				if closeinp=="c":
					break
		elif islem=="8":
			while a==1:
				os.system('cls' if os.name=='nt' else 'clear')
				print("File List:\n write none to cancel\n")
				dosyalar = os.listdir("./my_files/")
				sayici=0
				filenum=[]
				for dosya in dosyalar:
					if dosya.endswith(".4N0N"):
						sayici+=1
						print(dosya + "  --->>  "+ colored(str(sayici),'green'))
						filenum.insert(sayici,dosya)
				
				if sayici ==0:
					os.system('cls' if os.name=='nt' else 'clear')
					print(colored("THERE IS NO FILE",'red'))
					time.sleep(2)
					os.system('cls' if os.name=='nt' else 'clear')
					break
				file_num=input("\nThe number of file which will delete: ")
				if file_num=="none":
					break
				filepath='my_files/'+filenum.pop(int(file_num)-1)
				os.remove(filepath)
				print(colored('FILE DELETED SUCCESSFULLY','green'))
				closeinp=input("\n Write c to close : ")
				if closeinp=="c":
					break
		elif islem=="9":
			print("when you start the process everyfile in my_files/to_encrypt will encrypt and delete")
			willcontinue=input("y for YES , n for NO")
			if willcontinue=="y":
				dosyalar = os.listdir("./my_files/to_encrypt")
				for dosya in dosyalar:
					filepath='my_files/to_encrypt/'
					f = open(filepath+dosya,'r')
					c=1
					log=''
					while c==1 :
						new = f.readline()
						log = log + new
						if new=='':
							break
				f.close()
				log = asciisq(log)
				filepath='my_files/encrypted/'
				f = open(filepath+dosya,'w')
				os.system('cls' if os.name=='nt' else 'clear')
				f.write(log)
				f.close()
				os.remove("my_files/to_encrypt/"+dosya)
				print(colored("Process is compeleted successfully.",'green'))
				input("Press enter to continue")
			else:
				os.system('cls' if os.name=='nt' else 'clear')
		elif islem=="10":
			print("when you start the process everyfile in my_files/to_decrypt will decrypt and delete")
			willcontinue=input("y for YES , n for NO")
			if willcontinue=="y":
				dosyalar = os.listdir("./my_files/to_decrypt")
				for dosya in dosyalar:
					filepath='my_files/to_decrypt/'
					f = open(filepath+dosya,'r')
					c=1
					log=''
					while c==1 :
						new = f.readline()
						log = log + new
						if new=='':
							break
				f.close()
				log = asciisqd(log)
				filepath='my_files/decrypted/'
				f = open(filepath+dosya,'w')
				os.system('cls' if os.name=='nt' else 'clear')
				f.write(log)
				f.close()
				os.remove("my_files/to_decrypt/"+dosya)
			else:
				os.system('cls' if os.name=='nt' else 'clear')
		elif islem=="e":
			a=0
		elif islem=="c":
			os.system('cls' if os.name=='nt' else 'clear')
		# ekranı temizleme kodu = os.system('cls' if os.name=='nt' else 'clear')
else:
	print(colored("ACCESS DENIED",'red'))
