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
li $a0 5
sw $a0 8($sp)
sw $a0 12($sp)
li $a0 7
sw $a0 12($sp)
end:
li $v0 10
syscall