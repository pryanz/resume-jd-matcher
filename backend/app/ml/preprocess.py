import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]", " ",text)
    text = re.sub(r"\s+", " ",text).strip()
    return text

# samples = [
#     "PYTHON Developer!!!",
#     "  Data-Science @@@ Engineer ",
#     "C++ / Java / Python",
#     "Machine_Learning--Engineer"
# ]

# for s in samples:
#     print(clean_text(s))
    