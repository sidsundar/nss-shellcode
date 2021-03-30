all: victim-input victim-nonexec-stack-input test
	sudo sysctl -w kernel.randomize_va_space=0

victim-input:
	as -o shellcode shellcode.s
	readelf -x .text shellcode > shellcode_hex
	python3 prepare_shellcode.py 78 140737488347104 

victim-nonexec-stack-input:
	python3 prepare_rop.py

test:
	gcc shellcode.c -o test
