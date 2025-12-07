import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Load the combined dataset
df = pd.read_csv("data/ai_human.csv")

X = df["text"]
y = df["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create model pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("lr", LogisticRegression(max_iter=200))
])

# Train
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/ai_detector.joblib")

print("Model trained successfully!")
print("Saved as models/ai_detector.joblib")
