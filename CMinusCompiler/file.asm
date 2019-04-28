.data
newline: .align 4 
.asciiz "\n" 
negindex: .align 4 
.asciiz "Error de runtime: No se permiten indices negativos" 
outbounds: .align 4 
.asciiz "Error de runtime: Indice fuera de rango" 
globalarr: .space 12
.text
.globl main

j main

functionarrarys:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $v0 1
li $a0 0
move $a2 $sp
addiu $a2 $a2 20
lw $a2 0($a2)
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
move $a2 $sp
addiu $a2 $a2 20
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 2
move $a2 $sp
addiu $a2 $a2 20
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 0
move $a2 $sp
addiu $a2 $a2 16
lw $a2 0($a2)
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
move $a2 $sp
addiu $a2 $a2 16
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 0
move $a2 $sp
addiu $a2 $a2 12
lw $a2 0($a2)
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
move $a2 $sp
addiu $a2 $a2 12
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 0
move $a2 $sp
addiu $a2 $a2 8
lw $a2 0($a2)
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
move $a2 $sp
addiu $a2 $a2 8
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 2
move $a2 $sp
addiu $a2 $a2 8
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 3
move $a2 $sp
addiu $a2 $a2 8
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
syscall
li $v0 4
la $a0 newline
syscall
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 24
lw $fp 0($sp)
jr $ra

functionints:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
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
lw $a0 12($sp)
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
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 24
lw $fp 0($sp)
jr $ra

functionboth:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $v0 1
lw $a0 20($sp)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 0
move $a2 $sp
addiu $a2 $a2 16
lw $a2 0($a2)
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
move $a2 $sp
addiu $a2 $a2 16
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
lw $a0 12($sp)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 0
move $a2 $sp
addiu $a2 $a2 8
lw $a2 0($a2)
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
move $a2 $sp
addiu $a2 $a2 8
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
li $a0 2
move $a2 $sp
addiu $a2 $a2 8
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
syscall
li $v0 4
la $a0 newline
syscall
li $a0 1001
move $t0 $a0
li $a0 0
move $a2 $sp
addiu $a2 $a2 16
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 1002
move $t0 $a0
li $a0 1
move $a2 $sp
addiu $a2 $a2 16
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 24
lw $fp 0($sp)
jr $ra

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
li $a0 0
blt $a0 $zero Negindexerror
li $a2 3
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 60
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 2
move $t0 $a0
li $a0 1
blt $a0 $zero Negindexerror
li $a2 3
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 60
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 3
move $t0 $a0
li $a0 2
blt $a0 $zero Negindexerror
li $a2 3
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 60
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 4
move $t0 $a0
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 48
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 5
move $t0 $a0
li $a0 1
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 48
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 6
move $t0 $a0
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 40
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 7
move $t0 $a0
li $a0 1
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 40
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 8
move $t0 $a0
li $a0 0
blt $a0 $zero Negindexerror
li $a2 4
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 32
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 9
move $t0 $a0
li $a0 1
blt $a0 $zero Negindexerror
li $a2 4
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 32
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 10
move $t0 $a0
li $a0 2
blt $a0 $zero Negindexerror
li $a2 4
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 32
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 11
move $t0 $a0
li $a0 3
blt $a0 $zero Negindexerror
li $a2 4
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 32
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
sw $fp 0($sp)
addiu $sp $sp -4
move $a0 $sp
addiu $a0 64
sw $a0 0($sp)
addiu $sp $sp -4
move $a0 $sp
addiu $a0 56
sw $a0 0($sp)
addiu $sp $sp -4
move $a0 $sp
addiu $a0 52
sw $a0 0($sp)
addiu $sp $sp -4
move $a0 $sp
addiu $a0 48
sw $a0 0($sp)
addiu $sp $sp -4
jal functionarrarys
li $a0 1
move $t0 $a0
sw $t0 16($sp)
li $a0 2
move $t0 $a0
sw $t0 12($sp)
li $a0 3
move $t0 $a0
sw $t0 8($sp)
li $a0 4
move $t0 $a0
sw $t0 4($sp)
sw $fp 0($sp)
addiu $sp $sp -4
lw $a0 20($sp)
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 20($sp)
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 20($sp)
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 20($sp)
sw $a0 0($sp)
addiu $sp $sp -4
jal functionints
li $a0 1
move $t0 $a0
sw $t0 16($sp)
li $a0 2
move $t0 $a0
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 48
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 3
move $t0 $a0
li $a0 1
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 48
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 4
move $t0 $a0
sw $t0 12($sp)
li $a0 5
move $t0 $a0
li $a0 0
blt $a0 $zero Negindexerror
li $a2 3
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 60
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 6
move $t0 $a0
li $a0 1
blt $a0 $zero Negindexerror
li $a2 3
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 60
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 7
move $t0 $a0
li $a0 2
blt $a0 $zero Negindexerror
li $a2 3
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 60
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 2
move $t0 $a0
li $a0 0
li $a1 4
mul $a0 $a0 $a1
la $a1 globalarr
add $a1 $a1 $a0
sw $t0 0($a1)
li $a0 3
move $t0 $a0
li $a0 1
li $a1 4
mul $a0 $a0 $a1
la $a1 globalarr
add $a1 $a1 $a0
sw $t0 0($a1)
sw $fp 0($sp)
addiu $sp $sp -4
lw $a0 20($sp)
sw $a0 0($sp)
addiu $sp $sp -4
la $a0 globalarr
lw $a0 0($a0) 
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 24($sp)
sw $a0 0($sp)
addiu $sp $sp -4
move $a0 $sp
addiu $a0 76
sw $a0 0($sp)
addiu $sp $sp -4
jal functionboth
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
