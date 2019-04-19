.data
newline: .asciiz "\n" 
.text
.globl main

main:
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 4($sp)
addiu $sp $sp -4
li $a0 1
sw $a0 0($sp)
sw $a0 4($sp)
lw $a0 0($sp)
li $a1 2
add $a0 $a0 $a1
li $a0 3
li $a1 4
add $a1 $a0 $a1
lw $a0 0($sp)
li $a1 2
add $a0 $a0 $a1
li $a0 3
li $a1 4
add $a1 $a0 $a1
add $a0 $a0 $a1
li $a0 5
li $a1 6
add $a0 $a0 $a1
li $a0 7
li $a1 8
add $a1 $a0 $a1
li $a0 5
li $a1 6
add $a0 $a0 $a1
li $a0 7
li $a1 8
add $a1 $a0 $a1
add $a1 $a0 $a1
lw $a0 0($sp)
li $a1 2
add $a0 $a0 $a1
li $a0 3
li $a1 4
add $a1 $a0 $a1
lw $a0 0($sp)
li $a1 2
add $a0 $a0 $a1
li $a0 3
li $a1 4
add $a1 $a0 $a1
add $a0 $a0 $a1
li $a0 5
li $a1 6
add $a0 $a0 $a1
li $a0 7
li $a1 8
add $a1 $a0 $a1
li $a0 5
li $a1 6
add $a0 $a0 $a1
li $a0 7
li $a1 8
add $a1 $a0 $a1
add $a1 $a0 $a1
add $a0 $a0 $a1
sw $a0 0($sp)
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
li $a1 5
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
li $a1 5
add $a0 $a0 $a1
li $a1 6
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
li $a1 5
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
li $a1 5
add $a0 $a0 $a1
li $a1 6
add $a0 $a0 $a1
li $a1 7
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
li $a1 5
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
li $a1 5
add $a0 $a0 $a1
li $a1 6
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
li $a1 5
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
lw $a0 4($sp)
li $a1 2
add $a0 $a0 $a1
li $a1 3
add $a0 $a0 $a1
li $a1 4
add $a0 $a0 $a1
li $a1 5
add $a0 $a0 $a1
li $a1 6
add $a0 $a0 $a1
li $a1 7
add $a0 $a0 $a1
li $a1 8
add $a0 $a0 $a1
sw $a0 4($sp)
li $v0 1
lw $a0 0($sp)
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

end:
li $v0 10
syscall