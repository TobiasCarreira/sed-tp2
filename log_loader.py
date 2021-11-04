import pandas as pd
import re

TIME_COL = 'time'
PORT_COL = 'port'
VALUE_COL = 'value'
MESSAGE_TYPE_COL = 'message_type'
MODEL_ORIGIN_COL = 'model_origin'
MODEL_DEST_COL = 'model_dest'
COORDS_COL = 'coords'

coords_regex = re.compile('personas\((?P<x_coord>\d+),(?P<y_coord>\d+)\)\(\d+\)')

# parsea cada fila del dataframe
def parse_value(value: str):
    is_list = value.strip().startswith("[") and value.strip().endswith("]")
    if is_list:
        return tuple(int(float(num)) for num in value.replace('[', '').replace(']', '').split(', '))
    return int(float(value))


# conversion VTime a int
def time_to_secs(time):
    h, m, s, ms, r = time.split(':')
    return int(h)*60*60*1000 + int(m)*60*1000 + int(s) * 1000 + int(ms) + int(r)


def get_coords(model):
    d = coords_regex.match(model).groupdict()
    return int(d['x_coord']), int(d['y_coord'])


def load_log(filename):
    df_converters = {
        # VALUE_COL: parse_value,
        TIME_COL: time_to_secs
    }
    df = pd.read_csv(filename,
                delimiter=r' /\s+',
                engine='python',  # C engine doesnt work for regex
                converters=df_converters,
                names=[0, 1,  # Not sure what first two cols are
                       MESSAGE_TYPE_COL,
                       TIME_COL,
                       MODEL_ORIGIN_COL,
                       PORT_COL,
                       VALUE_COL,
                       MODEL_DEST_COL])
    df = df.loc[df[MESSAGE_TYPE_COL] == 'Y', [TIME_COL, MODEL_ORIGIN_COL, VALUE_COL]]
    df[VALUE_COL] = df[VALUE_COL].apply(parse_value)
    df[MODEL_ORIGIN_COL] = df[MODEL_ORIGIN_COL].apply(get_coords)
    return df.rename(columns={MODEL_ORIGIN_COL: COORDS_COL})
