# You are given an array of numbers and a target sum. Your task is to find the indices of the two numbers that add up to the target
nums = [2, 7, 11, 15]

for index, list_member in enumerate(nums):
    print(f"Index: {index}, Number: {list_member}")























# nums = [2, 7, 11, 15]
# target = 9

# answer_list = []

# for member_index in range(len(nums)):
#     if nums[member_index] > 9:
#         continue
#     else:
#         for next_index in range(len(nums[member_index+1: ])):
#             if nums[next_index] > 9:
#                 continue
#             elif (nums[member_index] + nums[next_index]) == 9:
#                 if nums[member_index] not in answer_list :
#                     answer_list.append(member_index)
#                     answer_list.append(next_index)

# print(answer_list)
            