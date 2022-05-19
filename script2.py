import os
from datetime import *
DATA = date.today()
print(f"If there are more than 1 '; --------------FILE AUTO GENERATED ON: {DATA}-----------' or another 'MOV AH, 06h', delete everything else after the first '; --------------FILE AUTO GENERATED ON: {DATA}-----------' until you see: 'mov ah, 0x0e'. ")
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

user = input("Would you like to INCLUDE this code with another file? ")
if user == "y" or user == "Y" or user == "Yes" or user == "yes":
	user2 = input("Enter the filename to write to: ")
	f = open(f"{user2}", "a")
	replace_line('src.asm', 0, f"""
; --------------FILE AUTO GENERATED ON: {DATA}-----------
MOV AH, 06h    ; Scroll up function
XOR AL, AL     ; Clear entire screen
XOR CX, CX     ; Upper left corner CH=row, CL=column
MOV DX, 184FH  ; lower right corner DH=row, DL=column 
MOV BH, 1Eh    ; YellowOnBlue
INT 10H
""")


	f.close()

	#open and read the file after the appending:
	f = open(f"{user2}", "r")
	print(f.read()) 
	user3 = input("Is that correct? ")
	if user3 == "Yes":
		quit()
	else:

		os.system("python3 script2.py")
elif user == "rep":
	replace_line('src.asm', 3, f"; --------------FILE AUTO GENERATED ON: {DATA}-----------")
	replace_line('src.asm', 4, f"MOV AH, 06h    ; Scroll up function")
	replace_line('src.asm', 5, f"XOR AL, AL ; clear screen")
	replace_line('src.asm', 6, f"MOV AH, 06h    ; Scroll up function")
	replace_line('src.asm', 7, f"XOR CX, CX     ; Upper left corner CH=row, CL=column")
	replace_line('src.asm', 8, f"MOV DX, 184FH")
	replace_line('src.asm', 9, f"MOV BH, 1Eh")
	replace_line('src.asm', 10, f"INT 10H")


else:
#cut
        user4 = input("Enter the filename to write to: ")
        f = open(f"{user4}", "w")
        f.write("""

; --------------FILE AUTO GENERATED ON: {DATA}-----------
MOV AH, 06h    ; Scroll up function
XOR AL, AL     ; Clear entire screen
XOR CX, CX     ; Upper left corner CH=row, CL=column
MOV DX, 184FH  ; lower right corner DH=row, DL=column 
MOV BH, 1Eh    ; YellowOnBlue
INT 10H

jmp $ ; jump to current address = infinite loop

; padding and magic number
times 510 - ($-$$) db 0
dw 0xaa55 

""")
        f.close()

        #open and read the file after the appending:
        f = open(f"{user4}", "r")
        print(f.read()) 
        user5 = input("Is that correct? ")
        if user5 == "Yes":
                quit()
        else:
                os.system("python3 script2.py")
# cut
