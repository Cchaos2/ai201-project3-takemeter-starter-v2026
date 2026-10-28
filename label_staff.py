import pandas as pd

df = pd.read_csv("my_staff_labels.csv", keep_default_na=False)
keys = {"a": "analysis", "h": "hot_take", "r": "reaction"}

for i, row in df.iterrows():
    print(f"\n[{i + 1}/30] {row['text']}")
    choice = ""
    while choice not in keys:
        choice = input("  a = analysis, h = hot_take, r = reaction: ").strip().lower()
    df.at[i, "label"] = keys[choice]
    df.at[i, "my_reason"] = input("  short reason (which rule?): ").strip()

df.to_csv("my_staff_labels.csv", index=False)
print("\nSaved my_staff_labels.csv")