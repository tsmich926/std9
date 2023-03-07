K = int(input())
count = [0]*5
for i in range(6):
    D,G = map(int,input().split())
    count[D] += G

a = count[1:]
b = list(set(a))

ner = b[0]*b[1]