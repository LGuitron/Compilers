.data
newline0: .align 4 
.asciiz "\n" 
negindex0: .align 4 
.asciiz "Error de runtime: No se permiten indices negativos" 
outbounds0: .align 4 
.asciiz "Error de runtime: Indice fuera de rango" 
input0: .align 4 
.asciiz "Intoduce un entero: " 
.space 40
x: .word 0
.text
.globl main

j main

minloc:

move $fp $sp
sw $ra 0($sp)
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
lw $a0 24($sp)
move $t0 $a0
sw $t0 4($sp)
lw $a0 24($sp)
move $a2 $sp
addiu $a2 $a2 28
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
move $t0 $a0
sw $t0 8($sp)
lw $t0 24($sp)
li $t1 1
add $a0 $t0 $t1
sw $a0 0($sp)
move $t0 $a0
sw $t0 12($sp)
while0:
lw $t0 12($sp)
lw $t1 20($sp)
slt $a0 $t0 $t1
sw $a0 0($sp)
beq $a0 $zero endwhile0
lw $a0 12($sp)
move $a2 $sp
addiu $a2 $a2 28
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a2 0($a2)
sw $a2 -4($sp)
lw $t0 -4($sp)
lw $t1 8($sp)
slt $a0 $t0 $t1
sw $a0 0($sp)
beq $a0 $zero endif0
lw $a0 12($sp)
move $a2 $sp
addiu $a2 $a2 28
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
move $t0 $a0
sw $t0 8($sp)
lw $a0 12($sp)
move $t0 $a0
sw $t0 4($sp)
addiu $sp $sp 0
j endif0
endif0:
lw $t0 12($sp)
li $t1 1
add $a0 $t0 $t1
sw $a0 0($sp)
move $t0 $a0
sw $t0 12($sp)
addiu $sp $sp 0
b while0
endwhile0:
lw $a0 4($sp)
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 20
lw $fp 0($sp)
jr $ra
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 20
lw $fp 0($sp)
jr $ra

sort:

move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 20($sp)
move $t0 $a0
sw $t0 8($sp)
while1:
lw $t0 16($sp)
li $t1 1
sub $a0 $t0 $t1
sw $a0 -8($sp)
lw $t0 8($sp)
lw $t1 -8($sp)
slt $a0 $t0 $t1
sw $a0 0($sp)
beq $a0 $zero endwhile1
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
sw $fp 0($sp)
addiu $sp $sp -4
move $a1 $sp
addiu $a1 32
lw $a0 0($a1)
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 20($sp)
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 32($sp)
sw $a0 0($sp)
addiu $sp $sp -4
jal minloc
move $t0 $a0
sw $t0 8($sp)
lw $a0 8($sp)
move $a2 $sp
addiu $a2 $a2 28
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
move $t0 $a0
sw $t0 4($sp)
lw $a0 12($sp)
move $a2 $sp
addiu $a2 $a2 28
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
lw $a0 0($a2)
move $t0 $a0
lw $a0 8($sp)
move $a2 $sp
addiu $a2 $a2 28
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
lw $a0 4($sp)
move $t0 $a0
lw $a0 12($sp)
move $a2 $sp
addiu $a2 $a2 28
lw $a2 0($a2)
li $a3 4
mul $a0 $a0 $a3
sub $a2 $a2 $a0
sw $t0 0($a2)
lw $t0 12($sp)
li $t1 1
add $a0 $t0 $t1
sw $a0 0($sp)
move $t0 $a0
sw $t0 12($sp)
addiu $sp $sp 4
b while1
endwhile1:
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 20
lw $fp 0($sp)
jr $ra

main:

li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
move $t0 $a0
sw $t0 4($sp)
while2:
lw $t0 4($sp)
li $t1 10
slt $a0 $t0 $t1
sw $a0 0($sp)
beq $a0 $zero endwhile2
li $v0 4
la $a0 input0
syscall
li $v0 5
syscall
move $a0 $v0
move $t0 $a0
lw $a0 4($sp)
li $a1 4
mul $a0 $a0 $a1
la $a1 x
sub $a1 $a1 $a0
sw $t0 0($a1)
lw $t0 4($sp)
li $t1 1
add $a0 $t0 $t1
sw $a0 0($sp)
move $t0 $a0
sw $t0 4($sp)
addiu $sp $sp 0
b while2
endwhile2:
sw $fp 0($sp)
addiu $sp $sp -4
la $a0 x
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 10
sw $a0 0($sp)
addiu $sp $sp -4
jal sort
li $a0 0
move $t0 $a0
sw $t0 4($sp)
while3:
lw $t0 4($sp)
li $t1 10
slt $a0 $t0 $t1
sw $a0 0($sp)
beq $a0 $zero endwhile3
lw $a0 4($sp)
blt $a0 $zero Negindexerror
li $a2 10
bge $a0 $a2 Outboundserror
li $a1 4
mul $a0 $a0 $a1
la $a1 x
sub $a1 $a1 $a0
lw $a0 0($a1)
li $v0 1
syscall
li $v0 4
la $a0 newline0
syscall
lw $t0 4($sp)
li $t1 1
add $a0 $t0 $t1
sw $a0 0($sp)
move $t0 $a0
sw $t0 4($sp)
addiu $sp $sp 0
b while3
endwhile3:

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
