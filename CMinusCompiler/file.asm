.data
newline: .asciiz "\n" 
negindex: .asciiz "Error de runtime: No se permiten indices negativos" 
outbounds: .asciiz "Error de runtime: Indice fuera de rango" 
.text
.globl main

li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
j main

suma:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
lw $a0 8($sp)
lw $a1 12($sp)
add $a0 $a0 $a1
sw $a0 0($sp)
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra

globalfunc:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $a0 1
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 8
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 12($sp)
lw $a1 0($a2)
mul $a0 $a0 $a1
sw $a0 0($sp)
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
move $a1 $a0
sw $a1 8($sp)
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
move $a1 $a0
sw $a1 4($sp)
li $v0 1
lw $a0 8($sp)
lw $a1 4($sp)
add $a0 $a0 $a1
sw $a0 0($sp)
syscall
li $v0 4
la $a0 newline
syscall
li $a0 5
move $a1 $a0
sw $a1 12($sp)
li $a0 11
move $a1 $a0
li $a0 1
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 8
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $a1 0($a2)
li $v0 1
sw $fp 0($sp)
addiu $sp $sp -4
sw $fp 0($sp)
addiu $sp $sp -4
jal void
sw $a0 0($sp)
addiu $sp $sp -4
jal globalfunc
syscall
li $v0 4
la $a0 newline
syscall

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
