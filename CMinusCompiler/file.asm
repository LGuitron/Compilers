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

perr:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
lw $a0 8($sp)
li $v0 1
syscall
li $v0 4
la $a0 newline0
syscall
li $a0 0
move $a2 $sp
addiu $a2 $a2 12
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a2 0($a2)
sw $a2 -4($sp)
lw $t0 -4($sp)
li $t1 32
add $a0 $t0 $t1
sw $a0 0($sp)
move $t0 $a0
li $a0 0
move $a2 $sp
addiu $a2 $a2 12
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
li $a0 0
move $a2 $sp
addiu $a2 $a2 20
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a2 0($a2)
sw $a2 -8($sp)
li $a0 0
move $a2 $sp
addiu $a2 $a2 16
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a2 0($a2)
sw $a2 -12($sp)
lw $t0 -8($sp)
lw $t1 -12($sp)
add $a0 $t0 $t1
sw $a0 -4($sp)
li $a0 0
move $a2 $sp
addiu $a2 $a2 12
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a2 0($a2)
sw $a2 -8($sp)
lw $t0 -4($sp)
lw $t1 -8($sp)
add $a0 $t0 $t1
sw $a0 0($sp)
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 24
lw $fp 0($sp)
jr $ra

can:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 32
move $t0 $a0
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 8
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
sw $fp 0($sp)
addiu $sp $sp -4
move $a1 $sp
addiu $a1 24
lw $a0 0($a1)
sw $a0 0($sp)
addiu $sp $sp -4
move $a1 $sp
addiu $a1 24
lw $a0 0($a1)
sw $a0 0($sp)
addiu $sp $sp -4
move $a0 $sp
addiu $a0 20
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 24
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a2 0($a2)
sw $a2 -4($sp)
lw $t0 -4($sp)
li $t1 10
add $a0 $t0 $t1
sw $a0 0($sp)
sw $a0 0($sp)
addiu $sp $sp -4
jal perr
addiu $sp $sp 8
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra

perro:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 100
move $t0 $a0
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 8
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
sw $fp 0($sp)
addiu $sp $sp -4
move $a1 $sp
addiu $a1 20
lw $a0 0($a1)
sw $a0 0($sp)
addiu $sp $sp -4
move $a0 $sp
addiu $a0 16
sw $a0 0($sp)
addiu $sp $sp -4
jal can
addiu $sp $sp 8
lw $ra 4($sp)
addiu $sp $sp 12
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
li $a0 1000
move $t0 $a0
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 12
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
sw $fp 0($sp)
addiu $sp $sp -4
move $a0 $sp
addiu $a0 16
sw $a0 0($sp)
addiu $sp $sp -4
jal perro
li $v0 1
syscall
li $v0 4
la $a0 newline0
syscall
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 12
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a2 0($a2)
sw $a2 -4($sp)
lw $t0 -4($sp)
li $t1 79
add $a0 $t0 $t1
sw $a0 0($sp)
move $t0 $a0
li $a0 0
blt $a0 $zero Negindexerror
li $a2 2
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 12
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
sw $fp 0($sp)
addiu $sp $sp -4
move $a0 $sp
addiu $a0 16
sw $a0 0($sp)
addiu $sp $sp -4
jal perro
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
