import re
import pickle
from tqdm import tqdm
from datasets import load_dataset
from datasets import Dataset
import requests
from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession
from concurrent.futures import ThreadPoolExecutor

def extract_title(page_url):
    return re.search(r'title=(.*?)&amp;', page_url).group(1)

def gen_request_url_for_2021_views(page_url):

    title = extract_title(page_url)

    url = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{title}/monthly/2021010100/2021123100'

    return url

headers = {
        'User-Agent': 'Antonio Lopardo',
        'From': 'antonio.lopardo@outlook.com'  # This is another valid field
    }

dataset = Dataset.from_file("/mnt/scratch/alopardo/natural_questions/natural_questions-train.arrow")

with FuturesSession(executor=ThreadPoolExecutor(max_workers=32)) as session:
    futures = [session.get(gen_request_url_for_2021_views(dataset[i]['document']["url"]), headers=headers) for i in tqdm(range(len(dataset)))]
    for future in as_completed(futures):
        resp = future.result()
        
results = [future.result().text for future in futures]

with open('monthly_views_results_full.pickle', 'wb') as handle:
    pickle.dump(results, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
