
def calculate_delta(elo_winner, elo_loser, score_winner, score_loser, k_multiplier=3):
    k_factor = k_multiplier * max(score_winner, score_loser)
    actual = elo_winner / (elo_winner + elo_loser)
    expected = 1 / (1 + 10 ** ((elo_loser - elo_winner) / 400))
    delta = k_factor * (actual - expected)
    return delta
