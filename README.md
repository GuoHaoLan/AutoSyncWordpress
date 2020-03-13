# AutoSyncWordpress
每日更新Wordpress，长期项目

## 如何使用脚本
系统要求：Linux，Python3，curl

创建目录

**mkdir -p /data/home/wordpress**

如果你不需要这个地址请改变量dir为你需要的目录，**请注意! 目录不需要用/结尾，而且必须是绝对路径，例如/data**

然后在Crontab中添加

**00 00 * * * /usr/bin/python3 /path/to/wp.py**

/path/to改为你wp.py文件目录，例如/root


