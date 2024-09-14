# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",123:"Name"}
# programming_dictionary[123] = "Changed_name"
# print(programming_dictionary)
#
# programming_dictionary["New_key"]="New_val"
# print(programming_dictionary)
from os import cpu_count
from typing import final

# capitals ={
#     "France":[ "Paris","Lille","Dijon"],
#     "Germany":["Stuttgart","Berlin"],
# }
# print(capitals["France"])
# for i in capitals:
#     for j in range(0,len(capitals[i])):
#         print(capitals[i][j])
#         j=0
# nested_list = ["a","b",["c,","d"]]
#
# # Printing the nested list
# for i in nested_list:
#     for j in range(0,len(i)):
#        print(i[j])

travel_log = {
    "France":{
        "France": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany":{
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":5
    }

}
# print(travel_log["France"]["France"][1])
# for i in travel_log:
#     for j in i:
#         print(j)
#
# travel_log["Plans"]="New plan"
# final_travel_log = travel_log
# print(final_travel_long["France"]
# print(final_travel_log["France"-1]) # will give an error

# final_travel_log = travel_log["Plans"]="New plan"  // final_travel_log = travel_log["Plans"]
# print(final_travel_log["France"]) // will give an error