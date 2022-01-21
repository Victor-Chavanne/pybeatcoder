import sys
import pygments
from pygments.lexers import PythonLexer
from mido import Message, MidiFile, MidiTrack

def generate_scale(file_name):
    # https://random-music-generators.herokuapp.com/melody
    scale = [79, 74, 76, 74, 72, 67, 71, 64, 65, 59, 64, 71]
    return scale

def generate_note(token):
    token_name = str(token[0]).split('.')[1]
    token_value = str(token[1])
    if (token_name == "Text" and token_value == " ") or token_name in ["Whitespace", "Escape", "Error", "Other"]:
        return 0
    elif token_name == "Text":
        return 1
    elif token_name == "Keyword":
        return 2
    elif token_name == "Name":
        return 3
    elif token_name == "Literal":
        return 4
    elif token_name == "String":
        return 5
    elif token_name == "Number":
        return 6
    elif token_name == "Punctuation":
        return 7
    elif token_name == "Operator":
        return 8
    elif token_name == "Comment":
        return 9
    elif token_name == "Generic":
        return 10
    else:
        return 11

def generate_bass_track(token_list, scale):
    track = MidiTrack()
    track.append(Message('program_change', program=12, time=0))
    for token in token_list:
        note = generate_note(token)
        track.append(Message('note_on', channel=0, note=scale[note], velocity=64, time=0))
        track.append(Message('note_off', note=scale[note], velocity=127, time=64))
    return track

def generate_token_notes(token_line):
    token_notes_list = []
    for token in token_line:
        pass

def main(input_file, output_file):
    # Temp line of code for testing
    temp_code = "from pygments.lexers import PythonLexer"

    # Iterate over tokens
    pl = PythonLexer()
    tokens_list = [x for x in pygments.lex(temp_code, pl)]

    # generate scale
    scale = generate_scale(input_file)

    # Create midi file
    mid = MidiFile()
    mid.tracks.append(generate_bass_track(tokens_list, scale))
    mid.save(output_file)

def print_help():
    print("""Usage: pybeatcoder [INPUT FILE] [OUTPUT FILE]""")

def print_midi(midi_file):
    mid = MidiFile(midi_file)
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            print(msg)

if __name__ == '__main__':
    if len(sys.argv)==2:
        if sys.argv[1] in ["-h", "--help"]:
            print_help()
    else :
        if sys.argv[1] in ["-p", "--print"]:
            print_midi(sys.argv[2])
        else:
            main(sys.argv[1], sys.argv[2])