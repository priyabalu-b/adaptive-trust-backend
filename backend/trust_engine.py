def calculate_trust_score(features):
    score = 100
    reasons = []

    # HTTPS check
    if not features["has_https"]:
        score -= 40
        reasons.append("Website is not using HTTPS")

    # Suspicious keywords check
    if features["suspicious_words"] >= 1:
        score -= 30
        reasons.append("Suspicious keywords found in URL")

    # High entropy check
    if features["entropy"] > 3.5:
        score -= 30
        reasons.append("URL structure looks random (high entropy)")

    score = max(0, min(score, 100))
    return score, reasons
def classify_risk(score):
    if score >= 80:
        return "TRUSTED"
    elif score >= 50:
        return "SUSPICIOUS"
    else:
        return "DANGEROUS"
