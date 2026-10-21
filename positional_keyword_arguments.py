# Building Full Clean Name
def clean_name(first_name, last_name="n/a", country="n/a"):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name.title(), "From", country)


clean_name(" MariA ", "SMITH ", "USA")  # Positional Arguments
clean_name(last_name="SMITH ",
           country="USA", first_name=" MariA ")  # Keyword Arguments

# Mix Arguments
clean_name(first_name=" MariA ", last_name="SMITH ", country="USA")

# Default Arguments
clean_name(" MariA ")
