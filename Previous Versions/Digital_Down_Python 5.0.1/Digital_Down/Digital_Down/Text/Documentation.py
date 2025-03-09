Documentation = '''
This is a list of all classes, their cooresponding methods and arguments.
This document can be called with "print (Documentation)".

The entire package relies on the following syntax:
(Class.Method(Method Argument(s)))

Classes 										Method(s)									Method Argument(s)
========================================================================================================================================================
Text
========================================================================================================================================================
AlbumMetadata									title 										Incunabula_Album
												type										Putting_On_The_Ritz_Album
												length										Incunabula_Revised_Album
												numsongs									Nervous_System_Album
												songs 										Open_Source_Nervous_System_Album
												start 										Open_Source_Nervous_System_II_Album
												end 										Strawberry_Gashes_Album
												release 									God_Of_The_Gaps_Album
												all 										Open_Source_Limbic_System_Album
--------------------------------------------------------------------------------------------------------------------------------------------------------
Documentation									N/A 										N/A
--------------------------------------------------------------------------------------------------------------------------------------------------------
LicenseGenerator								default										User Defined: "product name"
																							User Defined Optional: company="company name"
																							User Defined Optional: output_folder="Output File Path"
--------------------------------------------------------------------------------------------------------------------------------------------------------
SongMetadata									title										Incunabula
												length										Forest_Is_Trees
												scale										Living_In_A_Halo
												bpm											Stepdown
												timesignature								Putting_On_The_Ritz
												lyrics										Putting_On_The_Ritz_Single
												start 										Incunabula_Revised
												end 										Nervosa
												release										Beyond_The_Trees
												album 										Open_Source_Nervous_System
												all 										Amphetamine
													 										Positivity_For_The_Masochist
																							Nervous_System
																							With_No_Eyes
																							Lenvoi
																							Retina
																							Incunabula_Remastered
																							Words
																							Beyond_The_Trees_Remastered
																							Stepdown_Prologue
																							Stepdown_Alternate
																							Nervosa_II
																							What_Saturn_Lies_In_Death
																							Putting_On_The_Ritz_Remastered
																							Deluge
																							Heaven_Isnt_Here
																							Dr_Faust
																							Mind_Harvest
																							Open_Source_Nervous_System_Demo
																							Last_October
																							Heer_Public_Archive_1943
																							Embryo
																							Putting_On_The_Ritz_Radio_Edit
																							Latrodectus
																							Stella_Splendens
																							Maslows_Du_Vide
																							Strawberry_Gashes
																							Lorem_Ipsum
																							By_Proxy
																							Lappel_Du_Vide
																							Heer_Public_Archive_1945
																							Strawberry_Gashes_Single
																							Miss_Nothing
																							Heer_Public_Archive_1944
																							God_Of_The_Gaps
																							Last_Of_October
																							De_Finibus_Bonorum_Et_Malorum
																							Sleepwalking_In_Los_Angeles
																							The_Call_Of_The_Void
																							Lacrimosa
																							All
========================================================================================================================================================
Code
========================================================================================================================================================
ListAutomationTools								beginadd									User Defined: [Multiline List of Variables]
												endadd										User Defined: "Prefix"
												beginendadd									User Defined: "Suffix"
												remove										User Defined: "Old String"
												swap										User Defined: "New String"
--------------------------------------------------------------------------------------------------------------------------------------------------------
PythonToJava(not yet implemented)				convert										User Defined "Multiline Code String"
========================================================================================================================================================
Audio
========================================================================================================================================================
AudioSampleValues								wav_to_list									User Defined: "WAV File Path" 
												list_to_wav									User Defined: [List]	
												list_to_wav_mono							User Defined: "Output WAV File Name.wav"
--------------------------------------------------------------------------------------------------------------------------------------------------------
Chords											aug 										User Defined: "scale_root"
												aug11th
												augmaj7th
 												aug7th
  												aug6thitalian
 												aug6thfrench
 												aug6thgerman
 												dim
 												dimmaj7th
												dim7th
 												dom11th
												dommin9th
 												dom9th
 												dom7thsharp9
 												dom13th
 												dream
 												elektra
 												farben
 												lydian
 												magic
 												maj
 												maj11th
 												maj7th
 												maj7thsharp11
 												maj6th
 												maj6th9th
 												maj9th
 												maj13th
 												min
 												min11th
 												min7th
 												min9th
 												min6th
 												min6th9th
 												min13th
 												mystic
 												neapolitan
 												ninethaug5th
 												northernlights
 												hexa
 												petrushka
 												power
 												sevensix
 												seventhsus4
 												sowhat
 												thirteenthflat9th
 												thirteenthflat9thflat5th
 												viennese1
 												viennese2
--------------------------------------------------------------------------------------------------------------------------------------------------------
CompositionTools								chords_in_scale								User Defined: "scale letter"
																							User Defined: "scale type"
																							User Defined Optional: position="Chord Position"
--------------------------------------------------------------------------------------------------------------------------------------------------------
DissectionSynthesis 							OctavePlus									User Defined: "Input WAV File Path" 
												OctaveMinus 								User Defined: "Output WAV File Path" 
--------------------------------------------------------------------------------------------------------------------------------------------------------

OscillationExtraction 							fullphase									User Defined: [Audio List]
												singlephase 								User Defined Optional: LowSamplePhaseCount=# 
																							User Defined Optional: LSPCOperation='omit or ignore'													
--------------------------------------------------------------------------------------------------------------------------------------------------------
SurgicalSynthesis								ExtractionSynthesis							User Defined: "Input WAV File Path" 
																							User Defined: Output Folder
																							User Defined Optional: threshold=(0 to 32767) 
																							User Defined Optional: max_threshold=(0 to 32767)
																							User Defined Optional: methylphenethylamine=bool
																							User Defined Optional: normalize=bool
																							User Defined Optional: phase=full, positive or negative
												DissectionSynthesis(Not yet Implemented)
												IncisionSynthesis(Not yet Implemented)
--------------------------------------------------------------------------------------------------------------------------------------------------------
TemporalDissectionSynthesis 					TDSSlow										User Defined: "Input WAV File Path" 
												TDSFast										User Defined: "Output WAV File Path" 
--------------------------------------------------------------------------------------------------------------------------------------------------------
Methylphenethylamine							slow										User Defined: "WAV File Path" 
												fast										User Defined: Operation Value(1 for slow, 1-6 for fast)
--------------------------------------------------------------------------------------------------------------------------------------------------------
Scales											Ionian										User Defined: "scale_root"
												Dorian										User Defined Optional: position="Chord Position" (root - twelfth)
												Phrygian
												Lydian
												Mixolydian
												Aeolian
												Locrian
												Ultralocrian
												Superlocrian
												MelodicMinor
												DorianFlat2
												LydianAugmented
												LydianDominant
												MixolydianFlat6
												LocrianSharp2
												AlteredDominant
												HarmonicMinor
												LocrianNatural6
												IonianSharp5
												DorianSharp4
												PhrygianMajor
												LydianSharp2
												SuperlocrianDoubleFlat7
												MajorPentatonic
												MinorPentatonic
												EgyptianPentatonic
												BluesScale
												MajorBluesScale
												BebopDominant
												BebopMajor
												BebopMinor
												BebopHarmonicMinor
												DoubleHarmonic
												NeapolitanMinor
												NeapolitanMajor
												HungarianMinor
												HungarianMajor
												Enigmatic
												PersianScale
												ArabicScale
												TodiTheta
												WholeTone
												Diminished
												DominantDiminished
												Chromatic
												Algerian
												AugmentedScale
												Balinese
												Byzantine
												Chinese
												Hirajoshi
												InSen
												Iwato
												Kumoi
												Pelog
												Prometheus
												SixToneSymmetrical
												Yo
												Akebono
												Asavari
========================================================================================================================================================
Image
========================================================================================================================================================
AlphaImage										black										User Defined: Tolerance Number
												white 										User Defined: "Input Image File Path"
												red 										User Defined: "Output Image File Path"
												green
												blue
--------------------------------------------------------------------------------------------------------------------------------------------------------
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
--------------------------------------------------------------------------------------------------------------------------------------------------------
ImagePixelValues								png_to_list									User Defined: "Input PNG File Path"
												list_to_png									User Defined: "Pixels List"
																							User Defined: "Output PNG File Path"
========================================================================================================================================================
Video
========================================================================================================================================================
AlphaVideo										black										User Defined: Tolerance Number
												white 										User Defined: "Input Video File Path"
												red 										User Defined: "Output Video File Path"
												green
												blue
--------------------------------------------------------------------------------------------------------------------------------------------------------
AlphaOverVideo									black										User Defined: Tolerance Number
												white 										User Defined: "Input Video 1 File Path"
												red 										User Defined: "Input Video 2 File Path"
												green										User Defined: "Output Video File Path"
												blue
--------------------------------------------------------------------------------------------------------------------------------------------------------
FramesToVideo									create_video								User Defined: "Frames Folder File Path"
																							User Defined: "Output Video File Path"
																							User Defined: fps number
--------------------------------------------------------------------------------------------------------------------------------------------------------												
MindHarvestNetwork								horizontal									User Defined: "WAV File Path" 
												vertical									User Defined: "Video File Output Path"
--------------------------------------------------------------------------------------------------------------------------------------------------------
VideoPixelValues								video_to_list								User Defined: "Input Video File Path" (Accepts mov and avi)
												list_to_video								User Defined: "Frames List"
																							User Defined: "Output Video File Path" (Accepts mov and avi)
																							User Defined Optional: fps=##
																							User Defined Optional: codec="codec"
'''

'''=====================================================================================================================================================
========================================================================================================================================================
========================================================================================================================================================
========================================================================================================================================================
========================================================================================================================================================
========================================================================================================================================================
========================================================================================================================================================
========================================================================================================================================================
========================================================================================================================================================'''

Deprecated = '''
Classes 										Method(s)									Method Argument(s)
========================================================================================================================================================
Audio
========================================================================================================================================================
BetaPhaseExtraction								process_audio_folder_normalize				User Defined: Input Folder
												process_audio_folder						User Defined: Output Folder
																							User Defined Optional: threshold=(0 to 32767) 
																							User Defined Optional: max_threshold=(0 to 32767)
																							User Defined Optional: methylphenethylamine=bool	
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
========================================================================================================================================================
Code
========================================================================================================================================================
Dissection Synthesis 1.0.0						(GUI reference only)						(GUI reference only)
--------------------------------------------------------------------------------------------------------------------------------------------------------
Extraction Synthesis 1.0.0						(GUI reference only)						(GUI reference only)
--------------------------------------------------------------------------------------------------------------------------------------------------------
Extraction Synthesis 1.5.3 						(GUI reference only)						(GUI reference only)
--------------------------------------------------------------------------------------------------------------------------------------------------------
Methlphenethylamine 1.0.0						(GUI reference only)						(GUI reference only)
'''