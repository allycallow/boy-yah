!function(e,n){for(var t in n)e[t]=n[t]}(exports,function(e){var n={};function t(o){if(n[o])return n[o].exports;var i=n[o]={i:o,l:!1,exports:{}};return e[o].call(i.exports,i,i.exports,t),i.l=!0,i.exports}return t.m=e,t.c=n,t.d=function(e,n,o){t.o(e,n)||Object.defineProperty(e,n,{enumerable:!0,get:o})},t.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},t.t=function(e,n){if(1&n&&(e=t(e)),8&n)return e;if(4&n&&"object"==typeof e&&e&&e.__esModule)return e;var o=Object.create(null);if(t.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:e}),2&n&&"string"!=typeof e)for(var i in e)t.d(o,i,function(n){return e[n]}.bind(null,i));return o},t.n=function(e){var n=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(n,"a",n),n},t.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)},t.p="",t(t.s=9)}([function(e,n){e.exports=require("apollo-server")},function(e,n){e.exports=require("apollo-server-express")},function(e,n){e.exports=require("express")},function(e,n){e.exports=require("graphql-playground-middleware-express")},function(e,n){e.exports=require("serverless-http")},function(e,n){e.exports=require("node-fetch")},function(e,n,t){var o={kind:"Document",definitions:[{kind:"ObjectTypeDefinition",name:{kind:"Name",value:"Query"},interfaces:[],directives:[],fields:[{kind:"FieldDefinition",name:{kind:"Name",value:"test"},arguments:[],type:{kind:"NamedType",name:{kind:"Name",value:"Test"}},directives:[]}]},{kind:"ObjectTypeDefinition",name:{kind:"Name",value:"Mutation"},interfaces:[],directives:[],fields:[{kind:"FieldDefinition",name:{kind:"Name",value:"store_blood_pressure"},arguments:[{kind:"InputValueDefinition",name:{kind:"Name",value:"value"},type:{kind:"NamedType",name:{kind:"Name",value:"Int"}},directives:[]}],type:{kind:"NamedType",name:{kind:"Name",value:"BloodPressureRespone"}},directives:[]}]}],loc:{start:0,end:184}};o.loc.source={body:'#import "./type/test.graphql"\n#import "./type/blood-pressure-response.graphql"\n\ntype Query {\n  test: Test\n}\n\ntype Mutation {\n  store_blood_pressure(value: Int): BloodPressureRespone\n}\n',name:"GraphQL request",locationOffset:{line:1,column:1}};var i={};function r(e){return e.filter((function(e){if("FragmentDefinition"!==e.kind)return!0;var n=e.name.value;return!i[n]&&(i[n]=!0,!0)}))}o.definitions=o.definitions.concat(r(t(7).definitions)),o.definitions=o.definitions.concat(r(t(8).definitions)),e.exports=o},function(e,n){var t={kind:"Document",definitions:[{kind:"ObjectTypeDefinition",name:{kind:"Name",value:"Test"},interfaces:[],directives:[],fields:[{kind:"FieldDefinition",name:{kind:"Name",value:"ok"},arguments:[],type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"Boolean"}}},directives:[]}]}],loc:{start:0,end:29}};t.loc.source={body:"type Test {\n  ok: Boolean!\n}\n",name:"GraphQL request",locationOffset:{line:1,column:1}};e.exports=t},function(e,n){var t={kind:"Document",definitions:[{kind:"ObjectTypeDefinition",name:{kind:"Name",value:"BloodPressureRespone"},interfaces:[],directives:[],fields:[{kind:"FieldDefinition",name:{kind:"Name",value:"ok"},arguments:[],type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"Boolean"}}},directives:[]}]}],loc:{start:0,end:45}};t.loc.source={body:"type BloodPressureRespone {\n  ok: Boolean!\n}\n",name:"GraphQL request",locationOffset:{line:1,column:1}};e.exports=t},function(e,n,t){"use strict";t.r(n);var o=t(0),i=t(1),r=t(2),a=t.n(r),s=t(3),u=t.n(s),l=t(4),d=t.n(l),c=t(5),p=t.n(c);var m={Query:{test:async()=>({ok:!0})},Mutation:{store_blood_pressure:async(e,{value:n},t,o)=>{const{API_ENDPOINT:i}=Object({API_ENDPOINT:"https://rest.ehrscape.com/rest/v1/composition?ehrId=5f4401c5-071a-4b4e-8426-6f2ccb32fb04&templateId=NHSHD23%20BoYaA&committerName=Alexa&format=FLAT"}),r={"ctx/composer_name":"Alex Callow","ctx/language":"en","ctx/territory":"GB","nhshd23_boyaa/blood_pressure/systolic|magnitude":n,"nhshd23_boyaa/blood_pressure/systolic|unit":"mm[Hg]","nhshd23_boyaa/blood_pressure/diastolic|magnitude":80,"nhshd23_boyaa/blood_pressure/diastolic|unit":"mm[Hg]"},a=await p()(i,{method:"POST",body:JSON.stringify(r),headers:{"Content-Type":"application/json",Authorization:"Basic am9obi5tZXJlZGl0aEB3YWxlcy5uaHMudWs6ZWhyNGpvaG4ubWVyZWRpdGg="}});return console.log(await a.json()),{ok:!0}}}},f=t(6),y=t.n(f);t.d(n,"handler",(function(){return h}));const v=a()(),k=Object(o.makeExecutableSchema)({typeDefs:y.a,resolvers:m}),b=new i.ApolloServer({schema:k,context:({req:e})=>{const{headers:{authorization:n}}=e;return{token:n}},resolverValidationOptions:{requireResolversForResolveType:!1},inheritResolversFromInterfaces:!0,mocks:!0});Object(o.addResolveFunctionsToSchema)({schema:k,resolvers:m}),Object(o.addMockFunctionsToSchema)({schema:k,preserveResolvers:!0}),v.use("/graphql",(e,n,t)=>{n.header("Access-Control-Allow-Origin","*"),n.header("Access-Control-Allow-Headers","Content-Type, Authorization, Content-Length, X-Requested-With"),"OPTIONS"===e.method?n.sendStatus(200):t()}),b.applyMiddleware({app:v}),v.use("/playground",u()({endpoint:"/graphql"}));const h=d()(v)}]));