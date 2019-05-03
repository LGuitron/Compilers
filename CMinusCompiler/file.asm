.data
newline0: .align 4 
.asciiz "\n" 
negindex0: .align 4 
.asciiz "Error de runtime: No se permiten indices negativos" 
outbounds0: .align 4 
.asciiz "Error de runtime: Indice fuera de rango" 
input0: .align 4 
.asciiz "Intoduce un entero: " 
.text
.globl main

j main

gcd:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
lw $t0 8($sp)
li $t1 0
seq $a0 $t0 $t1
sw $a0 0($sp)
beq $a0 $zero false0
lw $a0 12($sp)
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra
j endif0
false0:
sw $fp 0($sp)
addiu $sp $sp -4
lw $a0 12($sp)
sw $a0 0($sp)
addiu $sp $sp -4
lw $t0 20($sp)
lw $t1 16($sp)
div $a0 $t0 $t1
sw $a0 -12($sp)
lw $t0 -12($sp)
lw $t1 16($sp)
mul $a0 $t0 $t1
sw $a0 -8($sp)
lw $t0 20($sp)
lw $t1 -8($sp)
sub $a0 $t0 $t1
sw $a0 0($sp)
sw $a0 0($sp)
addiu $sp $sp -4
jal gcd
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra
endif0:
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra

main:

li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $v0 4
la $a0 input0
syscall
li $v0 5
syscall
move $a0 $v0
move $t0 $a0
sw $t0 8($sp)
li $v0 4
la $a0 input0
syscall
li $v0 5
syscall
move $a0 $v0
move $t0 $a0
sw $t0 4($sp)
sw $fp 0($sp)
addiu $sp $sp -4
lw $a0 12($sp)
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 12($sp)
sw $a0 0($sp)
addiu $sp $sp -4
jal gcd
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
