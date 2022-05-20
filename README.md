# OS-MAKER
OS maker: an automated python script which can help you make an os in minutes!

# DESCRIPTION:

Making an OS in assembly may be hard, but with these automated python script(s), you can make an OS with ease!

# How to use:
To use this tool, you must run: script.py
to do the first thing: write whatever message you want to the screen.

After that, you can follow with: colors.py .
colors.py is _well, changing the color of the screen!_ Currently, there are only two options, but there will be more later on!

-------
# Warnings:
There is a well known bug which will write another color on top of a color without overwriting it. To fix this, you must go into: **src.asm** manually and remove the second: **;------AUTO GENERATED ON [today's date]-----** or third, or so on. along with that, remove the code under that until you see the start of the print code: "mov ah, 0x0e" Here is an example:

**src.asm:**

--------
```
; --------------FILE AUTO GENERATED ON: 2022-05-19-----------
MOV AH, 06h    ; Scroll up function
XOR AL, AL     ; Clear entire screen
XOR CX, CX     ; Upper left corner CH=row, CL=column
MOV DX, 184FH  ; lower right corner DH=row, DL=column 
MOV BH, 1Eh    ; YellowOnBlue
INT 10H

; --------------FILE AUTO GENERATED ON: 2022-05-19-----------
MOV AH, 06h    ; Scroll up function
XOR AL, AL     ; Clear entire screen
XOR CX, CX     ; Upper left corner CH=row, CL=column
MOV DX, 184FH  ; lower right corner DH=row, DL=column 
MOV BH, 28h    ; YellowOnBlue
INT 10H
mov ah, 0x0e ; tty mode 
mov al, 'W' 
int 0x10 
mov al, 'e' 
 int 0x10 
mov al, 'l' 
 int 0x10 
mov al, 'c' 
 int 0x10 
mov al, 'o' 
 int 0x10 
mov al, 'm' 
 int 0x10 
mov al, 'e' 
 int 0x10 
mov al, ' ' 
 int 0x10 
mov al, 't' 
 int 0x10 
mov al, 'o' 
 int 0x10 
mov al, ' ' 
 int 0x10 
mov al, 'B' 
 int 0x10 
mov al, 'a' 
 int 0x10 
mov al, 'r' 
 int 0x10 
mov al, 'r' 
 int 0x10 
mov al, 'e' 
 int 0x10 
mov al, 'l' 
 int 0x10 
mov al, ' ' 
 int 0x10 
mov al, 'O' 
 int 0x10 
mov al, 'S' 
 int 0x10

jmp $ ; jump to current address = infinite loop

; padding and magic number
times 510 - ($-$$) db 0
dw 0xaa55 
```



As you can see, there are TWO: "; --------------FILE AUTO GENERATED ON: [Date]-----------"
You must remove:

``` ; --------------FILE AUTO GENERATED ON: 2022-05-19-----------
MOV AH, 06h    ; Scroll up function
XOR AL, AL     ; Clear entire screen
XOR CX, CX     ; Upper left corner CH=row, CL=column
MOV DX, 184FH  ; lower right corner DH=row, DL=column 
MOV BH, 1Eh    ; YellowOnBlue
INT 10H
```


if you want gray/green, but remove:

``` ; --------------FILE AUTO GENERATED ON: 2022-05-19-----------
MOV AH, 06h    ; Scroll up function
XOR AL, AL     ; Clear entire screen
XOR CX, CX     ; Upper left corner CH=row, CL=column
MOV DX, 184FH  ; lower right corner DH=row, DL=column 
MOV BH, 28h    ; YellowOnBlue
INT 10H
```


if you want yellow/blue.

(Sometimes, there may NOT be: "; --------------FILE AUTO GENERATED ON: [Date]-----------", but don't worry! Just delete the code which would be under that if "; --------------FILE AUTO GENERATED ON: [Date]-----------" was there, as **";"** is just a comment in assembly.)


**if you still didn't understand, there will be two demos of the program soon!!!**



# Compilation:
To compile and run: src.asm, you would need to figure out a way to get it on real hardware, BUT, you can run the file in a "virtual machine". A virtual machine in a nutshell is fake hardware running on an OS which runs on real hardware. To compile, just use this command for installing the compiler:


`sudo apt install nasm    # for debian/debian-based distros`

`sudo pacman -S nasm      # for arch/arch-based distros`


to run on the virtual machine, you must first install it with:

`sudo apt install qemu-system-x86_64    # for debian/debian based distros`

`sudo pacman -S qemu-system-x86_64      # for arch/arch-based distros`



to compile, you must use:

`nasm -f bin src.asm -o src.bin`



to run on the virtual machine, you must use:


`qemu-system-x86_64 src.bin`


if you followed the instructions here, you should see something like this:
![image](https://user-images.githubusercontent.com/100057184/169425676-f9ac7109-3360-420f-b08b-78ed760ad7a7.png)


_of course, your result will vary depending on how you used the automated script..._






I hope this _README.md_ helped!








Bye, Bye!
