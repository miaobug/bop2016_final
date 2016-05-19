# -*- coding: utf-8 -*-


f = open("key.txt")
f2 = open("api_key.txt","w")

f = f.readlines()

for i in range(0, len(f), 13):
    print >> f2, f[i], f[i+1][:-1], f[i+2], f[i+4][:-1], f[i+5], f[i+9]
