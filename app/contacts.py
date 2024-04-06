from dataclasses import dataclass

@dataclass
class Contact:
    name: str
    number: int
    email: str
    address: str


CONTACTS = [
    Contact(
        "Ryan",
        5555555555,
        "hello@gmail.com",
        "1234 blueberry lane"
    ),

        Contact(
        "Emma",
        4578392234,
        "emma@gmail.com",
        "1234 chocolate lane"
    ),

        Contact(
        "Aurora",
        5678342222,
        "aurora@gmail.com",
        "1234 strawberry lane"
    ),

        Contact(
        "Kristin",
        5555555555,
        "kristin@gmail.com",
        "1234 cheesecake lane"
    )
]