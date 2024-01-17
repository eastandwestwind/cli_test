import json
with open('test_2_data.json') as user_file:
    file_contents = user_file.read()

parsed_json = json.loads(file_contents)

modified_data = dict()

for entry in parsed_json:
    orders = entry["order_list"]
    for order in orders:
        modified_data[order] = entry["address_info"]["zip"]

print(modified_data)