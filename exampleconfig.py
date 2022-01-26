from pathlib import Path

# Crawler URL
baseurl = "URL"
# Find the class to target
classfinder = ["class1","class2"]
# PATH for export files
p = Path("Path of your files")
p.mkdir(parents=True, exist_ok=True)
# Section of the URL to crawl
s = "URL"
# Regex for crawl out the category name, Zara in this case
regex = "Enter here your regex"
# Regex cheat sheet
# [] set of characters
# . any character
# ^ starts with
# $ ends with
# | this or either this
time = "21:00"

# Starting and ending of categories
start = 3
end = 17

