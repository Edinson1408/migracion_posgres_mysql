# mssql-python3.6-pyodbc
# Python runtime with pyodbc to connect to SQL Server
FROM ubuntu:18.04

# apt-get and system utilities
RUN apt-get update && apt-get install -y \
    curl wget unzip apt-utils libaio1 apt-transport-https debconf-utils gcc build-essential g++-5\
    && rm -rf /var/lib/apt/lists/*

#
RUN mkdir /opt/oracle
WORKDIR /opt/oracle
RUN wget https://download.oracle.com/otn_software/linux/instantclient/214000/instantclient-basic-linux.x64-21.4.0.0.0dbru.zip
RUN unzip instantclient-basic-linux.x64-21.4.0.0.0dbru.zip
RUN apt-get update && apt-get install libaio1
RUN sh -c "echo /opt/oracle/instantclient_21_4 > /etc/ld.so.conf.d/oracle-instantclient.conf"
RUN ldconfig
#

# adding custom MS repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# install libssl - required for sqlcmd to work on Ubuntu 18.04
RUN apt-get update && apt-get install -y libssl1.0.0 libssl-dev

# install SQL Server drivers
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev

# install SQL Server tools
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"

# python libraries
RUN apt-get update && apt-get install -y \
    python3-pip python3.8 python3-setuptools \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# install necessary locales
RUN apt-get update && apt-get install -y locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen
RUN pip3 install --upgrade pip

# install SQL Server Python SQL Server connector module - pyodbc
RUN pip3 install pyodbc
# install Oracle connector
RUN pip3 install cx_Oracle
# install additional utilities
RUN apt-get update && apt-get install gettext nano vim -y
#RUN apt-get install -y libmysqlclient-dev
RUN pip3 install sqlalchemy
RUN pip3 install pymysql
RUN pip3 install pandas
RUN pip3 install boto3
RUN pip3 install pyyaml
RUN pip3 install s3fs
#RUN apt-get install python-boto3
# add sample code

ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING utf8
RUN mkdir /xpedition
ADD . /xpedition
WORKDIR /xpedition

CMD  ALLCLI=true python3 main.py