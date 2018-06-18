import scrapper

#Returns quote, author and author link, indexes 0,1 and 2 respectively
quote = scrapper.get_quote()

user_input = input("Who is the author of the following quote?\n\n" + quote[0]).lower()

if user_input == quote[1].lower():
    print("pass")

print(quote[1])





