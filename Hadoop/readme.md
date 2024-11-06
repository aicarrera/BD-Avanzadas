##Iniciar docker
docker-compose up -d
##Entrar al namenode 
docker exec -ti hadoop-namenode-1 /bin/bash
##install nano if needed
yum install -y nano
##Listar los archivos una vez entrado al namenode
hdfs dfs -ls /
##Get Hadoop home
echo $HADOOP_HOME
##Check current directory 
pwd
##Crear un directorio
hdfs dfs -mkdir /input 
hdfs dfs -mkdir /output

hdfs dfs -put scripts/wordcount/book.txt /input/
##Find Hadoop Streaming jar
find / -name "hadoop-streaming-*.jar"

## Revisar que en los archivos python el final de la linea sea compatible con Linux, no CRLF sino LF
## test python
cat scripts/wordcount/bitcoin_tweets.csv | python scripts/wordcount/mappertweet.py
##Hadoop Streaming
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
  -input /input/book.txt \
  -output /output/output1.txt \
  -mapper /opt/hadoop/scripts/wordcount/mapper.py \
  -reducer /opt/hadoop/scripts/wordcount/reducer.py \
  -verbose


hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
  -input /input/bitcoin_tweets.csv \
  -output /output/output1.txt \
  -mapper /opt/hadoop/scripts/wordcount/mappertweet.py \
  -reducer /opt/hadoop/scripts/wordcount/reducer.py \
## Como ver la salida
 hadoop fs -cat /output/output1.txt/part-*