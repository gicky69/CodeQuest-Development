-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2023 at 01:27 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `users`
--

-- --------------------------------------------------------

--
-- Table structure for table `scores`
--

CREATE TABLE `scores` (
  `user_id` int(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `scores` int(255) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `solved_pset_table`
--

CREATE TABLE `solved_pset_table` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `problem_sets` varchar(255) NOT NULL DEFAULT 'wordcap,ctt,itr'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `solved_pset_table`
--

INSERT INTO `solved_pset_table` (`id`, `user_id`, `problem_sets`) VALUES
(0, 2, 'wordcap'),
(0, 3, 'wordcap'),
(0, 1, 'wordcap'),
(0, 4, 'wordcap'),
(0, 5, 'wordcap'),
(0, 2, 'CTT'),
(0, 6, 'wordcap'),
(0, 6, 'CTT'),
(0, 7, 'wordcap'),
(0, 7, 'CTT'),
(0, 3, 'ITR');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(100) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `scores` int(255) NOT NULL DEFAULT 0,
  `solved_psets` varchar(255) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `scores`, `solved_psets`) VALUES
(1, 'ADMIN3', 'ADMIN3', 0, 'wordcap,'),
(2, 'ADMIN', 'ADMIN', 7, 'CTT,'),
(3, 'Username', 'Password', 1, 'ITR,'),
(4, 'CARL', 'CARL', 1, '0wordcap,'),
(5, 'JIM', 'JIM', 1, '0wordcap,'),
(6, 'LOLOL', 'LOLOL', 2, '0wordcap,CTT,'),
(7, 'carl2', 'carl2', 2, '0wordcap,CTT,'),
(8, 'j', 'j', 0, '0');

-- --------------------------------------------------------

--
-- Table structure for table `users_2`
--

CREATE TABLE `users_2` (
  `id` int(11) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `uniqueID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users_2`
--

INSERT INTO `users_2` (`id`, `username`, `password`, `uniqueID`) VALUES
(6, 'ADMIN', 'ADMIN', 0),
(7, 'Username', 'Password', 0),
(8, 'ADMIN2', 'ADMING2', 0),
(9, 'ADMIN3', 'ADMIN3', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `scores`
--
ALTER TABLE `scores`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `solved_pset_table`
--
ALTER TABLE `solved_pset_table`
  ADD KEY `foreign` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users_2`
--
ALTER TABLE `users_2`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `scores`
--
ALTER TABLE `scores`
  MODIFY `user_id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users_2`
--
ALTER TABLE `users_2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `solved_pset_table`
--
ALTER TABLE `solved_pset_table`
  ADD CONSTRAINT `foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
