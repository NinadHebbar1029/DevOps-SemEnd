import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv(
    "data/goemotions.csv"
)

TEXT_COLUMN = "text"

# =====================================================
# EMOTION COLUMNS
# =====================================================

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

# =====================================================
# KEEP ONLY SINGLE LABEL ROWS
# =====================================================

df = df[
    df[emotion_columns].sum(axis=1) == 1
]

# =====================================================
# CREATE SINGLE LABEL
# =====================================================

df["emotion"] = df[
    emotion_columns
].idxmax(axis=1)

# =====================================================
# FEATURES + LABELS
# =====================================================

X = df[TEXT_COLUMN]

y = df["emotion"]

# =====================================================
# SPLIT DATA
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =====================================================
# LOAD SAVED FILES
# =====================================================

model = joblib.load(
    "models/best_model.pkl"
)

vectorizer = joblib.load(
    "models/vectorizer.pkl"
)

label_encoder = joblib.load(
    "models/label_encoder.pkl"
)

# =====================================================
# TRANSFORM TEST DATA
# =====================================================

X_test_tfidf = vectorizer.transform(
    X_test
)

# =====================================================
# BINARIZE LABELS
# =====================================================

classes = label_encoder.classes_

y_test_bin = label_binarize(
    y_test,
    classes=classes
)

# =====================================================
# GET MODEL SCORES
# =====================================================

scores = model.decision_function(
    X_test_tfidf
)

# =====================================================
# PLOT ROC CURVES
# =====================================================

plt.figure(figsize=(12, 10))

for i in range(len(classes)):

    fpr, tpr, _ = roc_curve(
        y_test_bin[:, i],
        scores[:, i]
    )

    roc_auc = auc(fpr, tpr)

    plt.plot(
        fpr,
        tpr,
        lw=2,
        label=f"{classes[i]} (AUC = {roc_auc:.2f})"
    )

# =====================================================
# RANDOM BASELINE
# =====================================================

plt.plot(
    [0, 1],
    [0, 1],
    linestyle='--'
)

# =====================================================
# LABELS
# =====================================================

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("Multiclass ROC-AUC Curve")

plt.legend(loc="lower right")

# =====================================================
# SAVE FIGURE
# =====================================================

plt.savefig(
    "reports/roc_auc_curve.png"
)

plt.show()

print("\nROC-AUC curve saved successfully")