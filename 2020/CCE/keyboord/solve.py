#!/usr/bin/env python3

enc = [0x63, 0x62, 0x67, 0x31, 0x34, 0x37, 0x36, 0x7c,0x63, 0x6c, 0x73, 0x69,
             0x63, 0x62, 0x7c, 0x6b, 0x4f, 0x61, 0x73, 0x70, 0x7f, 0x70,0x61, 0x62, 0x48,
                0x7d, 0x78, 0x69, 0x62, 0x43, 0x42, 0x41, 0x46, 0x45, 0x40, 0x4a, 0x02, 0x59]
enc = enc[:22] + enc[23:]

for i in range(37):
    enc[i] ^= i

flag = ''.join([chr(c) for c in enc])
assert flag == 'cce2020{keyboord_packet_easy___Yeah!}'

print(flag)
