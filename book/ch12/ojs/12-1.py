n=input()
l=len(n)
left=0
right=0

for i in range(l//2):
  left += int(n[i])
  right += int(n[i+l//2])
if left==right: print('LUCKY')
else:print('READY')