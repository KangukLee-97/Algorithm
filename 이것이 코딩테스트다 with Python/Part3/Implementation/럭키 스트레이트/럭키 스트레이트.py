n = input()
length = int(len(n)/2)

left = n[0:length]
right = n[length:]

lsum = 0
rsum = 0

for i in range(length):
    lsum += int(left[i])
    rsum += int(right[i])

print('LUCKY' if lsum == rsum else 'READY')
