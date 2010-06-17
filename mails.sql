-- phpMyAdmin SQL Dump
-- version 3.3.2deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 14, 2010 at 02:07 PM
-- Server version: 5.1.41
-- PHP Version: 5.3.2-1ubuntu4.2

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `smsmail`
--

-- --------------------------------------------------------

--
-- Table structure for table `mails`
--

CREATE TABLE IF NOT EXISTS `mails` (
  `mailid` int(11) NOT NULL,
  `email` varchar(40) NOT NULL,
  `from` varchar(70) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `mobile` varchar(13) NOT NULL,
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `sent` int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2043 ;

--
-- Dumping data for table `mails`
--

INSERT INTO `mails` (`mailid`, `email`, `from`, `subject`, `mobile`, `id`, `sent`) VALUES
(18, 'internatrails@gmail.com', ' Twitter <twitter-follow-internatrails=gmail.com@p', 'Sarang Basutkar is now following you on Twitter!\r\n\r\n', '+919940138729', 2041, 1),
(17, 'internatrails@gmail.com', ' Twitter <twitter-follow-internatrails=gmail.com@p', 'Karthik Subramanian is now following you on Twitter!\r\n\r\n', '+919940138729', 2040, 1),
(16, 'internatrails@gmail.com', ' Twitter\r\n <twitter-confirmation-internatrails=gma', 'Confirm your Twitter account, internatrails!\r\n\r\n', '+919940138729', 2039, 1),
(15, 'internatrails@gmail.com', ' Vignesh Raju <vignesh2510raju@gmail.com>\r\n\r\n', 'Re: Hey :) you\r\n http://0.0.0.0:3000/maverickhttp://0.0.0.0:3000/maverickhttp://0.0.0.0:3000/maveric', '+919940138729', 2038, 1),
(14, 'internatrails@gmail.com', ' Karthik S <karthik.s.sundaram@gmail.com>\r\n\r\n', 'dasdasd dai dogg\r\n\r\n', '+919940138729', 2037, 1),
(12, 'internatrails@gmail.com', ' Karthik S <karthik.s.sundaram@gmail.com>\r\n\r\n', 'Re: Sending mail from Python\r\n\r\n', '+919940138729', 2035, 1),
(13, 'internatrails@gmail.com', ' Karthik S <karthik.s.sundaram@gmail.com>\r\n\r\n', 'Hey its me!\r\n\r\n', '+919940138729', 2036, 1),
(11, 'internatrails@gmail.com', ' noreply+railsintern10@status.net\r\n\r\n', 'Email address confirmation\r\n\r\n', '+919940138729', 2034, 1),
(10, 'internatrails@gmail.com', ' Vignesh Raju <vignesh2510raju@gmail.com>\r\n\r\n', 'dsgsdf 2\r\n\r\n', '+919940138729', 2033, 1),
(9, 'internatrails@gmail.com', ' Vignesh Raju <vignesh2510raju@gmail.com>\r\n\r\n', 'gfsad 1\r\n\r\n', '+919940138729', 2032, 1),
(8, 'internatrails@gmail.com', ' Vignesh Raju <vignesh2510raju@gmail.com>\r\n\r\n', 'trgfvb\r\n\r\n', '+919940138729', 2031, 1),
(7, 'internatrails@gmail.com', ' Vignesh Raju <vignesh2510raju@gmail.com>\r\n\r\n', 'Fwd: ih\r\n\r\n', '+919940138729', 2030, 1),
(6, 'internatrails@gmail.com', ' Vignesh Raju <vignesh2510raju@gmail.com>\r\n\r\n', 'ih\r\n\r\n', '+919940138729', 2029, 1),
(4, 'internatrails@gmail.com', ' Vignesh Raju <vignesh2510raju@gmail.com>\r\n\r\n', 'hi\r\n\r\n', '+919940138729', 2027, 1),
(5, 'internatrails@gmail.com', ' Vignesh Raju <vignesh2510raju@gmail.com>\r\n\r\n', 'hi * the Grid Display will give you a developer-oriented summary of\r\n recent buildbot activity. * th', '+919940138729', 2028, 1),
(3, 'internatrails@gmail.com', ' Gmail Team <mail-noreply@google.com>\r\n\r\n', 'Customize Gmail with colors and themes\r\n\r\n', '+919940138729', 2026, 1),
(2, 'internatrails@gmail.com', ' Gmail Team <mail-noreply@google.com>\r\n\r\n', 'Import your contacts and old email\r\n\r\n', '+919940138729', 2025, 1),
(1, 'internatrails@gmail.com', ' Gmail Team <mail-noreply@google.com>\r\n\r\n', 'Access Gmail on your mobile phone\r\n\r\n', '+919940138729', 2024, 1),
(23, 'internatrails@gmail.com', ' Vignesh Raju <vignesh2510raju@gmail.com>\r\n\r\n', '=?windows-1252?Q?Fwd=3A_poda_vethu_phpMySQL_=2A_Official_Rack_Website_=2A_I?=\r\n =?windows-1252?Q?ntr', '+919940138729', 2042, 1);
