import queries

print("Seeding the database with initial users...")

try:
    # Adding a Manager
    # Parameters: Name, GitHub Username, Role, Login Username, Login Password
    queries.createUserQuery("Jabril Manager", "jabril-github", "manager", "jabril", "pass123")
    print("✅ Manager 'jabril' created! (Password: pass123)")

    # Adding a Developer
    queries.createUserQuery("Debbie Developer", "debbie-github", "developer", "debbie", "pass123")
    print("✅ Developer 'debbie' created! (Password: pass123)")

except Exception as e:
    print(f"❌ Error creating users: {e}")