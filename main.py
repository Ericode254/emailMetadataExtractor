import email
from email import policy
from email.parser import BytesParser
import glob

# get the file
emails = glob.glob("*.eml")

with open(emails[0], "rb") as fp:
    message = BytesParser(policy=policy.default).parse(fp)

text = message.get_body(preferencelist=("plain")).get_content()
print(text)
