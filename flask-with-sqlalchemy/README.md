# API
+ GET /users  
    + __response__
        + `[{"id": id, "name": "name", "email": "email"}, ...]`
+ POST /users
    + __request__
        + `{"name": "name", "email": "email"}`
    + __response__
        + `{"message": "User added successfully"}`
+ DELETE /users
    + __request__
        + `{"user_id": user_id}`
    + __response__
        + `{"message": "User deleted successfully"}`

# Edit
+ __models.py__
    + `DATABASE_URL`
