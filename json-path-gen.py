import json, sys

filename = sys.argv[1]
output_filename = sys.argv[2]



# read file
print("Reading input json file")
with open(filename, 'r') as jsonsample:
    data=jsonsample.read()

json_obj = json.loads(data)

#print(type(json_obj["date"]["s"]))


def find_keys_recurse(path_str, json_obj, paths_array):
    for key, value in json_obj.items() :
       # print (f"[{key}]")
        new_path = "%s.%s" %(path_str,key)
        if isinstance(value, dict):
            find_keys_recurse(new_path,value,paths_array)
        else:
           # print(new_path)
            paths_array.append(new_path)
           # print(paths_array)

print("Extracting json paths...")
paths_array = []
find_keys_recurse("$",json_obj,paths_array)

jsonpaths_obj = {}

jsonpaths_obj["jsonpaths"] = paths_array

output_json = json.dumps(jsonpaths_obj,indent=4)

print("Json Paths: ")
print("----------------------------------------------------------------------------------")
print(output_json)
print("----------------------------------------------------------------------------------")

with open(output_filename, "w") as output_file:
   output_file.write(output_json)