import typing
import strawberry


reviews = [
    {
        "id": "f77d2ace-dbfe-406a-8254-bdcf66d9dd47",
        "body": "難しい",
        "author_id": "68658431-cd2c-417b-b7b5-8ac26ed78a42", # kiyotani
        "product_id": "30c4dbc0-71a9-487c-91cd-ea316ffa96c8", # 実践ドメイン駆動設計
    },
    {
        "id": "8aac307b-b642-43d7-9762-f942aae380d2",
        "body": "つまらない",
        "author_id": "6af68b0a-a1df-4ba0-bcf9-8a44f5057dcd", # inoue
        "product_id":"7f090e58-c276-43d7-9984-72347aae88de", # スマッシュブラザース
    },
    {
        "id": "e49733e4-df61-4a44-9b68-f47157db1944",
        "body": "面白い",
        "author_id": "68658431-cd2c-417b-b7b5-8ac26ed78a42", # kiyotani
        "product_id": "7f090e58-c276-43d7-9984-72347aae88de", # スマッシュブラザース
    },
]


def get_user_reviews(root: "User"):
    return [
        Review(
            id=review["id"],
            body=review["body"],
            author=User(id=review["author_id"]),
            product=Product(id=review["product_id"]),
        )
        for review in filter(lambda review: review["author_id"] == root.id, reviews)
    ]


def get_product_reviews(root: "Product"):
    return [
        Review(
            id=review["id"],
            body=review["body"],
            author=User(id=review["author_id"]),
            product=Product(id=review["product_id"]),
        )
        for review in filter(lambda review: review["product_id"] == root.id, reviews)
    ]

@strawberry.type
class Review:
    id: strawberry.ID
    body: str
    author: "User"
    product: "Product"


@strawberry.federation.type(extend=True, keys=["id"])
class User:
    id: strawberry.ID = strawberry.federation.field(external=True)
    reviews: typing.List[Review] = strawberry.field(resolver=get_user_reviews)

    @classmethod
    def resolve_reference(cls, id: strawberry.ID):
        return User(id=id)


@strawberry.federation.type(extend=True, keys=["id"])
class Product:
    id: strawberry.ID = strawberry.federation.field(external=True)
    reviews: typing.List[Review] = strawberry.field(resolver=get_product_reviews)

    @classmethod
    def resolve_reference(cls, id: strawberry.ID):
        return Product(id=id)


@strawberry.type
class Query:
    _service: typing.Optional[str]

schema = strawberry.federation.Schema(query=Query, types=[Review, User, Product])
