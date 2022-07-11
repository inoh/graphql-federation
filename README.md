# GraphQL Federation

[Introduction to Apollo Federation](https://www.apollographql.com/docs/federation/) の構成を実装しました。

```shell
$ docker-compose up
```

access to: http://localhost:4000

## Testing

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
