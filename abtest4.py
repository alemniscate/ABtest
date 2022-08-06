import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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
cov = c["order_value"]
eov = e["order_value"]

from scipy.stats import mannwhitneyu
U1, p = mannwhitneyu(cov, eov, method="auto")
U1 = np.round(U1, 1)
#print(U1)
#print(p)

print("Mann-Whitney U test")
if p > 0.05:
    print(f"U1 = {U1}, p-value > 0.05")
    print("Reject null hypothesis: no")
    print("Distributions are same: yes")
else:
    print(f"U1 = {U1}, p-value <= 0.05")
    print("Reject null hypothesis: yes")
    print("Distributions are same: no")