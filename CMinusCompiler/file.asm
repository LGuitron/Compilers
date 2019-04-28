.data
newline: .asciiz "\n" 
negindex: .asciiz "Error de runtime: No se permiten indices negativos" 
outbounds: .asciiz "Error de runtime: Indice fuera de rango" 
global: .word 0 
globalarr: .space 40
.text
.globl main

j main

suma:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
lw $t0 12($sp)
lw $t1 16($sp)
add $a0 $t0 $t1
sw $a0 0($sp)
addiu $sp $sp 4
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra

globalfunc:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 5
move $t0 $a0
la $a0 global
sw $t0 0($a0)
la $a0 global
lw $a0 0($a0) 
addiu $sp $sp 4
lw $ra 4($sp)
addiu $sp $sp 20
lw $fp 0($sp)
jr $ra

arrmanagement:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $a0 14
move $t0 $a0
li $a0 0
li $a1 4
mul $a0 $a0 $a1
la $a1 globalarr
add $a1 $a1 $a0
sw $t0 0($a1)
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 8
lw $fp 0($sp)
jr $ra

largeoperations:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 1
move $t0 $a0
sw $t0 32($sp)
li $a0 2
move $t0 $a0
sw $t0 28($sp)
li $a0 3
move $t0 $a0
sw $t0 24($sp)
li $a0 4
move $t0 $a0
sw $t0 20($sp)
li $a0 5
move $t0 $a0
li $a0 4
blt $a0 $zero Negindexerror
li $a2 10
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 72
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 6
move $t0 $a0
sw $t0 12($sp)
li $a0 7
move $t0 $a0
sw $t0 8($sp)
li $a0 8
move $t0 $a0
li $a0 5
blt $a0 $zero Negindexerror
li $a2 10
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 72
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
lw $t0 32($sp)
lw $t1 28($sp)
add $a0 $t0 $t1
sw $a0 -12($sp)
lw $t0 24($sp)
lw $t1 20($sp)
add $a0 $t0 $t1
sw $a0 -16($sp)
lw $t0 -12($sp)
lw $t1 -16($sp)
add $a0 $t0 $t1
sw $a0 -8($sp)
li $a0 4
blt $a0 $zero Negindexerror
li $a2 10
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 72
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $t0 0($a2)
lw $t1 12($sp)
add $a0 $t0 $t1
sw $a0 -16($sp)
li $a0 5
blt $a0 $zero Negindexerror
li $a2 10
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 72
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $t0 8($sp)
lw $t1 0($a2)
add $a0 $t0 $t1
sw $a0 -20($sp)
lw $t0 -16($sp)
lw $t1 -20($sp)
add $a0 $t0 $t1
sw $a0 -12($sp)
lw $t0 -8($sp)
lw $t1 -12($sp)
add $a0 $t0 $t1
sw $a0 -4($sp)
lw $t0 -4($sp)
li $t1 5
mul $a0 $t0 $t1
sw $a0 0($sp)
move $t0 $a0
sw $t0 4($sp)
li $v0 1
lw $a0 4($sp)
syscall
li $v0 4
la $a0 newline
syscall
addiu $sp $sp 72
lw $ra 4($sp)
addiu $sp $sp 8
lw $fp 0($sp)
jr $ra

main:

li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 4
move $t0 $a0
sw $t0 8($sp)
li $v0 1
sw $fp 0($sp)
addiu $sp $sp -4
li $a0 7
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 3
sw $a0 0($sp)
addiu $sp $sp -4
jal suma
syscall
li $v0 4
la $a0 newline
syscall
li $a0 3
move $t0 $a0
sw $t0 4($sp)
li $v0 1
lw $t0 8($sp)
lw $t1 4($sp)
add $a0 $t0 $t1
sw $a0 0($sp)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
sw $fp 0($sp)
addiu $sp $sp -4
li $a0 4
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 3
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 1
sw $a0 0($sp)
addiu $sp $sp -4
jal globalfunc
syscall
li $v0 4
la $a0 newline
syscall
li $a0 4
move $t0 $a0
li $a0 1
li $a1 4
mul $a0 $a0 $a1
la $a1 globalarr
add $a1 $a1 $a0
sw $t0 0($a1)
li $a0 4
move $t0 $a0
la $a0 global
sw $t0 0($a0)
li $a0 17
move $t0 $a0
li $a0 1
li $a1 4
mul $a0 $a0 $a1
la $a1 globalarr
add $a1 $a1 $a0
sw $t0 0($a1)
li $v0 1
la $a0 global
lw $a0 0($a0) 
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 1
li $a1 4
mul $a0 $a0 $a1
la $a1 globalarr
add $a1 $a1 $a0
lw $a0 0($a1)
syscall
li $v0 4
la $a0 newline
syscall
sw $fp 0($sp)
addiu $sp $sp -4
jal arrmanagement
li $v0 1
li $a0 0
li $a1 4
mul $a0 $a0 $a1
la $a1 globalarr
add $a1 $a1 $a0
lw $a0 0($a1)
syscall
li $v0 4
la $a0 newline
syscall
sw $fp 0($sp)
addiu $sp $sp -4
jal largeoperations

End:
li $v0 10
syscall
Negindexerror:
li $v0 4
la $a0 negindex
syscall
j End
Outboundserror:
li $v0 4
la $a0 outbounds
syscall
j End
