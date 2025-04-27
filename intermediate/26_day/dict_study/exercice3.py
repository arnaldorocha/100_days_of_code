# student_dict = {
#     "Alice": 85,
#     "Bob": 78,
#     "Charlie": 92,
#     "David": 88,
#     "Eva": 95,
# }

#Looping through the dictionary and printing the name and score of each student
# for (key, value) in student_dict.items():
#     print(f"{key}: {value}")



# import pandas as pd

# student_data_frame = pd.DataFrame(student_dict.items(), columns=["Name", "Score"])
# print(student_data_frame)
# print(f'\n{student_data_frame["Name"]}')


# for index, (key, value) in enumerate(student_dict.items()):
#     print(f"{index + 1}. {key}: {value}")

# # loop through rows of a DataFrame
# import pandas as pd 

# student_data_frame = pd.DataFrame(student_dict.items(), columns=["Name", "Score"])
# print(student_data_frame)
                                  
# for index, row in student_data_frame.iterrows():
#         print(f"\n{index + 1}. {row['Name']}: {row['Score']}")


student_dict = {
    "names": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "scores": [85, 78, 92, 88, 95],
}

# Looping through the dictionary and printing the name and score of each student
for (key, value) in student_dict.items():
    print(f"{key}: {value}")

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

#loop through a DataFrame 
# for (key, value) in student_data_frame.items():
#     print(f"{value}")

#loop through rows of a DataFrame
for (index, row) in student_data_frame.iterrows():
    if row.names == "Alice":
        print(row.scores)

# {new_key: new_value for (index, row) in df.iterrows()}

# TODO 1: Create a dictionary in this format: {"A":Alfa, "B":Bravo, "C":Charlie}
# TODO 2: Create a list of the phonetic alphabet code words that the user inputs.