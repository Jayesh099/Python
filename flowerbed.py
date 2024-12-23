# # 605. Can Place Flowers
# # Easy
# # Topics
# # Companies
# # You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# # Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# # Example 1:

# # Input: flowerbed = [1,0,0,0,1], n = 1
# # Output: true
# # Example 2:

# # Input: flowerbed = [1,0,0,0,1], n = 2
# # Output: false

# flowerbed = [1,0,0,0,1]
# n = 1
# counter =  0
# output1= []
# real_output =  []
# for  i in range(len(flowerbed)):
#     if flowerbed[i] == 1:
#         output1.append(flowerbed[i])
#     else:
#         output1.append(flowerbed[i])
#         # print(f"\n\n\n\n\\n\n\n\n\n output1 :: {output1}")
#         for oi in range(len(output1)):    
#             if output1[oi] ==  1:
#                 pass
#             elif output1[oi-1] != 1 and output1[oi] == 0:
#                 real_output.append(1)
#                 flowerbed[i] = 1

# print(f"\n\n\n real_output ::: {real_output}")
# print(f"\n\n output1 :: {output1}")
# print(f"flowerbed :: {flowerbed}")
    


flowerbed = [1,0, 0,0,0,1]
n = 2
counter =  0
new_list = []
print(f"\nflowerbed :: {flowerbed}")
max_len = len(flowerbed)

for flower in range(len(flowerbed)):
    if flower == 1:
        if flowerbed[flower] ==  0:
            pass
    else:
        if flowerbed[flower-1] == 0 and flowerbed[flower] == 0:
            counter += 1
            flowerbed[flower] = 1 

        elif flower == max_len:
            print(f"jayesh  :: {flowerbed[flower]}")
            if flowerbed[flower-1] == 0 and flowerbed[flower] == 0:
                counter += 1
                flowerbed[flower] = 1 
                
            else:
                counter =counter - 1

print(f"\n\n\n counter :: {counter}")


             