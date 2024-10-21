from pydantic import BaseModel, EmailStr, ValidationError
from typing import List, Optional

# Define an Address model
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

# Define a User model with an address
class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: Optional[Address] = None  # Address is optional
    tags: List[str] = []  # Default to an empty list

# Function to create a user
def create_user(id: int, name: str, email: str, street: Optional[str] = None,
                city: Optional[str] = None, zip_code: Optional[str] = None) -> User:
    address = Address(street=street, city=city, zip_code=zip_code) if street and city and zip_code else None
    return User(id=id, name=name, email=email, address=address)

if __name__ == "__main__":
    try:

        user_with_address = create_user(
            id=1, name="uday", email="uday@gmail.com",
            street="mannguda", city="hyderabad", zip_code="501510"
        )
        print(user_with_address)

        user_without_address = create_user(
            id=2, name="rajashekar", email="rajashekar@gmail.com"
        )
        print(user_without_address)

        invalid_user = create_user(
            id=3, name="umama",email="not-an-email"
        )
        print(invalid_user)

    except ValidationError as e:
        print("Error creating user:", e)
