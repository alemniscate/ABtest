import pandas as pd
import numpy as np
from statsmodels.stats.power import tt_ind_solve_power

df = pd.read_csv("c:/private/src/python/idea/ABtest/ab_test.csv")
control = df[df["group"] == "Control"]["order_value"]
experimental = df[df["group"] == "Experimental"]["order_value"]

#d1 = np.mean(control) - np.mean(experimental)
#d2 = np.sqrt((np.std(control)**2 + np.std(experimental)**2) / 2)
#d = d1/d2
#print("effect size:",d)

n = tt_ind_solve_power(effect_size=0.2, alpha=0.05, power=0.8)
#print("sample size:",n)

print(f"Sample size: {int(np.round(n, -2))}")
print()
print(f"Control group: {len(control)}")
print(f"Experimental group: {len(experimental)}")