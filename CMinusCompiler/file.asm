.data
newline: .asciiz "\n" 
negindex: .asciiz "Error de runtime: No se permiten indices negativos" 
outbounds: .asciiz "Error de runtime: Indice fuera de rango" 
.text
.globl main

li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
j main

mil:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $a0 1000
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 8
lw $fp 0($sp)
jr $ra

printMil:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 18
move $a1 $a0
sw $a1 4($sp)
li $v0 1
sw $fp 0($sp)
addiu $sp $sp -4
jal mil
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
addiu $sp $sp 4
lw $ra 4($sp)
addiu $sp $sp 8
lw $fp 0($sp)
jr $ra

main:

sw $fp 0($sp)
addiu $sp $sp -4
jal printMil

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
