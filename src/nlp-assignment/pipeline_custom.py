import nltk


def process(text):
    tagged = preprocess(text)
    fixed_tokens = [token for token, _ in tagged]
    i = 0
    while i < len(fixed_tokens):
        replacement, consumed = apply_bit_delay_rule(fixed_tokens, i)
        fixed_tokens[i : i + consumed] = replacement
        i += len(replacement)
    return fixed_tokens


def preprocess(text: str):
    words = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(words)
    tagged_lower = [(token.lower(), tag) for token, tag in tagged]
    return tagged_lower


def apply_bit_delay_rule(tokens, idx):
    n = len(tokens)
    if idx + 2 >= n:
        return [tokens[idx]], 1
    w0, w1, w2 = tokens[idx], tokens[idx + 1], tokens[idx + 2]
    if w0 == "although" and w1 == "bit" and w2 == "delay":
        return ["although", "a", "bit", "delayed"], 3
    return [tokens[idx]], 1


text = "Anyway, I believe the team, although bit delay and less communication at recent days, they really tried best for paper and cooperation."  # noqa: E501

processed_text = process(text)
print(processed_text)
