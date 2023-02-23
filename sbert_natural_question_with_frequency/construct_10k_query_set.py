import pickle
import json
import numpy as np

from datasets import load_dataset
from datasets import Dataset


with open('monthly_views_results_full.pickle', 'rb') as handle:
    results = pickle.load(handle)

print(f"The number of queries in the Natural Questions train split is: {len(results)}")


# question entries: dataset[i]['question']['text']
dataset = Dataset.from_file("/mnt/scratch/alopardo/natural_questions/natural_questions-train.arrow")
print("finished loading the dataset")

def get_total_views(result):
    json_results = json.loads(result)
    try:
        monthly_views = [item["views"] for item in json_results["items"]]
    except:
        monthly_views = [-1] # for 404 responses
    
    return sum(monthly_views)

total_views_per_query = [get_total_views(results[i]) for i in range(len(results))]
views_per_query_array = np.array(total_views_per_query)
ids_non_404_responses = np.where(views_per_query_array != -1)
ids_non_404_responses_array = np.where(views_per_query_array != -1)[0]
views_per_query_filtered = views_per_query_array[ids_non_404_responses]
total_views = sum(views_per_query_filtered)
view_percentile = views_per_query_filtered / total_views
assert view_percentile.shape[0] == ids_non_404_responses_array.shape[0]

percentile_id_array = [(view_percentile[i], ids_non_404_responses_array[i]) for i in range(view_percentile.shape[0])]
percentile_id_array_sorted = sorted(percentile_id_array, reverse=True)

# reconstruct 10k queries
nq = 10 * 1000
count = 0
ids = []
for percentile, id in percentile_id_array_sorted:
    query_count = int(percentile * nq)
    if query_count > 0:
        ids += [id] * query_count
        count += query_count
    else: # < 1 count as 1
        ids += [id] 
        count += 1
    if count == nq:
        break

np.random.seed(123)
np.random.shuffle(ids)

result_queries = [] # list of dict
for i, id in enumerate(ids):
    q = dict()
    q["id"] = int(i)
    q["query"] = dataset[int(id)]['question']['text']
    result_queries.append(q)
    print(q)

fname = "sbert_query_reconstructed.jsonl"
with open(fname, 'w') as f:
    for query in result_queries:
        json.dump(query, f)
        f.write('\n')