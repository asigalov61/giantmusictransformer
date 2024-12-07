# Giant Music Transformer
## [Giant Music Transformer](https://github.com/asigalov61/Giant-Music-Transformer) as a PyPi package

![Giant-Music-Transformer-Artwork (10)](https://github.com/user-attachments/assets/e532fed2-4aee-44ba-bd72-e3ad3a2a4e1b)

***

## Install

```sh
pip install giantmusictransformer
```

#### (Optional) [FluidSynth](https://github.com/FluidSynth/fluidsynth/wiki/Download) for MIDI to Audio functinality

##### Ubuntu or Debian

```sh
sudo apt-get install fluidsynth
```

##### Windows (with [Chocolatey](https://github.com/chocolatey/choco))

```sh
choco install fluidsynth
```

***

## Quick-start use example

```python
import giantmusictransformer as gmt

# Load desired Giant Music Transformer model
# There are several to choose from...
model = gmt.load_model('medium')

# Get sample seed MIDI path
sample_midi_path = gmt.get_sample_midi_files()[6][1]

# Load seed MIDI
input_tokens = gmt.midi_to_tokens(sample_midi_path)

# Generate seed MIDI continuation
output_tokens = gmt.generate(model, input_tokens, 600, return_prime=True)

# Save output to MIDI
gmt.tokens_to_midi(output_tokens[0])
```

***

### Project Los Angeles
### Tegridy Code 2024
