'''
[3:12 PM, 1/11/2021] Amit sawant: Home-work:3:
[3:13 PM, 1/11/2021] Amit sawant: Write a python script which has list of duplicate numbers
numbers = [1,1,2,3,3,3,4,4,5,6]
using dictionary remove  the duplicate elements and print only unique elements. so the output should be
1,2,3,4,5,6
'''
uniqe_number={}
numbers = [1,1,2,3,3,3,4,4,5,6]
for number in numbers:
  uniqe_number[number]=""
for number in uniqe_number:
  print(number)
