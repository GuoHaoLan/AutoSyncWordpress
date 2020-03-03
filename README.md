# AutoSyncWordpress
每日更新Wordpress，长期项目

## 如何使用脚本
系统要求：Linux，Python3，curl

创建目录
mkdir -p /data/home/wordpress

如果你不需要这个地址请改源码
然后在Crontab中添加
00 00 * * * /usr/bin/python3 /path/to/wp.py
/path/to改为你wp.py文件目录，例如/root



## 国内Wordpress镜像

http://demosisto.cn/wordpress/latest.zip

每日EST时间12点自动同步Wordpress
