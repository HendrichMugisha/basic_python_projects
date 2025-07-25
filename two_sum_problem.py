# You are given an array of numbers and a target sum. Your task is to find the indices of the two numbers that add up to the target

nums_list = [4,2,7,8,1]
target = 9

def sum_problem(nums_list, target):
    # create a empty dictionary
    num_dict = {}

    #iterate through the list using enumerate
    for index, num in enumerate(nums_list):
        complement = target - num
        if complement not in num_dict:
            num_dict[num] = index
        else:
            return [num, complement]
    return []

sum_problem(nums_list, target)




























def sum(nums_list, target):
    num_dict = {} #define a dictionary
    
    for index, num in enumerate(nums_list): #iterate over the list and keep both the index and the number
        complement = target - num

        if complement in num_dict:
            return [num_dict[complement], index]
        num_dict[num] = index
    return []

print(sum(nums_list, target)[:])




















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
            