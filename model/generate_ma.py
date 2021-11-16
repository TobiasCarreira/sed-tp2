from jinja2 import Environment, FileSystemLoader, select_autoescape
from random import randint, sample, normalvariate
import numpy as np

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape(),
)
ma_template = env.get_template("prisioneros.ma.j2")

sentences = [100, 1000, 5000]
delays = [(0,5), (0,10), (5,10), (10,20)]
betrayal_probas = ['randInt(4) = 0', 'randInt(1) = 0', 'randInt(4) != 0'] # [1/5, 1/2, 4/5]
num_prisioners = 30
num_runs = 15
width = 12


def random_prisoners(width, height, quantity, mean_initial_sentence=50, std_initial_sentence=10):
    positions = sample(list(np.ndindex((width, height))), quantity)
    return [
        dict(x=x, y=y, direction=randint(1,4), sentence=100*max(5, int(normalvariate(mean_initial_sentence, std_initial_sentence))))
        for x,y in positions
    ]

prisioners_template = env.get_template("prisioneros.val.j2")
for i in range(num_runs):
    with open(f"prisioneros.val.{i}", "w") as f:
        f.write(prisioners_template.render(prisioners=random_prisoners(width, width, num_prisioners)))

suffix=0
suffixes={}
for sentence in sentences:
    for delay in delays:
        for betrayal in betrayal_probas:
            min_delay, max_delay = delay
            for i in range(num_runs):

                with open(f"prisioneros.ma.{suffix}", "w") as f:
                    f.write(ma_template.render(prisioners=list(range(num_prisioners)),
                                            max_delay=max_delay,
                                            min_delay=min_delay,
                                            initial_values_file=f"prisioneros.val.{i}",
                                            added_sentence=sentence,
                                            betrayal_proba=betrayal,
                                            width=width,
                                            height=width))
                suffixes[suffix] = (sentence, delay, betrayal)
                suffix +=1

print(suffixes)

