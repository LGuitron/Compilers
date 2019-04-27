.data
newline: .asciiz "\n" 
negindex: .asciiz "Error de runtime: No se permiten indices negativos" 
outbounds: .asciiz "Error de runtime: Indice fuera de rango" 
global: .word 0 
globalarr: .space 40
.text
.globl main

j main

function:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 12
lw $fp 0($sp)
jr $ra

main:

li $a0 5
move $t0 $a0
la $a0 global
sw $t0 0($a0)
li $a0 3
move $t0 $a0
li $a0 4
li $a1 4
mul $a0 $a0 $a1
la $a1 globalarr
add $a1 $a1 $a0
sw $t0 0($a1)
li $a0 2
move $t0 $a0
li $a0 3
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
li $a0 4
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
li $a0 3
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
