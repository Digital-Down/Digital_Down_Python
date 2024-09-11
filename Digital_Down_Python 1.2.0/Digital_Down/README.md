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
DD.AudioSampleValues.list_to_wav([Input_List],'Output_wav_File_Path')
```

Convert a wav file to a list and then back into a wav (Useless on its own, but showcases the possibilities for further processing):
```python
DD.AudioSampleValues.list_to_wav([DD.AudioSampleValues.wav_to_list('Input_wav_File_Path')],'Output_wav_File_Path')
```

### ExtractionSynthesis

Extract the oscillations of a folder of wav files (useful for music):
```python
DD.ExtractionSynthesis.process_audio_folder('Input_Folder_Path', 'Output_Folder_Path')
```

Normalized Extractions (useful for stems):
```python
DD.ExtractionSynthesis.process_audio_folder_normalize('Input_Folder_Path', 'Output_Folder_Path')
```

### SinglePhaseExtraction

Extract the single phase oscillations of a folder of wav files (useful for music):
```python
DD.SinglePhaseExtraction.process_audio_folder('Input_Folder_Path', 'Output_Folder_Path')
```

Normalized Extractions (useful for stems):
```python
DD.SinglePhaseExtraction.process_audio_folder_normalize('Input_Folder_Path', 'Output_Folder_Path')
```

### Methylphenethylamine

- Halve the speed of the input wav file:
  ```python
  DD.Methylphenethylamine.slow('Input_wav_File_Path', 1)
  ```

- Double the speed of the input wav file:
  ```python
  DD.Methylphenethylamine.fast('Input_wav_File_Path', 1)
  ```

- Triple the speed of the input wav file:
  ```python
  DD.Methylphenethylamine.fast('Input_wav_File_Path', 2)
  ```

- Quadruple the speed of the input wav file:
  ```python
  DD.Methylphenethylamine.fast('Input_wav_File_Path', 3)
  ```

- Quintuple the speed of the input wav file:
  ```python
  DD.Methylphenethylamine.fast('Input_wav_File_Path', 4)
  ```

- Sextuple the speed of the input wav file:
  ```python
  DD.Methylphenethylamine.fast('Input_wav_File_Path', 5)
  ```

- Septuple the speed of the input wav file:
  ```python
  DD.Methylphenethylamine.fast('Input_wav_File_Path', 6)
  ```

## Code

Coming Soon

## Image

### ImageProselyte

Check for image files in a folder and convert them to a designated file format:

```python
DD.ImageProselyte.ImageToPNG('Input_wav_File_Path', 'Output_File_Path')
DD.ImageProselyte.ImageToJPEG('Input_wav_File_Path', 'Output_File_Path')
DD.ImageProselyte.ImageToBMP('Input_wav_File_Path', 'Output_File_Path')
DD.ImageProselyte.ImageToGIF('Input_wav_File_Path', 'Output_File_Path')
DD.ImageProselyte.ImageToTIFF('Input_wav_File_Path', 'Output_File_Path')
DD.ImageProselyte.ImageToWebP('Input_wav_File_Path', 'Output_File_Path')
DD.ImageProselyte.ImageToICO('Input_wav_File_Path', 'Output_File_Path')
DD.ImageProselyte.ImageToPPM('Input_wav_File_Path', 'Output_File_Path')
DD.ImageProselyte.ImageToPCX('Input_wav_File_Path', 'Output_File_Path')
DD.ImageProselyte.ImageToEPS('Input_wav_File_Path', 'Output_File_Path')
```

## Text

### Documentation

```python
print(DD.Documentation)
```

## Video

### MindHarvestNetwork

Create a horizontal MindHarvestNetwork visualization:
```python
DD.MindHarvestNetwork.horizontal('Input_wav_File_Path', 'Output_File_Path')
```

Create a vertical MindHarvestNetwork visualization (useful for TikTok or YT Shorts):
```python
DD.MindHarvestNetwork.vertical('Input_wav_File_Path', 'Output_File_Path')
```
