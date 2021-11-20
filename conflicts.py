import pandas as pd
from tqdm import tqdm
from model.experiment_utils import sentences, delays, betrayal_probas
from plots import get_conflicts, search_experiment_results


def process(c, d, p):
    return pd.DataFrame(
        [
            (len(get_conflicts(df)), c, d, p)
            for df in search_experiment_results(c, d, p)
        ],
        columns=["num", "c", "d", "p"],
    )


all_experiments = [
    (c, d, p) for c in sentences for d in delays for p in betrayal_probas
]

all_conflicts = {
    experiment: pd.DataFrame(
        [
            c
            for df in tqdm(search_experiment_results(*experiment))
            for c in get_conflicts(df)
        ],
        columns=["buchoneado", "buchon", "time"],
    )
    for experiment in all_experiments
}

# num_conflicts.to_csv('conflicts.csv', index=False)

for experiment, conflicts in all_conflicts.items():
    conflicts["experiment"] = str(experiment)
    conflicts["sentence"] = str(experiment[0])
    conflicts["delay"] = str(experiment[1])
    conflicts["betrayal"] = str(experiment[2])
    conflicts["normalized_time"] = (conflicts.time - conflicts.time.min()) / (conflicts.time.max() - conflicts.time.min())

all_conflicts_df = pd.concat(all_conflicts.values())
all_conflicts_df.to_csv("all_conflicts.csv")