""" File: plot_saturation.py
	Author: Sarah Lindner
	Date of last change: 03.12.2014

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sys import argv

#initial guess of fit parameters
param_init = [2, 14000.0]
fit_flag = 0

my_file = argv[1] 	# get the arguments from the command line
								# by default, the executing script is also passed to argv[0]; 
if len(argv) > 2:
	if argv[2] == 'fit':
		fit_flag = 1
if len(argv) > 3:
	param_init = [ float( argv[2] ), float( argv[3] ) ]


print "Loading file..."
my_output = my_file.replace('.txt', '')

data = np.loadtxt(my_file)
xdata = data[:,0]
ydata = data[:,1]

if (fit_flag == 1):

	print "Fitting"

	def fit_func(p, p_sat, i_inf):
	    return i_inf * p /( p + p_sat )


	fit_param, param_cov = curve_fit(fit_func, xdata, ydata, param_init)

	print param_cov

	sigma = np.sqrt(np.diag(param_cov))

	print("P_sat = {} +- {}".format(fit_param[0], sigma[0]))
	print("I_inf = {} +- {}".format(fit_param[1], sigma[1]))

	parameter_file = open(my_output + '_parameters.txt', 'w')
	parameter_file.write("P_sat = {} +- {}\n".format(fit_param[0], sigma[0]))
	parameter_file.write("I_inf = {} +- {}".format(fit_param[1], sigma[1]))





print "Plotting file: %r" % my_file
plt.plot( xdata, ydata, 'ko', markersize=4 )

if (fit_flag == 1):
	plt.plot(xdata, fit_func(xdata, fit_param[0], fit_param[1]), '-', linewidth=1.5, color = 'red')

plt.title(my_output, fontsize = 23)
plt.xlabel('Excitation Power (mW)', fontsize = 20)
plt.ylabel('Intensity (cps)', fontsize = 20)
plt.tick_params(axis = 'both', labelsize = 15)

plt.tight_layout() # suppress chopping off labels

plt.savefig( (my_output +'.png'))
plt.savefig( (my_output +'.pdf'))

plt.show()
