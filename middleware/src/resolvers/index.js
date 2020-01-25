import { storeBloodPressure } from "./mutations";
import { getTest } from "./query";

const resolvers = {
  Query: {
    test: getTest
  },
  Mutation: {
    store_blood_pressure: storeBloodPressure
  }
};

export default resolvers;
