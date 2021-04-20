import numpy as np
import matplotlib.pyplot as plt 
import scipy.stats as st
import matplotlib

matplotlib.rcParams.update({'font.size': 12, 'font.family': 'serif', 'text.usetex': True})

debug = np.genfromtxt('./debug_exec_time.txt')
release = np.genfromtxt('./release_exec_time.txt')
num_exp = len(debug)
n_exp = np.linspace(1,num_exp,num_exp)

# Compute statistics
mean_debug = np.mean(debug)
mean_release = np.mean(release)
median_debug = np.median(debug)
median_release = np.median(release)
std_debug = np.std(debug)
std_release = np.std(release)

# Compute confidence interval
CI_release = st.t.interval(0.95, len(release)-1, loc=np.mean(release), scale=st.sem(release))#st.norm.interval(alpha=0.95, loc=np.mean(release), scale=st.sem(release))
CI_debug = st.t.interval(0.95, len(debug)-1, loc=np.mean(debug), scale=st.sem(debug))#st.norm.interval(alpha=0.95, loc=np.mean(debug), scale=st.sem(debug))

# Plot execution time vs experiment
plt.figure()
plt.plot(n_exp,release,'-ko')
plt.xlabel('Experimento',fontsize='large')
plt.ylabel('Tempo de execucao (s)',fontsize='large')
plt.title('Release')
plt.show()
plt.savefig('./exec_release.png',dpi = 300)

plt.figure()
plt.plot(n_exp,debug,'-ko')
plt.xlabel('Experimento',fontsize='large')
plt.ylabel('Tempo de execucao (s)',fontsize='large')
plt.title('Debug')
plt.show()
plt.savefig('./exec_debug.png',dpi = 300)

# Plot histograms
plt.figure()
plt.hist(debug, bins=10)
plt.xlabel('Tempo de execucao (s)',fontsize='large')
plt.ylabel('Frequencia',fontsize='large')
plt.title('Debug')
plt.show()
plt.savefig('./histogram_debug.png',dpi = 300)

plt.figure()
plt.hist(release, bins=10)
plt.xlabel('Tempo de execucao (s)',fontsize='large')
plt.ylabel('Frequencia',fontsize='large')
plt.title('Release')
plt.show()
plt.savefig('./histogram_release.png',dpi = 300)

fig, ax = plt.subplots()
experiments = ["Release", "Debug"]
x_pos =  np.arange(len(experiments))
y_pos = [mean_release, mean_debug]
error = [2*std_release, 2*std_debug]
#error = [CI_release[1] - CI_release[0], CI_debug[1] - CI_debug[0]]
ax.bar(x_pos, y_pos, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Tempo de execucao (s)',fontsize='large')
ax.set_xticks(x_pos)
ax.set_xticklabels(experiments,fontsize='large')
ax.set_title('Media')
ax.yaxis.grid(True)
plt.show()
plt.savefig('./mean.png',dpi = 300)

fig, ax = plt.subplots()
experiments = ["Release", "Debug"]
x_pos =  np.arange(len(experiments))
y_pos = [median_release, median_debug]
error = [2*std_release, 2*std_debug]
#error = [CI_release[1] - CI_release[0], CI_debug[1] - CI_debug[0]]
ax.bar(x_pos, y_pos, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Tempo de execucao (s)',fontsize='large')
ax.set_xticks(x_pos)
ax.set_xticklabels(experiments,fontsize='large')
ax.set_title('Mediana')
ax.yaxis.grid(True)
plt.show()
plt.savefig('./media.png',dpi = 300)

fig, ax = plt.subplots()
experiments = ["Media", "Median"]
x_pos =  np.arange(len(experiments))
y_pos = [mean_release, median_release]
error = [2*std_release, 2*std_release]
#error = [CI_release[1] - CI_release[0], CI_debug[1] - CI_debug[0]]
ax.bar(x_pos, y_pos, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Tempo de execucao (s)',fontsize='large')
ax.set_xticks(x_pos)
ax.set_xticklabels(experiments,fontsize='large')
ax.set_title('Release')
ax.yaxis.grid(True)
plt.show()
plt.savefig('./statistics_release.png',dpi = 300)

fig, ax = plt.subplots()
experiments = ["Media", "Median"]
x_pos =  np.arange(len(experiments))
y_pos = [mean_debug, median_debug]
error = [2*std_debug, 2*std_debug]
#error = [CI_release[1] - CI_release[0], CI_debug[1] - CI_debug[0]]
ax.bar(x_pos, y_pos, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Tempo de execucao (s)',fontsize='large')
ax.set_xticks(x_pos)
ax.set_xticklabels(experiments,fontsize='large')
ax.set_title('Debug')
ax.yaxis.grid(True)
plt.show()
plt.savefig('./statistics_debug.png',dpi = 300)