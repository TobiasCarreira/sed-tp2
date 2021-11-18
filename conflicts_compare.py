import pandas as pd
from tqdm import tqdm
from model.experiment_utils import sentences, delays, betrayal_probas, num_prisioners
from plots import get_conflicts, search_experiment_results


def compare(conflicts):
    num_buchoneado = [0] * num_prisoners
    num_buchonea = [0] * num_prisoners
    for conflict in conflicts:
	    num_buchoneado[conflict['buchoneado']] +=1
	    num_buchonea[conflict['buchon']] +=1
    return zip(num_buchoneado, num_buchonea)


def process(c,d,p):
    return pd.DataFrame([
        (buchoneado, buchonea, c, d, p)
        for df in search_experiment_results(c, d, p)
	    for buchoneado, buchonea in compare(get_conflicts(df))
    ], columns=['num', 'c', 'd', 'p'])


all_experiments = [
    (c,d,p)
    for c in sentences
    for d in delays
    for p in betrayal_probas
]

num_conflicts = pd.concat([process(c,d,p) for c,d,p in tqdm(all_experiments)])

num_conflicts.to_csv('conflicts.csv')
