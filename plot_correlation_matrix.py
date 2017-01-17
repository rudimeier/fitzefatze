import numpy as np
from math import factorial 
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

# plotting color coded correlation matrix
def plot_corr(corr_matrix):	
	
	N_col  = np.shape(corr_matrix)[1]
	extend = (0.5 , N_col+0.5 , N_col+0.5, 0.5 )
	
	fig , ax = plt.subplots(figsize=(15, 12))
	ax.tick_params('both', length=15, width=8, which='major')
	plt.subplots_adjust(left=0.10, right=0.95, top=0.95, bottom=0.12)
	
	#cmin = corr_matrix.min()
	#cmax = corr_matrix.max()
	cmin = -0.3
	cmax = 0.25
	
	plt.imshow(corr_matrix, vmin=cmin, vmax=cmax, extent=extend)
	
	cbar = plt.colorbar()
	#cbar.set_label('Some Units', labelpad=-40, y=0.45)
	
	for t in cbar.ax.get_yticklabels():
		t.set_fontsize(50)
	plt.xticks(fontsize = 50)
	plt.yticks(fontsize = 50)
	plt.xlabel('Nodes', fontsize = 50)
	plt.ylabel('Nodes', fontsize = 50)
	return fig 	

data_dir = '/home/sheyma/devel/fitzefatze/data/jobs_adj/'
file_in  = data_dir + 'acp_w_thr_0.98_sigma=0.05_D=0.05_v=30.0_tmax=45000_FHN_corr.dat'
file_in = data_dir+'acp_w_thr_0.98_sigma=0.05_D=0.05_v=30.0_tmax=45000_FHN_spearm.dat'

#data_dir = '/home/sheyma/HD/sheyma_bayrak_2015/jobs_corr/'
#file_in  = data_dir + 'acp_w_0_ADJ_thr_0.50_sigma=0.05_D=0.05_v=30.0_tmax=45000_FHN_corr.dat'

corr_matrix = np.loadtxt(file_in)
figure      = plot_corr(corr_matrix)
plt.show()
