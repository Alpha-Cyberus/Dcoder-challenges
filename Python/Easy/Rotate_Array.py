iN,iK = input().split()
iA = input().split()

  
def rotateArray(n, k, arr):
  arrTemp = []
  for i in range(k):
    arrTemp.append(arr[0])
    arr.pop(0)
    arr.append(arrTemp[i])
  arrTemp.clear  
  print(*arr, sep=" ")
  return arr


rotateArray(int(iN), int(iK), iA)
