global _start

section .text
_start:
    mov rdi, 0
    mov rax, 60
    syscall

; EOF