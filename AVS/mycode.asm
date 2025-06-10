.model small
.stack 100h

.data
array db 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
array_length equ ($ - array)

b db 70

.code
main proc
    mov ax, @data
    mov ds, ax

    mov cl, 0 
    mov ax, 0 
    mov dl, 0 

    mov si, 0 
    mov ch, 1 

loop_start:
    cmp ch, 1
    jne next_element
    mov al, array[si]
    cmp al, 0
    jle next_element
    add ax, al
    inc cl

next_element:
    mov ch, 1
    add si, 1
    cmp si, array_length
    jae loop_end

    mov ch, 0
    jmp loop_start

loop_end:
    mov dl, 0 ; ������� ����� ������ B
    mov si, 0 ; ������ �������
    mov bl, b ; �������� B

loop_check_b:
    mov al, array[si]
    cmp al, bl
    jl increment_counter

increment_counter:
    inc dl

    inc si
    cmp si, array_length
    jae loop_end2

    jmp loop_check_b

loop_end2:
    mov ah, 0 ; ��� ����������� �������
    div cl ; ������� ����� �� ����������
    mov cx, ax ; ������� �������������� ������������� ����� �� �������� ��������

    mov ax, cx
    mov bx, dx
    call print_result

    mov ax, dl ; ���������� ����� ������ B
    call print_result

    mov ax, 4C00h
    int 21h
main endp

print_result proc
    mov bx, 10 ; ��������� ������� ���������

    xor dx, dx ; ����� �������� dx ��� �������
    div bx ; ������� �� ��������� ������� ���������
    push dx ; ���������� ������� �� �������

    mov ah, 2 ; ����� �������
    add dl, '0' ; �������������� ����� � ������
    int 21h

    pop dx ; �������������� ������� �� �������
    cmp ax, 0 ; ��������, ���� �� ����� ��� �������� ���������
    jz end_print_result

    jmp print_result

end_print_result:
    mov dl, 10 ; ������ ����� ������
    mov ah, 2 ; ����� �������
    int 21h

    ret
print_result endp

end main