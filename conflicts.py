import pandas as pd
from tqdm import tqdm
from model.experiment_utils import sentences, delays, betrayal_probas
from plots import get_conflicts, search_experiment_results


def process(c,d,p):
    return pd.DataFrame([
        (len(get_conflicts(df)),c,d,p)
        for df in search_experiment_results(c, d, p)
    ], columns=['num', 'c', 'd', 'p'])


all_experiments = [
    (c,d,p)
    for c in sentences
    for d in delays
    for p in betrayal_probas
]

num_conflicts = pd.concat([process(c,d,p) for c,d,p in tqdm(all_experiments)])

num_conflicts.to_csv('conflicts.csv', index=False)
