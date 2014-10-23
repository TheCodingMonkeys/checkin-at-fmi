# Хардуерни зависимости:
* Virtual Private Server
* >= 1GB RAM
* >= RAM
* >= 10GB HHD

# Софтуерни зависимости:
* python 2.7
* virtualenv (Виртуална среда за python проекти)
* pip 1.5.4 (Програма за менижиране на python пакети)
* python-dev (header files and )

## Важно!
Пакетите, които се изискват са специфични за Ubuntu базирани Linux дистрибуции.  

Как се инсталират тези пакети:
```
sudo apt-get install python-pip
```

# Инсталиране на python 2.7, virtualenv и pip 1.5.4
```
sudo apt-get install python
sudo apt-get install python-virtualenv
sudo apt-get install python-pip
```

# Стартиране на виртуална среда за работа с python 2.7
```
virtualenv <the path where you want to place it> -p <path to python2.7>
source <the path where you placed it>bin/activate
```

# Свалане на проекта.
Най-новата версия на проекта може да бъде намерена в GitHub на адрес: https://github.com/TheCodingMonkeys/checkin-at-fmi
```
git clone https://github.com/TheCodingMonkeys/checkin-at-fmi.git
```

# Инсталиране на зависимости
```
sudo apt-get install python-dev
sudo apt-get install libmysqlclient-dev
pip install -r requirements/base.txt
```

# Създаване на базата данни
Проекта работи с MySQL, PostreSQL, SQLite бази дани. Примера по-доло е за MySQL база данни.

```
sudo apt-get install mysql-server
# server should be started automatically, but just in case restart it
sudo service mysql restart
mysql -u root -p
# now you should be prompted to enter your password
# and if you authed correctly
CREATE DATABASE <dbname> CHARACTER SET utf8;
```
