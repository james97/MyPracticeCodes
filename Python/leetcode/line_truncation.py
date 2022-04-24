def wrapLines(words, line_len: int):
    output = []
    new_line = ""
    for word in words:
        if len(word) >= line_len and not new_line:
            output.append(word)
        else:
            if len(new_line) + len(word) + 1 > line_len:
                output.append(new_line)
                new_line = word
            else:
                if not new_line:
                    new_line = word
                else:
                    new_line = new_line + "-" + word
    if new_line:
        output.append(new_line)
    return output


if __name__ == "__main__":
    test =  [ "The", "day", "began", "as", "still", "as", "the",
              "night", "abruptly", "lighted", "with", "brilliant",
              "flame" ]

    print(wrapLines(test, 13))

