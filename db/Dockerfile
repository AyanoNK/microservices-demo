# Dockerfile for PostgreSQL
FROM postgres:latest
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=blogs

EXPOSE 5432

COPY init.sql /docker-entrypoint-initdb.d/
