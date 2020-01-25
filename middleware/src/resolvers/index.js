const getTest = async () => ({
  ok: true
});


const storeBloodPressure = async () => ({
  ok: false
})


const resolvers = {
  Query: {
    test: getTest
  }
  Mutation: {
    store_blood_pressure: storeBloodPressure
  }

};

export default resolvers;
