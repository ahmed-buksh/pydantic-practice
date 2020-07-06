from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str

    # Validate that email should not have ! in it

    # Validate that no field in User should have % in it

    # Parse user via file i.e. sample_user.txt


def playground():
    pass


if __name__ == '__main__':
    playground()
