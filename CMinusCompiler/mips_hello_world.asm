.text
.globl main

main:
    li $a0 7
    sw $a0 0($sp)
    addiu $sp $sp -4
    li $a0 5
    lw $t1 4($sp)
    add $a0 $a0 $t1
    addiu $sp $sp 4
    
end:
    li $v0, 10
    syscall
