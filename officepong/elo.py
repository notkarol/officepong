
def calculate_delta(elo_w, elo_l, score_w, score_l, k_multiplier=3):
    k_factor = k_multiplier * max(score_w, score_l)
    actual = elo_w / (elo_w + elo_l)
    expected = 1 / (1 + 10 ** ((elo_l - elo_w) / 400))
    delta = k_factor * (actual - expected)
    return delta
