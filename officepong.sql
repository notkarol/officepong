
CREATE TABLE IF NOT EXISTS player (
    id INTEGER PRIMARY KEY,
    name VARCHAR(16) UNIQUE NOT NULL,
    elo FLOAT DEFAULT 1500 NOT NULL,
    games INTEGER DEFAULT 0 NOT NULL,
    win_rate FLOAT DEFAULT 0 NOT NULL
);

CREATE TABLE IF NOT EXISTS team (
    id INTEGER PRIMARY KEY,
    player1_id INTEGER NOT NULL,
    player2_id INTEGER NOT NULL,
    elo FLOAT DEFAULT 1500 NOT NULL,
    games INTEGER DEFAULT 0 NOT NULL,
    win_rate FLOAT DEFAULT 0 NOT NULL,
    FOREIGN KEY (player1_id) REFERENCES player(id),
    FOREIGN KEY (player2_id) REFERENCES player(id)
);

CREATE TABLE IF NOT EXISTS singles_match (
    timestamp INTEGER PRIMARY KEY,
    win_user_id INTEGER NOT NULL,
    lose_user_id INTEGER NOT NULL,
    win_score INTEGER NOT NULL,
    lose_score INTEGER NOT NULL,
    expected_percent FLOAT NOT NULL,
    elo_delta FLOAT NOT NULL,
    FOREIGN KEY (win_user_id) REFERENCES player(id),
    FOREIGN KEY (lose_user_id) REFERENCES player(id)
);

CREATE TABLE IF NOT EXISTS doubles_match (
    timestamp INTEGER PRIMARY KEY,
    win_team_id INTEGER NOT NULL,
    lose_team_id INTEGER NOT NULL,
    win_score INTEGER NOT NULL,
    lose_score INTEGER NOT NULL,
    expected_percent FLOAT NOT NULL,
    elo_delta FLOAT NOT NULL,
    FOREIGN KEY (win_team_id) REFERENCES team(id),
    FOREIGN KEY (lose_team_id) REFERENCES team(id)
);

-- INSERT INTO single_match VALUES (NULL, 16, 17, 15, 13, 0.5, 25);