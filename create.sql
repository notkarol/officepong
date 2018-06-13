CREATE TABLE IF NOT EXISTS player (
    name VARCHAR(16) PRIMARY KEY,
    elo FLOAT DEFAULT 1500
);
CREATE TABLE IF NOT EXISTS match (
    timestamp FLOAT PRIMARY KEY,
    winners VARCHAR(32),
    losers VARCHAR(32),
    winning_score INTEGER,
    losing_score INTEGER
);
