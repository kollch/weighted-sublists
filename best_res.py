import statistics
import json
import math

with open("list_results.json", "r") as f:
    all_lists = json.load(f)

all_best_results = []
for results in all_lists:
    best_results = [0]
    best_var = math.inf
    for result in results:
        sums = [sum(result[i]) for i in range(3)]
        variance = statistics.pvariance(sums)
        if variance < best_var:
            #print("best_var =", best_var)
            best_var = variance
            best_results.clear()
            best_results.append(result)
            #print("variance =", variance)
            #print("best_results.append(result) -->", best_results)
        elif variance == best_var:
            best_results.append(result)
            #print("best_var =", best_var)
            #print("variance =", variance)
            #print("They have the same variance.")
            #print("best_results.append(result) -->", best_results)
    all_best_results.append(best_results)
    #print("all_best_results:", all_best_results)
    #break

with open("best_results.json", "w") as f:
    json.dump(all_best_results, f)
