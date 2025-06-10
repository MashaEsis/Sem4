section .data
    numbers db 3, 7, 4, -2, 9, -6, 1, 5, -8, 10  ; пример входных данных
    size equ $ - numbers  ; вычисление размера массива
    B db 6  ; заданное значение B

section .text
    global _start

_start:
    xor eax, eax  ; сумма положительных чисел
    xor ebx, ebx  ; количество положительных чисел
    xor ecx, ecx  ; количество чисел, меньших B
    
    mov edi, 1  ; индекс элемента массива (нечетное место)
    
loop_start:
    cmp edi, size  ; проверка, достигли ли конца массива
    jge loop_end
    
    movsx edx, byte[numbers + edi]  ; загрузка числа в EDX (знаковое расширение)
    
    test edx, edx  ; проверка знака числа
    jle skip_negative  ; пропустить отрицательные числа
    
    add eax, edx  ; добавить положительное число к сумме
    inc ebx  ; увеличить количество положительных чисел
    
skip_negative:
    cmp edx, byte[B]  ; сравнение числа с B
    jge skip_less_than_B  ; пропустить числа, большие или равные B
    
    inc ecx  ; увеличить количество чисел, меньших B
    
skip_less_than_B:
    add edi, 2  ; увеличить индекс на 2 (следующее нечетное место)
    jmp loop_start
    
loop_end:
    cmp ebx, 0  ; проверка, были ли найдены положительные числа
    jz average_end
    
    cdq  ; знаковое расширение EAX в EDX:EAX
    idiv ebx  ; деление суммы на количество чисел
    
    ; результат находится в регистре EAX (среднее арифметическое)
    
average_end:
    ; результаты находятся в регистрах EAX и ECX
    ; можно использовать их для дальнейших операций или вывода
    
    ; остановка программы
    mov eax, 1
    xor ebx, ebx
    int 0x80