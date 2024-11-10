#main() function inputs the user for a string
#and calls the convert() function
def main():
    text = input("text: ")
    convert(text)

#convert function replaces te emoticons with emojis
def convert(emoji):
    emoji = emoji.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    print(emoji) 

main()
