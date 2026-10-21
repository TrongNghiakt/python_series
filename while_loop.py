# count = 1
# while count <= 5:
#     print(count)
#     count += 1


# answer = ""
# while answer.lower() != 'yes':
#     answer = input("Do you agree? (yes/no): ")
# print("Thank you for agreeing!")

attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer.lower() == 'yes':
        print("Glad we are on the same page!")
        break
    attempts += 1
else:
    print("3 Strikes, You are out!")
