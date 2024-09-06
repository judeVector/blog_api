# Blog API Project

This is a Django-based Blog API for creating, reading, updating, and deleting blog posts. The API supports token-based authentication and includes features such as pagination, post author assignment, and more.

## Features

- **Create Post**: Authenticated users can create blog posts.
- **List Posts**: Anyone can view the list of blog posts.
- **Update Post**: Only the author of the post can update it.
- **Delete Post**: Only the author of the post can delete it.
- **Pagination**: Supports pagination of posts.
- **Authentication**: Token-based authentication (JWT).

## Technologies Used

- **Django**: The web framework used to build the API.
- **Django REST Framework**: Used for building the API endpoints.
- **PostgreSQL**: The database used for storing blog posts.
- **Supabase**: Database service for PostgreSQL.
- **Railway**: Hosting service for the production environment.

## Installation

### Requirements

- Python 3.9+
- PostgreSQL
- Django 4.x
- Django REST Framework
- djangorestframework-simplejwt (for JWT authentication)
