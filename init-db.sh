#!/bin/bash
docker-compose up -d db
sleep 10
docker-compose exec db psql -U user -d dbname -c "CREATE DATABASE dbname;"
docker-compose exec db psql -U user -d dbname -c "CREATE USER user WITH PASSWORD 'password';"
docker-compose exec db psql -U user -d dbname -c "ALTER ROLE user SET client_encoding TO 'utf8';"
docker-compose exec db psql -U user -d dbname -c "ALTER ROLE user SET default_transaction_isolation TO 'read committed';"
docker-compose exec db psql -U user -d dbname -c "ALTER ROLE user SET timezone TO 'UTC';"
docker-compose exec db psql -U user -d dbname -c "GRANT ALL PRIVILEGES ON DATABASE dbname TO user;"
