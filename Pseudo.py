# import random
# lst= sorted([random.randint(1,1000) for _ in range(100)])

# def binarySearch(lst,target):
#     start=0
#     end= len(lst)-1  
#     mid=(start+end)//2
#     while start<end:
#         if lst[mid]==target:
#             return True
#         if target<lst[mid]:
#             end=mid-1
#         elif target>lst[mid]:
#             low=mid+1
    
#         mid=(start+end)//2
#     return False

# x=12
# print(binarySearch(lst,x))
# print(x in lst)



# def changeCalculator(cash,price):
#     currency=[50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
#     currency=[x*100 for x in currency]
#     change=(cash-price)*100
#     pointer=0
#     toReturn=[]
#     while change>0:
#         if currency[pointer]>change:
#             pointer+=1
#         else:
#             toReturn.append(currency[pointer]/100)
#             change-= currency[pointer]
#     return toReturn
# print(changeCalculator(50,29.75))


def isPrime():
    num=int(input("Enter Number:"))
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return False
        else:
            return True
    else:
        return False
print(isPrime())