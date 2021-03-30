
 
int main()	{
	asm(
			"jmp str\n"
			"start: \n"
		        "popq %rsi \n"
			"xorq %rax, %rax \n"
			"xorq %rdx, %rdx \n"
			"movb $1, %al   \n"
			"movq %rax, %rdi   \n"
			"movb $12, %dl  \n"
			"syscall         \n"
			"dec %rdi   \n"
			"movb $60, %al  \n"
			"syscall         \n"
			"str: \n"
			"call start      \n"
			".string \"Hello world!\" \n"
	   ); 
}
