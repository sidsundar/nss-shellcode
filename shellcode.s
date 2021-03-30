jmp str
start: 
popq %rsi 
xorq %rax, %rax 
xorq %rdx, %rdx 
movb $1, %al   
movq %rax, %rdi   
movb $12, %dl  
syscall         
dec %rdi   
movb $60, %al  
syscall         
str: 
call start      
.string "Hello world!" 
