.data
newline0: .align 4 
.asciiz "\n" 
negindex0: .align 4 
.asciiz "Error de runtime: No se permiten indices negativos" 
outbounds0: .align 4 
.asciiz "Error de runtime: Indice fuera de rango" 
.space 12
globalarr: .word 0
global: .word 0
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
la $a0 newline0
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
la $a0 newline0
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
la $a0 newline0
syscall
li $a0 4
move $t0 $a0
sw $t0 8($sp)
li $v0 1
lw $a0 8($sp)
syscall
li $v0 4
la $a0 newline0
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
li $t0 0
li $t1 1
sub $a0 $t0 $t1
sw $a0 0($sp)
move $t0 $a0
la $a0 global
sw $t0 0($a0)
sw $fp 0($sp)
addiu $sp $sp -4
la $a0 globalarr
sw $a0 0($sp)
addiu $sp $sp -4
la $a0 global
lw $a0 0($a0)
sw $a0 0($sp)
addiu $sp $sp -4
jal recarr
li $v0 1
li $t0 1
li $t1 2
add $a0 $t0 $t1
sw $a0 -12($sp)
li $t0 3
li $t1 4
add $a0 $t0 $t1
sw $a0 -16($sp)
lw $t0 -12($sp)
lw $t1 -16($sp)
add $a0 $t0 $t1
sw $a0 -8($sp)
li $t0 5
li $t1 6
add $a0 $t0 $t1
sw $a0 -16($sp)
li $t0 7
li $t1 8
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
li $t1 10
mul $a0 $t0 $t1
sw $a0 0($sp)
syscall
li $v0 4
la $a0 newline0
syscall
li $v0 1
la $a0 global
lw $a0 0($a0) 
syscall
li $v0 4
la $a0 newline0
syscall
li $v0 1
la $a0 global
lw $a0 0($a0) 
li $a1 4
mul $a0 $a0 $a1
la $a1 globalarr
sub $a1 $a1 $a0
lw $a0 0($a1)
syscall
li $v0 4
la $a0 newline0
syscall
li $v0 1
la $a0 global
lw $a0 0($a0) 
blt $a0 $zero Negindexerror
li $a2 3
bge $a0 $a2 Outboundserror
move $a2 $sp
addiu $a2 $a2 12
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
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
