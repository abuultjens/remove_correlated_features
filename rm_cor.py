


import numpy as np
import pandas as pd

import sys
DATA = sys.argv[1]
OUTFILE_NAME = sys.argv[2]

# load data
data_tr = pd.read_csv(DATA, header=0, index_col=0)
data = data_tr.transpose()

# remove highly correlated features
corr = data.corr()
columns = np.full((corr.shape[0],), True, dtype=bool)
for i in range(corr.shape[0]):
    for j in range(i+1, corr.shape[0]):
        if corr.iloc[i,j] == 1.0 or corr.iloc[i,j] == -1.0:
            if columns[j]:
                columns[j] = False
selected_columns = data.columns[columns]
data_UNCORRELATED = data[selected_columns]
data = data_UNCORRELATED

# write to file
data_UNCORRELATED_tr = data_UNCORRELATED.transpose()
data_UNCORRELATED_tr.to_csv("%s" % OUTFILE_NAME)


