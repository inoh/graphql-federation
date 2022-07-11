const { ApolloServer } = require("apollo-server");
const { ApolloGateway, IntrospectAndCompose } = require("@apollo/gateway");

const gateway = new ApolloGateway({
  supergraphSdl: new IntrospectAndCompose({
    subgraphs: [
      { name: "users", url: "http://users:8000/graphql" },
      { name: "products", url: "http://products:8000/graphql" },
      { name: "reviews", url: "http://reviews:8000/graphql" },
    ],
  }),
});

const server = new ApolloServer({ gateway });

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
}).catch(err => {console.error(err)});
