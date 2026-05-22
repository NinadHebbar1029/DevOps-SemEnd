import re
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