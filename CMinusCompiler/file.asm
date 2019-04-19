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
sw $a0 4($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 8($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 12($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 16($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 20($sp)
addiu $sp $sp -4
li $a0 2
sw $a0 0($sp)
li $a0 1
move $a1 $a0
lw $a0 0($sp)
blt $a0 $zero Negindexerror
li $a2 3
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 12
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $a1 0($a2)
li $a0 1
sw $a0 0($sp)
sw $a0 4($sp)
sw $a0 8($sp)
li $a0 7
li $a1 8
add $a0 $a0 $a1
sw $a0 72($sp)
li $a0 6
lw $a1 72($sp)
add $a0 $a0 $a1
sw $a0 64($sp)
li $a0 5
lw $a1 64($sp)
add $a0 $a0 $a1
sw $a0 56($sp)
li $a0 4
lw $a1 56($sp)
add $a0 $a0 $a1
sw $a0 48($sp)
li $a0 3
lw $a1 48($sp)
add $a0 $a0 $a1
sw $a0 40($sp)
li $a0 2
lw $a1 40($sp)
add $a0 $a0 $a1
sw $a0 32($sp)
lw $a0 0($sp)
lw $a1 32($sp)
add $a0 $a0 $a1
sw $a0 24($sp)
sw $a0 0($sp)
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
sw $a0 48($sp)
lw $a0 48($sp)
li $a1 3
add $a0 $a0 $a1
sw $a0 44($sp)
lw $a0 44($sp)
li $a1 4
add $a0 $a0 $a1
sw $a0 40($sp)
lw $a0 40($sp)
li $a1 5
add $a0 $a0 $a1
sw $a0 36($sp)
lw $a0 36($sp)
li $a1 6
add $a0 $a0 $a1
sw $a0 32($sp)
lw $a0 32($sp)
li $a1 7
add $a0 $a0 $a1
sw $a0 28($sp)
lw $a0 28($sp)
li $a1 8
add $a0 $a0 $a1
sw $a0 24($sp)
sw $a0 4($sp)
lw $a0 8($sp)
li $a1 2
add $a0 $a0 $a1
sw $a0 32($sp)
li $a0 3
li $a1 4
add $a0 $a0 $a1
sw $a0 36($sp)
lw $a0 32($sp)
lw $a1 36($sp)
add $a0 $a0 $a1
sw $a0 28($sp)
li $a0 5
li $a1 6
add $a0 $a0 $a1
sw $a0 36($sp)
li $a0 8
lw $a1 8($sp)
mul $a0 $a0 $a1
sw $a0 48($sp)
li $a0 7
lw $a1 48($sp)
add $a0 $a0 $a1
sw $a0 40($sp)
lw $a0 36($sp)
lw $a1 40($sp)
add $a0 $a0 $a1
sw $a0 32($sp)
lw $a0 28($sp)
lw $a1 32($sp)
add $a0 $a0 $a1
sw $a0 24($sp)
sw $a0 8($sp)
li $v0 1
lw $a0 0($sp)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
lw $a0 4($sp)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
lw $a0 8($sp)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
lw $a0 (12, 3)($sp)
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
