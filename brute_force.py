import json

def rec_num_elements(old_nums, curr, n, results):
    num_sublists = len(old_nums)
    if curr == num_sublists - 1:
        results.append(old_nums.copy())
        return
    nums = old_nums.copy()
    total_to_curr = sum(nums[:curr])
    while nums[curr] * (num_sublists - curr) + total_to_curr >= n:
        if nums[curr] >= (n - total_to_curr) // 2:
            nums[curr + 1] = n - total_to_curr - nums[curr] - num_sublists + curr + 2
        else:
            nums[curr + 1] = nums[curr]
        rec_num_elements(nums, curr + 1, n, results)
        nums[curr] -= 1

def num_elements5(n, num_sublists):
    results = []
    nums = [0 for i in range(num_sublists)]
    nums[0] = n - num_sublists + 1
    rec_num_elements(nums, 0, n, results)
    return results

def rec_poss(result, nums, num_sublists, index, curr_els, scen, results):
    for i in range(num_sublists):
        if curr_els[i] == scen[i]:
            continue
        result[i].append(nums[index])
        curr_els[i] += 1
        if index != len(nums) - 1:
            rec_poss(result, nums, num_sublists, index + 1, curr_els, scen, results)
        else:
            results.append([sublist.copy() for sublist in result])
        result[i].pop()
        curr_els[i] -= 1

def poss_comb(scens, nums):
    results = []
    num_sublists = len(scens[0])
    if len(nums) == 0:
        return [[] for i in range(num_sublists)]
    elif len(nums) == 1:
        result = [[] for i in range(num_sublists)]
        result[0].append(nums[0])
        return result
    for scen in scens:
        curr_els = [0 for i in range(num_sublists)]
        result = [[] for i in range(num_sublists)]
        rec_poss(result, nums, num_sublists, 0, curr_els, scen, results)
    rm_dups(results)
    return results

def rm_dups(results):
    for result in results:
        result.sort()
    results.sort()
    for_del = []
    for i in range(len(results) - 1):
        if results[i] == results[i + 1]:
            for_del.append(i)
    for i in reversed(for_del):
        results.pop(i)

with open("list_data.json", "r") as f:
    all_lists = json.load(f)

all_results = []
for test in all_lists:
    test.sort()
    #print(str(10) + ":")
    scens = num_elements5(len(test), 3)
    #for i, scen in enumerate(scens):
    #    print('{0:3d}: [{1:2d}, {2:2d}, {3:2d}]'.format(i + 1, scen[0], scen[1], scen[2]))
    #print("")
    results = poss_comb(scens, test)
    #for i, result in enumerate(results):
    #    print(i + 1, result)
    all_results.append(results)

with open("list_results.json", "w") as f:
    json.dump(all_results, f)
