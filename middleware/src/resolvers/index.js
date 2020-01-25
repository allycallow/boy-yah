const getTest = async () => ({
  ok: true
});


const storeBloodPressure = async (root, args, context, info) => {
  const {  BACKEND_ENDPOINT, TOKEN } = proces.env;

  const data = {
    "ctx/composer_name": "Alex Callow",
    "ctx/language": "en",
    "ctx/territory": "GB",
    "nhshd23_boyaa/blood_pressure/systolic|magnitude": 2,
    "nhshd23_boyaa/blood_pressure/systolic|unit": "mm[Hg]",
    "nhshd23_boyaa/blood_pressure/diastolic|magnitude": 80,
    "nhshd23_boyaa/blood_pressure/diastolic|unit": "mm[Hg]"
  }

  const res await fetch(BACKEND_ENDPOINT, {
    method: 'POST',
    body: JSON.stringify(data) },
    headers: {
      'Content-Type': 'application/json',
      "Authorization": `Basic ${TOKEN}`
    }
  });

  console.log(res.json());

  return {
    ok: true
  }
}


const resolvers = {
  Query: {
    test: getTest
  }
  Mutation: {
    store_blood_pressure: storeBloodPressure
  }

};

export default resolvers;


{
	"ctx/composer_name": "Yann McN",
	"ctx/language": "en",
	"ctx/territory": "GB",
	"nhshd23_boyaa/blood_pressure/systolic|magnitude": 2,
	"nhshd23_boyaa/blood_pressure/systolic|unit": "mm[Hg]",
	"nhshd23_boyaa/blood_pressure/diastolic|magnitude": 80,
	"nhshd23_boyaa/blood_pressure/diastolic|unit": "mm[Hg]"
}