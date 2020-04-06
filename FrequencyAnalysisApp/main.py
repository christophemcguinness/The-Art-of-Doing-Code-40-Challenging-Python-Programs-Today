print("Welcome to the Frequency Analysis App")

valid_letters = "qwertyuiopasdfghjklzxcvbnm"
phrase_dict = {}
total = 0

phrase = "Let's be clear. The planet is not in jeopardy. We are in jeopardy. We haven't got the power to destroy the " \
         "planet - or to save it. But we might have the power to save ourselves."

breakdown = [x for x in phrase.lower() if x in valid_letters]

for x in sorted(set(breakdown)):
    phrase_dict[x] = phrase.count(x)
    total += phrase_dict[x]

print("\n:: Phrase 1 ::")
print("'{0}'".format(phrase))
print("\nLetter \tOccurrence \tPercentage")
for x in phrase_dict.keys():
    print("{0} \t\t{1} \t\t\t{2}%".format(x, phrase_dict[x], round((phrase_dict[x] / total) * 100, 2)))

print("\nUnique Letters In Order:")
print("".join(sorted(set(breakdown))))

phrase_dict = {}
total = 0

phrase = "Living systems are never in equilibrium. They are inherently unstable. They may seem stable, but they’re " \
         "not. Everything is moving and changing. In a sense, everything is on the edge of collapse."

breakdown = [x for x in phrase.lower() if x in valid_letters]

for x in sorted(set(breakdown)):
    phrase_dict[x] = phrase.count(x)
    total += phrase_dict[x]

print("\n:: Phrase 2 ::")
print("'{0}'".format(phrase))
print("\nLetter \tOccurrence \tPercentage")
for x in phrase_dict.keys():
    print("{0} \t\t{1} \t\t\t{2}%".format(x, phrase_dict[x], round((phrase_dict[x] / total) * 100, 2)))

print("\nUnique Letters In Order:")
print("".join(sorted(set(breakdown))))

encode_decode = input("\nWould you like to encode a message or decode a message? ")
encryption_list = [x for x in
                   "190-=!""£$%^&*()_+QWERTYUIOP{}ASDFGHJKertyuiop[]asdfghjkl;'#L:@~ZXCVB2345678NM<>?|qwzxcvbnm,./ "]
encryption_map = [x for x in
                   "23-=!""£$%^&*(VBNM<>?|qw56)_+QWERTYUIOP{kl;'#zxcvbnm,./ }ASDFGHJ1KL:@~ZXC7ertyuiop[]asdfgh4890j"]

if encode_decode.lower() == "encode":
    code = input("\nWhich message would you like to encode? ")
    code_list = []
    for x in code:
        code_list.append(encryption_map[encryption_list.index(x)])
    print("\nYour new encrypted message is:")
    print("".join(code_list))

elif encode_decode.lower() == "decode":
    code = input("\nWhich message would you like to decode? ")
    code_list = []
    for x in code:
        code_list.append(encryption_list[encryption_map.index(x)])
    print("Your new encrypted message is:")
    print("".join(code_list))

else:
    print("No valid choice was given. Good bye.")
