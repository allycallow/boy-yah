import {
  addMockFunctionsToSchema,
  addResolveFunctionsToSchema,
  makeExecutableSchema
} from "apollo-server";
import { ApolloServer } from "apollo-server-express";
import express from "express";
import expressPlayground from "graphql-playground-middleware-express";
import serverless from "serverless-http";

import resolvers from "./resolvers";
import typeDefs from "./type-defs/schema.graphql";

const app = express();

const schema = makeExecutableSchema({
  typeDefs,
  resolvers
});

const server = new ApolloServer({
  schema,
  context: ({ req }) => {
    const {
      headers: { authorization }
    } = req;
    return {
      token: authorization
    };
  },
  resolverValidationOptions: {
    requireResolversForResolveType: false
  },
  inheritResolversFromInterfaces: true,
  mocks: true
});

addResolveFunctionsToSchema({ schema, resolvers });

addMockFunctionsToSchema({
  schema,
  preserveResolvers: true
});

app.use("/graphql", (req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Content-Type, Authorization, Content-Length, X-Requested-With"
  );
  if (req.method === "OPTIONS") {
    res.sendStatus(200);
  } else {
    next();
  }
});

server.applyMiddleware({ app });

app.use("/playground", expressPlayground({ endpoint: "/graphql" }));

export const handler = serverless(app);
