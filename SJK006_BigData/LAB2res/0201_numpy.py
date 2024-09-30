import argparse as arg
import logging as log

import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

import Common as Comm

_log = Comm.LoggingHelper.get_logger("INFO")

n=1000
df = pd.read_csv('https://krono.act.uji.es/IDIA/airline-passengers.csv')


print(df.tail())