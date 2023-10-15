import textgrid

def extract_single_occurrences(textgrid_file):
    tg = textgrid.TextGrid()
    tg.read(textgrid_file)

    tier = tg.getFirst('token')  # Replace 'token' with name of the tier you want to check.

    tokens_count = {}

    for interval in tier:
        token = interval.mark.strip()
        if token:
            start_time = interval.minTime
            end_time = interval.maxTime
            if token in tokens_count:
                tokens_count[token].append((start_time, end_time))
            else:
                tokens_count[token] = [(start_time, end_time)]

    # Find and print tokens with not exactly 2 occurrences.
    for token, times in tokens_count.items():
        if len(times) != 2:
            for start_time, end_time in times:
                print(f"{token}, {start_time}, {end_time}")

if __name__ == '__main__':
    textgrid_file = 'input.TextGrid'  # replace with your file path
    extract_single_occurrences(textgrid_file)
