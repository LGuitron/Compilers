.data
newline: .align 4 
.asciiz "\n" 
negindex: .align 4 
.asciiz "Error de runtime: No se permiten indices negativos" 
outbounds: .align 4 
.asciiz "Error de runtime: Indice fuera de rango" 
global: .word 0
.space 12
globalarr: .word 0
.text
.globl main

j main

another:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
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
li $a0 2
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
lw $a0 8($sp)
syscall
li $v0 4
la $a0 newline
syscall
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra

final:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
sw $fp 0($sp)
addiu $sp $sp -4
move $a1 $sp
addiu $a1 16
lw $a0 0($a1)
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 16($sp)
sw $a0 0($sp)
addiu $sp $sp -4
jal another
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra

recarr:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
sw $fp 0($sp)
addiu $sp $sp -4
move $a1 $sp
addiu $a1 16
lw $a0 0($a1)
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 16($sp)
sw $a0 0($sp)
addiu $sp $sp -4
jal final
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra

main:

li $a0 1
move $t0 $a0
li $a0 0
li $a1 4
mul $a0 $a0 $a1
la $a1 globalarr
sub $a1 $a1 $a0
sw $t0 0($a1)
li $a0 2
move $t0 $a0
li $a0 1
li $a1 4
mul $a0 $a0 $a1
la $a1 globalarr
sub $a1 $a1 $a0
sw $t0 0($a1)
li $a0 3
move $t0 $a0
li $a0 2
li $a1 4
mul $a0 $a0 $a1
la $a1 globalarr
sub $a1 $a1 $a0
sw $t0 0($a1)
li $a0 1000
move $t0 $a0
la $a0 global
sw $t0 0($a0)
sw $fp 0($sp)
addiu $sp $sp -4
la $a0 globalarr
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 4
sw $a0 0($sp)
addiu $sp $sp -4
jal recarr
li $v0 1
la $a0 global
lw $a0 0($a0) 
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
