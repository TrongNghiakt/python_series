case_rule = "n/a"  # Global variable


def clean_text(name):  # Parameter
    cleaned = name.strip()  # Local variable
    if case_rule == "lower":
        cleaned = cleaned.lower()
    print("Raw:", name)
    print("Cleaned:", cleaned)


clean_text("   python PROgramming   ")
print("The rule is", case_rule)
