# n = int(input())
# pi = [int(input())for i in range(n)]
# diff=[]
# for i in range(n):
#     for j in range(n):
#         if i != j:
#             diff+=[abs(pi[i]-pi[j])]
# print(f"Debug messages...{diff}")
# print(min(diff))

# n = int(input())
# pi = [int(input())for i in range(n)]
# diff=[]
# pi.sort
# for i in range(n-1):
#     diff+=[abs(pi[i]-pi[i+1])]
# print(diff)
# print(min(diff))


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
b = ''.join(format(ord(ch), '07b')  for ch in message)
print(b)
chno=0
pchar=""
output=""
while True:
    char=b[chno:chno+1]
    if char=="1" and pchar==char:
        output=output+"0"
    elif char=="1" and pchar!=char:
        output+=" 0 0"
    if char=="0" and pchar==char:
        output=output+"0"
    elif char=="0" and pchar!=char:
        output+=" 00 0"
    pchar=char
    chno+=1
    if chno==len(b):
        break
print(output)
