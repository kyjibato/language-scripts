import textgrid

def modify_textgrid(filename):
    # Load the TextGrid
    tg = textgrid.TextGrid()
    tg.read(filename)
    
    # Find the "token" tier
    for t in tg:
        if t.name.lower() == 'token':
            tier = t
            break
    else:
        raise ValueError("No 'token' tier found in TextGrid")

    seen_words = {}

    for interval in tier:
        word = interval.mark.strip()  # Remove any surrounding spaces
        if word and not word.endswith(")"):
            if word in seen_words:
                seen_words[word] += 1
            else:
                seen_words[word] = 1
            interval.mark = f"{word}_{seen_words[word]}"

    # Save the modified TextGrid
    tg.write(filename[:-9] + "_modified.TextGrid")  # change the filename as per your preference

# Call the function with your TextGrid file name
modify_textgrid("input.TextGrid")
