
CREATE TABLE `event` (
  `event_id` int NOT NULL AUTO_INCREMENT,
  `event_name` varchar(100) NOT NULL,
  `event_category` varchar(100) NOT NULL,
  `event_date` date NOT NULL,
  `event_time` time NOT NULL,
  `place_address` varchar(255) DEFAULT NULL,
  `event_place` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `place` (
  `place_id` int NOT NULL AUTO_INCREMENT,
  `event_id` int DEFAULT NULL,
  `place_name` varchar(255) DEFAULT NULL,
  `place_address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`place_id`),
  KEY `event_id` (`event_id`),
  CONSTRAINT `place_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `event` (`event_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;