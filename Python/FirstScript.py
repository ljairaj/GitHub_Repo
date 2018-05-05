import sys
import random
import os

c = "LJR"
x, a, b = 'foo', 10, 1000.0001
# sys.stdout.write(x+"\n");
# print("\n\n\n\n");
# print(c);



# # Code to check prime number
# iVal1 = 2
# iMax = 30
# while (iVal1 <= iMax):
#     # print("\nInput Value:"+str(iVal1))
#     iVal2 = 2
#     isPrime = 0
#     while (iVal2 <= (iVal1 / 2)):
#         # print("Checking Value:"+str(iVal2)+" Output:"+str(iVal1%iVal2))
#         if (iVal1 % iVal2 == 0):
#             isPrime = 1
#             break
#         iVal2 += 1
#
#     if (isPrime == 1): print("The number " + str(iVal1) + " is not prime.")
#     # else: print("The number "+str(iVal1)+" is not prime.")
#
#     iVal1 += 1

# # Code to generate Fibonacci series.
# iVal1 = 0
# iVal2 = 1
# iSum = 1
# iMaxCnt = 10
#
# for iNum in range(0,20):
#     print("Value:",iSum)
#     iSum = iVal1 + iVal2
#
#     if(iNum%2==0):
#         iVal1 = iSum
#     else:
#         iVal2 = iSum

# super_villans = {'Fiddler' : 'Isaac Bowia',
#                  'Captain Cold' : 'Leonard Smart',
#                  'Weather Wizard' : 'Mark Mardon',
#                  'Mirror Master':'San Scudder',
#                  'Pied Piper':'Thomas Peterson'}
#
# fruit_list = ['apples','oranges','pineapples','watermelons','bananas']
#
# num_list = [[1,2,3],[30,40],[70,80,90,100]]
#
#
# i = 0
# while(i < len(num_list)):
#     j = 0
#     print("Value1:", num_list[i])
#     while(j < len(num_list[i])):
#         print("Value2:", num_list[i][j])
#         j += 1
#     i += 1

# Input_String = 'This message is to be delivered to [Jairaj,Amit,Mahesh] in regard to the recent projects [Proj1,Proj2].'

def createList(sInpStr, cLookup, temp_list):
    iIndx = 0
    while(iIndx<len(sInpStr)):
        iIndx = sInpStr.find(cLookup,iIndx)
        if(iIndx == -1):
            break
        temp_list.append(iIndx)
        iIndx += len(cLookup)

def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)

# Text1 = 'This message is to be delivered to [Jairaj L,Amit Nanda,Mahesh Gopal] in regard to the recent project [Proj1,Proj2]. This will be communicated accordingly.'
Text1 = 'This message is to be delivered to [Jairaj,Amit,Mahesh] in regard to the recent project.'

opnBrk_loc_list = []
createList(Text1,"[",opnBrk_loc_list)
print("Output: ",opnBrk_loc_list)

cldBrk_loc_list = []
createList(Text1,"]",cldBrk_loc_list)
print("Output: ",cldBrk_loc_list)

if(len(opnBrk_loc_list) != len(cldBrk_loc_list)):
    print("The string format is not correct.")
    exit(1)

Raw_Text1 = ''
sText_val_list = []
sText_val_Map = {}
iStart = 0
for iCnt1 in range(0,len(opnBrk_loc_list)):
    Raw_Text1 += (Text1[iStart:int(opnBrk_loc_list[iCnt1])]+"Temptxt"+str(iCnt1))
    sText_val_list.append(Text1[int(opnBrk_loc_list[iCnt1]+1):int(cldBrk_loc_list[iCnt1])].split(','))
    sText_val_Map["Temptxt"+str(iCnt1)]=Text1[int(opnBrk_loc_list[iCnt1]+1):int(cldBrk_loc_list[iCnt1])].split(',')
    iStart = cldBrk_loc_list[iCnt1]+1

    if(iCnt1 == len(opnBrk_loc_list)-1):
        Raw_Text1 += Text1[iStart:len(Text1)]

print("String Val: ",Raw_Text1)
print("Output1: ",sText_val_list)
print("Output2: ",sText_val_Map)

# iTotalStr = 0
# for iCnt2 in range(0,len(sText_val_list)):
#     if(iCnt2 == 0):
#         iTotalStr = len(sText_val_list[iCnt2])
#     else:
#         iTotalStr *= len(sText_val_list[iCnt2])
#
# print("Total Size:",iTotalStr)

# for iLp1 in range(len(sText_val_list[0])):
#     for iLp2 in range(len(sText_val_list[1])):
#         print("Output: ",sText_val_list[0][iLp1]+" , "+sText_val_list[1][iLp2])







