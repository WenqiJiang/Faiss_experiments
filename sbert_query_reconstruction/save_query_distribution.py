import pickle
import json
import numpy as np
from tqdm import tqdm
import scipy

with open('monthly_views_results_full.pickle', 'rb') as handle:
    results = pickle.load(handle)
    
print(f"The number of queries in the Natural Questions train split is: {len(results)}")
    
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
ids_404_responses = np.where(views_per_query_array == -1)
views_per_query_filtered = views_per_query_array[ids_non_404_responses]

print(f"After filtering the queries with no API response, the queryset is composed of {views_per_query_filtered.shape[0]} queries")
print("\nCalculating percentiles...")

# This could be made much faster but we only need to run it once so it should not be an issue
percentiles = [scipy.stats.percentileofscore(views_per_query_filtered, i) for i in tqdm(views_per_query_filtered)]

percentiles = np.array(percentiles)

print(f"The shape of the percentiles array is {percentiles.shape}")

print("\nSaving percentiles and ids of the queries that received a correct response from the API and those that did not")

with open('percentiles.npy', 'wb') as f:
    np.save(f, percentiles)
    
with open("ids_non_404_responses.npy", "wb") as f:
    np.save(f, ids_non_404_responses)
    
with open("ids_404_responses.npy", "wb") as f:
    np.save(f, ids_404_responses)

