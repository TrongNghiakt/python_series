domains = ['www.google.com', 'openai.com',
           'localhost', 'WWW.DATAWITHBARAA.COM']

cleaned = [
    # Data Transformation
    # For Loop
    # Data Filtering
    d
    for d in domains
    if '.' in d
]
print(cleaned)
