import pandas as pd
import joblib
import re

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv(
    "data/goemotions.csv"
)

print("\nDATA LOADED SUCCESSFULLY\n")

# ==========================================
# TEXT COLUMN
# ==========================================

TEXT_COLUMN = "text"

# ==========================================
# EMOTION COLUMNS
# ==========================================

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

# ==========================================
# KEEP ONLY SINGLE LABEL ROWS
# ==========================================

df = df[
    df[emotion_columns].sum(axis=1) == 1
]

# ==========================================
# CREATE LABEL
# ==========================================

df["emotion"] = df[
    emotion_columns
].idxmax(axis=1)

print("\nEMOTION COUNTS:\n")

print(
    df["emotion"].value_counts()
)

# ==========================================
# TEXT CLEANING
# ==========================================

def clean_text(text):

    text = str(text).lower()

    # HANDLE NEGATIONS
    text = text.replace("don't", "not")
    text = text.replace("dont", "not")
    text = text.replace("didn't", "not")
    text = text.replace("didnt", "not")
    text = text.replace("isn't", "not")
    text = text.replace("isnt", "not")
    text = text.replace("wasn't", "not")
    text = text.replace("wasnt", "not")
    text = text.replace("can't", "not")
    text = text.replace("cant", "not")

    # REMOVE LINKS
    text = re.sub(r"http\S+", "", text)

    # REMOVE SPECIAL CHARS
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # REMOVE EXTRA SPACES
    text = re.sub(r"\s+", " ", text).strip()

    return text


df[TEXT_COLUMN] = df[
    TEXT_COLUMN
].apply(clean_text)

# ==========================================
# FEATURES + LABELS
# ==========================================

X = df[TEXT_COLUMN]

y = df["emotion"]

# ==========================================
# LABEL ENCODING
# ==========================================

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

joblib.dump(
    label_encoder,
    "models/label_encoder.pkl"
)

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

# ==========================================
# TF-IDF
# ==========================================

vectorizer = TfidfVectorizer(

    max_features=100000,

    ngram_range=(1,3),

    stop_words=None,

    sublinear_tf=True,

    min_df=2,

    max_df=0.90
)

X_train_tfidf = vectorizer.fit_transform(
    X_train
)

X_test_tfidf = vectorizer.transform(
    X_test
)

joblib.dump(
    vectorizer,
    "models/vectorizer.pkl"
)

# ==========================================
# MODELS
# ==========================================

models = {

    "Logistic Regression":

        LogisticRegression(

            max_iter=3000,

            class_weight='balanced',

            C=5
        ),

    "LinearSVC":

        LinearSVC(

            class_weight='balanced',

            C=5
        ),

    "MultinomialNB":

        MultinomialNB(
            alpha=0.5
        )
}

# ==========================================
# TRAIN + EVALUATE
# ==========================================

results = []

best_f1 = 0

best_model = None

best_model_name = ""

for name, model in models.items():

    print(f"\n====================")
    print(f"TRAINING: {name}")
    print(f"====================\n")

    model.fit(
        X_train_tfidf,
        y_train
    )

    predictions = model.predict(
        X_test_tfidf
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        average='weighted',
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        average='weighted',
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        average='weighted',
        zero_division=0
    )

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\nCLASSIFICATION REPORT:\n")

    print(
        classification_report(
            y_test,
            predictions,
            target_names=label_encoder.classes_,
            zero_division=0
        )
    )

    results.append({

        "Model": name,

        "Accuracy": accuracy,

        "Precision": precision,

        "Recall": recall,

        "F1": f1
    })

    # BEST MODEL
    if f1 > best_f1:

        best_f1 = f1

        best_model = model

        best_model_name = name

# ==========================================
# SAVE RESULTS
# ==========================================

results_df = pd.DataFrame(results)

results_df.to_csv(
    "reports/metrics.csv",
    index=False
)

print("\nRESULTS SAVED")

# ==========================================
# BEST MODEL
# ==========================================

print(f"\nBEST MODEL: {best_model_name}")

# SAVE BEST MODEL
joblib.dump(
    best_model,
    "models/best_model.pkl"
)
print(df["emotion"].value_counts())
print("\nBEST MODEL SAVED SUCCESSFULLY")