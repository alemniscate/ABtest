import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
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

def get_limit(data):
    newdata = np.sort(data)
    limit = int(np.floor(len(newdata)*0.99))
    limit_value = newdata[limit]
    return limit_value

df = pd.read_csv("c:/private/src/python/idea/ABtest/ab_test.csv")

sd_limit = get_limit(df["session_duration"])
ov_limit = get_limit(df["order_value"])

d = df[(sd_limit > df["session_duration"]) & (ov_limit > df["order_value"])]
d = d["order_value"]

ov_mean = np.round(np.mean(d), 2)
ov_std = np.round(np.std(d, axis=None, dtype=None, out=None, ddof=0, keepdims=False), 2)
ov_max = np.max(d)

#print(f"Mean: {ov_mean}")
#print(f"Standard deviation: {ov_std}")
#print(f"Max: {ov_max}")

d = df[(sd_limit > df["session_duration"]) & (ov_limit > df["order_value"])]
c = d[d["group"] == "Control"]
e = d[d["group"] == "Experimental"]
cov = np.log(c["order_value"])
eov = np.log(e["order_value"])

d = d.rename(columns={'order_value': 'log_order_value'})
dov = np.log(d["log_order_value"])
dov.plot(kind="hist", xlabel="Log order value", ylabel="Frequency", legend="log_order_value")
plt.show()

#from scipy.stats import mannwhitneyu
#U1, p = mannwhitneyu(cov, eov, method="auto")
#U1 = np.round(U1, 1)
#print(U1)
#print(p)

#print("Mann-Whitney U test")
#if p > 0.05:
#    print(f"U1 = {U1}, p-value > 0.05")
#    print("Reject null hypothesis: no")
#    print("Distributions are same: yes")
#else:
#    print(f"U1 = {U1}, p-value <= 0.05")
#    print("Reject null hypothesis: yes")
#    print("Distributions are same: no")

stat, p = levene(cov, eov)

print("Levene's test")
null_hypothesis_test(stat, p, 0.05, "W", "Variances")

print()
print('T-test')
stat, p = stats.ttest_ind(cov, eov, equal_var=False)
null_hypothesis_test(stat, p, 0.05, "t", "Means")
