import json

# Function to convert beat to milliseconds based on BPM
def beat_to_ms(bpm, beat):
    ms_per_beat = 60000 / bpm  # 60000 ms in a minute
    return int(ms_per_beat * beat)

holding = None
def check_position(current_position, previous_position):
    if current_position == 3 and previous_position in [4, 5, 6]:
        if holding is True:
            return 1
        else:
            return 2
    elif current_position == 3 and previous_position in [0, 1, 2]:
        if holding is True:
            return 2
        else:
            return 1
    elif current_position == 2:
        return 1
    elif current_position == 1:
        return 1
    elif current_position == 0:
        return 1
    elif current_position == 3 and previous_position in [4, 5, 6]:
        return 2
    elif current_position == 4:
        return 2
    elif current_position == 5:
        return 2
    elif current_position == 6:
        return 2
    else:
        return 1

# Read the input JSON file
with open('kiseki.json', 'r') as infile:
    data = json.load(infile)

bpm = None
output = {
    "live_difficulty_id": None,
    "live_notes": []
}

# Track the id enumeration
note_id = 1

# Process the JSON data
for i in range(len(data)):
    item = data[i]
    
    # Handle BPM
    if item['type'] == 'BPM':
        bpm = item['bpm']  # Set the bpm
    
    # Handle Single notes
    elif item['type'] == 'Single' and bpm is not None:
        # Check for previous position
        if i > 0 and 'lane' in data[i - 1]:
            previous_position = data[i - 1]['lane']
        else:
            previous_position = None  # No previous position for the first entry or if 'lane' key is missing

        # Create the live_note structure
        live_note = {
            "id": note_id,
            "call_time": beat_to_ms(bpm, item['beat']),
            "note_type": 1 if item['type'] == 'Single' else None,
            "note_position": check_position(item.get("lane", 0), previous_position),  # Default lane to 0 if missing
            "gimmick_id": 0,
            "note_action": 1,
            "wave_id": 0,
            "note_random_drop_color": 99,
            "auto_judge_type": 20
        }
        output['live_notes'].append(live_note)
        note_id += 1  # Increment the id for each note

    # Handle Slide or Long notes
    elif (item['type'] == 'Slide' or item['type'] == 'Long') and bpm is not None:
        holding = True
        connections = item.get('connections', [])
        if connections:
            # First connection
            first_connection = connections[0]
            first_lane = first_connection.get('lane', 0)  # Get lane from connections or default to 0

            # Check for previous position
            if i > 0 and 'lane' in data[i - 1]:
                previous_position = data[i - 1]['lane']
            else:
                previous_position = None  # No previous position for the first entry or if 'lane' key is missing

            first_live_note = {
                "id": note_id,
                "call_time": beat_to_ms(bpm, first_connection['beat']),
                "note_type": 2,  # Slide start
                "note_position": check_position(first_lane, previous_position),
                "gimmick_id": 0,
                "note_action": 1,
                "wave_id": 0,
                "note_random_drop_color": 99,
                "auto_judge_type": 20
            }
            output['live_notes'].append(first_live_note)
            note_id += 1  # Increment the id for each note

            # Last connection
            holding = False
            last_connection = connections[-1]
            last_live_note = {
                "id": note_id,
                "call_time": beat_to_ms(bpm, last_connection['beat']),
                "note_type": 3,  # Slide end
                "note_position": check_position(first_lane, previous_position),
                "gimmick_id": 0,
                "note_action": 1,
                "wave_id": 0,
                "note_random_drop_color": 99,
                "auto_judge_type": 20
            }
            output['live_notes'].append(last_live_note)
            note_id += 1  # Increment the id for each note

# Write the output to a new JSON file
live_notes_fixup_hard = output['live_notes']
live_notes_fixup_hard.sort(key=lambda x: int(x['call_time']))
for idx_finalize_hard, item_finalize_hard in enumerate(live_notes_fixup_hard):
    item_finalize_hard['id'] = idx_finalize_hard + 1
with open('output.json', 'w') as outfile:
    json.dump(output, outfile, indent=4)

print("Conversion complete. Output saved to 'output.json'.")
