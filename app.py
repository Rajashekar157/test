from pydantic import BaseModel

# Define a User model
class User(BaseModel):
    id: int
    name: str
    email: str
# Function to create a user
def create_user(id: int, name: str, email: str) -> User:
    return User(id=id, name=name, email=email)

if __name__ == "__main__":
    try:
        # Valid input
        user = create_user(id=1, name="Alice", email="alice@example.com")
        print(user)

        # Invalid input (email)
        invalid_user = create_user(id=2, name="Bob", email="not-an-email")
        print(invalid_user)
    except str as e:
        print("Error creating user:", e)
