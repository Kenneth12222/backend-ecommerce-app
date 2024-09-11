



def create_admin_user(username, password):
    from main import db, User  # Moved inside the function to avoid circular import

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        print(f"User {username} already exists!")
        return

    admin_user = User(username=username, is_admin=True)
    admin_user.set_password(password)
    db.session.add(admin_user)
    db.session.commit()
    print(f"Admin user {username} created successfully!")
