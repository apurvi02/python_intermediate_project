# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here
def get_unique_teams_set():
    data=read_ipl_data_csv(path,dtype='S50')
    a=np.unique(data[:,3:5])

    return set(a)
get_unique_teams_set()


