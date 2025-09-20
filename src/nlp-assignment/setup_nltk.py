import nltk


def download_resources():
    # You can add/remove resources depending on what you use
    nltk.download("punkt")  # tokenizer
    nltk.download("punkt_tab")
    nltk.download("stopwords")  # stopword lists
    nltk.download("wordnet")  # lemmatizer
    nltk.download("averaged_perceptron_tagger")  # POS tagger
    nltk.download("state_union")


if __name__ == "__main__":
    download_resources()
