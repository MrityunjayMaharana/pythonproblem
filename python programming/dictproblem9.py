sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
minimum_value = min(sample_dict.values())
minimum_keys = [key for key in sample_dict if sample_dict[key]==minimum_value]
print(minimum_keys)