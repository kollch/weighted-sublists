import random
import json

def make_list(length=10, min_num=0, max_num=100):
    return [random.randrange(min_num, max_num + 1) for i in range(length)]

all_results = []
for i in range(1000):
    all_results.append(make_list(random.randrange(3, 10)))
with open("list_data.json", "w") as f:
    json.dump(all_results, f)
