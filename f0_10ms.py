import textgrid
import parselmouth
import csv

#pip install praat-parselmouth
#pip install textgrid

def extract_f0_for_interval(pitch, start_time, end_time):
    # Extract f0 values every 10ms within the given time interval
    times = [start_time + i*0.01 for i in range(int((end_time - start_time) * 100) + 1)]
    f0_values = [(t, pitch.get_value_at_time(t)) for t in times]

    # Remove undefined values (0.0 in parselmouth)
    f0_values = [(t, f0) for t, f0 in f0_values if f0 != 0]

    return f0_values

def main(textgrid_file_path, wav_file_path, csv_file_path):
    # Load TextGrid
    tg = textgrid.TextGrid()
    tg.read(textgrid_file_path)

    # Get the event and token tiers
    event_tier = tg.getFirst("event")
    token_tier = tg.getFirst("token")

    # Pre-compute the pitch for the entire sound file
    sound = parselmouth.Sound(wav_file_path)
    pitch = sound.to_pitch()

    # Extract intervals and f0
    csv_data = []

    last_token_interval_index = 0
    for interval in event_tier:
        label = interval.mark
        if label.startswith('v') or label.startswith('n'):  # If it's a vowel
            start_time = interval.minTime
            end_time = interval.maxTime
            f0_values = extract_f0_for_interval(pitch, start_time, end_time)

            # Find corresponding word from token tier
            word = None
            for i in range(last_token_interval_index, len(token_tier)):
                token_interval = token_tier[i]
                if token_interval.minTime <= start_time <= token_interval.maxTime:
                    word = token_interval.mark
                    last_token_interval_index = i
                    break
            
            if not word.endswith('(n)'):
                for t, f0 in f0_values:
                    csv_data.append([word, label, t, t+0.01, f0])

    # Write to CSV
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["word", "vowel", "start time", "end time", "f0"])
        writer.writerows(csv_data)

if __name__ == "__main__":
    textgrid_file_path = "input.TextGrid"
    wav_file_path = "input.wav"
    csv_file_path = "output_10ms.csv"

    main(textgrid_file_path, wav_file_path, csv_file_path)
