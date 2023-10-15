import textgrid
import parselmouth
import csv

def extract_f0_for_interval(pitch, start_time, end_time):
    # Compute mean f0 within the given time interval
    f0_values = [pitch.get_value_at_time(t) for t in 
                 [t for t in pitch.ts() if start_time <= t <= end_time]]

    # Remove undefined values (0.0 in parselmouth)
    f0_values = [f0 for f0 in f0_values if f0 != 0]

    if not f0_values:
        return None

    f0_mean = sum(f0_values) / len(f0_values)

    return f0_mean

def main(textgrid_file_path, wav_file_path, csv_file_path):
    # Load TextGrid
    tg = textgrid.TextGrid()
    tg.read(textgrid_file_path)

    # Get the event and token tiers
    event_tier = tg.getFirst("event")
    token_tier = tg.getFirst("token")

    # Pre-compute the pitch for the entire sound file
    sound = parselmouth.Sound(wav_file_path)
    pitch = sound.to_pitch(time_step=0.01, pitch_floor=75, pitch_ceiling=600)
    
    # Extract intervals and f0
    csv_data = []

    last_token_interval_index = 0
    for interval in event_tier:
        label = interval.mark
        if label.startswith('v') or label.startswith('n'):  # If it's a vowel or 'n'
            start_time = interval.minTime
            end_time = interval.maxTime
            f0 = extract_f0_for_interval(pitch, start_time, end_time)

            # Find corresponding word from token tier
            word = None
            for i in range(last_token_interval_index, len(token_tier)):
                token_interval = token_tier[i]
                if token_interval.minTime <= start_time <= token_interval.maxTime:
                    word = token_interval.mark
                    last_token_interval_index = i
                    break
            
            if not word.endswith('(n)'): #Exclude error words
                csv_data.append([word, label, start_time, end_time, f0])


    # Write to CSV
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["word", "vowel", "start time", "end time", "f0"])
        writer.writerows(csv_data)

if __name__ == "__main__":
    textgrid_file_path = "input.TextGrid"
    wav_file_path = "input.wav"
    csv_file_path = "output.csv"

    main(textgrid_file_path, wav_file_path, csv_file_path)
