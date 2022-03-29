# start to python day-10 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 24-03-2022
# went on vacation
# programing_dict = {"Rushi": "This is me", "Babita": "She is my mother", "Jivan": "He is my father"}
#
# #print(programing_dict["Rushi"])
#
# for name in programing_dict:
#     print(name)
#     print(programing_dict[name])
#
# empty_dict = {}
#
# for name in empty_dict:
#     empty_dict = input("Enter key and value")
#
# #print(empty_dict[name])
#
# student_scores = {"Ram": 91,
#                   "Sam": 87,
#                   "Tam": 73,
#                   "Pam": 56,
#                   "Zam": 34}
#
# student_grades = {}
#
# for student in student_scores:
#     scores = student_scores[student]
#     if scores > 90:
#         student_grades[student] = "Outstanding"
#     elif scores < 90 and scores > 80:
#         student_grades[student] = "Good"
#     elif scores < 80 and scores > 60:
#         student_grades[student] = "Average"
#     elif scores < 60 and scores > 35:
#         student_grades[student] = "Poor"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)
#
# for grades in student_grades:
#
#     print(grades +"'s performance has been "+ student_grades[grades])
#     # print(student_grades[grades])

# nesting dict
capitals = {"Maharashtra": "Mumbai",
            "Kerela": "Trivandrum",
            "MadhyaPradesh": "Bhopal"}

# nesting in list in a dict
travel_log = {"Maharashtra": ["Mumbai", "Pune", "Nagpur"],
              "Kerela": ["Trivandrum", "Kochi", "Alleppy"],
              "MadhyaPradesh": ["Bhopal", "Indore"]}

# nesting in dict in dist
travel_log1 = {"Maharashtra": {"cities_visited": ["Mumbai", "Pune", "Nagpur"], "total_visits": 12},
               "Kerela": {"cities_visited": ["Trivandrum", "Kochi", "Alleppy"], "total_visits": 8},
               "MadhyaPradesh": {"cities_visited": ["Bhopal", "Indore"], "total_visits": 3}}

# nesting dist in a list
travel_log2 = [
    {
        "State": "Maharashtra",
        "cities_visited": ["Mumbai", "Pune", "Nagpur"],
        "total_visits": "12"
    },
    {
        "State": "Kerela",
        "cities_visited": ["Trivandrum", "Kochi", "Alleppy"],
        "total_visits": 8
    },
    {
        "State": "MadhyaPradesh",
        "cities_visited": ["Bhopal", "Indore"],
        "total_visits": 3
    },
]

# function to add new data to list
# def add_new_state(State, cities_visited, total_visits):
#
#     new_state = {}
#     new_state["State"] = State
#     new_state["cities_visited"] = cities_visited
#     new_state["total_visits"] = total_visits
#     travel_log2.append(new_state)
#
# add_new_state("Rajasthan", ["Jaipur", "Udaypur"], 9)
# print(travel_log2)
#

# to print particular value
print("When i visited " + travel_log2[0]["State"] + " and went to " + travel_log2[0]["cities_visited"][
    2] + " that was my " + travel_log2[0]["total_visits"] + "th time")


