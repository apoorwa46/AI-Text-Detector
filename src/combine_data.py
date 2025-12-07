import pandas as pd

# Load both CSV files
ai_df = pd.read_csv("data/AI_Generated.csv")
human_df = pd.read_csv("data/Human-Written.csv")

# IMPORTANT: The column containing text must be named the same.
# Check the column name in your CSVs.

# Let's assume the text column is named "text"
ai_df = ai_df.rename(columns={ai_df.columns[0]: "text"})
human_df = human_df.rename(columns={human_df.columns[0]: "text"})

# Add labels
ai_df["label"] = 1        # 1 = AI generated
human_df["label"] = 0     # 0 = Human written

# Combine
combined = pd.concat([ai_df, human_df], ignore_index=True)

# Save combined dataset
combined.to_csv("data/ai_human.csv", index=False)

print("Combined CSV saved as data/ai_human.csv")
print("Shape:", combined.shape)
