from scipy.io import loadmat
from datetime import datetime
import os
import time
import sys
from tqdm import tqdm
from pathlib import Path
import argparse
import numpy as np

x= []
for i in range(100):
    x.append(i)
a=np.array(x)
print(a.shape)
