import re
patterns = ['term1','term2']
text ='This is a string with term1, not the others!'

for pattern in patterns:
    print("I'm searching for: "+pattern)

    if re.search(pattern,text):
        print("MATCH")
    else:
        print("No Match")


split_term = "@"

email = "User@gmail.com"
print(re.split(split_term,email))


def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searchin for pattern: {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'
test_patterns = ['sd*']

multi_re_find(test_patterns,test_phrase)