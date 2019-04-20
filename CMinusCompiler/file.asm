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
li $a0 1
move $a1 $a0
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 8
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $a1 0($a2)
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 8
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 8
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
lw $a1 0($a2)
mul $a0 $a0 $a1
sw $a0 -8($sp)
li $a0 5
lw $a1 -8($sp)
sub $a0 $a0 $a1
sw $a0 0($sp)
move $a1 $a0
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 8
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $a1 0($a2)
sw $a1 12($sp)
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
lw $a0 12($sp)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 8
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 1
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 8
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
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
