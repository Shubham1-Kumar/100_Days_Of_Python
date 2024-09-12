# Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")
def calculate_love_score(name1, name2):
    count1 = 0
    count2 =0
    lower_name = name1+name2
    print(lower_name)
    for letter in lower_name:
        if letter == 't':
            count1+=1
        elif letter == 'r':
            count1 += 1
        elif letter == 'u':
            count1+=1
        elif letter == 'e':
            count1 += 1
            count2+=1
        elif letter == 'l':
            count2 +=1
        elif letter == 'o':
            count2 +=1
        elif letter == 'v':
            count2 +=1
    print(f"{count1}{count2}")

calculate_love_score("Kanye West", "Kim Kardashian")
