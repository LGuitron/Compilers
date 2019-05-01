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

func:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
lw $a0 8($sp)
li $v0 1
syscall
li $v0 4
la $a0 newline0
syscall
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
li $a0 4
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
move $a0 $sp
addiu $a0 24
sw $a0 0($sp)
addiu $sp $sp -4
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
li $t1 3
add $a0 $t0 $t1
sw $a0 0($sp)
sw $a0 0($sp)
addiu $sp $sp -4
jal func

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
