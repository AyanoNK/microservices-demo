# microservices-demo

Microservices demo using Python

```bash
docker network create --driver overlay blog --attachable
docker swarm init
docker stack deploy -c docker-compose.yml blogstack
```

### List all running services within the Swarm orchestrator

```bash
docker service ls
```

### List all tasks within the Swarm orchestrator

```bash
docker service ps [service_name]
```

For example

```bash
docker service ps blogstack_blogsvc
```

To scale a service

```bash
docker service scale blogstack_[service_name]=3
```

For example

```bash
docker service scale blogstack_usersvc=3
```

To shutdown the stack,

```bash
docker swarm leave
```
