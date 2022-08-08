# GraphQL Federation

[Introduction to Apollo Federation](https://www.apollographql.com/docs/federation/) の構成を実装しました。

```shell
$ docker-compose up
```

access to: http://localhost:4000

## Testing

#### Query

以下のクエリを実行します。

```graphql
query ExampleQuery {
  allUsers {
    name
    purchases {
      name
      price
      reviews {
        ...reviewFields
        author {
          name
        }
      }
    }
    reviews {
      ...reviewFields
      product {
        name
      }
    }
  }
}
fragment reviewFields on Review {
  body
}
```

これらが返ってきます。

```json
{
  "data": {
    "allUsers": [
      {
        "name": "inoue",
        "purchases": [
          {
            "name": "実践ドメイン駆動設計",
            "price": 5200,
            "reviews": [
              {
                "body": "難しい",
                "author": {
                  "name": "kiyotani"
                }
              }
            ]
          },
          {
            "name": "もっとさがして にゃんこ大戦争",
            "price": 1000,
            "reviews": []
          }
        ],
        "reviews": [
          {
            "body": "つまらない",
            "product": {
              "name": "スマッシュブラザース"
            }
          }
        ]
      },
      {
        "name": "watanabe",
        "purchases": [
          {
            "name": "スマッシュブラザース",
            "price": 5980,
            "reviews": [
              {
                "body": "つまらない",
                "author": {
                  "name": "inoue"
                }
              },
              {
                "body": "面白い",
                "author": {
                  "name": "kiyotani"
                }
              }
            ]
          }
        ],
        "reviews": []
      },
      {
        "name": "kiyotani",
        "purchases": [],
        "reviews": [
          {
            "body": "難しい",
            "product": {
              "name": "実践ドメイン駆動設計"
            }
          },
          {
            "body": "面白い",
            "product": {
              "name": "スマッシュブラザース"
            }
          }
        ]
      }
    ]
  }
}
```

#### Mutation

以下のクエリを実行します。

```graphql
mutation {
  review1: addReview(body: "また読みたいです！", authorId: "5cd03c42-2b15-48dd-82d4-ba1c22a37042", productId: "30c4dbc0-71a9-487c-91cd-ea316ffa96c8") {
    ...reviewFields
  }
  review2: addReview(body: "勉強になりました", authorId: "5cd03c42-2b15-48dd-82d4-ba1c22a37042", productId: "6a0b0f62-97b6-4f65-b3bf-c0744cb98fa9") {
    ...reviewFields
  }
}
fragment reviewFields on Review {
  id
  author {
    name
  }
  product {
    name
  }
}
```

登録した結果が返却される。

```json
{
  "data": {
    "review1": {
      "id": "85b67178-5a41-4a1a-8395-a4d8812d3073",
      "author": {
        "name": "watanabe"
      },
      "product": {
        "name": "実践ドメイン駆動設計"
      }
    },
    "review2": {
      "id": "cc650f6c-39ad-4610-9d08-d809bb6fe4d6",
      "author": {
        "name": "watanabe"
      },
      "product": {
        "name": "もっとさがして にゃんこ大戦争"
      }
    }
  }
}
```

取得クエリを再度取得すると、追加されたレビューも返却される。

```json
{
  "data": {
    "allUsers": [
      {
        "id": "6af68b0a-a1df-4ba0-bcf9-8a44f5057dcd",
        "name": "inoue",
        "purchases": [
          {
            "id": "30c4dbc0-71a9-487c-91cd-ea316ffa96c8",
            "name": "実践ドメイン駆動設計",
            "price": 5200,
            "reviews": [
              {
                "body": "難しい",
                "author": {
                  "name": "kiyotani"
                }
              },
              {
                "body": "また読みたいです！",
                "author": {
                  "name": "watanabe"
                }
              }
            ]
          },
          {
            "id": "6a0b0f62-97b6-4f65-b3bf-c0744cb98fa9",
            "name": "もっとさがして にゃんこ大戦争",
            "price": 1000,
            "reviews": [
              {
                "body": "勉強になりました",
                "author": {
                  "name": "watanabe"
                }
              }
            ]
          }
        ],
        "reviews": [
          {
            "body": "つまらない",
            "product": {
              "name": "スマッシュブラザース"
            }
          }
        ]
      },
      {
        "id": "5cd03c42-2b15-48dd-82d4-ba1c22a37042",
        "name": "watanabe",
        "purchases": [
          {
            "id": "7f090e58-c276-43d7-9984-72347aae88de",
            "name": "スマッシュブラザース",
            "price": 5980,
            "reviews": [
              {
                "body": "つまらない",
                "author": {
                  "name": "inoue"
                }
              },
              {
                "body": "面白い",
                "author": {
                  "name": "kiyotani"
                }
              }
            ]
          }
        ],
        "reviews": [
          {
            "body": "また読みたいです！",
            "product": {
              "name": "実践ドメイン駆動設計"
            }
          },
          {
            "body": "勉強になりました",
            "product": {
              "name": "もっとさがして にゃんこ大戦争"
            }
          }
        ]
      },
      {
        "id": "68658431-cd2c-417b-b7b5-8ac26ed78a42",
        "name": "kiyotani",
        "purchases": [],
        "reviews": [
          {
            "body": "難しい",
            "product": {
              "name": "実践ドメイン駆動設計"
            }
          },
          {
            "body": "面白い",
            "product": {
              "name": "スマッシュブラザース"
            }
          }
        ]
      }
    ]
  }
}
```
