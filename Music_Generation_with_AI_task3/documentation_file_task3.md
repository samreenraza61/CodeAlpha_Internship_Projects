
# Music Generation with LSTM Neural Networks

## Overview

This script demonstrates how to generate music using Long Short-Term Memory (LSTM) neural networks. It leverages MIDI files to create a dataset, trains an LSTM model to learn musical patterns, and generates new music sequences. The generated music is then converted from MIDI to WAV and MP3 formats for easy listening.

## Features

- **MIDI File Handling**: Upload, extract, and process MIDI files.
- **Data Preparation**: Convert MIDI notes into fixed-length sequences for training.
- **Model Training**: Train an LSTM neural network to predict musical sequences.
- **Music Generation**: Generate new music sequences based on a seed sequence.
- **File Conversion**: Convert generated MIDI sequences to WAV and MP3 formats.

## Requirements

Before running this script, ensure you have the following libraries installed:

- `pretty_midi` for MIDI file processing
- `tensorflow` for building and training the neural network
- `midi2audio` for converting MIDI to audio
- `pydub` for audio format conversion

Install the required libraries using:

```bash
pip install pretty_midi tensorflow midi2audio pydub
```

Additionally, you need to install FluidSynth and download a soundfont file:

```bash
!apt-get install -y fluidsynth
!wget https://github.com/FluidSynth/fluidsynth/blob/main/examples/midi/FluidR3_GM.sf2 -O FluidR3_GM.sf2
```

## Main Functions

1. **`midi_to_note_sequences(midi_file_path)`**: Converts MIDI files into sequences of notes, extracting pitch, start time, and end time.

2. **`notes_to_sequence(notes, sequence_length)`**: Converts a list of notes into a fixed-length sequence for model input.

3. **`create_dataset(midi_directory, sequence_length)`**: Creates a dataset of note sequences from MIDI files in a specified directory.

4. **`prepare_data(sequences, sequence_length)`**: Prepares data for model training by splitting sequences and applying one-hot encoding.

5. **`train_model(X, y)`**: Builds and trains an LSTM model on the prepared dataset. Saves the trained model to disk.

6. **`generate_music(model, seed_sequence, length)`**: Uses the trained model to generate a new sequence of notes based on a seed sequence.

7. **`sequence_to_midi(sequence, output_file)`**: Converts a sequence of notes back into a MIDI file.

8. **`convert_midi_to_wav(midi_file, wav_file)`**: Converts a MIDI file into a WAV file using FluidSynth.

9. **`convert_wav_to_mp3(wav_file, mp3_file)`**: Converts a WAV file into an MP3 file using pydub.

## Model

The script uses an LSTM (Long Short-Term Memory) neural network, a type of recurrent neural network (RNN) well-suited for sequence prediction tasks. The model consists of two LSTM layers with dropout for regularization and a dense softmax output layer to predict the next note in the sequence.

## References

- [PrettyMIDI Documentation](https://github.com/craffel/pretty-midi)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [midi2audio Documentation](https://github.com/mik3y/midi2audio)
- [pydub Documentation](https://pydub.com/)
- [FluidSynth GitHub Repository](https://github.com/FluidSynth/fluidsynth)

