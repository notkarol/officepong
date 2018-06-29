"""
Store of ELO-related functions.
"""

def calculate_delta(elo_winner, elo_loser, score_winner, score_loser, k_factor=5):
    """
    A custom ELO calculation that takes in account how much the winner
    won by. This allows us to score games on a deeper level than just
    win-lose but some statistical properties are mollified a bit.

    args:
      elo_winner: winner's elo points
      elo_winner: loser's elo points
      score_winner: winner's point value
      score_winner: loser's point value
    kwargs:
      k_factor: How much to multiply delta by. (default: 5)
    """
    n_points = score_winner + score_loser
    actual = score_winner / n_points
    expected = 1 / (1 + 10 ** ((elo_loser - elo_winner) / 400))
    delta = n_points * k_factor * (actual - expected)
    return actual, expected, delta
    
