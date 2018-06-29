CREATE TABLE IF NOT EXISTS player (
    name VARCHAR(16) PRIMARY KEY,
    elo FLOAT DEFAULT 1500 NOT NULL,
    games INTEGER DEFAULT 0 NOT NULL
);
CREATE TABLE IF NOT EXISTS match (
    timestamp INTEGER NOT NULL,
    winners VARCHAR(32) NOT NULL,
    losers VARCHAR(32) NOT NULL,
    winning_score INTEGER NOT NULL,
    losing_score INTEGER NOT NULL,
    actual FLOAT NOT NULL,
    expected FLOAT NOT NULL,
    delta FLOAT NOT NULL
);
