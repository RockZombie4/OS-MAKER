import os

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

user = input("Would you like to use the colors of your original program as your shell, or use a different color for your shell? \n")
if user == "Use the colors of my original program":
	f = open("src.asm", "a")
	replace_line("src.asm", 49, "%include 'shell.asm'")
elif user == "Use a different color":
	val = input("What color do you want? ")
	if val == "red/blue":
		f1 = open("src.asm", "a")

		replace_line("src.asm", 0, """
;---------------user input red/blue: code here. Delete other block of code if you dont want it. LOL, more info on that roughly 144 lines README.md on github.----------------------
MOV AH, 06h    ; Scroll up function
XOR AL, AL     ; Clear entire screen
XOR CX, CX     ; Upper left corner CH=row, CL=column
MOV DX, 184FH  ; lower right corner DH=row, DL=column 
MOV BH, 14h    ; RedOnBlue
INT 10H

""")

