.data
newline: .asciiz "\n" 
negindex: .asciiz "Error de runtime: No se permiten indices negativos" 
outbounds: .asciiz "Error de runtime: Indice fuera de rango" 
.text
.globl main

main:
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
li $a0 2
sw $a0 16($sp)
li $a0 1
li $a1 5
mul $a0 $a0 $a1
sw $a0 -8($sp)
li $a0 2
li $a1 3
mul $a0 $a0 $a1
sw $a0 -12($sp)
lw $a0 -8($sp)
lw $a1 -12($sp)
sub $a0 $a0 $a1
sw $a0 -4($sp)
lw $a0 -4($sp)
li $a1 11
add $a0 $a0 $a1
sw $a0 0($sp)
sw $a0 20($sp)
li $a0 5
li $a1 3
sub $a0 $a0 $a1
sw $a0 -4($sp)
li $a0 6
li $a1 1
sub $a0 $a0 $a1
sw $a0 -8($sp)
lw $a0 -4($sp)
lw $a1 -8($sp)
mul $a0 $a0 $a1
sw $a0 0($sp)
move $a1 $a0
li $a0 0
blt $a0 $zero Negindexerror
li $a2 3
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 12
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $a1 0($a2)
li $a0 5
move $a1 $a0
lw $a0 16($sp)
blt $a0 $zero Negindexerror
li $a2 3
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 12
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $a1 0($a2)
li $v0 1
lw $a0 20($sp)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
lw $a0 16($sp)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 0
blt $a0 $zero Negindexerror
li $a2 3
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 12
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 ($a2)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 1
blt $a0 $zero Negindexerror
li $a2 3
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 12
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 ($a2)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 2
blt $a0 $zero Negindexerror
li $a2 3
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 12
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 ($a2)
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
