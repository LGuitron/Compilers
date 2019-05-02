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

factorial:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
lw $t0 8($sp)
li $t1 0
seq $a0 $t0 $t1
sw $a0 0($sp)
beq $a0 $zero false0
li $a0 1
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 12
lw $fp 0($sp)
jr $ra
addiu $sp $sp 0
j endif0
false0:
lw $a0 8($sp)
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 12
lw $fp 0($sp)
jr $ra
addiu $sp $sp 0
endif0:
li $a0 0
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 12
lw $fp 0($sp)
jr $ra
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 12
lw $fp 0($sp)
jr $ra

main:

sw $fp 0($sp)
addiu $sp $sp -4
li $a0 7
sw $a0 0($sp)
addiu $sp $sp -4
jal factorial
li $v0 1
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
