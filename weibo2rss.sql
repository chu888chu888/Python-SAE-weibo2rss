--请到SAE导入该SQL语句

CREATE TABLE IF NOT EXISTS `weibo2rss_accesstoken` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` bigint(20) NOT NULL,
  `access_token` varchar(100) NOT NULL,
  `expires_in` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;
