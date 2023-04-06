DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS chat;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE chat (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  user_input TEXT NOT NULL,
  bot_response TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id)
);