import familiar
from scipy.stats import ttest_1samp,ttest_ind,chi2_contingency
vein_pack_lifespans = familiar.lifespans(package='vein')


vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print(format(vein_pack_test.pvalue, '0.10f'))

if vein_pack_test.pvalue < .05:
  print('The Vain Pack is Proven To Make You Live Longer!')
else:
  print('The Vein Pack is Probably Good For You Somehow!')
  
artery_pack_lifespans = familiar.lifespans(package='artery')

package_comparison_results = ttest_ind(artery_pack_lifespans, vein_pack_lifespans)

if package_comparison_results.pvalue < .05:
  print('the Artery Package guarantees even stronger results!')
else:
  print('The Artery Package is also a great product!')

iron_contingency_table = familiar.iron_counts_for_package()

_,iron_pvalue,_,_ = chi2_contingency(iron_contingency_table)

if iron_pvalue < .05:
  print('The Artery Package Is Proven To Make You Healthier')
else:
  print('While We Can\'t Say The Artery Package Will Help You, I Bet It\'s Nice!')
