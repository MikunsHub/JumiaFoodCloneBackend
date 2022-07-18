# nums = [45,22,14,65,97,72]
# for i in range(len(nums)):
#     if nums[i] % 3 == 0 and nums[i] % 5 == 0:
#         nums[i] = 'fizzbuzz'
#     elif  nums[i] % 3 == 0:
#         nums[i] = 'fuzz'
#     elif nums[i] % 5 == 0:
#         nums[i] = 'buzz'
# print(nums)

# for x in range(6):
#     if x == 3: continue
#     if x == 6: break
#     print(x)


password = input('Password must be strong with a capital and symbol:')

for i in password:
 if i.isupper() or  i.isdigit():
     print('valid')
     break
 else:
     print('password at least  a capital letter and a number')   
 break
 print(password)


    