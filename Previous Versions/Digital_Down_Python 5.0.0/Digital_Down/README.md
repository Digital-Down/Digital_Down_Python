# Digital Down Python

## Installation
To install Digital Down, use pip:
```
pip install Digital-Down
```

## Usage
Digital Down proposes an obvious convention for implementing the import statement:
```python
import Digital_Down as DD
```
Digital_Down_Python implements a single line of code execution that goes in the order of DD.ClassName.ClassMethod(Method Arguments)

## Audio

### AudioSampleValues
Convert a wav file to a list of its raw audio values:
```python
DD.AudioSampleValues.wav_to_list('Input_wav_File_Path')
```
Convert a list of raw audio values to a wav file:
```python
DD.AudioSampleValues.list_to_wav([Input_List], 'Output_wav_File_Path')
```
Convert a list of raw audio values to a mono wav file:
```python
DD.AudioSampleValues.list_to_wav_mono([Input_List], 'Output_wav_File_Name.wav')
```

### Chords
Generate various chord types. Example with augmented chord:
```python
DD.Chords.aug("scale_root")
```
Available chord types:
aug, aug11th, augmaj7th, aug7th, aug6thitalian, aug6thfrench, aug6thgerman, dim, dimmaj7th, dim7th, dom11th, dommin9th, dom9th, dom7thsharp9, dom13th, dream, elektra, farben, lydian, magic, maj, maj11th, maj7th, maj7thsharp11, maj6th, maj6th9th, maj9th, maj13th, min, min11th, min7th, min9th, min6th, min6th9th, min13th, mystic, neapolitan, ninethaug5th, northernlights, hexa, petrushka, power, sevensix, seventhsus4, sowhat, thirteenthflat9th, thirteenthflat9thflat5th, viennese1, viennese2

### CompositionTools
Get chords in a scale:
```python
DD.CompositionTools.chords_in_scale("scale letter", "scale type", position="Chord Position")
```

### DissectionSynthesis
Process audio files:
```python
DD.DissectionSynthesis.OctavePlus('Input_WAV_File_Path', 'Output_WAV_File_Path')
DD.DissectionSynthesis.OctaveMinus('Input_WAV_File_Path', 'Output_WAV_File_Path')
```

### ExtractionSynthesis
Extract the oscillations of a folder of wav files (useful for music):
```python
DD.ExtractionSynthesis.process_audio_folder('Input_Folder_Path', 'Output_Folder_Path', threshold=0, max_threshold=32767, methylphenethylamine=False)
```
Normalized Extractions (useful for stems):
```python
DD.ExtractionSynthesis.process_audio_folder_normalize('Input_Folder_Path', 'Output_Folder_Path', threshold=0, max_threshold=32767, methylphenethylamine=False)
```

### OscillationExtraction
Extract full phase or single phase from audio:
```python
DD.OscillationExtraction.fullphase([Audio_List])
DD.OscillationExtraction.singlephase([Audio_List], LowSamplePhaseCount=0, LSPCOperation='omit')
```

### SinglePhaseExtraction
Extract the single phase oscillations of a folder of wav files:
```python
DD.SinglePhaseExtraction.process_audio_folder('Input_Folder_Path', 'Output_Folder_Path', threshold=0, max_threshold=32767, methylphenethylamine=False, phase='positive')
```
Normalized Extractions:
```python
DD.SinglePhaseExtraction.process_audio_folder_normalize('Input_Folder_Path', 'Output_Folder_Path', threshold=0, max_threshold=32767, methylphenethylamine=False, phase='positive')
```

### TemporalDissectionSynthesis
Process audio files:
```python
DD.TemporalDissectionSynthesis.TDSSlow('Input_WAV_File_Path', 'Output_WAV_File_Path')
DD.TemporalDissectionSynthesis.TDSFast('Input_WAV_File_Path', 'Output_WAV_File_Path')
```

### Methylphenethylamine
Adjust the speed of the input wav file:
```python
DD.Methylphenethylamine.slow('Input_wav_File_Path', 1)
DD.Methylphenethylamine.fast('Input_wav_File_Path', 1)  # Double speed
```
Speed can be adjusted from 1 (double) to 6 (septuple) for the fast method.

### Scales
Generate various scales. Example with Ionian scale:
```python
DD.Scales.Ionian("scale_root", position="Chord Position")
```
Available scales:
Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian, Ultralocrian, Superlocrian, MelodicMinor, DorianFlat2, LydianAugmented, LydianDominant, MixolydianFlat6, LocrianSharp2, AlteredDominant, HarmonicMinor, LocrianNatural6, IonianSharp5, DorianSharp4, PhrygianMajor, LydianSharp2, SuperlocrianDoubleFlat7, MajorPentatonic, MinorPentatonic, EgyptianPentatonic, BluesScale, MajorBluesScale, BebopDominant, BebopMajor, BebopMinor, BebopHarmonicMinor, DoubleHarmonic, NeapolitanMinor, NeapolitanMajor, HungarianMinor, HungarianMajor, Enigmatic, PersianScale, ArabicScale, TodiTheta, WholeTone, Diminished, DominantDiminished, Chromatic, Algerian, AugmentedScale, Balinese, Byzantine, Chinese, Hirajoshi, InSen, Iwato, Kumoi, Pelog, Prometheus, SixToneSymmetrical, Yo, Akebono, Asavari

## Code

### ListAutomationTools
Automate list operations:
```python
DD.ListAutomationTools.beginadd([Multiline_List_of_Variables], "Prefix")
DD.ListAutomationTools.endadd([Multiline_List_of_Variables], "Suffix")
DD.ListAutomationTools.beginendadd([Multiline_List_of_Variables], "Prefix", "Suffix")
DD.ListAutomationTools.remove([Multiline_List_of_Variables], "Old String")
DD.ListAutomationTools.swap([Multiline_List_of_Variables], "Old String", "New String")
```

## Image

### AlphaImage
Process images based on color:
```python
DD.AlphaImage.black(Tolerance_Number, 'Input_Image_File_Path', 'Output_Image_File_Path')
DD.AlphaImage.white(Tolerance_Number, 'Input_Image_File_Path', 'Output_Image_File_Path')
DD.AlphaImage.red(Tolerance_Number, 'Input_Image_File_Path', 'Output_Image_File_Path')
DD.AlphaImage.green(Tolerance_Number, 'Input_Image_File_Path', 'Output_Image_File_Path')
DD.AlphaImage.blue(Tolerance_Number, 'Input_Image_File_Path', 'Output_Image_File_Path')
```

### ImageProselyte
Check for image files in a folder and convert them to a designated file format:
```python
DD.ImageProselyte.ImageToPNG('Input_Folder', 'Output_Folder')
DD.ImageProselyte.ImageToJPEG('Input_Folder', 'Output_Folder')
DD.ImageProselyte.ImageToBMP('Input_Folder', 'Output_Folder')
DD.ImageProselyte.ImageToGIF('Input_Folder', 'Output_Folder')
DD.ImageProselyte.ImageToTIFF('Input_Folder', 'Output_Folder')
DD.ImageProselyte.ImageToWebP('Input_Folder', 'Output_Folder')
DD.ImageProselyte.ImageToICO('Input_Folder', 'Output_Folder')
DD.ImageProselyte.ImageToPPM('Input_Folder', 'Output_Folder')
DD.ImageProselyte.ImageToPCX('Input_Folder', 'Output_Folder')
DD.ImageProselyte.ImageToEPS('Input_Folder', 'Output_Folder')
```

### ImagePixelValues
Convert PNG to list and vice versa:
```python
DD.ImagePixelValues.png_to_list('Input_PNG_File_Path')
DD.ImagePixelValues.list_to_png([Pixels_List], 'Output_PNG_File_Path')
```

## Text

### AlbumMetadata
Retrieve album metadata:
```python
DD.AlbumMetadata.title(DD.Album_Name)
DD.AlbumMetadata.type(DD.Album_Name)
DD.AlbumMetadata.length(DD.Album_Name)
DD.AlbumMetadata.numsongs(DD.Album_Name)
DD.AlbumMetadata.songs(DD.Album_Name)
DD.AlbumMetadata.start(DD.Album_Name)
DD.AlbumMetadata.end(DD.Album_Name)
DD.AlbumMetadata.release(DD.Album_Name)
DD.AlbumMetadata.all(DD.Album_Name)
```

### Documentation
Print the full documentation:
```python
print(DD.Documentation)
```

### LicenseGenerator
Generate a license:
```python
DD.LicenseGenerator.default("product name", company="company name", output_folder="Output File Path")
```

### SongMetadata
Retrieve song metadata:
```python
DD.SongMetadata.title(DD.Song_Name)
DD.SongMetadata.length(DD.Song_Name)
DD.SongMetadata.scale(DD.Song_Name)
DD.SongMetadata.bpm(DD.Song_Name)
DD.SongMetadata.timesignature(DD.Song_Name)
DD.SongMetadata.lyrics(DD.Song_Name)
DD.SongMetadata.start(DD.Song_Name)
DD.SongMetadata.end(DD.Song_Name)
DD.SongMetadata.release(DD.Song_Name)
DD.SongMetadata.album(DD.Song_Name)
DD.SongMetadata.all(DD.Song_Name)
```

## Video

### AlphaVideo
Process videos based on color:
```python
DD.AlphaVideo.black(Tolerance_Number, 'Input_Video_File_Path', 'Output_Video_File_Path')
DD.AlphaVideo.white(Tolerance_Number, 'Input_Video_File_Path', 'Output_Video_File_Path')
DD.AlphaVideo.red(Tolerance_Number, 'Input_Video_File_Path', 'Output_Video_File_Path')
DD.AlphaVideo.green(Tolerance_Number, 'Input_Video_File_Path', 'Output_Video_File_Path')
DD.AlphaVideo.blue(Tolerance_Number, 'Input_Video_File_Path', 'Output_Video_File_Path')
```

### AlphaOverVideo
Process videos with alpha over effect:
```python
DD.AlphaOverVideo.black(Tolerance_Number, 'Input_Video_1_File_Path', 'Input_Video_2_File_Path', 'Output_Video_File_Path')
DD.AlphaOverVideo.white(Tolerance_Number, 'Input_Video_1_File_Path', 'Input_Video_2_File_Path', 'Output_Video_File_Path')
DD.AlphaOverVideo.red(Tolerance_Number, 'Input_Video_1_File_Path', 'Input_Video_2_File_Path', 'Output_Video_File_Path')
DD.AlphaOverVideo.green(Tolerance_Number, 'Input_Video_1_File_Path', 'Input_Video_2_File_Path', 'Output_Video_File_Path')
DD.AlphaOverVideo.blue(Tolerance_Number, 'Input_Video_1_File_Path', 'Input_Video_2_File_Path', 'Output_Video_File_Path')
```

### FramesToVideo
Create a video from frames:
```python
DD.FramesToVideo.create_video('Frames_Folder_File_Path', 'Output_Video_File_Path', fps_number)
```

### MindHarvestNetwork
Create MindHarvestNetwork visualizations:
```python
DD.MindHarvestNetwork.horizontal('Input_wav_File_Path', 'Output_File_Path')
DD.MindHarvestNetwork.vertical('Input_wav_File_Path', 'Output_File_Path')
```

### VideoPixelValues
Convert video to list and vice versa:
```python
DD.VideoPixelValues.video_to_list('Input_Video_File_Path')
DD.VideoPixelValues.list_to_video([Frames_List], 'Output_Video_File_Path', fps=30, codec="libx264")
```
