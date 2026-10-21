# score = 82
# # if score >= 90:
# #     print("A")
# # elif score >= 80:
# #     print("B")
# # else:
# #     print("F")


# grade = (
#     "A" if score >= 90
#     else "B" if score >= 80
#     else "F")
# print(grade)


country = "USA"
# if country == "India":
#     print("IN")
# elif country == "United States":
#     print("US")
# elif country == "United Kingdom":
#     print("UK")
# elif country == "Canada":
#     print("CA")
# else:
#     print("Unknown country")


# Match case statement
match country:
    case "India":
        print("IN")
    case "United States" | "USA":
        print("US")
    case "United Kingdom":
        print("UK")
    case "Canada":
        print("CA")
    case _:
        print("Unknown country")
