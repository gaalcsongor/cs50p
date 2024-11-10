import emoji


user_emoji = input("Input: ")
print(f"Output: {emoji.emojize(user_emoji, language='alias')}")
