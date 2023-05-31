USE Messenger;

CREATE TABLE messages (
  id INT AUTO_INCREMENT PRIMARY KEY,
  sender VARCHAR(50),
  received VARCHAR(50),
  text TEXT,
  send_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50),
  password VARCHAR(50),
  usertype VARCHAR(50),
  email VARCHAR(100)
);
