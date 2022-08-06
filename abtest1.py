import numpy as np
import re
from scipy.stats import levene
from scipy import stats

def null_hypothesis_test(stat, p, threshold, stat_name, target_name):
    stat = np.round(stat, 3)
    p = np.round(p, 3)
    if p > threshold:
        print(f"{stat_name} = {stat}, p-value > 0.05")
        print("Reject null hypothesis: no")
        print(f"{target_name} are equal: yes")
    else:
        print(f"{stat_name} = {stat}, p-value <= 0.05")
        print("Reject null hypothesis: yes")
        print(f"{target_name} are equal: no")

with open(r"C:\private\src\python\idea\ABtest\aa_test.csv", encoding="utf-8") as f:
    lines = f.readlines()

a = np.array([float(x.split(",")[0]) for x in lines[1:]])
b = np.array([float(re.split("[,\n]", x)[1]) for x in lines[1:]])

stat, p = levene(a, b, center="mean")

print("Levene's test")
null_hypothesis_test(stat, p, 0.05, "W", "Variances")

print()
print('T-test')
stat, p = stats.ttest_ind(a, b)
null_hypothesis_test(stat, p, 0.05, "t", "Means")
