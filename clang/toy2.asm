	.file	"toy2.c"
	.text
	.section	.rodata
.LC0:
	.string	"%d\n"
.LC1:
	.string	"%d is odd\n"
.LC2:
	.string	"It is one"
.LC3:
	.string	"It is two"
.LC4:
	.string	"It is not one nor two"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$48, %rsp
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	movl	$10, -32(%rbp)
	movl	$20, -28(%rbp)
	movl	$30, -24(%rbp)
	movl	$40, -20(%rbp)
	movl	$0, -44(%rbp)
	jmp	.L2
.L3:
	movl	-44(%rbp), %eax
	cltq
	movl	-32(%rbp,%rax,4), %eax
	movl	%eax, %esi
	leaq	.LC0(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	addl	$1, -44(%rbp)
.L2:
	cmpl	$3, -44(%rbp)
	jle	.L3
	movl	$0, -40(%rbp)
	movl	$0, -40(%rbp)
	jmp	.L4
.L7:
	movl	-40(%rbp), %eax
	andl	$1, %eax
	testl	%eax, %eax
	jne	.L15
	movl	-40(%rbp), %eax
	movl	%eax, %esi
	leaq	.LC1(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	jmp	.L6
.L15:
	nop
.L6:
	addl	$1, -40(%rbp)
.L4:
	cmpl	$19, -40(%rbp)
	jle	.L7
	movl	$10, -36(%rbp)
	cmpl	$1, -36(%rbp)
	je	.L8
	cmpl	$2, -36(%rbp)
	je	.L9
	jmp	.L14
.L8:
	leaq	.LC2(%rip), %rax
	movq	%rax, %rdi
	call	puts@PLT
	jmp	.L11
.L9:
	leaq	.LC3(%rip), %rax
	movq	%rax, %rdi
	call	puts@PLT
	jmp	.L11
.L14:
	leaq	.LC4(%rip), %rax
	movq	%rax, %rdi
	call	puts@PLT
	nop
.L11:
	movl	$0, %eax
	movq	-8(%rbp), %rdx
	subq	%fs:40, %rdx
	je	.L13
	call	__stack_chk_fail@PLT
.L13:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
