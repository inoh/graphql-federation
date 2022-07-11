import typing
import strawberry


products = [
    {
        "id": "30c4dbc0-71a9-487c-91cd-ea316ffa96c8",
        "name": "実践ドメイン駆動設計",
        "user_id": "6af68b0a-a1df-4ba0-bcf9-8a44f5057dcd",
        "price": 5200,
    },
    {
        "id": "6a0b0f62-97b6-4f65-b3bf-c0744cb98fa9",
        "name": "もっとさがして にゃんこ大戦争",
        "user_id": "6af68b0a-a1df-4ba0-bcf9-8a44f5057dcd",
        "price": 1000,
    },
    {
        "id": "7f090e58-c276-43d7-9984-72347aae88de",
        "name": "スマッシュブラザース",
        "user_id": "5cd03c42-2b15-48dd-82d4-ba1c22a37042",
        "price": 5980,
    },
]


@strawberry.federation.type(keys=['id'])
class Product:
    id: strawberry.ID
    name: str
    price: int

    @classmethod
    def resolve_reference(cls, id: strawberry.ID):
        product = next(filter(lambda product: product["id"] == id, products), None)
        return Product(id=product["id"], name=product["name"], price=product["price"])


def get_purchases(root: "User") -> typing.List[Product]:
    return [
        Product(id=product["id"], name=product["name"], price=product["price"])
        for product in filter(lambda product: product["user_id"] == root.id, products)
    ]


@strawberry.federation.type(extend=True, keys=["id"])
class User:
    id: strawberry.ID = strawberry.federation.field(external=True)
    purchases: typing.List[Product] = strawberry.field(resolver=get_purchases)

    @classmethod
    def resolve_reference(cls, id: strawberry.ID):
        return User(id=id)


@strawberry.type
class Query:
    _service: typing.Optional[str]

schema = strawberry.federation.Schema(query=Query, types=[User, Product])
