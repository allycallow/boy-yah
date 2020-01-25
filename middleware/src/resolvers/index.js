const getTest = async () => ({
  ok: true
});

const resolvers = {
  Query: {
    test: getTest
  }
};

export default resolvers;
