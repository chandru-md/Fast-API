from fontTools.designspaceLib.types import userRegionToDesignRegion

user_dict = {
    "username":"Chandru",
    "location":"India",
    "age":23
}

print(user_dict)

print(user_dict.get("username"))

print(user_dict.keys())

user_dict["Married"]=False

print(user_dict)

print(user_dict.values())

user_dict.pop('age')

print(user_dict)


for x in user_dict.items():
    print(x)

user_dict_2 = user_dict.copy()


print(user_dict_2)