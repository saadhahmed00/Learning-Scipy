import numpy as np
import fetchmaker
from scipy.stats import binom_test,f_oneway,chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

rottweiler_tl = fetchmaker.get_tail_length('rottweiler')
print(np.mean(rottweiler_tl))
print(np.std(rottweiler_tl))

#Binomial Test
whippet_rescue = fetchmaker.get_is_rescue('whippet')
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(num_whippet_rescues)
pval = binom_test(num_whippet_rescues, n=len(whippet_rescue), p=.08)
print(pval)

#ANOVA Test
whip_w =fetchmaker.get_weight('whippet')
pit_w = fetchmaker.get_weight('pitbull')
ter_w=fetchmaker.get_weight('terrier')
_,pval_anova = f_oneway(whip_w, pit_w, ter_w)
print(pval_anova)

#Tukey Range Test
v = np.concatenate([whip_w, pit_w, ter_w])
labels = ['whippet']*len(whip_w) + ['pitbull']*len(pit_w) + ['terrier']*len(ter_w)
tukey_results = pairwise_tukeyhsd(v, labels,.05)
print(tukey_results)

#Chi Squared Analysis
poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')
colors = ['black', 'brown', 'gold', 'grey', 'white']
pood_lst = []
shih_lst = []
for animal in ['poodle', 'shihtzu']:
  if animal == 'poodle':
    for elem in colors:
      pood_lst.append(np.count_nonzero(poodle_colors == elem))
  else:
    for elem in colors:
      shih_lst.append(np.count_nonzero(shihtzu_colors == elem))
color_table = zip(pood_lst, shih_lst)

_,pval_chi,_,_ = chi2_contingency(color_table)
print(pval_chi)