# run a new postgresql DB
docker run --name db \
     -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
     -e POSTGRES_USER=$POSTGRES_USER \
     -e PGDATA=/var/lib/postgresql/data/pgdata \
     -e POSTGRES_DB=postgres \
     -v ./data:/var/lib/postgresql/data/pgdata \
     -d -p 5432:5432 postgres
