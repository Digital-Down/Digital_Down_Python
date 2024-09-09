Documentation = '''
This is a list of all classes, their cooresponding methods and arguments.
This document can be called with "print (Documentation)".

The entire package relies on the following syntax:
(Class.Method(Method Argument(s)))

Classes 										Method(s)									Method Argument(s)
========================================================================================================================================================
Text
========================================================================================================================================================
Documentation									N/A 										N/A
========================================================================================================================================================
Code
========================================================================================================================================================
PythonToJava(not yet implemented)				convert										User Defined "Multiline Code String"
--------------------------------------------------------------------------------------------------------------------------------------------------------
Extraction Synthesis 1.0.0						(GUI reference only)						(GUI reference only)
--------------------------------------------------------------------------------------------------------------------------------------------------------
Extraction Synthesis 1.5.3 						(GUI reference only)						(GUI reference only)
--------------------------------------------------------------------------------------------------------------------------------------------------------
Methlphenethylamine 1.0.0						(GUI reference only)						(GUI reference only)
========================================================================================================================================================
Audio
========================================================================================================================================================
AudioSampleValues								wav_to_list									User Defined: "WAV File Name.wav" (Place WAV alongside running script directory)
												list_to_wav									User Defined: [List]	
												list_to_wav_mono							User Defined: "Output WAV File Name.wav" (Argument for list_to_wav and list_to_wav_mono)
--------------------------------------------------------------------------------------------------------------------------------------------------------
ExtractionSynthesis								process_audio_folder_normalize				User Defined: Input Folder
												process_audio_folder						User Defined: Output Folder
																							User Defined Optional: threshold=(0 to 32767) 
																							User Defined Optional: max_threshold=(0 to 32767)
																							User Defined Optional: methylphenethylamine=bool
--------------------------------------------------------------------------------------------------------------------------------------------------------
SinglePhaseExtraction							process_audio_folder_normalize				User Defined: Input Folder
												process_audio_folder						User Defined: Output Folder
																							User Defined Optional: threshold=(0 to 32767) 
																							User Defined Optional: max_threshold=(0 to 32767)
																							User Defined Optional: methylphenethylamine=bool
																							User Defined Optional: phase='positive or negative'	
--------------------------------------------------------------------------------------------------------------------------------------------------------
Methylphenethylamine							slow										User Defined: [List]
												fast										User Defined: Operation Value(1 for slow, 1-6 for fast)
========================================================================================================================================================
Image
========================================================================================================================================================
ImageProselyte									ImageToPNG									User Defined: "Input Folder"
												ImageToJPEG									User Defined: "Output Folder"
												ImageToBMP
												ImageToGIF
												ImageToTIFF
												ImageToWebP
												ImageToICO
												ImageToPPM
												ImageToPCX
												ImageToEPS
========================================================================================================================================================
Video
========================================================================================================================================================
MindHarvestNetwork								horizontal									User Defined: "WAV File Name.wav" (Place WAV alongside running script directory)
												vertical
'''
