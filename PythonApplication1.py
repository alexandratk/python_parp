#!/usr/bin/python

import csv
arr=[]
with open('tmdb_5000_movies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         arr.append(int(row['budget']))
for i in range(len(arr)):
    print(arr[i],end='\n')
sum=0
for i in range(len(arr)):
    sum+=arr[i]
print (sum)   
arif=sum/len(arr)
print (arif)
disp=0
for i in range(len(arr)):
    disp+=(arr[i]-arif)*(arr[i]-arif)
disp=disp/(len(arr)-1)
print (disp)
vidh=0
vidh=disp ** (0.5)
print (vidh)


mediana=0
arr.sort()
if(len(arr)%2==0):
    mediana=(arr[int(len(arr)/2)]+arr[int(len(arr)/2-1)])/2
else:
    mediana=arr[int(len(arr)/2)]
print (mediana)


max=arr[len(arr)-1]
print (max)
min=arr[0]
print (min)
rozmah=max-min
print (rozmah)


arr[1000] = 11
arr[1001] = 16
arr[1002] = 11
#print (list(map(arr.count, arr)))
arr1 = list(map(arr.count, arr))
most = 0
for i in range(len(arr1)):
    if (most < arr1[i]):
        most = arr1[i]
#print (most)
res = list(set(filter(lambda x: arr.count(x) == most, arr)))
print('Мода- ', most, res)


def quantile(q):
  arr.sort()
  n = len(arr) 
  div = 1 / q
  ind = int(n // div)
  if n % div == 0:
      median1 = arr[ind] 
      median2 = arr[ind - 1] 
      median = (median1 + median2) / 2
  else: 
      median = arr[ind] 
  print('Квантиль ', q, ' - ', median)
  return median
quantile(0.1)
quantile(0.25)
quantile(0.5)
quantile(0.75)