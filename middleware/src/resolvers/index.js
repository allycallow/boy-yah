import fetch from "node-fetch";

const getTest = async () => ({
  ok: true
});

const storeBloodPressure = async (root, { value }, context, info) => {
  const { API_ENDPOINT } = process.env;

  const data = {
    "ctx/composer_name": "Alex Callow",
    "ctx/language": "en",
    "ctx/territory": "GB",
    "nhshd23_boyaa/blood_pressure/systolic|magnitude": value,
    "nhshd23_boyaa/blood_pressure/systolic|unit": "mm[Hg]",
    "nhshd23_boyaa/blood_pressure/diastolic|magnitude": 80,
    "nhshd23_boyaa/blood_pressure/diastolic|unit": "mm[Hg]"
  };

  const res = await fetch(API_ENDPOINT, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
      Authorization: `Basic am9obi5tZXJlZGl0aEB3YWxlcy5uaHMudWs6ZWhyNGpvaG4ubWVyZWRpdGg=`
    }
  });

  console.log(await res.json());

  return {
    ok: true
  };
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
