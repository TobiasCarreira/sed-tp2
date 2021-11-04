from log_loader import load_log, TIME_COL, VALUE_COL, COORDS_COL
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_size = 10
y_size = 10

direction_to_unicode = {
    1: u'\u2192',
    2: u'\u2193',
    3: u'\u2190',
    4: u'\u2191'
}

# TODO: hacer lo mismo para conseguir direcciones y tiempos, pensar si hacer diccionario de id_agente a los otros datos
def get_agents(df, time):
    timed_df = df[df[TIME_COL] == time]
    agents = np.zeros((x_size, y_size), dtype=int)
    directions = {}
    life_time = {}
    for _, row in timed_df.iterrows():
        x, y = row[COORDS_COL]
        val = row[VALUE_COL]
        if val != 0:
            i, d, t = val
            agents[x, y] = i
            directions[i] = d
            life_time[i] = t
    return agents, directions, life_time


def plot_agents(data):
    agents, directions, life_time = data
    # print(data)

    plt.axes().clear()
    pc = plt.pcolor(agents, cmap='Dark2', edgecolors='k', linewidths=1)
    pc.update_scalarmappable()

    plt.xticks([])
    plt.yticks([])

    ax = pc.axes
    ax.invert_yaxis()

    for p, color, value in zip(pc.get_paths(), pc.get_facecolors(), pc.get_array()):
        if value > 0:
            x, y = p.vertices[:-2, :].mean(0)
            if np.all(color[:3] > 0.5):
                color = (0.0, 0.0, 0.0)
            else:
                color = (1.0, 1.0, 1.0)
            direction = directions[value]
            text = f'{value}\n{direction_to_unicode[direction]}\n{life_time[value]}'
            ax.text(x, y, text, ha="center", va="center", color=color, fontsize='x-large')


if __name__ == '__main__':
    df = load_log('model/log/log.log01')
    frames = [get_agents(df, time) for time in df['time'].unique()]

    fig = plt.figure(figsize=(10, 10))
    anim = FuncAnimation(fig, plot_agents, frames=frames, interval=500)
    anim.save('animation.mp4', writer='imagemagick')
