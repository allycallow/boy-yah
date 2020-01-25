!function(e,n){for(var t in n)e[t]=n[t]}(exports,function(e){var n={};function t(r){if(n[r])return n[r].exports;var o=n[r]={i:r,l:!1,exports:{}};return e[r].call(o.exports,o,o.exports,t),o.l=!0,o.exports}return t.m=e,t.c=n,t.d=function(e,n,r){t.o(e,n)||Object.defineProperty(e,n,{enumerable:!0,get:r})},t.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},t.t=function(e,n){if(1&n&&(e=t(e)),8&n)return e;if(4&n&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(t.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&n&&"string"!=typeof e)for(var o in e)t.d(r,o,function(n){return e[n]}.bind(null,o));return r},t.n=function(e){var n=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(n,"a",n),n},t.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)},t.p="",t(t.s=7)}([function(e,n){e.exports=require("apollo-server")},function(e,n){e.exports=require("apollo-server-express")},function(e,n){e.exports=require("express")},function(e,n){e.exports=require("graphql-playground-middleware-express")},function(e,n){e.exports=require("serverless-http")},function(e,n,t){var r={kind:"Document",definitions:[{kind:"ObjectTypeDefinition",name:{kind:"Name",value:"Query"},interfaces:[],directives:[],fields:[{kind:"FieldDefinition",name:{kind:"Name",value:"test"},arguments:[],type:{kind:"NamedType",name:{kind:"Name",value:"Test"}},directives:[]}]}],loc:{start:0,end:59}};r.loc.source={body:'#import "./type/test.graphql"\n\ntype Query {\n  test: Test\n}\n',name:"GraphQL request",locationOffset:{line:1,column:1}};var o={};r.definitions=r.definitions.concat(t(6).definitions.filter((function(e){if("FragmentDefinition"!==e.kind)return!0;var n=e.name.value;return!o[n]&&(o[n]=!0,!0)}))),e.exports=r},function(e,n){var t={kind:"Document",definitions:[{kind:"ObjectTypeDefinition",name:{kind:"Name",value:"Test"},interfaces:[],directives:[],fields:[{kind:"FieldDefinition",name:{kind:"Name",value:"ok"},arguments:[],type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"Boolean"}}},directives:[]}]}],loc:{start:0,end:29}};t.loc.source={body:"type Test {\n  ok: Boolean!\n}\n",name:"GraphQL request",locationOffset:{line:1,column:1}};e.exports=t},function(e,n,t){"use strict";t.r(n);var r=t(0),o=t(1),i=t(2),s=t.n(i),a=t(3),u=t.n(a),l=t(4),c=t.n(l);var d={Query:{test:async()=>({ok:!0})}},p=t(5),f=t.n(p);t.d(n,"handler",(function(){return h}));const m=s()(),v=Object(r.makeExecutableSchema)({typeDefs:f.a,resolvers:d}),y=new o.ApolloServer({schema:v,context:({req:e})=>{const{headers:{authorization:n}}=e;return{token:n}},resolverValidationOptions:{requireResolversForResolveType:!1},inheritResolversFromInterfaces:!0,mocks:!0});Object(r.addResolveFunctionsToSchema)({schema:v,resolvers:d}),Object(r.addMockFunctionsToSchema)({schema:v,preserveResolvers:!0}),m.use("/graphql",(e,n,t)=>{n.header("Access-Control-Allow-Origin","*"),n.header("Access-Control-Allow-Headers","Content-Type, Authorization, Content-Length, X-Requested-With"),"OPTIONS"===e.method?n.sendStatus(200):t()}),y.applyMiddleware({app:m}),m.use("/playground",u()({endpoint:"/graphql"}));const h=c()(m)}]));