DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS chat;

CREATE TABLE user (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `username` VARCHAR(30) NOT NULL,
  `password` VARCHAR(255) NOT NULL
);


CREATE TABLE chat (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int,
  `msgs` JSON,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  FOREIGN KEY (user_id) REFERENCES user(id) 
);

