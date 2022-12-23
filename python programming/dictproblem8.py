sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
print("initial 1st dictionary", sample_dict)
 
sample_dict['location'] = sample_dict['city']
del sample_dict['city']
print("final dictionary", str(sample_dict))