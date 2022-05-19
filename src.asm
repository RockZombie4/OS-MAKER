
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

