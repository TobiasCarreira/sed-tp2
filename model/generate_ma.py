from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape(),
)
template = env.get_template("prisioneros.ma.j2")

sentences = [100, 1000, 5000]
delay = [(0,5), (0,10), (5,10), (10,20)]
betrayal_probas = ['randInt(4) = 0', 'randInt(1) = 0', 'randInt(4) != 0'] # [1/5, 1/2, 4/5]
prisioners_number = 5
# TODO: generar varios 'prisioneros.val' aleatorios

with open("prisioneros.ma", "w") as f:
    f.write(template.render(prisioners=list(range(prisioners_number)),
                            max_delay=4,
                            min_delay=0,
                            initial_values_file='prisioneros.val',
                            added_sentence=100,
                            betrayal_proba='randInt(1) = 0'))
