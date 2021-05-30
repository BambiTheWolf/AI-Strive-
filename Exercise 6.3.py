text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a Mr. Smith could chuck wood\n\r\t."""

text = text.replace("\n", " ")

new_text = ""
for e in text:
       if e.isalnum() or e == " ":
           print(e)
           new_text += e
           
final_text = new_text.lower().strip().split(" ")

counter = 0

for word in final_text:
    if word == "wood":
        counter += 1
print(f"The final count is {counter}")

