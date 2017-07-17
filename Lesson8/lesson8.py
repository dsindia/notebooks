import matplotlib
matplotlib.use('Agg')
from datascience import *
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')




def positive_correlation():
    disease_data=(Table.read_table('prisoners_over_time.csv'))
    disease_data.sort('Prisoners admitted to Hospitals').plot('Prisoners admitted to Hospitals')
    disease_data.scatter('Prisoners admitted to Hospitals')
    
