from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape(),
)
template = env.get_template("prisioneros.ma.j2")

with open("prisioneros.ma", "w") as f:
    f.write(template.render(prisioners=list(range(5)), max_delay=4))
