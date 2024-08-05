# Bookstore-django

## Introduction

This project is a dummy REST API to view and (only for registered users) add/edit/delete books and book authors built with Django Rest Framework. This readme file provides instructions on how to build and run this app using Docker.

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

To build the image and run the Docker container, use the following command (make sure that Docker is running before executing this command):

```
docker compose up -d
```

### 3. Access the application

Open a web browser and go to `http://localhost:8000/api/store/` to access the API running in the Docker container.

### 4. API endpoints

Authors:

* GET `api/store/authors/` - list all authors
* POST `api/store/authors/` - add a new author (only for registered users)
* GET `api/store/authors/{author_id}` - retrieve an entry about the author with the given id
* PUT/PATCH `api/store/authors/{author_id}` - update an entry about the author with the given id (only for registered users)
* DELETE `api/store/authors/{author_id}` - delete an entry about the author with the given id (only for registered users)

Books:

* GET `api/store/books/` - list all books
* POST `api/store/books/` - add a new book (only for registered users)
* GET `api/store/books/{book_id}` - retrieve an entry about the book with the given id
* PUT/PATCH `api/store/books/{book_id}` - update an entry about the book with the given id (only for registered users)
* DELETE `api/store/books/{book_id}` - delete an entry about the book with the given id (only for registered users)

## Stopping and removing the container

To stop the running container and remove it, use the following command:

```
docker compose down
```
