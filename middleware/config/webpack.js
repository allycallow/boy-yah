const webpack = require("webpack");
const path = require("path");
const nodeExternals = require("webpack-node-externals");
const slsw = require("serverless-webpack");
const outputFolder = ".webpack";

const { API_ENDPOINT } = slsw.lib.serverless.service.provider.environment;

require("dotenv").config();

module.exports = {
  entry: slsw.lib.entries,
  output: {
    libraryTarget: "commonjs",
    path: path.join(__dirname, outputFolder),
    filename: "src/index.js"
  },
  target: "node",
  externals: [
    nodeExternals(),
    {
      vertx: "commonjs vertx"
    }
  ],
  mode: "production",
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: ["babel-loader", "eslint-loader"]
      },
      {
        test: /\.(graphql|gql)$/,
        exclude: /node_modules/,
        loader: "graphql-tag/loader"
      }
    ]
  },
  stats: {
    warnings: false
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        API_ENDPOINT: JSON.stringify(API_ENDPOINT)
      }
    })
  ]
};
