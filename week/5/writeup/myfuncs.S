section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        ;your code goes here!
        mov rax, 0    ; set i = 0
        jmp condition
m_loop:
        mov [rdi + rax], sil ;  str[i] = val;
        add rax, 1    ; i++
condition:
        cmp rdx, rax  ; If len > i
        jge m_loop      ; If len > i go to loop else finish


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


        mov rax, 0  ; set i = 0
        jmp str_cond
s_loop:
        mov bl, [rsi +rax]  ; Move the char to a temporary reg
        mov [rdi + rax], bl ; dst[i] = src[i]
        add rax, 1    ; i++
str_cond:
        cmp rdx, rax  ; if len > i
        jge s_loop    ; if len > i go to loop else finish


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
