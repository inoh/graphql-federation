import typing
import strawberry


users = [
    {
        "id": "6af68b0a-a1df-4ba0-bcf9-8a44f5057dcd",
        "name": "inoue"
    },
    {
        "id": "5cd03c42-2b15-48dd-82d4-ba1c22a37042",
        "name": "watanabe"
    },
    {
        "id": "68658431-cd2c-417b-b7b5-8ac26ed78a42",
        "name": "kiyotani"
    },
]


@strawberry.federation.type(keys=['id'])
class User:
    id: strawberry.ID
    name: str

    @classmethod
    def resolve_reference(cls, id: strawberry.ID):
        user = next(filter(lambda review: review["id"] == id, users), None)
        return User(id=id, name=user["name"])


def get_all_users() -> typing.List[User]:
    return [User(id=user["id"], name=user["name"]) for user in users]


@strawberry.type
class Query:
    all_users: typing.List[User] = strawberry.field(resolver=get_all_users)


schema = strawberry.federation.Schema(query=Query, types=[User])
