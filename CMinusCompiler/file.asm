.data
newline0: .align 4 
.asciiz "\n" 
negindex0: .align 4 
.asciiz "Error de runtime: No se permiten indices negativos" 
outbounds0: .align 4 
.asciiz "Error de runtime: Indice fuera de rango" 
.text
.globl main

j main

main:

li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 1
move $t0 $a0
sw $t0 8($sp)
li $a0 8
move $t0 $a0
sw $t0 4($sp)
li $v0 1
lw $a0 8($sp)
syscall
li $v0 4
la $a0 newline0
syscall
lw $a0 8($sp)
sne $a0 $a0 $zero
sw $a0 0($sp)
addiu $sp $sp -4
beq $a0 $zero false0
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $v0 1
li $a0 100
syscall
li $v0 4
la $a0 newline0
syscall
j endif0
false0:
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $v0 1
li $a0 5
syscall
li $v0 4
la $a0 newline0
syscall
endif0:
lw $a0 16($sp)
addiu $sp $sp 4
beq $a0 $zero falserec0
addiu $sp $sp -12
j ifrecoverend0
falserec0:
addiu $sp $sp -12
ifrecoverend0:
li $v0 1
lw $a0 28($sp)
syscall
li $v0 4
la $a0 newline0
syscall

End:
li $v0 10
syscall
Negindexerror:
li $v0 4
la $a0 negindex0
syscall
j End
Outboundserror:
li $v0 4
la $a0 outbounds0
syscall
j End
