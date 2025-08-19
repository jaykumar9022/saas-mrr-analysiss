import pandas as pd
import matplotlib.pyplot as plt

# Quarterly MRR growth data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "MRR_Growth": [8.66, 3.44, 11.36, 7.69]
}

df = pd.DataFrame(data)
df["Industry_Target"] = 15

# Calculate average
avg_growth = df["MRR_Growth"].mean()
print(f"Average MRR Growth: {avg_growth:.2f}")  # Should be 7.79

# Visualization
plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["MRR_Growth"], marker="o", label="Company MRR Growth")
plt.axhline(y=15, color="r", linestyle="--", label="Industry Target (15%)")

plt.title("Quarterly MRR Growth vs Industry Benchmark")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("mrr_growth_trend.png")
plt.show()
