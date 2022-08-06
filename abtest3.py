import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def get_limit(data):
    newdata = np.sort(data)
    limit = int(np.floor(len(newdata)*0.99))
    limit_value = newdata[limit]
    return limit_value

df = pd.read_csv("c:/private/src/python/idea/ABtest/ab_test.csv")

d = df

sd_limit = get_limit(df["session_duration"])
ov_limit = get_limit(df["order_value"])

c = df[df["group"] == "Control"]
csd = c["session_duration"]
csd_limit = get_limit(csd)
cov = c["order_value"]
cov_limit = get_limit(cov)

e = df[df["group"] == "Experimental"]
esd = e["session_duration"]
esd_limit = get_limit(esd)
eov = e["order_value"]
eov_limit = get_limit(eov)

cdate = c["date"]
edate = e["date"]

cdate = cdate.value_counts().sort_index()
edate = edate.value_counts().sort_index()

df = pd.DataFrame()
df["control"] = cdate
df["experimental"] = edate
df.index = pd.to_datetime(df.index)
month = df.index[0].strftime("%B")

labels = list(df.index.strftime("%d"))
labels = [int(x) for x in labels]
df.index = labels

df.plot(kind="bar", xlabel=month, ylabel="Number of sessions")
plt.show()

cov = c["order_value"]
eov = e["order_value"]
csd = c["session_duration"]
esd = e["session_duration"]

fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(hspace=1)

n_bins = 10

# We can set the number of bins with the *bins* keyword argument.
axs[0][0].hist(cov, bins=n_bins)
axs[0][1].hist(eov, bins=n_bins)

axs[0][0].set_title('Control')
axs[0][1].set_title('Experimentals')

axs[0][0].set_ylabel('Frequency')
axs[0][0].set_xlabel("Order Value")
axs[0][1].set_xlabel("Order Value")

axs[1][0].hist(csd, bins=n_bins)
axs[1][1].hist(esd, bins=n_bins)

axs[1][0].set_title('Control')
axs[1][1].set_title('Experimentals')

axs[1][0].set_ylabel('Frequency')
axs[1][0].set_xlabel("Session Duration")
axs[1][1].set_xlabel("Session Duration")

plt.show()

c = c[(sd_limit > c["session_duration"]) & (ov_limit > c["order_value"])]
e = e[(sd_limit > e["session_duration"]) & (ov_limit > e["order_value"])]
#c = c[cov_limit > c["order_value"]]
#e = e[eov_limit > e["order_value"]]

d = list(c["order_value"]) + list(e["order_value"])

ov_mean = np.round(np.mean(d), 2)
ov_std = np.round(np.std(d, axis=None, dtype=None, out=None, ddof=0, keepdims=False), 2)
ov_max = np.max(d)

print(f"Mean: {ov_mean}")
print(f"Standard deviation: {ov_std}")
print(f"Max: {ov_max}")
