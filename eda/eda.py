import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create plots folder automatically
os.makedirs("plots", exist_ok=True)


hd = pd.read_csv("D:/Datasets/Data Sets for Exam/HeartDisease.csv")
hd1=hd.iloc[:,1:]

hd1.columns=["sysp","chol","his","ob","age","hd"]

print(hd1.head())
print(hd1.shape)
print(hd1.info())
print(hd1.describe(include="all"))

# -----------------------------
# Histograms
# -----------------------------

# Age
plt.figure(figsize=(5,4))
plt.hist(hd1["age"], color="skyblue", edgecolor="black")
plt.title("Age")
plt.xlabel("Age")
plt.savefig("plots/age_histogram.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# Systolic Pressure
plt.figure(figsize=(5,4))
plt.hist(hd1["sysp"], color="lightgreen", edgecolor="black")
plt.title("Systolic Pressure")
plt.xlabel("mmHg")
plt.savefig("plots/sysp_histogram.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# Cholesterol
plt.figure(figsize=(5,4))
plt.hist(hd1["chol"], color="salmon", edgecolor="black")
plt.title("Cholesterol")
plt.xlabel("mmol/L")
plt.savefig("plots/chol_histogram.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

sns.boxplot(y=hd1["age"], ax=axes[0], color="skyblue")
axes[0].set_title("Age")

sns.boxplot(y=hd1["sysp"], ax=axes[1], color="lightgreen")
axes[1].set_title("Systolic Pressure")

sns.boxplot(y=hd1["chol"], ax=axes[2], color="salmon")
axes[2].set_title("Cholesterol")

plt.tight_layout()

# Save the figure
plt.savefig("plots/boxplots_age_sysp_chol.png", dpi=300, bbox_inches="tight")

# Optional: display on screen
plt.show()

# Close figure
plt.close()
# -----------------------------
# Bar plots
# -----------------------------
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

hd1["hd"].value_counts().sort_index().plot( 
    kind="bar", color=["lightgreen", "tomato"], ax=axes[0]
)
axes[0].set_title("Heart Disease Distribution")
axes[0].set_ylabel("Count")

hd1["his"].value_counts().sort_index().plot( 
    kind="bar", color=["steelblue", "orange"], ax=axes[1]
)
axes[1].set_title("Family History")

plt.tight_layout()

# Save figure
plt.savefig("plots/barplots_hd_his.png", dpi=300, bbox_inches="tight")

plt.show()
plt.close()


# -----------------------------
# Boxplots: Age & Blood Pressure vs Heart Disease
# -----------------------------
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

sns.boxplot(x="hd", y="age", data=hd1, 
            palette=["lightgreen", "tomato"], ax=axes[0])
axes[0].set_title("Age vs Heart Disease")

sns.boxplot(x="hd", y="sysp", data=hd1, 
            palette=["lightgreen", "tomato"], ax=axes[1])
axes[1].set_title("Blood Pressure vs Heart Disease")

plt.tight_layout()

# Save figure
plt.savefig("plots/age_sysp_vs_hd.png", dpi=300, bbox_inches="tight")

plt.show()
plt.close()


# -----------------------------
# Boxplots: Cholesterol & Obesity vs Heart Disease
# -----------------------------
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

sns.boxplot(x="hd", y="chol", data=hd1, 
            palette=["lightgreen", "tomato"], ax=axes[0])
axes[0].set_title("Cholesterol vs Heart Disease")

sns.boxplot(x="hd", y="ob", data=hd1, 
            palette=["lightgreen", "tomato"], ax=axes[1])
axes[1].set_title("Obesity vs Heart Disease")

plt.tight_layout()

# Save figure
plt.savefig("plots/chol_ob_vs_hd.png", dpi=300, bbox_inches="tight")

plt.show()
plt.close()



