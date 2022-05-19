# Script for OS generation
from datetime import date
import os

date = date.today()


user = input("Enter what you want to do: ")
if user == "print" :
	f = open("src.asm", "w")
	f.write(f";-------------FILE AUTO-GENERATED ON: {date}--------------- \n")
	f.write("mov ah, 0x0e ; tty mode \n")
	user2 = input("Enter character 1/20: \n ")
	f.write(f"mov al, '{user2}' \n")
	f.write("int 0x10 \n")
	user3 = input("Enter character 2/20: \n ")
	f.write(f"mov al, '{user3}' \n ")
	f.write("int 0x10 \n")
	user4 = input("Enter character 3/20: \n ")
	f.write(f"mov al, '{user4}' \n ")
	f.write("int 0x10 \n")
	user5 = input("Enter character 4/20: \n ") # Change indent
	f.write(f"mov al, '{user5}' \n ") # Change indent
	f.write("int 0x10 \n")
	user5 = input("Enter character 5/20: \n ") # Change indent
	f.write(f"mov al, '{user5}' \n ") # Change indent
	f.write("int 0x10 \n")
	user6 = input("Enter character 6/20: \n ")
	f.write(f"mov al, '{user6}' \n ")
	f.write("int 0x10 \n")
	user7 = input("Enter character 7/20: \n ")
	f.write(f"mov al, '{user7}' \n ")
	f.write("int 0x10 \n")
	user8 = input("Enter character 8/20: \n ")
	f.write(f"mov al, '{user8}' \n ")
	f.write("int 0x10 \n")
	user9 = input("Enter character 9/20: \n ")
	f.write(f"mov al, '{user9}' \n ")
	f.write("int 0x10 \n")
	user10 = input("Enter character 10/20: \n ")
	f.write(f"mov al, '{user10}' \n ")
	f.write("int 0x10 \n")
	user11 = input("Enter character 11/20: \n ")
	f.write(f"mov al, '{user11}' \n ")
	f.write("int 0x10 \n")
	user12 = input("Enter character 12/20: \n ")
	f.write(f"mov al, '{user12}' \n ")
	f.write("int 0x10 \n")
	user13 = input("Enter character 13/20: \n ")
	f.write(f"mov al, '{user13}' \n ")
	f.write("int 0x10 \n")
	user14 = input("Enter character 14/20: \n ")
	f.write(f"mov al, '{user14}' \n ")
	f.write("int 0x10 \n")
	user15 = input("Enter character 15/20: \n ")
	f.write(f"mov al, '{user15}' \n ")
	f.write("int 0x10 \n")
	user16 = input("Enter character 16/20: \n ")
	f.write(f"mov al, '{user16}' \n ")
	f.write("int 0x10 \n")
	user17 = input("Enter character 17/20: \n ")
	f.write(f"mov al, '{user17}' \n ")
	f.write("int 0x10 \n")
	user18 = input("Enter character 18/20: \n ")
	f.write(f"mov al, '{user18}' \n ")
	f.write("int 0x10 \n")
	user19 = input("Enter character 19/20: \n ")
	f.write(f"mov al, '{user19}' \n ")
	f.write("int 0x10 \n")
	user20 = input("Enter character 20/20: \n ")
	f.write(f"mov al, '{user20}' \n ")
	f.write("int 0x10")
	f.write("""

jmp $ ; jump to current address = infinite loop

; padding and magic number
times 510 - ($-$$) db 0
dw 0xaa55 

""")
	f.close()

	#open and read the file after the appending:
	f = open("src.asm", "r")
	print(f.read()) 
	user22 = input("Is that correct? ")
	if user22 == "Yes":
		quit()
	else:
		os.system("python3 script.py")
