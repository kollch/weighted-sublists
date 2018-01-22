#import statistics
#import time
import json

def algo1(orig_list, num_sublists, result=None):
    """Find the minimal variance of summed lists."""
    if result is None:
        result = [[] for i in range(num_sublists)]
    sums = [sum(result[i]) for i in range(num_sublists)]
    for num in reversed(sorted(orig_list)):
        # Start with the largest number, then get the smallest summed sublist
        i = sums.index(min(sums))
        result[i].append(num)
        sums[i] += num
    return result

def traverse_list(sorted_list, optimal):
    result = []
    for num in sorted_list:
        result.append(num)
        if sum(result) > optimal:
            result.pop()
    return result

def algo2(orig_list, num_sublists):
    """Find the minimal variance of summed lists."""
    result = [[] for i in range(num_sublists)]
    optimal = sum(orig_list) / num_sublists
    remaining = list(reversed(sorted(orig_list)))
    for i in range(num_sublists):
        for num in remaining[:]:
            result[i].append(num)
            if sum(result[i]) > optimal:
                result[i].pop()
            else:
                remaining.remove(num)
    if remaining:
        # Check if empty
        result = algo1(remaining, num_sublists, result)
    return result

def find_optimal(orig_list, num_sublists):
    """Find the minimal variance of summed lists."""
    optimal = sum(orig_list) / num_sublists
    if max(orig_list) > optimal:
        # Choose fast but not ideal algorithm; ideal doesn't work on this list
        result = algo1(orig_list, num_sublists)
    else:
        # Choose slower algorithm that will have better results
        result = algo2(orig_list, num_sublists)
    return result

def num_sublists(orig_list):
    """Find the smallest division of a list into equally summed smaller lists."""
    total = sum(orig_list)
    max_num = max(orig_list)
    valid_lists = []
    for i in reversed(range(1, len(orig_list) + 1)):
        if max_num > total / i:
            continue
        poss_list = find_optimal(orig_list, i)
        for sublist in poss_list:
            if sum(sublist) != total / i:
                break
        else:
            valid_lists.append(i)
    return valid_lists

with open("list_data.json", "r") as f:
    all_lists = json.load(f)

all_results = []
for test in all_lists:
    result = find_optimal(test, 3)
    for sublist in result:
        sublist.sort()
    result.sort()
    all_results.append(result)

with open("alg_results.json", "w") as f:
    json.dump(all_results, f)

#list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#t00 = time.perf_counter()
#result1 = algo1(list1, 5)
#t01 = time.perf_counter()
#sums1 = [sum(result1[i]) for i in range(5)]
#t10 = time.perf_counter()
#result2 = algo2(list1, 5)
#t11 = time.perf_counter()
#sums2 = [sum(result2[i]) for i in range(5)]
#print("Algorithm 1:", result1)
#print("Algo 1 speed:", t01 - t00)
#print("Variance 1:", statistics.pvariance(sums1))
#print("Algorithm 2:", result2)
#print("Algo 2 speed:", t11 - t10)
#print("Variance 2:", statistics.pvariance(sums2))
