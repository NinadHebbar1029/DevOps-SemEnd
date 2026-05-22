import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import joblib

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv(
    "data/goemotions.csv"
)

TEXT_COLUMN = "text"

# =========================================================
# EMOTION COLUMNS
# =========================================================

emotion_columns = [
    'admiration', 'amusement', 'anger', 'annoyance',
    'approval', 'caring', 'confusion', 'curiosity',
    'desire', 'disappointment', 'disapproval',
    'disgust', 'embarrassment', 'excitement',
    'fear', 'gratitude', 'grief', 'joy',
    'love', 'nervousness', 'optimism', 'pride',
    'realization', 'relief', 'remorse',
    'sadness', 'surprise', 'neutral'
]

# =========================================================
# KEEP ONLY SINGLE LABEL ROWS
# =========================================================

df = df[
    df[emotion_columns].sum(axis=1) == 1
]

# =========================================================
# CREATE LABELS
# =========================================================

df["emotion"] = df[
    emotion_columns
].idxmax(axis=1)

# =========================================================
# CLEAN TEXT
# =========================================================

def clean_text(text):

    text = str(text).lower()

    return text


df[TEXT_COLUMN] = df[
    TEXT_COLUMN
].apply(clean_text)

X = df[TEXT_COLUMN]

y = df["emotion"]

# =========================================================
# TRAIN TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================================================
# LOAD FILES
# =========================================================

model = joblib.load(
    "models/best_model.pkl"
)

vectorizer = joblib.load(
    "models/vectorizer.pkl"
)

label_encoder = joblib.load(
    "models/label_encoder.pkl"
)

# =========================================================
# TRANSFORM
# =========================================================

X_test_tfidf = vectorizer.transform(
    X_test
)

# =========================================================
# PREDICT
# =========================================================

predictions = model.predict(
    X_test_tfidf
)

# =========================================================
# CONVERT LABELS
# =========================================================

predictions = label_encoder.inverse_transform(
    predictions
)

# =========================================================
# LABELS
# =========================================================

labels = label_encoder.classes_

# =========================================================
# CONFUSION MATRIX
# =========================================================

cm = confusion_matrix(
    y_test,
    predictions,
    labels=labels
)

plt.figure(figsize=(12, 10))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=labels,
    yticklabels=labels
)

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.title("Confusion Matrix")

plt.savefig(
    "reports/confusion_matrix.png"
)

plt.show()

print("\nConfusion matrix saved successfully")