-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: avrn_rfiddb
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `trn_povendors`
--

DROP TABLE IF EXISTS `trn_povendors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trn_povendors` (
  `I_POID` int(11) NOT NULL AUTO_INCREMENT,
  `I_VendorID` int(11) NOT NULL,
  `V_PONumber` varchar(50) DEFAULT NULL,
  `V_RMCode` varchar(50) DEFAULT NULL,
  `Dt_PODate` date DEFAULT NULL,
  `Dt_ToDate` date DEFAULT '0000-00-00',
  `I_QuantityOrdered` int(11) DEFAULT NULL,
  `I_QuantityReceived` int(11) DEFAULT '0',
  `B_IsCompleted` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT '0',
  `I_CreatedBy` int(11) DEFAULT '0',
  `Dt_Created` datetime DEFAULT '0000-00-00 00:00:00',
  `I_UpdatedBy` int(11) DEFAULT '0',
  `Dt_Updated` datetime DEFAULT '0000-00-00 00:00:00',
  `Dt_LastUpdated` datetime DEFAULT '0000-00-00 00:00:00',
  `DisplayFlag` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT '1',
  PRIMARY KEY (`I_POID`),
  KEY `I_VendorID_idx` (`I_VendorID`),
  CONSTRAINT `I_VendorID` FOREIGN KEY (`I_VendorID`) REFERENCES `mst_vendor` (`I_VendorID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trn_povendors`
--

LOCK TABLES `trn_povendors` WRITE;
/*!40000 ALTER TABLE `trn_povendors` DISABLE KEYS */;
INSERT INTO `trn_povendors` VALUES (1,3,'11','1125','2020-01-11','2020-01-15',8,6,'0',42,'2020-01-11 00:00:00',43,'2020-01-11 00:00:00','2020-01-16 15:19:47','1'),(3,4,'34','1123','2020-01-11','2020-01-19',9,2,'0',22,'2020-01-11 00:00:00',23,'2020-01-11 00:00:00','2020-01-16 15:19:53','1'),(12,5,'14','1145','2020-01-11','0000-00-00',6,3,'0',0,'2020-01-11 16:08:11',0,'0000-00-00 00:00:00','2020-01-16 15:20:02','1'),(13,7,'12','2234','2020-01-12','0000-00-00',7,4,'0',0,'2020-01-12 14:21:58',0,'0000-00-00 00:00:00','2020-01-16 15:20:07','1'),(16,8,'20','11667','2020-01-12','0000-00-00',9,7,'0',0,'2020-01-12 16:42:24',0,'0000-00-00 00:00:00','2020-01-16 15:17:53','1'),(17,9,'97','900','2020-01-12','0000-00-00',10,6,'0',0,'2020-01-12 17:14:58',0,'0000-00-00 00:00:00','2020-01-16 22:21:12','0');
/*!40000 ALTER TABLE `trn_povendors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-18 15:35:57
