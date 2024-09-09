-- Tabela de dispositivos
CREATE TABLE devices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mac_address VARCHAR(255) UNIQUE,
    name VARCHAR(255),
    status ENUM('paired', 'unpaired'),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

