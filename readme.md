# Advanced Authentication Project

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Django](https://img.shields.io/badge/Django-5.1-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Build Status](https://img.shields.io/badge/Build-Passing-success.svg)

This project implements advanced authentication mechanisms using Django, Django REST Framework (DRF), and third-party libraries like `djoser`, `django-allauth`, and `django-oauth-toolkit`. The project includes features such as JWT authentication, OAuth2, and social authentication with providers like Google, GitHub, and Facebook.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Authentication Methods](#authentication-methods)
   - [JWT Authentication](#1-jwt-authentication)
   - [OAuth2 Authentication](#2-oauth2-authentication)
   - [Social Authentication](#3-social-authentication)
4. [Security Best Practices](#security-best-practices)
5. [Setup Instructions](#setup-instructions)
6. [Customization](#customization)
7. [Study Section](#study-section)
   - [Djoser Serializers](#djoser-serializers)
   - [Token-Based Authentication](#token-based-authentication)
   - [JSON Web Token (JWT) Authentication](#json-web-token-jwt-authentication)
8. [Mixins in Django](#mixins-in-django)
9. [Logout Behavior in JWT](#logout-behavior-in-jwt)

---

## Overview

This project demonstrates how to implement secure and scalable authentication mechanisms for modern web applications. It includes:

- **JWT Authentication**: Stateless token-based authentication.
- **OAuth2**: Secure API access using the OAuth2 framework.
- **Social Authentication**: Login with third-party providers like Google, GitHub, and Facebook.

---

## Features

- **JWT Authentication**: Secure API access with token-based authentication.
- **OAuth2**: Implemented using `django-oauth-toolkit`.
- **Social Authentication**: Integrated with `django-allauth` for Google, GitHub, and Facebook login.
- **Custom User Model**: Extended Django's default user model for additional fields.
- **Security Best Practices**: Includes token revocation, rate limiting, and secure storage.

---

## Authentication Methods

### **1. JWT Authentication**

- **Library**: `djangorestframework-simplejwt`
- **Features**:
  - Token generation and refresh.
  - Blacklisting for token revocation.
  - Stateless authentication for APIs.

### **2. OAuth2 Authentication**

- **Library**: `django-oauth-toolkit`
- **Features**:
  - Implements OAuth2 provider and client.
  - Secure API access with OAuth2 scopes and grants.
  - Token management and refreshing.

### **3. Social Authentication**

- **Library**: `django-allauth`
- **Features**:
  - Login with Google, GitHub, and Facebook.
  - Link social accounts to existing users.
  - Customize login, signup, and profile management.

---

## Security Best Practices

- Use `httpOnly` cookies for secure JWT storage.
- Implement token revocation and blacklisting.
- Protect endpoints with rate limiting (`django-ratelimit`).
- Use `django.middleware.security.SecurityMiddleware`.

---

## Setup Instructions

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/advanced-authentication.git
cd advanced-authentication
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Configure Environment Variables**

Create a `.env` file in the root directory and add the following:

```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
OAuth2_google_client_id=your_google_client_id
OAuth2_google_secret_key=your_google_secret_key
```

### **4. Apply Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Run the Development Server**

```bash
python manage.py runserver
```

---

## Customization

### **Custom User Model**

The project uses a custom user model (`CustomUser`) to extend Django's default user model. Additional fields like `first_name`, `last_name`, and `email` are included.

### **Custom Djoser Serializers**

To customize user registration, the `UserCreateSerializer` is extended:

```python
class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
```

---

## Study Section

### **Djoser Serializers**

Djoser provides default serializers for user authentication tasks. Some important ones include:

- `UserCreateSerializer`: Handles user registration.
- `UserSerializer`: Returns user details.
- `TokenCreateSerializer`: Manages token creation.

### **Token-Based Authentication**

- Stateless authentication using tokens.
- Tokens are stored in the client (e.g., local storage or cookies).
- Tokens are validated on every request.

### **JSON Web Token (JWT) Authentication**

- **Library**: `djangorestframework-simplejwt`
- **Features**:
  - Compact, self-contained tokens.
  - Stateless authentication.
  - Includes token expiration, refresh, and blacklisting.

---

## Mixins in Django

Mixins are reusable classes that provide additional functionality to Django views or models. They are commonly used in:

- **Class-Based Views (CBVs)**.
- **Django REST Framework (DRF) views**.
- **Django models**.

---

## Logout Behavior in JWT

### **Default Behavior**

JWTs are stateless, so logging out does not automatically invalidate the token. The client must delete the token from local storage or cookies.

### **Proper Logout Handling**

1. **Enable Token Blacklisting**:
   Use the `rest_framework_simplejwt.token_blacklist` app to revoke tokens.
2. **Store JWT in HTTP-Only Cookies**:
   Delete the cookies on logout to invalidate the session.


## API Documentation by Swagger

The project includes Swagger API documentation for easy testing and exploration of the API endpoints.

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

Swagger provides an interactive UI to test API endpoints, while ReDoc offers a clean and responsive API documentation interface.

---

This section has been added to the **README.md** file at the appropriate location. Let me know if you need further adjustments!

---

This document provides a structured overview of the project and its features. For more details, refer to the source code or the official documentation of the libraries used.
