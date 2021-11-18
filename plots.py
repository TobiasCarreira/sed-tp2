from log_loader import load_log, TIME_COL, VALUE_COL, COORDS_COL
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

x_size = 12
y_size = 12

direction_to_unicode = {1: "\u2192", 2: "\u2193", 3: "\u2190", 4: "\u2191"}
direction_cell = {1:(0,1), 2:(1,0), 3:(0,-1), 4:(-1,0)}


def next_cell(cell, direction):
    x,y = cell
    dx,dy = direction_cell[direction]
    return ((x+dx) % x_size, (y+dy) % y_size)


log_index = {
    0: (100, (0, 5), "randInt(4) = 0"),
    1: (100, (0, 5), "randInt(4) = 0"),
    2: (100, (0, 5), "randInt(4) = 0"),
    3: (100, (0, 5), "randInt(4) = 0"),
    4: (100, (0, 5), "randInt(4) = 0"),
    5: (100, (0, 5), "randInt(4) = 0"),
    6: (100, (0, 5), "randInt(4) = 0"),
    7: (100, (0, 5), "randInt(4) = 0"),
    8: (100, (0, 5), "randInt(4) = 0"),
    9: (100, (0, 5), "randInt(4) = 0"),
    10: (100, (0, 5), "randInt(4) = 0"),
    11: (100, (0, 5), "randInt(4) = 0"),
    12: (100, (0, 5), "randInt(4) = 0"),
    13: (100, (0, 5), "randInt(4) = 0"),
    14: (100, (0, 5), "randInt(4) = 0"),
    15: (100, (0, 5), "randInt(1) = 0"),
    16: (100, (0, 5), "randInt(1) = 0"),
    17: (100, (0, 5), "randInt(1) = 0"),
    18: (100, (0, 5), "randInt(1) = 0"),
    19: (100, (0, 5), "randInt(1) = 0"),
    20: (100, (0, 5), "randInt(1) = 0"),
    21: (100, (0, 5), "randInt(1) = 0"),
    22: (100, (0, 5), "randInt(1) = 0"),
    23: (100, (0, 5), "randInt(1) = 0"),
    24: (100, (0, 5), "randInt(1) = 0"),
    25: (100, (0, 5), "randInt(1) = 0"),
    26: (100, (0, 5), "randInt(1) = 0"),
    27: (100, (0, 5), "randInt(1) = 0"),
    28: (100, (0, 5), "randInt(1) = 0"),
    29: (100, (0, 5), "randInt(1) = 0"),
    30: (100, (0, 5), "randInt(4) != 0"),
    31: (100, (0, 5), "randInt(4) != 0"),
    32: (100, (0, 5), "randInt(4) != 0"),
    33: (100, (0, 5), "randInt(4) != 0"),
    34: (100, (0, 5), "randInt(4) != 0"),
    35: (100, (0, 5), "randInt(4) != 0"),
    36: (100, (0, 5), "randInt(4) != 0"),
    37: (100, (0, 5), "randInt(4) != 0"),
    38: (100, (0, 5), "randInt(4) != 0"),
    39: (100, (0, 5), "randInt(4) != 0"),
    40: (100, (0, 5), "randInt(4) != 0"),
    41: (100, (0, 5), "randInt(4) != 0"),
    42: (100, (0, 5), "randInt(4) != 0"),
    43: (100, (0, 5), "randInt(4) != 0"),
    44: (100, (0, 5), "randInt(4) != 0"),
    45: (100, (0, 10), "randInt(4) = 0"),
    46: (100, (0, 10), "randInt(4) = 0"),
    47: (100, (0, 10), "randInt(4) = 0"),
    48: (100, (0, 10), "randInt(4) = 0"),
    49: (100, (0, 10), "randInt(4) = 0"),
    50: (100, (0, 10), "randInt(4) = 0"),
    51: (100, (0, 10), "randInt(4) = 0"),
    52: (100, (0, 10), "randInt(4) = 0"),
    53: (100, (0, 10), "randInt(4) = 0"),
    54: (100, (0, 10), "randInt(4) = 0"),
    55: (100, (0, 10), "randInt(4) = 0"),
    56: (100, (0, 10), "randInt(4) = 0"),
    57: (100, (0, 10), "randInt(4) = 0"),
    58: (100, (0, 10), "randInt(4) = 0"),
    59: (100, (0, 10), "randInt(4) = 0"),
    60: (100, (0, 10), "randInt(1) = 0"),
    61: (100, (0, 10), "randInt(1) = 0"),
    62: (100, (0, 10), "randInt(1) = 0"),
    63: (100, (0, 10), "randInt(1) = 0"),
    64: (100, (0, 10), "randInt(1) = 0"),
    65: (100, (0, 10), "randInt(1) = 0"),
    66: (100, (0, 10), "randInt(1) = 0"),
    67: (100, (0, 10), "randInt(1) = 0"),
    68: (100, (0, 10), "randInt(1) = 0"),
    69: (100, (0, 10), "randInt(1) = 0"),
    70: (100, (0, 10), "randInt(1) = 0"),
    71: (100, (0, 10), "randInt(1) = 0"),
    72: (100, (0, 10), "randInt(1) = 0"),
    73: (100, (0, 10), "randInt(1) = 0"),
    74: (100, (0, 10), "randInt(1) = 0"),
    75: (100, (0, 10), "randInt(4) != 0"),
    76: (100, (0, 10), "randInt(4) != 0"),
    77: (100, (0, 10), "randInt(4) != 0"),
    78: (100, (0, 10), "randInt(4) != 0"),
    79: (100, (0, 10), "randInt(4) != 0"),
    80: (100, (0, 10), "randInt(4) != 0"),
    81: (100, (0, 10), "randInt(4) != 0"),
    82: (100, (0, 10), "randInt(4) != 0"),
    83: (100, (0, 10), "randInt(4) != 0"),
    84: (100, (0, 10), "randInt(4) != 0"),
    85: (100, (0, 10), "randInt(4) != 0"),
    86: (100, (0, 10), "randInt(4) != 0"),
    87: (100, (0, 10), "randInt(4) != 0"),
    88: (100, (0, 10), "randInt(4) != 0"),
    89: (100, (0, 10), "randInt(4) != 0"),
    90: (100, (5, 10), "randInt(4) = 0"),
    91: (100, (5, 10), "randInt(4) = 0"),
    92: (100, (5, 10), "randInt(4) = 0"),
    93: (100, (5, 10), "randInt(4) = 0"),
    94: (100, (5, 10), "randInt(4) = 0"),
    95: (100, (5, 10), "randInt(4) = 0"),
    96: (100, (5, 10), "randInt(4) = 0"),
    97: (100, (5, 10), "randInt(4) = 0"),
    98: (100, (5, 10), "randInt(4) = 0"),
    99: (100, (5, 10), "randInt(4) = 0"),
    100: (100, (5, 10), "randInt(4) = 0"),
    101: (100, (5, 10), "randInt(4) = 0"),
    102: (100, (5, 10), "randInt(4) = 0"),
    103: (100, (5, 10), "randInt(4) = 0"),
    104: (100, (5, 10), "randInt(4) = 0"),
    105: (100, (5, 10), "randInt(1) = 0"),
    106: (100, (5, 10), "randInt(1) = 0"),
    107: (100, (5, 10), "randInt(1) = 0"),
    108: (100, (5, 10), "randInt(1) = 0"),
    109: (100, (5, 10), "randInt(1) = 0"),
    110: (100, (5, 10), "randInt(1) = 0"),
    111: (100, (5, 10), "randInt(1) = 0"),
    112: (100, (5, 10), "randInt(1) = 0"),
    113: (100, (5, 10), "randInt(1) = 0"),
    114: (100, (5, 10), "randInt(1) = 0"),
    115: (100, (5, 10), "randInt(1) = 0"),
    116: (100, (5, 10), "randInt(1) = 0"),
    117: (100, (5, 10), "randInt(1) = 0"),
    118: (100, (5, 10), "randInt(1) = 0"),
    119: (100, (5, 10), "randInt(1) = 0"),
    120: (100, (5, 10), "randInt(4) != 0"),
    121: (100, (5, 10), "randInt(4) != 0"),
    122: (100, (5, 10), "randInt(4) != 0"),
    123: (100, (5, 10), "randInt(4) != 0"),
    124: (100, (5, 10), "randInt(4) != 0"),
    125: (100, (5, 10), "randInt(4) != 0"),
    126: (100, (5, 10), "randInt(4) != 0"),
    127: (100, (5, 10), "randInt(4) != 0"),
    128: (100, (5, 10), "randInt(4) != 0"),
    129: (100, (5, 10), "randInt(4) != 0"),
    130: (100, (5, 10), "randInt(4) != 0"),
    131: (100, (5, 10), "randInt(4) != 0"),
    132: (100, (5, 10), "randInt(4) != 0"),
    133: (100, (5, 10), "randInt(4) != 0"),
    134: (100, (5, 10), "randInt(4) != 0"),
    135: (100, (10, 20), "randInt(4) = 0"),
    136: (100, (10, 20), "randInt(4) = 0"),
    137: (100, (10, 20), "randInt(4) = 0"),
    138: (100, (10, 20), "randInt(4) = 0"),
    139: (100, (10, 20), "randInt(4) = 0"),
    140: (100, (10, 20), "randInt(4) = 0"),
    141: (100, (10, 20), "randInt(4) = 0"),
    142: (100, (10, 20), "randInt(4) = 0"),
    143: (100, (10, 20), "randInt(4) = 0"),
    144: (100, (10, 20), "randInt(4) = 0"),
    145: (100, (10, 20), "randInt(4) = 0"),
    146: (100, (10, 20), "randInt(4) = 0"),
    147: (100, (10, 20), "randInt(4) = 0"),
    148: (100, (10, 20), "randInt(4) = 0"),
    149: (100, (10, 20), "randInt(4) = 0"),
    150: (100, (10, 20), "randInt(1) = 0"),
    151: (100, (10, 20), "randInt(1) = 0"),
    152: (100, (10, 20), "randInt(1) = 0"),
    153: (100, (10, 20), "randInt(1) = 0"),
    154: (100, (10, 20), "randInt(1) = 0"),
    155: (100, (10, 20), "randInt(1) = 0"),
    156: (100, (10, 20), "randInt(1) = 0"),
    157: (100, (10, 20), "randInt(1) = 0"),
    158: (100, (10, 20), "randInt(1) = 0"),
    159: (100, (10, 20), "randInt(1) = 0"),
    160: (100, (10, 20), "randInt(1) = 0"),
    161: (100, (10, 20), "randInt(1) = 0"),
    162: (100, (10, 20), "randInt(1) = 0"),
    163: (100, (10, 20), "randInt(1) = 0"),
    164: (100, (10, 20), "randInt(1) = 0"),
    165: (100, (10, 20), "randInt(4) != 0"),
    166: (100, (10, 20), "randInt(4) != 0"),
    167: (100, (10, 20), "randInt(4) != 0"),
    168: (100, (10, 20), "randInt(4) != 0"),
    169: (100, (10, 20), "randInt(4) != 0"),
    170: (100, (10, 20), "randInt(4) != 0"),
    171: (100, (10, 20), "randInt(4) != 0"),
    172: (100, (10, 20), "randInt(4) != 0"),
    173: (100, (10, 20), "randInt(4) != 0"),
    174: (100, (10, 20), "randInt(4) != 0"),
    175: (100, (10, 20), "randInt(4) != 0"),
    176: (100, (10, 20), "randInt(4) != 0"),
    177: (100, (10, 20), "randInt(4) != 0"),
    178: (100, (10, 20), "randInt(4) != 0"),
    179: (100, (10, 20), "randInt(4) != 0"),
    180: (1000, (0, 5), "randInt(4) = 0"),
    181: (1000, (0, 5), "randInt(4) = 0"),
    182: (1000, (0, 5), "randInt(4) = 0"),
    183: (1000, (0, 5), "randInt(4) = 0"),
    184: (1000, (0, 5), "randInt(4) = 0"),
    185: (1000, (0, 5), "randInt(4) = 0"),
    186: (1000, (0, 5), "randInt(4) = 0"),
    187: (1000, (0, 5), "randInt(4) = 0"),
    188: (1000, (0, 5), "randInt(4) = 0"),
    189: (1000, (0, 5), "randInt(4) = 0"),
    190: (1000, (0, 5), "randInt(4) = 0"),
    191: (1000, (0, 5), "randInt(4) = 0"),
    192: (1000, (0, 5), "randInt(4) = 0"),
    193: (1000, (0, 5), "randInt(4) = 0"),
    194: (1000, (0, 5), "randInt(4) = 0"),
    195: (1000, (0, 5), "randInt(1) = 0"),
    196: (1000, (0, 5), "randInt(1) = 0"),
    197: (1000, (0, 5), "randInt(1) = 0"),
    198: (1000, (0, 5), "randInt(1) = 0"),
    199: (1000, (0, 5), "randInt(1) = 0"),
    200: (1000, (0, 5), "randInt(1) = 0"),
    201: (1000, (0, 5), "randInt(1) = 0"),
    202: (1000, (0, 5), "randInt(1) = 0"),
    203: (1000, (0, 5), "randInt(1) = 0"),
    204: (1000, (0, 5), "randInt(1) = 0"),
    205: (1000, (0, 5), "randInt(1) = 0"),
    206: (1000, (0, 5), "randInt(1) = 0"),
    207: (1000, (0, 5), "randInt(1) = 0"),
    208: (1000, (0, 5), "randInt(1) = 0"),
    209: (1000, (0, 5), "randInt(1) = 0"),
    210: (1000, (0, 5), "randInt(4) != 0"),
    211: (1000, (0, 5), "randInt(4) != 0"),
    212: (1000, (0, 5), "randInt(4) != 0"),
    213: (1000, (0, 5), "randInt(4) != 0"),
    214: (1000, (0, 5), "randInt(4) != 0"),
    215: (1000, (0, 5), "randInt(4) != 0"),
    216: (1000, (0, 5), "randInt(4) != 0"),
    217: (1000, (0, 5), "randInt(4) != 0"),
    218: (1000, (0, 5), "randInt(4) != 0"),
    219: (1000, (0, 5), "randInt(4) != 0"),
    220: (1000, (0, 5), "randInt(4) != 0"),
    221: (1000, (0, 5), "randInt(4) != 0"),
    222: (1000, (0, 5), "randInt(4) != 0"),
    223: (1000, (0, 5), "randInt(4) != 0"),
    224: (1000, (0, 5), "randInt(4) != 0"),
    225: (1000, (0, 10), "randInt(4) = 0"),
    226: (1000, (0, 10), "randInt(4) = 0"),
    227: (1000, (0, 10), "randInt(4) = 0"),
    228: (1000, (0, 10), "randInt(4) = 0"),
    229: (1000, (0, 10), "randInt(4) = 0"),
    230: (1000, (0, 10), "randInt(4) = 0"),
    231: (1000, (0, 10), "randInt(4) = 0"),
    232: (1000, (0, 10), "randInt(4) = 0"),
    233: (1000, (0, 10), "randInt(4) = 0"),
    234: (1000, (0, 10), "randInt(4) = 0"),
    235: (1000, (0, 10), "randInt(4) = 0"),
    236: (1000, (0, 10), "randInt(4) = 0"),
    237: (1000, (0, 10), "randInt(4) = 0"),
    238: (1000, (0, 10), "randInt(4) = 0"),
    239: (1000, (0, 10), "randInt(4) = 0"),
    240: (1000, (0, 10), "randInt(1) = 0"),
    241: (1000, (0, 10), "randInt(1) = 0"),
    242: (1000, (0, 10), "randInt(1) = 0"),
    243: (1000, (0, 10), "randInt(1) = 0"),
    244: (1000, (0, 10), "randInt(1) = 0"),
    245: (1000, (0, 10), "randInt(1) = 0"),
    246: (1000, (0, 10), "randInt(1) = 0"),
    247: (1000, (0, 10), "randInt(1) = 0"),
    248: (1000, (0, 10), "randInt(1) = 0"),
    249: (1000, (0, 10), "randInt(1) = 0"),
    250: (1000, (0, 10), "randInt(1) = 0"),
    251: (1000, (0, 10), "randInt(1) = 0"),
    252: (1000, (0, 10), "randInt(1) = 0"),
    253: (1000, (0, 10), "randInt(1) = 0"),
    254: (1000, (0, 10), "randInt(1) = 0"),
    255: (1000, (0, 10), "randInt(4) != 0"),
    256: (1000, (0, 10), "randInt(4) != 0"),
    257: (1000, (0, 10), "randInt(4) != 0"),
    258: (1000, (0, 10), "randInt(4) != 0"),
    259: (1000, (0, 10), "randInt(4) != 0"),
    260: (1000, (0, 10), "randInt(4) != 0"),
    261: (1000, (0, 10), "randInt(4) != 0"),
    262: (1000, (0, 10), "randInt(4) != 0"),
    263: (1000, (0, 10), "randInt(4) != 0"),
    264: (1000, (0, 10), "randInt(4) != 0"),
    265: (1000, (0, 10), "randInt(4) != 0"),
    266: (1000, (0, 10), "randInt(4) != 0"),
    267: (1000, (0, 10), "randInt(4) != 0"),
    268: (1000, (0, 10), "randInt(4) != 0"),
    269: (1000, (0, 10), "randInt(4) != 0"),
    270: (1000, (5, 10), "randInt(4) = 0"),
    271: (1000, (5, 10), "randInt(4) = 0"),
    272: (1000, (5, 10), "randInt(4) = 0"),
    273: (1000, (5, 10), "randInt(4) = 0"),
    274: (1000, (5, 10), "randInt(4) = 0"),
    275: (1000, (5, 10), "randInt(4) = 0"),
    276: (1000, (5, 10), "randInt(4) = 0"),
    277: (1000, (5, 10), "randInt(4) = 0"),
    278: (1000, (5, 10), "randInt(4) = 0"),
    279: (1000, (5, 10), "randInt(4) = 0"),
    280: (1000, (5, 10), "randInt(4) = 0"),
    281: (1000, (5, 10), "randInt(4) = 0"),
    282: (1000, (5, 10), "randInt(4) = 0"),
    283: (1000, (5, 10), "randInt(4) = 0"),
    284: (1000, (5, 10), "randInt(4) = 0"),
    285: (1000, (5, 10), "randInt(1) = 0"),
    286: (1000, (5, 10), "randInt(1) = 0"),
    287: (1000, (5, 10), "randInt(1) = 0"),
    288: (1000, (5, 10), "randInt(1) = 0"),
    289: (1000, (5, 10), "randInt(1) = 0"),
    290: (1000, (5, 10), "randInt(1) = 0"),
    291: (1000, (5, 10), "randInt(1) = 0"),
    292: (1000, (5, 10), "randInt(1) = 0"),
    293: (1000, (5, 10), "randInt(1) = 0"),
    294: (1000, (5, 10), "randInt(1) = 0"),
    295: (1000, (5, 10), "randInt(1) = 0"),
    296: (1000, (5, 10), "randInt(1) = 0"),
    297: (1000, (5, 10), "randInt(1) = 0"),
    298: (1000, (5, 10), "randInt(1) = 0"),
    299: (1000, (5, 10), "randInt(1) = 0"),
    300: (1000, (5, 10), "randInt(4) != 0"),
    301: (1000, (5, 10), "randInt(4) != 0"),
    302: (1000, (5, 10), "randInt(4) != 0"),
    303: (1000, (5, 10), "randInt(4) != 0"),
    304: (1000, (5, 10), "randInt(4) != 0"),
    305: (1000, (5, 10), "randInt(4) != 0"),
    306: (1000, (5, 10), "randInt(4) != 0"),
    307: (1000, (5, 10), "randInt(4) != 0"),
    308: (1000, (5, 10), "randInt(4) != 0"),
    309: (1000, (5, 10), "randInt(4) != 0"),
    310: (1000, (5, 10), "randInt(4) != 0"),
    311: (1000, (5, 10), "randInt(4) != 0"),
    312: (1000, (5, 10), "randInt(4) != 0"),
    313: (1000, (5, 10), "randInt(4) != 0"),
    314: (1000, (5, 10), "randInt(4) != 0"),
    315: (1000, (10, 20), "randInt(4) = 0"),
    316: (1000, (10, 20), "randInt(4) = 0"),
    317: (1000, (10, 20), "randInt(4) = 0"),
    318: (1000, (10, 20), "randInt(4) = 0"),
    319: (1000, (10, 20), "randInt(4) = 0"),
    320: (1000, (10, 20), "randInt(4) = 0"),
    321: (1000, (10, 20), "randInt(4) = 0"),
    322: (1000, (10, 20), "randInt(4) = 0"),
    323: (1000, (10, 20), "randInt(4) = 0"),
    324: (1000, (10, 20), "randInt(4) = 0"),
    325: (1000, (10, 20), "randInt(4) = 0"),
    326: (1000, (10, 20), "randInt(4) = 0"),
    327: (1000, (10, 20), "randInt(4) = 0"),
    328: (1000, (10, 20), "randInt(4) = 0"),
    329: (1000, (10, 20), "randInt(4) = 0"),
    330: (1000, (10, 20), "randInt(1) = 0"),
    331: (1000, (10, 20), "randInt(1) = 0"),
    332: (1000, (10, 20), "randInt(1) = 0"),
    333: (1000, (10, 20), "randInt(1) = 0"),
    334: (1000, (10, 20), "randInt(1) = 0"),
    335: (1000, (10, 20), "randInt(1) = 0"),
    336: (1000, (10, 20), "randInt(1) = 0"),
    337: (1000, (10, 20), "randInt(1) = 0"),
    338: (1000, (10, 20), "randInt(1) = 0"),
    339: (1000, (10, 20), "randInt(1) = 0"),
    340: (1000, (10, 20), "randInt(1) = 0"),
    341: (1000, (10, 20), "randInt(1) = 0"),
    342: (1000, (10, 20), "randInt(1) = 0"),
    343: (1000, (10, 20), "randInt(1) = 0"),
    344: (1000, (10, 20), "randInt(1) = 0"),
    345: (1000, (10, 20), "randInt(4) != 0"),
    346: (1000, (10, 20), "randInt(4) != 0"),
    347: (1000, (10, 20), "randInt(4) != 0"),
    348: (1000, (10, 20), "randInt(4) != 0"),
    349: (1000, (10, 20), "randInt(4) != 0"),
    350: (1000, (10, 20), "randInt(4) != 0"),
    351: (1000, (10, 20), "randInt(4) != 0"),
    352: (1000, (10, 20), "randInt(4) != 0"),
    353: (1000, (10, 20), "randInt(4) != 0"),
    354: (1000, (10, 20), "randInt(4) != 0"),
    355: (1000, (10, 20), "randInt(4) != 0"),
    356: (1000, (10, 20), "randInt(4) != 0"),
    357: (1000, (10, 20), "randInt(4) != 0"),
    358: (1000, (10, 20), "randInt(4) != 0"),
    359: (1000, (10, 20), "randInt(4) != 0"),
    360: (5000, (0, 5), "randInt(4) = 0"),
    361: (5000, (0, 5), "randInt(4) = 0"),
    362: (5000, (0, 5), "randInt(4) = 0"),
    363: (5000, (0, 5), "randInt(4) = 0"),
    364: (5000, (0, 5), "randInt(4) = 0"),
    365: (5000, (0, 5), "randInt(4) = 0"),
    366: (5000, (0, 5), "randInt(4) = 0"),
    367: (5000, (0, 5), "randInt(4) = 0"),
    368: (5000, (0, 5), "randInt(4) = 0"),
    369: (5000, (0, 5), "randInt(4) = 0"),
    370: (5000, (0, 5), "randInt(4) = 0"),
    371: (5000, (0, 5), "randInt(4) = 0"),
    372: (5000, (0, 5), "randInt(4) = 0"),
    373: (5000, (0, 5), "randInt(4) = 0"),
    374: (5000, (0, 5), "randInt(4) = 0"),
    375: (5000, (0, 5), "randInt(1) = 0"),
    376: (5000, (0, 5), "randInt(1) = 0"),
    377: (5000, (0, 5), "randInt(1) = 0"),
    378: (5000, (0, 5), "randInt(1) = 0"),
    379: (5000, (0, 5), "randInt(1) = 0"),
    380: (5000, (0, 5), "randInt(1) = 0"),
    381: (5000, (0, 5), "randInt(1) = 0"),
    382: (5000, (0, 5), "randInt(1) = 0"),
    383: (5000, (0, 5), "randInt(1) = 0"),
    384: (5000, (0, 5), "randInt(1) = 0"),
    385: (5000, (0, 5), "randInt(1) = 0"),
    386: (5000, (0, 5), "randInt(1) = 0"),
    387: (5000, (0, 5), "randInt(1) = 0"),
    388: (5000, (0, 5), "randInt(1) = 0"),
    389: (5000, (0, 5), "randInt(1) = 0"),
    390: (5000, (0, 5), "randInt(4) != 0"),
    391: (5000, (0, 5), "randInt(4) != 0"),
    392: (5000, (0, 5), "randInt(4) != 0"),
    393: (5000, (0, 5), "randInt(4) != 0"),
    394: (5000, (0, 5), "randInt(4) != 0"),
    395: (5000, (0, 5), "randInt(4) != 0"),
    396: (5000, (0, 5), "randInt(4) != 0"),
    397: (5000, (0, 5), "randInt(4) != 0"),
    398: (5000, (0, 5), "randInt(4) != 0"),
    399: (5000, (0, 5), "randInt(4) != 0"),
    400: (5000, (0, 5), "randInt(4) != 0"),
    401: (5000, (0, 5), "randInt(4) != 0"),
    402: (5000, (0, 5), "randInt(4) != 0"),
    403: (5000, (0, 5), "randInt(4) != 0"),
    404: (5000, (0, 5), "randInt(4) != 0"),
    405: (5000, (0, 10), "randInt(4) = 0"),
    406: (5000, (0, 10), "randInt(4) = 0"),
    407: (5000, (0, 10), "randInt(4) = 0"),
    408: (5000, (0, 10), "randInt(4) = 0"),
    409: (5000, (0, 10), "randInt(4) = 0"),
    410: (5000, (0, 10), "randInt(4) = 0"),
    411: (5000, (0, 10), "randInt(4) = 0"),
    412: (5000, (0, 10), "randInt(4) = 0"),
    413: (5000, (0, 10), "randInt(4) = 0"),
    414: (5000, (0, 10), "randInt(4) = 0"),
    415: (5000, (0, 10), "randInt(4) = 0"),
    416: (5000, (0, 10), "randInt(4) = 0"),
    417: (5000, (0, 10), "randInt(4) = 0"),
    418: (5000, (0, 10), "randInt(4) = 0"),
    419: (5000, (0, 10), "randInt(4) = 0"),
    420: (5000, (0, 10), "randInt(1) = 0"),
    421: (5000, (0, 10), "randInt(1) = 0"),
    422: (5000, (0, 10), "randInt(1) = 0"),
    423: (5000, (0, 10), "randInt(1) = 0"),
    424: (5000, (0, 10), "randInt(1) = 0"),
    425: (5000, (0, 10), "randInt(1) = 0"),
    426: (5000, (0, 10), "randInt(1) = 0"),
    427: (5000, (0, 10), "randInt(1) = 0"),
    428: (5000, (0, 10), "randInt(1) = 0"),
    429: (5000, (0, 10), "randInt(1) = 0"),
    430: (5000, (0, 10), "randInt(1) = 0"),
    431: (5000, (0, 10), "randInt(1) = 0"),
    432: (5000, (0, 10), "randInt(1) = 0"),
    433: (5000, (0, 10), "randInt(1) = 0"),
    434: (5000, (0, 10), "randInt(1) = 0"),
    435: (5000, (0, 10), "randInt(4) != 0"),
    436: (5000, (0, 10), "randInt(4) != 0"),
    437: (5000, (0, 10), "randInt(4) != 0"),
    438: (5000, (0, 10), "randInt(4) != 0"),
    439: (5000, (0, 10), "randInt(4) != 0"),
    440: (5000, (0, 10), "randInt(4) != 0"),
    441: (5000, (0, 10), "randInt(4) != 0"),
    442: (5000, (0, 10), "randInt(4) != 0"),
    443: (5000, (0, 10), "randInt(4) != 0"),
    444: (5000, (0, 10), "randInt(4) != 0"),
    445: (5000, (0, 10), "randInt(4) != 0"),
    446: (5000, (0, 10), "randInt(4) != 0"),
    447: (5000, (0, 10), "randInt(4) != 0"),
    448: (5000, (0, 10), "randInt(4) != 0"),
    449: (5000, (0, 10), "randInt(4) != 0"),
    450: (5000, (5, 10), "randInt(4) = 0"),
    451: (5000, (5, 10), "randInt(4) = 0"),
    452: (5000, (5, 10), "randInt(4) = 0"),
    453: (5000, (5, 10), "randInt(4) = 0"),
    454: (5000, (5, 10), "randInt(4) = 0"),
    455: (5000, (5, 10), "randInt(4) = 0"),
    456: (5000, (5, 10), "randInt(4) = 0"),
    457: (5000, (5, 10), "randInt(4) = 0"),
    458: (5000, (5, 10), "randInt(4) = 0"),
    459: (5000, (5, 10), "randInt(4) = 0"),
    460: (5000, (5, 10), "randInt(4) = 0"),
    461: (5000, (5, 10), "randInt(4) = 0"),
    462: (5000, (5, 10), "randInt(4) = 0"),
    463: (5000, (5, 10), "randInt(4) = 0"),
    464: (5000, (5, 10), "randInt(4) = 0"),
    465: (5000, (5, 10), "randInt(1) = 0"),
    466: (5000, (5, 10), "randInt(1) = 0"),
    467: (5000, (5, 10), "randInt(1) = 0"),
    468: (5000, (5, 10), "randInt(1) = 0"),
    469: (5000, (5, 10), "randInt(1) = 0"),
    470: (5000, (5, 10), "randInt(1) = 0"),
    471: (5000, (5, 10), "randInt(1) = 0"),
    472: (5000, (5, 10), "randInt(1) = 0"),
    473: (5000, (5, 10), "randInt(1) = 0"),
    474: (5000, (5, 10), "randInt(1) = 0"),
    475: (5000, (5, 10), "randInt(1) = 0"),
    476: (5000, (5, 10), "randInt(1) = 0"),
    477: (5000, (5, 10), "randInt(1) = 0"),
    478: (5000, (5, 10), "randInt(1) = 0"),
    479: (5000, (5, 10), "randInt(1) = 0"),
    480: (5000, (5, 10), "randInt(4) != 0"),
    481: (5000, (5, 10), "randInt(4) != 0"),
    482: (5000, (5, 10), "randInt(4) != 0"),
    483: (5000, (5, 10), "randInt(4) != 0"),
    484: (5000, (5, 10), "randInt(4) != 0"),
    485: (5000, (5, 10), "randInt(4) != 0"),
    486: (5000, (5, 10), "randInt(4) != 0"),
    487: (5000, (5, 10), "randInt(4) != 0"),
    488: (5000, (5, 10), "randInt(4) != 0"),
    489: (5000, (5, 10), "randInt(4) != 0"),
    490: (5000, (5, 10), "randInt(4) != 0"),
    491: (5000, (5, 10), "randInt(4) != 0"),
    492: (5000, (5, 10), "randInt(4) != 0"),
    493: (5000, (5, 10), "randInt(4) != 0"),
    494: (5000, (5, 10), "randInt(4) != 0"),
    495: (5000, (10, 20), "randInt(4) = 0"),
    496: (5000, (10, 20), "randInt(4) = 0"),
    497: (5000, (10, 20), "randInt(4) = 0"),
    498: (5000, (10, 20), "randInt(4) = 0"),
    499: (5000, (10, 20), "randInt(4) = 0"),
    500: (5000, (10, 20), "randInt(4) = 0"),
    501: (5000, (10, 20), "randInt(4) = 0"),
    502: (5000, (10, 20), "randInt(4) = 0"),
    503: (5000, (10, 20), "randInt(4) = 0"),
    504: (5000, (10, 20), "randInt(4) = 0"),
    505: (5000, (10, 20), "randInt(4) = 0"),
    506: (5000, (10, 20), "randInt(4) = 0"),
    507: (5000, (10, 20), "randInt(4) = 0"),
    508: (5000, (10, 20), "randInt(4) = 0"),
    509: (5000, (10, 20), "randInt(4) = 0"),
    510: (5000, (10, 20), "randInt(1) = 0"),
    511: (5000, (10, 20), "randInt(1) = 0"),
    512: (5000, (10, 20), "randInt(1) = 0"),
    513: (5000, (10, 20), "randInt(1) = 0"),
    514: (5000, (10, 20), "randInt(1) = 0"),
    515: (5000, (10, 20), "randInt(1) = 0"),
    516: (5000, (10, 20), "randInt(1) = 0"),
    517: (5000, (10, 20), "randInt(1) = 0"),
    518: (5000, (10, 20), "randInt(1) = 0"),
    519: (5000, (10, 20), "randInt(1) = 0"),
    520: (5000, (10, 20), "randInt(1) = 0"),
    521: (5000, (10, 20), "randInt(1) = 0"),
    522: (5000, (10, 20), "randInt(1) = 0"),
    523: (5000, (10, 20), "randInt(1) = 0"),
    524: (5000, (10, 20), "randInt(1) = 0"),
    525: (5000, (10, 20), "randInt(4) != 0"),
    526: (5000, (10, 20), "randInt(4) != 0"),
    527: (5000, (10, 20), "randInt(4) != 0"),
    528: (5000, (10, 20), "randInt(4) != 0"),
    529: (5000, (10, 20), "randInt(4) != 0"),
    530: (5000, (10, 20), "randInt(4) != 0"),
    531: (5000, (10, 20), "randInt(4) != 0"),
    532: (5000, (10, 20), "randInt(4) != 0"),
    533: (5000, (10, 20), "randInt(4) != 0"),
    534: (5000, (10, 20), "randInt(4) != 0"),
    535: (5000, (10, 20), "randInt(4) != 0"),
    536: (5000, (10, 20), "randInt(4) != 0"),
    537: (5000, (10, 20), "randInt(4) != 0"),
    538: (5000, (10, 20), "randInt(4) != 0"),
    539: (5000, (10, 20), "randInt(4) != 0"),
}
indices = sorted([str(i) for i in log_index.keys()])
indices = list(map(int, indices))
# log_index[i] = log_index[indices[i]] for i in range(len(indices))
log_index = {i: log_index[v] for i, v in enumerate(indices)}


def search_experiment_results(c, delay, p):
    first_experiment = min([i for i, v in log_index.items() if v == (c, delay, p)])
    experiments_index = range(first_experiment, first_experiment + 15)
    # print(experiments_index)
    assert len(experiments_index) == 15
    # print([indices[i] for i in experiments_index])
    return [load_log(f"model/log-{indices[i]}/log.log01") for i in experiments_index]


def proba_text(n):
    assert n in [20,50,80]
    if n == 20:
        return "randInt(4) = 0"
    if n == 50:
        return "randInt(1) = 0"
    if n == 80:
        return "randInt(4) != 0"


def get_agents(df, time):
    timed_df = df[df[TIME_COL] == time]
    agents = np.zeros((x_size, y_size), dtype=int)
    directions = {}
    life_time = {}
    todos_enojos = {}
    for _, row in timed_df.iterrows():
        x, y = row[COORDS_COL]
        val = row[VALUE_COL]
        if val != 0:
            i, d, t, *enojos = val
            agents[x, y] = i
            directions[i] = d
            life_time[i] = t
            # print((time, t, i, enojos))
    return agents, directions, life_time


def get_conflicts(df):
    buchoneos = []
    last_turn_agents, last_turn_dir, last_turn_life_time = get_agents(df, 0)
    for time in df['time'].unique():
        agents, directions, life_time = get_agents(df, time)
        timed_df = df[df[TIME_COL] == time]
        for _, row in timed_df.iterrows():
            x, y = row[COORDS_COL]
            val = row[VALUE_COL]
            if val != 0:
                i, d, t, *enojos = val
                if last_turn_life_time[i] < life_time[i]:
                    # Fui buchoneado
                    buchon_x, buchon_y = next_cell((x,y), last_turn_dir[i])
                    buchoneos.append(dict(buchoneado=i, buchon=last_turn_agents[buchon_x, buchon_y], time=time))
        last_turn_agents, last_turn_dir, last_turn_life_time = agents, directions, life_time
    return buchoneos


def plot_agents(data):
    agents, directions, life_time = data
    # print(data)

    plt.axes().clear()
    pc = plt.pcolor(agents, cmap="Dark2", edgecolors="k", linewidths=1)
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
            text = f"{value}\n{direction_to_unicode[direction]}\n{life_time[value]}"
            ax.text(x, y, text, ha="center", va="center", color=color, fontsize="x-large")


def count_agents_frame(frame):
    agents, directions, life_time = frame
    return len(directions)


def count_agents(df_log):
    return pd.DataFrame([
        (count_agents_frame(get_agents(df_log, time)), time)
        for time in df_log["time"].unique()
    ], columns=['num_alive', 'time'])


def total_life_times(df_log):
    num = count_agents_frame(get_agents(df_log, 0))
    res = []
    for time in df_log["time"].unique():
        new_num = count_agents_frame(get_agents(df_log, time))
        res += [time]*(num - new_num)
        num = new_num
    return res


def total_life_time_agents(df_log):
    indexes = set(get_agents(df_log, 0)[1].keys())
    res = {}
    for time in df_log["time"].unique():
        new_indexes = set(get_agents(df_log, time)[1].keys())
        for i in indexes.difference(new_indexes):
            res[i] = time
        indexes = new_indexes
    return res


# Agrega 0s al final de las simulaciones, para que todas tengan el mismo largo
# Si no se hiciera esto, calcularia mal los estadisticos
def fill_counts(counts_list):
    max_times = [counts['time'].max() for counts in counts_list]
    total_max = max(max_times)
    def fill(counts, max_time):
        times = range(max_time+100, total_max+100, 100)
        return counts.append(pd.DataFrame(dict(num_alive=[0]*len(times), time=[t for t in times])))
    return [fill(counts, max_time) for counts, max_time in zip(counts_list, max_times)]


def plot_uncertainty(stats, title):
    fig = plt.figure(figsize=(16, 9))
    plt.fill_between(stats['time'], stats['25%'], stats['75%'], alpha=0.5, label='Intervalo 25%/75%')
    plt.plot(stats['time'], stats['50%'], label='Mediana prisioneros que siguen en la carcel')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()


def agents_count_stats(df_log_list):
    counts_list = fill_counts([count_agents(df_log) for df_log in df_log_list])
    # agrego columna de que corrida es
    for i, counts in enumerate(counts_list):
        counts.loc[:,'run'] = i
    # tomo mediana y cuartiles
    stats = pd.concat(counts_list).groupby('time')['num_alive'].describe().reset_index()
    return stats


def make_animation(df_log, filename="animation"):
    fig = plt.figure(figsize=(10, 10))
    frames = [get_agents(df_log, time) for time in df_log["time"].unique()]
    anim = FuncAnimation(fig, plot_agents, frames=frames, interval=500)
    anim.save(f"{filename}.gif", writer="imagemagick")


def plot_histogram(life_times, title):
    plt.figure(figsize=(16, 9))
    plt.hist(life_times, bins=range(0, max(life_times)+100, 100))
    plt.title(title)
    plt.show()


def main():
    df = load_log("model/log/log.log01")
    # make_animation(df)

    log_dfs = [load_log(f"model/log{i}/log.log01") for i in range(10)]

    stats = agents_count_stats(log_dfs)
    plot_uncertainty(stats, 'Experimento 100 de condena agregada, 0 a 5 turnos para avisar buchoneo, 20% probabilidad de buchoneo')

    plot_histogram(sum([total_life_times(log_df) for log_df in log_dfs], []), 'Tiempo de condena total')


if __name__ == "__main__":
    main()
