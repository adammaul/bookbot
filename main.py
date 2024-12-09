with open("books/frakenstein.txt") as f:
    file_contents = f.read()
    each_word = file_contents.lower()
    character_dict = {}

    for i in each_word:
        if i != " " and i.isalpha():
            if i not in character_dict.keys():
                character_dict[i] = 1
            else:
                character_dict[i] += 1


print("""--- Begin report of books/frankenstein.txt ---
77986 words found in the document
      """)

for char, count_char in sorted(
    character_dict.items(), key=lambda item: item[1], reverse=True
):
    print(f"The '{char}' character was found {count_char} times")
print("--- End report ---")
