import re
import math
from collections import Counter
import validators

def url_entropy(url):
    probabilities = Counter(url)
    length = len(url)
    return -sum((count / length) * math.log2(count / length) for count in probabilities.values())

def extract_features(url):
    features = {}

    features["is_valid_url"] = validators.url(url)
    features["length"] = len(url)
    features["entropy"] = round(url_entropy(url), 2)
    features["has_https"] = url.startswith("https")
    features["suspicious_words"] = len(
        re.findall(r"(login|verify|free|secure|account|update)", url.lower())
    )

    return features

if __name__ == "__main__":
    test_url = "http://free-login-secure-update.com"
    print(extract_features(test_url))
