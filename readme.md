# Bookstore-django

## Introduction

This project is a dummy REST API to add/edit/delete books and book authors built with Django Rest Framework. This readme file provides instructions on how to build and run this app using Docker.

## Prerequisites

You need to have [Docker ](https://docs.docker.com/get-docker/)installed on your local machine. Make sure you also have [Docker Compose](https://docs.docker.com/compose/install/) installed.

## Getting Started

### 1. Clone the Repository

First, clone the repository to your local machine. Run the folloring command inside your terminal:

```
git clone https://github.com/osydorchuk89/bookstore.git
```

Next, navigate to the newly created directory:

```
cd bookstore
```

### 2. Build the Docker image and run the Docker container

To build the image and run the docker container, use the following command:

```
docker compose up -d
```

### 3. Access the application

Open a web browser and go to `http://localhost:8000` to access the application running in the Docker container.

## Stopping and removing the container

To stop the running container and remove it, use the following command:

```
docker compose down
```
