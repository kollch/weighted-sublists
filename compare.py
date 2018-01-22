import statistics
import time
import json

with open("best_results.json", "r") as f:
    brute_force = json.load(f)

with open("alg_results.json", "r") as f:
    alg_res = json.load(f)

correct = 0
variance_diff = 0
serious_bug = 0
for i, results in enumerate(brute_force):
    if alg_res[i] in results:
        print(str(i + 1) + ": Success! They match!")
        correct += 1
    else:
        print(str(i + 1) + ": They don't match.")
        force_sums = [sum(results[0][j]) for j in range(3)]
        force_var = statistics.pvariance(force_sums)
        alg_sums = [sum(alg_res[i][j]) for j in range(3)]
        alg_var = statistics.pvariance(alg_sums)
        print("Brute force:", results)
        print("Algorithm   :", alg_res[i])
        print("Brute force variance:", force_var)
        print("Algorithm variance  :", alg_var)
        if force_var > alg_var:
            serious_bug += 1
        variance_diff += alg_var - force_var
avg_var_diff = variance_diff / (len(brute_force) - correct)
print("Total right:", correct)
print("Total:", len(brute_force))
print("% correct:", correct / len(brute_force) * 100)
print("Avg difference in variance:", avg_var_diff)
