iN,iK = input().split()
iA = input().split()
for i in range(len(iA)):
  iA[i] = int(iA[i])
  
def rotateArray(n, k, arr):
  arrTemp = []
  for i in range(k):
    arrTemp.append(arr[n-1])
    arr.pop(n-1)
    arr.insert(0, arrTemp[i])
  print(*arr, sep=" ")
  return arr

rotateArray(int(iN), int(iK), iA)
