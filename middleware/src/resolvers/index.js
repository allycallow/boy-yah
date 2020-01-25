/* eslint-disable no-console */
import fetch from "node-fetch";
import { ApolloError } from "apollo-server";

const getTest = async () => ({
  ok: true
});

const storeBloodPressure = async (
  root,
  { systolic_number, diastolic_number }
) => {
  const { API_ENDPOINT, TOKEN } = process.env;

  const data = {
    "ctx/composer_name": "Alex Callow",
    "ctx/language": "en",
    "ctx/territory": "GB",
    "nhshd23_boyaa/blood_pressure/systolic|magnitude": systolic_number,
    "nhshd23_boyaa/blood_pressure/systolic|unit": "mm[Hg]",
    "nhshd23_boyaa/blood_pressure/diastolic|magnitude": diastolic_number,
    "nhshd23_boyaa/blood_pressure/diastolic|unit": "mm[Hg]"
  };

  const res = await fetch(API_ENDPOINT, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
      Authorization: `Basic ${TOKEN}`
    }
  });

  // * PRINT RESULT *
  console.log(res.ok);
  console.log(await res.json());

  if (res.ok) {
    return await res.json();
  }

  throw new ApolloError("Could not store blood pressure results", 500);
};

const resolvers = {
  Query: {
    test: getTest
  },
  Mutation: {
    store_blood_pressure: storeBloodPressure
  }
};

export default resolvers;
