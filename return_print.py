def clean_name(name):
    low_cleaned = name.strip().lower()
    up_cleaned = name.strip().upper()
    return low_cleaned, up_cleaned


lo_name, up_name = clean_name(" sdfsddsd")
print(lo_name, up_name)  # Output: John Doe
