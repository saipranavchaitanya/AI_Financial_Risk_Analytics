import pandas as pd

# Read the engineered dataset
df = pd.read_csv("data/train_data_engineered.csv")

# Remove TARGET column if present
if "TARGET" in df.columns:
    df = df.drop(columns=["TARGET"])

# Save the first row as the template
df.iloc[[0]].to_csv("data/template_input.csv", index=False)

print("✅ template_input.csv created successfully!")
print("Shape:", df.iloc[[0]].shape)