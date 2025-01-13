## Set up Sharding using Docker Containers

### Config servers
Start config servers (3 member replica set)
```
docker-compose -f config-server/docker-compose.yaml up -d
```
To erase all volumes if needed
```
docker-compose down --volumes --remove-orphans
docker volume rm cfgsvr1 cfgsvr2 cfgsvr3
```


Initiate bash in any configuration server
```
docker exec -it cfgsvr1 bash
```

Entrar a mongo
```
mongosh --host localhost --port 27017
```
Revisar el status del replica set
```
rs.status()
```
Iniciar el configuration server.
```
rs.initiate({
  _id: "cfgrs",
  configsvr: true,
  members: [
    { _id: 0, host: "cfgsvr1:27017" },
    { _id: 1, host: "cfgsvr2:27017" },
    { _id: 2, host: "cfgsvr3:27017" }
  ]
});

rs.status()
```

### Shard 1 servers
Start shard 1 servers (3 member replicas set)
```
docker-compose -f shard1/docker-compose.yaml up -d
```
Initiate bash en shard
```
docker exec -it shard1svr1 bash
```

Entrar a mongo
```
mongosh --host localhost --port 27017
```
```
rs.initiate({
  _id: "shard1rs",
  members: [
    { _id: 0, host: "shard1svr1:27017" },
    { _id: 1, host: "shard1svr2:27017" },
    { _id: 2, host: "shard1svr3:27017" }
  ]
});
rs.status()
```

### Mongos Router
Start mongos query router
```
docker-compose -f mongos/docker-compose.yaml up -d
```

### Add shard to the cluster
Connect to mongos
```
mongo mongodb://192.168.1.81:60000
```
Add shard
```
mongos>  sh.addShard("shard1rs/shard1svr1:27017,shard1svr2:27017,shard1svr3:27017")
mongos> sh.status()
```
## Adding another shard
### Shard 2 servers
Start shard 2 servers (3 member replicas set)
```
docker-compose -f shard2/docker-compose.yaml up -d
```
Initiate replica set
```
mongo mongodb://192.168.1.81:50004
```
```
rs.initiate(
  {
    _id: "shard2rs",
    members: [
      { _id : 0, host : "192.168.1.81:50004" },
      { _id : 1, host : "192.168.1.81:50005" },
      { _id : 2, host : "192.168.1.81:50006" }
    ]
  }
)

rs.status()
```
### Add shard to the cluster
Connect to mongos
```
mongo mongodb://192.168.1.81:60000
```
Add shard
```
mongos> sh.addShard("shard2rs/192.168.1.81:50004,192.168.1.81:50005,192.168.1.81:50006")
mongos> sh.status()
```
