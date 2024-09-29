"""
__________________________________________________________________________________
##############
#SongMetadata#
##############

This module returns text-based MetaData of any given Digital Down song.

Simple tutorial:

print (SongMetadata.Insert Method Here(Insert Method Argument Here))
__________________________________________________________________________________

###########
##Methods##
###########

1.title				Title of song
2.length			Length of song in minutes and seconds
3.scale				Scale(s) of song
4.bpm				BPM(s) of song
5.timesignature		Time Signature(s) of song
6.lyrics			Lyrics of song
7.start				Start date of making the song
8.end				Completion date of the finished song
9.release			Release date of the song to the public
10.album			Album(s) the song is included on (including alternate versions)
11.notes 			notes have been removed due to being to personal for now... it is too dark
12.all 				All of the above notes
Combined Methods (Currently Working On)
1.dates				Start, End and Release Dates
2.composition		scale, bpm, and time signature
__________________________________________________________________________________
####################
##Method Arguments##
####################

Incunabula
Forest_Is_Trees
Living_In_A_Halo
Stepdown
Putting_On_The_Ritz
Putting_On_The_Ritz_Single
Incunabula_Revised
Nervosa
Beyond_The_Trees
Open_Source_Nervous_System
Amphetamine
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
__________________________________________________________________________________
"""
######
#Main#
######
class SongMetadata:
	def __init__(self, title, length, scale, bpm, timesignature, lyrics, start, end, release, album, all): 

		self.title = title
		self.length = length
		self.scale = scale
		self.bpm = bpm
		self.timesignature = timesignature
		self.lyrics = lyrics
		self.start = start
		self.end = end
		self.release = release
		self.album = album
		self.all = all


	def title(self):
		return self.title

	def length(self):
		return self.length

	def scale(self):
		return self.scale

	def bpm(self):
		return self.bpm
	
	def timesignature(self):
		return self.timesignature

	def lyrics(self):
		return self.lyrics

	def start(self):
		return self.start

	def end(self):
		return self.end

	def release(self):
		return self.release

	def album(self):
		return self.album

	def all(self):
		return '\n'.join(str(item) for item in self.all)

#Combined Functions (Still working on this part)

	def dates(self):
		return f'''
{self.title}\n
Start Date\n {self.start}
End Date\n {self.end}
Release Date\n {self.release}'''

	def composition(self):
		return f'''
{self.title}\n
\n {self.scale}
\n {self.bpm}
\n {self.timesignature}'''

####################
#Additional Strings#
####################

novocals = "There are no vocals on this song."
#Copy and paste this into songs with no lyrics: (f"{novocals}")

#######
#Songs#
#######

Incunabula_Variables = ['Incunabula',
	'3:21', 
	'F Dorian', 
	'69', 
	'4/4', 
	' Lay me down,\n all alone.\n Trying to hide,\n for so long.\n Hazes that come,\n and you\'re not the skies.\n ' 
	'I\'m trying to get there,\n and that\'s what war\'s for.\n\n Trying to breath,\n ooh I\'m trying,\n forever.\n '
	'I\'m not what you, \n would like to see,\n please.\n Saving me time,\n time I could use to,\n try and fly.\n '
	'There\'s an angel for it.\n\n Try and protect,\n my mind.\n Try and live,\n all down to home.\n Father protect,\n my time.\n '
	'Calming the mind.\n I\'m trying too hard.\n\n Trying to breath,\n ooh I\'m trying,\n forever.\n '
	'I\'m not what you, \n would like to see,\n please.\n Saving me time,\n time I could use to,\n try and fly.\n '
	'There\'s an angel for it.\n\n Trying to breath,\n ooh I\'m trying,\n forever.\n '
	'I\'m not what you, \n would like to see,\n please.\n Saving me time,\n time I could use to,\n try and fly.\n '
	'There\'s an angel for it.',
	'01-24-2013', 
	'01-25-2013', 
	'11-02-2015',
	'Incunabula\nOpen Source Nervous System']

Forest_Is_Trees_Variables = ['Forest Is Trees', 
	'4:48', 
	'C Aeolian', 
	'77', 
	'4/4', 
	' You\'re my energy.\n (Energy)\n It\'s gone,\n way too long.\n Is it not their time?\n (Ah)\n You\'re a victim '
	'or a friend?\n (It will turn on me)\n Come see me.\n I want to calm you,\n your self disguised.\n\n '
	'But could you try,\n and cross the line,\n for me.\n I\'m going up,\n you\'re coming down.\n Forest is trees,\n '
	'come over please.\n You can never leave,\n I won\'t let you be.\n\n And time,\n is like a knife,\n and yours is mine.\n '
	'I can\'t deny you anything.\n Eye for an eye,\n let\'s try and breathe,\n and try and get,\n through to...\n\n '
	'You\'re not getting anything for it.\n I\'m just another leaf from the trees,\n trees,\n please.\n I can tell that '
	'you\'re mistaken in this. \n You\'re just another tight one. \n You\'re just another leaf on the trees, \n on the trees,'
	'\n please. \n You can\'t...\n\n '
	'But could you try,\n and cross the line,\n for me.\n I\'m going up,\n you\'re coming down.\n Forest is trees,\n '
	'come over please.\n You can never leave,\n I won\'t let you be.\n\n And time,\n is like a knife,\n and yours is mine.\n '
	'I can\'t deny you anything.\n Eye for an eye,\n let\'s try and breathe,\n and try and get,\n through to...\n\n '
	'(It really didn\'t affect me that much, it didn\'t really seem like a big deal to me as a kid and you\'re younger than I am, '
	'and for you to see that and be younger than I am, I would think that it made even less of an impact, but you\'re saying '
	'it made more. I didn\'t really understand what was going on. I didn\'t really care. It wasn\'t important to my life at that point.)\n\n '
	'But could you try,\n and cross the line,\n for me.\n I\'m going up,\n you\'re coming down.\n Forest is trees,\n '
	'come over please.\n You can never leave,\n I won\'t let you be.\n\n And time,\n is like a knife,\n and yours is mine.\n '
	'I can\'t deny you anything.\n Eye for an eye,\n let\'s try and breathe,\n and try and get,\n through to...', 
	'01-21-2013', 
	'01-22-2013', 
	'11-02-2015', 
	'Incunabula']

Living_In_A_Halo_Variables = ['Living In A Halo', 
	'4:59', 
	'G Phrygian', 
	'82.5', 
	'4/4', 
	' (Get over this,\n '
	'get over this,\n '
	'get over.)\n\n How much will I wait in here,\n for someone strong.\n Damn-a-nation angel for an eye are not enough for '
	'someone strong,\n for someone strong.\n\n You were only sickened. \n (Get over this,\n '
	'get over this,\n '
	'get over.)\n\n I can feel an angel,\n coming over me.\n I don\'t have the patience now,\n that I\'m the one diseased.\n '
	'Living in a halo,\n death is faster I know.\n Living in a halo,\n there\'s no time to let go.\n (I can feel an angel.)\n\n '
	'If an angel sings,\n or an angel screams,\n is it really just enough to die \n (for)?\n to die.\n And I\'ve been trying all this '
	'time,\n for you,\n for you.\n\n '
	'It\'s not that it\'s late for an angel.\n (Won\'t you make her?)\n Mary take her halo,\n take her under.\n Victorian Needle.\n '
	'You seem high enough for,\n not to be torn. \n\n You were only sickened. \n (Get over this,\n '
	'get over this,\n '
	'get over.)\n\n '
	'I can feel an angel,\n coming over me.\n I don\'t have the patience now,\n that I\'m the one diseased.\n '
	'Living in a halo,\n death is faster I know.\n Living in a halo,\n there\'s no time to let go.\n (I can feel an angel.)\n\n '
	'If an angel sings,\n or an angel screams,\n is it really just enough to die \n (for)?\n to die.\n And I\'ve been trying all this '
	'time,\n for you,\n for you.\n\n '
	'If an angel sings,\n or an angel screams,\n is it really just enough to die \n (for)?\n to die.\n And I\'ve been trying all this '
	'time,\n for you,\n for you.', 
	'05-14-2012', 
	'01-06-2013', 
	'11-02-2015', 
	'Incunabula']

Stepdown_Variables = ['Stepdown', 
	'4:32', 
	'C# Locrian', 
	'96', 
	'4/4', 
	'''	Sara says there's no one around
	Culminating nothing right now
	You can never say enough
	Turn away and then save yourself
	There is no help allowed
	You could fix it if you wanted to
	But you chose to break it into me
	Why are you
	In denial
	Why are you
	Self is in the bottom of a self served I'd
	And I am not trying to prove to you anything
	Ego had someone missing
	(Time to stepdown)
	You had more on your mind
	(On your mind) (time to stepdown)
	You wish you were everything
	(It's the same thing)
	Everything seemed so right
	Why is a pseudo so loud
	Terminating everything right now
	Was an evil in your pocket before you were born
	Or was it something more vain like this anthem was for
	Forewarned
	Something strong
	What could it be if you were
	Wrong
	Why are you
	In denial
	Why are you
	In denial
	Self is in the bottom of a self served I'd
	And I am not trying to prove to you anything
	(Anything)
	Ego had someone missing
	(Time to stepdown)
	You had more on your mind
	(On your mind) (time to stepdown)
	You wish you were everything
	(It's the same thing)
	Everything seemed so right
	Now that you know
	(Now that you're)
	You're out of control
	(It's time to)
	Bring it on back
	(Now that you're)
	You're out of control
	Now that you know
	(Now that you're)
	You're out of control
	(It's time to)
	Bring it on back
	(Right)
	Self is in the bottom of a self served I'd
	And I am not trying to prove to you anything
	Ego had someone missing
	(Time to stepdown)
	You had more on your mind
	(On your mind) (time to stepdown)
	You wish you were everything
	(It's the same thing)
	Everything seemed so right
	(Time to time to)
	Stepdown
	Why won't you
	Stepdown
	(Time to
	Life anymore)
	Stepdown stepdown
	(Can you not do this for me)
	Why won't you
	Stepdown''', 
	'04-12-2011', 
	'01-29-2013', 
	'11-02-2015',
	'Incunabula\nOpen Source Nervous System']

Putting_On_The_Ritz_Variables = ['Putting On The Ritz', 
	'2:24', 
	'D Aeolian', 
	'98', 
	'4/4', 
	'''	If you're blue
	And you don't know where to go to
	Why don't you go where fashion shits
	Putting on the ritz

	Different types who wear a day coat
	Pants with stripes and cutaway coat
	Perfect fits
	Putting on the ritz

	Dressed up like a million dollar trooper
	Trying hard to look like Gary Cooper

	Come let's mix where Rockafellers
	Walk with sticks or umbrellas
	In their mitts
	Putting on the ritz

	If you're blue
	And you don't know where to go to
	Why don't you go where fashion shits
	Putting on the ritz

	Dressed up like a million dollar trooper
	Trying hard to look like Gary Cooper

	If you're blue
	And you don't know where to go to
	Why don't you go where fashion shits
	Putting on the ritz

	Different types who wear a day coat
	Pants with stripes and cutaway coat
	Perfect fits
	Putting on the ritz

	Dressed up like a million dollar trooper
	Trying hard to look like Gary Cooper''', 
	'10-17-2012', 
	'10-19-2012', 
	'11-02-2015',
	'Incunabula\nPutting On The Ritz\nOpen Source Nervous System\nOpen Source Nervous System II']

Putting_On_The_Ritz_Single_Variables = ['Putting On The Ritz (Single)', 
	'2:24', 
	'D Aeolian', 
	'98', 
	'4/4', 
	'''	If you're blue
	And you don't know where to go to
	Why don't you go where fashion shits
	Putting on the ritz

	Different types who wear a day coat
	Pants with stripes and cutaway coat
	Perfect fits
	Putting on the ritz

	Dressed up like a million dollar trooper
	Trying hard to look like Gary Cooper

	Come let's mix where Rockafellers
	Walk with sticks or umbrellas
	In their mitts
	Putting on the ritz

	If you're blue
	And you don't know where to go to
	Why don't you go where fashion shits
	Putting on the ritz

	Dressed up like a million dollar trooper
	Trying hard to look like Gary Cooper

	If you're blue
	And you don't know where to go to
	Why don't you go where fashion shits
	Putting on the ritz

	Different types who wear a day coat
	Pants with stripes and cutaway coat
	Perfect fits
	Putting on the ritz

	Dressed up like a million dollar trooper
	Trying hard to look like Gary Cooper''', 
	'10-17-2012', 
	'10-19-2012', 
	'11-02-2015',
	'Incunabula\nPutting On The Ritz\nOpen Source Nervous System\nOpen Source Nervous System II']

Incunabula_Revised_Variables = ['Incunabula (Revised)', 
	'3:11', 
	'F Dorian', 
	'69', 
	'4/4', 
	' Lay me down,\n all alone.\n Trying to hide,\n for so long.\n Hazes that come,\n and you\'re not the skies.\n ' 
	'I\'m trying to get there,\n and that\'s what war\'s for.\n\n Trying to breath,\n ooh I\'m trying,\n forever.\n '
	'I\'m not what you, \n would like to see,\n please.\n Saving me time,\n time I could use to,\n try and fly.\n '
	'There\'s an angel for it.\n\n Try and protect,\n my mind.\n Try and live,\n all down to home.\n Father protect,\n my time.\n '
	'Calming the mind.\n I\'m trying too hard.\n\n Trying to breath,\n ooh I\'m trying,\n forever.\n '
	'I\'m not what you, \n would like to see,\n please.\n Saving me time,\n time I could use to,\n try and fly.\n '
	'There\'s an angel for it.\n\n Trying to breath,\n ooh I\'m trying,\n forever.\n '
	'I\'m not what you, \n would like to see,\n please.\n Saving me time,\n time I could use to,\n try and fly.\n '
	'There\'s an angel for it.', 
	'07-09-2016', 
	'07-14-2016', 
	'11-15-2016', 
	'Incunabula (Revised)']

Nervosa_Variables = ['Nervosa', 
	'0:59', 
	'N/A', 
	'120', 
	'4/4', 
	(f"{novocals}"), 
	'08-01-2012', 
	'08-24-2012', 
	'11-15-2016', 
	'Incunabula (Revised)']

Beyond_The_Trees_Variables = ['Beyond The Trees', 
	'4:48', 
	'C Aeolian', 
	'77', 
	'4/4', 
	' You\'re my energy.\n (Energy)\n It\'s gone,\n way too long.\n Is it not their time?\n (Ah)\n You\'re a victim '
	'or a friend?\n (It will turn on me)\n Come see me.\n I want to calm you,\n your self disguised.\n\n '
	'But could you try,\n and cross the line,\n for me.\n I\'m going up,\n you\'re coming down.\n Forest is trees,\n '
	'come over please.\n You can never leave,\n I won\'t let you be.\n\n And time,\n is like a knife,\n and yours is mine.\n '
	'I can\'t deny you anything.\n Eye for an eye,\n let\'s try and breathe,\n and try and get,\n through to...\n\n '
	'You\'re not getting anything for it.\n I\'m just another leaf from the trees,\n trees,\n please.\n I can tell that '
	'you\'re mistaken in this. \n You\'re just another tight one. \n You\'re just another leaf on the trees, \n on the trees,'
	'\n please. \n You can\'t...\n\n '
	'But could you try,\n and cross the line,\n for me.\n I\'m going up,\n you\'re coming down.\n Forest is trees,\n '
	'come over please.\n You can never leave,\n I won\'t let you be.\n\n And time,\n is like a knife,\n and yours is mine.\n '
	'I can\'t deny you anything.\n Eye for an eye,\n let\'s try and breathe,\n and try and get,\n through to...\n\n '
	'But could you try,\n and cross the line,\n for me.\n I\'m going up,\n you\'re coming down.\n Forest is trees,\n '
	'come over please.\n You can never leave,\n I won\'t let you be.\n\n And time,\n is like a knife,\n and yours is mine.\n '
	'I can\'t deny you anything.\n Eye for an eye,\n let\'s try and breathe,\n and try and get,\n through to...', 
	'12-23-2013', 
	'10-30-2016', 
	'11-15-2016', 
	'Incunabula (Revised)\nOpen Source Nervous System']

Open_Source_Nervous_System_Variables = ['Open Source Nervous System', 
	'1:05', 
	'F# Aeolian', 
	'106', 
	'4/4', 
	'(Gibberish)', 
	'10-11-2015', 
	'02-23-2017', 
	'05-20-2017', 
	'Nervous System\nOpen Source Nervous System']

Amphetamine_Variables = ['Amphetamine', 
	'1:42', 
	'C# Phrygian', 
	'164',
	'4/4, 2/4',  
	' Deep inside, \n you know it\'s true, \n the lies you see, \n the things you do. \n Try, \n you try and leave it all but you\'ve got, \n nothing on the mind\n \n'
	' Everyone around you doesn\'t see it like you do. \n Everyone around you doesn\'t want to be like you. \n \n'  
	' Ooh, \n there\'s nothing to do, \n but, \n you\'re safe in your room, \n so, \n you\'re talking out loud to your self again. \n \n'
	' Everyone around you doesn\'t see it like you do. \n Everyone around you doesn\'t want to be like... \n \n'
	' Everyone around you doesn\'t see it like you do. \n Everyone around you doesn\'t want to be like you.', 
	'10-13-2015', 
	'10-14-2015', 
	'05-20-2017', 
	'Nervous System']

Positivity_For_The_Masochist_Variables = ['Positivity For The Masochist', 
	'2:39', 
	'C Aeolian', 
	'120', 
	'4/4, 3/4', 
	'''	Back and forth
	Say you're nothing
	Lay it down for me
	Back and forth
	Empty offspring
	Lay it down so softer
	And I'm not gonna play this right now
	(Gonna play this right now)
	(Play this right now)
	Now it's close to over
	(Close to over)
	(Close to ver)
	Cause I'm on the last step now
	One last mistake
	You could not make
	Caress this mess
	Facing me
	The day I will not think twice
	That day I will end your life
	And it won't come done to me
	And I'm not gonna play this right now
	(Gonna play this right now)
	(Play this right now)
	Now it's close to over
	(Close to over)
	(Close to ver)
	Cause I'm on the last step now
	(The path to self realization lies within the confines
	Speech is on the contrary
	A burden to our thoughts)''', 
	'03-11-2016', 
	'04-04-2016', 
	'05-20-2017', 
	'Nervous System']

Nervous_System_Variables = ['Nervous System', 
	'2:03', 
	'F Aeolian', 
	'82', 
	'4/4', 
	'''	(It's Only been one hour. These last twenty minutes have been a lifetime. I wish I could fake sincerity. I'm some raving 
	lunatic, look what I've become. This doesn't make sense, none of this makes sense. Fourteen seconds and I'm still 
	contemplating on what important message I need to relay to the sober me, If any. That's it, time does not exist. This was 
	never me Patrick, I never existed, and you know it. This may become a frenzy that becomes out of hand. Me and Patrick, sworn 
	enemies.I can see myself coming out of the woods, sword in hand, Patrick with his battleaxe coming out of the ocean. A fierce
	fight should soon ensue. Why am I smoking this electronic.... (spit).... I've just been poisoned. There's a void, some 
	witchcraft or wizardry he's trying to make. How Many Hours?)''', 
	'10-08-2014', 
	'10-12-2014', 
	'05-20-2017', 
	'Nervous System']

With_No_Eyes_Variables = ['With No Eyes', 
	'2:45', 
	'B Phrygian', 
	'120', 
	'4/4', 
	'''	There's a man in my room and his face on the wall with no eyes,
	There's a man in my room and his face on the wall with no eyes,
	There's a man in my room and his face on the wall with no eyes,
	If I make a sound he'll know that I'm stirring inside,
	If I make a sound he'll know that I'm trying to hide,
	Everybody knows,
	Everybody knows hate takes a lifetime,
	Everybody knows,
	Everybody knows hate is the eyesight,
	It's the eyesight,
	Hate takes a lifetime,
	It's just a reflection of all of the time that's gone by,
	It's just a reflection of all of the time I've been high,
	Everybody knows,
	Everybody knows hate takes a lifetime,
	Everybody knows,
	Everybody knows hate is the eyesight,
	It's the eyesight,
	Hate takes a lifetime,
	Everybody knows,
	Everybody knows hate takes a lifetime,
	Everybody knows,
	Everybody knows hate is the eyesight,
	It's the eyesight''', 
	'03-29-2017', 
	'04-01-2017', 
	'05-20-2017', 
	'Nervous System']

Lenvoi_Variables = ['L\'envoi', 
	'2:13', 
	'F# Aeolian', 
	'101', 
	'1/4, 4/4', 
	'''	Play dead, cover it up said, "Is it normal now, is it normal now"?
	Play dead, cover it up said, "Is it normal now, is it normal now"?
	Play dead, cover it up said, "Is it normal now, is it normal now"?
	Play dead, cover it up said, "Is it normal now, is it normal now"?
	Play dead, cover it up said, "Is it normal now, is it normal now"?
	Play dead, cover it up said, "Is it normal now, is it normal now"?
	Normal now, is it normal now?''', 
	'10-01-2016', 
	'02-23-2017', 
	'05-20-2017', 
	'Nervous System']

Retina_Variables = ['Retina', 
	'1:03', 
	'Chromatic', 
	'120', 
	'4/4', 
	'''(Damnit)(I got a feelin')(My god, oh god)(Bad Society)''', 
	'05-29-2009', 
	'05-29-2009', 
	'09-03-2017', 
	'Open Source Nervous System']

Incunabula_Remastered_Variables = ['Incunabula (Remastered)', 
	'3:21', 
	'F Dorian', 
	'69', 
	'4/4', 
	' Lay me down,\n all alone.\n Trying to hide,\n for so long.\n Hazes that come,\n and you\'re not the skies.\n ' 
	'I\'m trying to get there,\n and that\'s what war\'s for.\n\n Trying to breath,\n ooh I\'m trying,\n forever.\n '
	'I\'m not what you, \n would like to see,\n please.\n Saving me time,\n time I could use to,\n try and fly.\n '
	'There\'s an angel for it.\n\n Try and protect,\n my mind.\n Try and live,\n all down to home.\n Father protect,\n my time.\n '
	'Calming the mind.\n I\'m trying too hard.\n\n Trying to breath,\n ooh I\'m trying,\n forever.\n '
	'I\'m not what you, \n would like to see,\n please.\n Saving me time,\n time I could use to,\n try and fly.\n '
	'There\'s an angel for it.\n\n Trying to breath,\n ooh I\'m trying,\n forever.\n '
	'I\'m not what you, \n would like to see,\n please.\n Saving me time,\n time I could use to,\n try and fly.\n '
	'There\'s an angel for it.',
	'01-24-2013', 
	'02-23-2017', 
	'09-03-2017', 
	'Open Source Nervous System\nIncunabula']
Beyond_The_Trees_Remastered_Variables = ['Beyond The Trees', 
	'4:48', 
	'C Aeolian', 
	'77', 
	'4/4', 
	' You\'re my energy.\n (Energy)\n It\'s gone,\n way too long.\n Is it not their time?\n (Ah)\n You\'re a victim '
	'or a friend?\n (It will turn on me)\n Come see me.\n I want to calm you,\n your self disguised.\n\n '
	'But could you try,\n and cross the line,\n for me.\n I\'m going up,\n you\'re coming down.\n Forest is trees,\n '
	'come over please.\n You can never leave,\n I won\'t let you be.\n\n And time,\n is like a knife,\n and yours is mine.\n '
	'I can\'t deny you anything.\n Eye for an eye,\n let\'s try and breathe,\n and try and get,\n through to...\n\n '
	'You\'re not getting anything for it.\n I\'m just another leaf from the trees,\n trees,\n please.\n I can tell that '
	'you\'re mistaken in this. \n You\'re just another tight one. \n You\'re just another leaf on the trees, \n on the trees,'
	'\n please. \n You can\'t...\n\n '
	'But could you try,\n and cross the line,\n for me.\n I\'m going up,\n you\'re coming down.\n Forest is trees,\n '
	'come over please.\n You can never leave,\n I won\'t let you be.\n\n And time,\n is like a knife,\n and yours is mine.\n '
	'I can\'t deny you anything.\n Eye for an eye,\n let\'s try and breathe,\n and try and get,\n through to...\n\n '
	'But could you try,\n and cross the line,\n for me.\n I\'m going up,\n you\'re coming down.\n Forest is trees,\n '
	'come over please.\n You can never leave,\n I won\'t let you be.\n\n And time,\n is like a knife,\n and yours is mine.\n '
	'I can\'t deny you anything.\n Eye for an eye,\n let\'s try and breathe,\n and try and get,\n through to...', 
	'12-23-2013', 
	'10-30-2016', 
	'09-13-2017', 
	'Incunabula (Revised)\nOpen Source Nervous System']

Words_Variables = ['Words', 
	'1:08', 
	'C Aeolian', 
	'99', 
	'4/4', 
	'''	All the words can stay,
	all the words away,
	your way,
	all the way now,
	all the way,
	all the way,
	your way now.''', 
	'07-19-2013', 
	'07-21-2013', 
	'09-03-2017', 
	'Open Source Nervous System']

Stepdown_Prologue_Variables = ['Stepdown Prologue', 
	'0:33', 
	'C# Locrian', 
	'96', 
	'4/4', 
	(f"{novocals}"), 
	'04-12-2011', 
	'03-11-2017', 
	'09-03-2017', 
	'Open Source Nervous System']

Stepdown_Alternate_Variables = ['Stepdown (Alternate)', 
	'4:22', 
	'C# Locrian', 
	'96', 
	'4/4', 
	'''	Sara says there's no one around
	Culminating nothing right now
	You can never say enough
	Turn away and then save yourself
	There is no help allowed
	You could fix it if you wanted to
	But you chose to break it into me
	Why are you
	In denial
	Why are you
	Self is in the bottom of a self served I'd
	And I am not trying to prove to you anything
	Ego had someone missing
	(Time to stepdown)
	You had more on your mind
	(On your mind) (time to step...)
	You wish you were everything
	(It's the same thing)
	Everything seemed so right
	Why is a pseudo so loud
	Terminating everything right now
	Was an evil in your pocket before you were born
	Or was it something more vain like this anthem was for
	Forewarned
	Something strong
	What could it be if you were
	Wrong
	Why are you
	In denial
	Why are you
	In denial
	Self is in the bottom of a self served I'd
	And I am not trying to prove to you anything
	(Anything)
	Ego had someone missing
	(Time to stepdown)
	You had more on your mind
	(On your mind) (time to step...)
	You wish you were everything
	(It's the same thing)
	Everything seemed so right
	Now that you know
	(Now that you're)
	You're out of control
	(It's time to)
	Bring it on back
	(Now that you're)
	You're out of control
	Now that you know
	(Now that you're)
	You're out of control
	(It's time to)
	Bring it on back
	(Right)
	Self is in the bottom of a self served I'd
	And I am not trying to prove to you anything
	Goddamn
	Really gives a good goddamn about it 
	Ego had someone missing
	(Time to stepdown)
	You had more on your mind
	(On your mind) (time to step...)
	You wish you were everything
	(It's the same thing)
	Everything seemed so right
	(Time to time to)
	Stepdown
	Why won't you
	Stepdown
	(Time to
	Life anymore)
	Stepdown stepdown
	(Can you not do this for me)
	Why won't you
	Stepdown''', 
	'04-12-2011', 
	'08-18-2017', 
	'09-03-2017', 
	'Open Source Nervous System\nIncunabula']

Nervosa_II_Variables = ['Nervosa II', 
	'0:59', 
	'N/A', 
	'120', 
	'4/4', 
	'''	I'm going to start taking diet pills cause I'm fat
	I don't want to be fat when I come back to Alabama
	Cause I used to be so pretty but now I'm not
	I'm so fat
	And I can't stop eating
	Cause I'm so depressed''', 
	'08-01-2012', 
	'08-24-2012', 
	'09-03-2017', 
	'Open Source Nervous System']

What_Saturn_Lies_In_Death_Variables = ['What Saturn Lies In Death', 
	'1:00', 
	'Currently Unknown', 
	'Currently Unknown', 
	'Currently Unknown', 
	(f"{novocals}"), 
	'Currently Unknown', 
	'Currently Unknown', 
	'09-03-2017', 
	'Open Source Nervous System']

Putting_On_The_Ritz_Remastered_Variables = ['Putting On The Ritz (Remastered)', 
	'2:24', 
	'D Aeolian', 
	'98', 
	'4/4', 
	'''	If you're blue
	And you don't know where to go to
	Why don't you go where fashion shits
	Putting on the ritz

	Different types who wear a day coat
	Pants with stripes and cutaway coat
	Perfect fits
	Putting on the ritz

	Dressed up like a million dollar trooper
	Trying hard to look like Gary Cooper

	Come let's mix where Rockafellers
	Walk with sticks or umbrellas
	In their mitts
	Putting on the ritz

	If you're blue
	And you don't know where to go to
	Why don't you go where fashion shits
	Putting on the ritz

	Dressed up like a million dollar trooper
	Trying hard to look like Gary Cooper

	If you're blue
	And you don't know where to go to
	Why don't you go where fashion shits
	Putting on the ritz

	Different types who wear a day coat
	Pants with stripes and cutaway coat
	Perfect fits
	Putting on the ritz

	Dressed up like a million dollar trooper
	Trying hard to look like Gary Cooper''',
	'10-17-2012',
	'05-04-2017', 
	'09-03-2017', 
	'Incunabula\nPutting On The Ritz\nOpen Source Nervous System\nOpen Source Nervous System II']

Deluge_Variables = ['Deluge', 
	'1:02', 
	'C Aeolian', 
	'72', 
	'4/4', 
	(f"{novocals}"), 
	'02-10-2013', 
	'02-10-2013', 
	'09-03-2017', 
	'Open Source Nervous System']

Heaven_Isnt_Here_Variables = ['Heaven Isn\'t Here', 
	'4:04', 
	'A# Aeolian', 
	'105', 
	'4/4', 
	'''	Ooh
	Heaven isn't here
	Don't you wish you heard more closer from a phantom
	Jesus isn't here
	Not here
	I
	sheltered isn't here
	Sorry but you'll hurt more likely than a phantom
	Jesus isn't here
	Not here
	Would you ever like to
	Ring your remedy
	Cause I've found Jesus isn't here
	Didn't die for
	Another beat is on
	His active body
	You could find a better way
	Too
	Jesus isn't here
	Sorry but you'll find more faith in an angel
	Heaven isn't here
	well not near
	Ooh
	Heaven isn't near
	If there ever was a glimpse of an angel
	Heaven would appear
	But not here
	Would you ever like to
	Ring your remedy
	Cause I've found Jesus isn't here
	Didn't die for
	Another beat is on
	His active body
	You could find a better way
	Too
	Would you ever like to
	Ring your remedy
	Cause I've found Jesus isn't here
	Didn't die for
	Another beat is on
	His active body
	You could find a better way
	Too
	Would you ever like to
	Ring your remedy
	Cause I've found Jesus isn't here
	Didn't die for
	Another beat is on
	His active body
	You could find a better way
	Too''', 
	'02-27-2013', 
	'02-27-2013', 
	'09-03-2017', 
	'Open Source Nervous System']

Dr_Faust_Variables = ['Dr. Faust', 
	'1:47', 
	'Chromatic', 
	'100', 
	'4/4', 
	'''	I manipulated war and nature
	Never want morales
	I never want to be part of that world
	Ever''', 
	'11-12-2011', 
	'06-23-2013', 
	'09-03-2017', 
	'Open Source Nervous System']

Mind_Harvest_Variables = ['Mind Harvest', 
	'0:40', 
	'N/A', 
	'96', 
	'4/4', 
	(f"{novocals}"), 
	'01-24-2013', 
	'01-24-2013', 
	'09-03-2017', 
	'Open Source Nervous System']

Open_Source_Nervous_System_Demo_Variables = ['Open Source Nervous System (Demo)', 
	'1:05', 
	'F# Aeolian', 
	'106', 
	'4/4', 
	'(Gibberish)', 
	'10-11-2015', 
	'10-11-2015', 
	'09-03-2017', 
	'Open Source Nervous System\nNervous System']

Last_October_Variables = ['Last October', 
	'2:36', 
	'B Aeolian', 
	'132', 
	'4/4', 
	'''	Once upon
	The midnight moon it's...
	A coorelated story that I never knew
	(Tell it right)
	The same lies
	It's been a good night but
	It's one week
	Longer than the angels cry
	October she weeps
	Slowly as she sleeps
	(When all things come to an ending)
	October she weeps
	I couldn't see
	Any clearer 
	All that's ever been
	(Right in front of me)
	Right in front of you
	The same lies
	It's been a good night but
	It's one week
	Longer than the angels lie
	October she weeps
	Slowly as she sleeps
	(When all things come to an ending)
	October she weeps
	(You'll find)
	The same lies
	It's been a good night but
	It's one week
	Longer than the angels lie
	October she weeps
	Slowly as she sleeps
	(When all things come to an ending)''', 
	'10-02-2015', 
	'10-03-2015', 
	'09-03-2017', 
	'Open Source Nervous System']

Heer_Public_Archive_1943_Variables = ['Heer Public Archive 1943', 
	'11:57', 
	'N/A', 
	'85', 
	'N/A', 
	(f"{novocals}"), 
	'08-12-2011', 
	'08-13-2011', 
	'09-03-2017', 
	'Open Source Nervous System']

Embryo_Variables = ['Embryo', 
	'0:31', 
	'C Aeolian', 
	'92', 
	'4/4', 
	(f"{novocals}"), 
	'01-30-2013', 
	'01-31-2013', 
	'08-04-2018', 
	'Open Source Nervous System II']

Putting_On_The_Ritz_Radio_Edit_Variables = ['Putting On The Ritz (Radio Edit)', 
	'2:24', 
	'D Aeolian', 
	'98', 
	'4/4', 
	'''	If you're blue
	And you don't know where to go to
	Why don't you go where fashion shi-
	Putting on the ritz

	Different types who wear a day coat
	Pants with stripes and cutaway coat
	Perfect fits
	Putting on the ritz

	Dressed up like a million dollar trooper
	Trying hard to look like Gary Cooper

	Come let's mix where Rockafellers
	Walk with sticks or umbrellas
	In their mitts
	Putting on the ritz

	If you're blue
	And you don't know where to go to
	Why don't you go where fashion shi-
	Putting on the ritz

	Dressed up like a million dollar trooper
	Trying hard to look like Gary Cooper

	If you're blue
	And you don't know where to go to
	Why don't you go where fashion shi-
	Putting on the ritz

	Different types who wear a day coat
	Pants with stripes and cutaway coat
	Perfect fits
	Putting on the ritz

	Dressed up like a million dollar trooper
	Trying hard to look like Gary Cooper''',
	'10-17-2012',
	'05-04-2017', 
	'08-04-2018', 
	'Incunabula\nPutting On The Ritz\nOpen Source Nervous System\nOpen Source Nervous System II']

Latrodectus_Variables = ['Latrodectus', 
	'1:36', 
	'D Ionian', 
	'90', 
	'4/4', 
	(f"{novocals}"), 
	'02-05-2013', 
	'02-05-2013', 
	'08-04-2018', 
	'Open Source Nervous System II']

Stella_Splendens_Variables = ['Stella Splendens', 
	'1:44', 
	'C Mixolydian', 
	'120', 
	'2/4', 
	(f"{novocals}"), 
	'10-20-2017', 
	'10-20-2017', 
	'08-04-2018', 
	'Open Source Nervous System II']

Maslows_Du_Vide_Variables = ['Maslow\'s Du Vide', 
	'1:52', 
	'C Aeolian', 
	'102', 
	'4/4', 
	(f"{novocals}"), 
	'05-16-2017', 
	'05-16-2017', 
	'08-04-2018', 
	'Open Source Nervous System II']

Strawberry_Gashes_Variables = ['Strawberry Gashes', 
	'4:51', 
	'G# Aeolian', 
	'148', 
	'3/4', 
	'''	(Kill me
	She said kill me
	She said kill me
	She said kill me)
	Kill me
	I lay quiet
	Waiting for her voice to say,
	"Some Things you lose and some things you just give away"
	(Get away from me)
	Scold me
	Failed her
	If only I held on tighter to her
	Pale white skin
	(with)
	Strawberry gashes all over
	Watch me
	(It's almost like losing, like losing, like losing)
	Watch me
	(It's almost like losing, like...)
	She said kill me faster with strawberry gashes all over
	The poison that runs it's course
	(The poison that runs it's course through)
	Asked her if she was improving
	She said, "feels fine, it's wonderful, wonderful here"
	(It's wonderful, wonderful)
	Curse me
	Sold her
	The poison that runs it's course through her
	Pale white skin with 
	Strawberry gashes all over
	Watch me
	(It's almost like losing, like losing, like losing)
	Living like a disaster
	She said kill me faster with strawberry gashes all over
	Watch me
	Lose her
	It's almost like losing myself
	(It's almost like...)
	Give her
	My soul
	And let them take somebody else
	(Get away from me)
	I lay quiet
	Waiting for her voice to say,
	"Some Things you lose and some things you just give away"
	(Get away from me)
	Scold me
	Failed her
	If only I held on tighter to her
	Pale white skin
	That
	Twisted and withered away
	(Away from me)
	Watch me
	Lose her
	It's almost like losing myself
	Give her
	My soul
	And let them take somebody else
	Watch me
	(It's almost like losing, like losing myself
	She said kill me)
	She said kill me faster with strawberry gashes all over''', 
	'11-13-2017', 
	'01-31-2018', 
	'08-04-2018', 
	'Open Source Nervous System\nStrawberry Gashes']

Lorem_Ipsum_Variables = ['Lorem Ipsum', 
	'1:40', 
	'C Aeolian', 
	'120', 
	'4/4', 
	(f"{novocals}"), 
	'05-17-2018', 
	'05-19-2018', 
	'08-04-2018', 
	'Open Source Nervous System II']

By_Proxy_Variables = ['By Proxy', 
	'4:25', 
	'D# Aeolian', 
	'95', 
	'4/4', 
	'''	A stranger... a stranger... a stranger... a stranger... a stranger 
	Cover up heaven, and they cover up heaven, and they cover up heaven, and they cover up heaven and they
	Cover up heaven, and they cover up heaven, and they cover up heaven, and they cover up heaven and they
	Cover up heaven, and they cover up heaven, and they cover up heaven, and they cover up heaven and they
	Cover up heaven, and they cover up heaven, and they cover up heaven, and they cover up heaven and they
	Cover up heaven, and they cover up heaven, and they cover up heaven, and they cover up heaven and they
	Cover up hea-''', 
	'08-28-2011', 
	'09-26-2017', 
	'08-04-2018', 
	'Open Source Nervous System II']

Lappel_Du_Vide_Variables = ['L\'appel Du Vide', 
	'2:31', 
	'G# Aeolian', 
	'135', 
	'4/4', 
	'''	Am I real
	Tell me so
	I just overdosed on opium
	Everyone around 
	Please don't be real
	Tell me so
	I just overdosed on opium
	Everyone around 
	Please don't be real
	There's a needle
	On the floor
	I want it more and more than any time before
	There's a halo
	On the door
	I see it more and more but I'm stuck on this floor
	Am I real
	Tell me so
	I just overdosed on opium
	Everyone around 
	Please don't be real
	Tell me so
	I just overdosed on opium
	Everyone around 
	Please don't be real
	(Tell me so
	I just overdosed on opium
	Everyone around 
	Please don't be real
	Tell me so
	I just overdosed on opium
	Everyone around 
	Please don't be real)''', 
	'11-21-2017', 
	'02-05-2018', 
	'08-04-2018', 
	'Open Source Nervous System II']

Heer_Public_Archive_1945_Variables = ['Heer Public Archive 1945', 
	'12:27', 
	'N/A', 
	'120', 
	'N/A', 
	(f"{novocals}"), 
	'08-12-2011', 
	'09-02-2011', 
	'08-04-2018', 
	'Open Source Nervous System II']

Strawberry_Gashes_Single_Variables = ['Strawberry Gashes', 
	'4:51', 
	'G# Aeolian', 
	'148', 
	'3/4', 
	'''	(Kill me
	She said kill me
	She said kill me
	She said kill me)
	Kill me
	I lay quiet
	Waiting for her voice to say,
	"Some Things you lose and some things you just give away"
	(Get away from me)
	Scold me
	Failed her
	If only I held on tighter to her
	Pale white skin
	(with)
	Strawberry gashes all over
	Watch me
	(It's almost like losing, like losing, like losing)
	Watch me
	(It's almost like losing, like...)
	She said kill me faster with strawberry gashes all over
	The poison that runs it's course
	(The poison that runs it's course through)
	Asked her if she was improving
	She said, "feels fine, it's wonderful, wonderful here"
	(It's wonderful, wonderful)
	Curse me
	Sold her
	The poison that runs it's course through her
	Pale white skin with 
	Strawberry gashes all over
	Watch me
	(It's almost like losing, like losing, like losing)
	Living like a disaster
	She said kill me faster with strawberry gashes all over
	Watch me
	Lose her
	It's almost like losing myself
	(It's almost like...)
	Give her
	My soul
	And let them take somebody else
	(Get away from me)
	I lay quiet
	Waiting for her voice to say,
	"Some Things you lose and some things you just give away"
	(Get away from me)
	Scold me
	Failed her
	If only I held on tighter to her
	Pale white skin
	That
	Twisted and withered away
	(Away from me)
	Watch me
	Lose her
	It's almost like losing myself
	Give her
	My soul
	And let them take somebody else
	Watch me
	(It's almost like losing, like losing myself
	She said kill me)
	She said kill me faster with strawberry gashes all over''', 
	'11-13-2017', 
	'01-31-2018', 
	'07-29-2019', 
	'Open Source Nervous System\nStrawberry Gashes']

Miss_Nothing_Variables = ['Miss Nothing', 
	'2:31', 
	'C# Aeolian', 
	'105', 
	'4/4', 
	'''	Hey misses nothing say nothing's true
	Lie like an angel sees demons too
	Cry like your heaven sees through and through
	Not that safe for me and you
	Hey miss nothing
	You say you're straight sluttin'
	And I called just to figure you out
	Now there's nothing
	The day you'll leave no one around
	This has nothing to do with you
	Hey misses nothing is nothing true
	Lie like the angel sees demons too
	Cry like your heaven sees through and through
	And dine on the newer things
	(Forget about you)
	Hey miss nothing
	You say you're straight sluttin'
	And I called just to figure you out
	Now there's nothing
	The day you'll leave no one around
	This has nothing to do with you
	This has nothing to do with you
	And we'll be the ones to make it through
	This has nothing to do with you
	We'll be the ones to make it through
	This has nothing to do with you
	(And I called just to figure you out)
	Hey miss nothing
	You say you're straight sluttin'
	And I called just to figure you out
	Now there's nothing
	The day you'll leave no one around
	This has nothing to do with you
	(This has nothing to do with you)''', 
	'04-28-2016', 
	'06-10-2016', 
	'07-29-2019', 
	'Strawberry Gashes']

Heer_Public_Archive_1944_Variables = ['Heer Public Archive 1944', 
	'1:40', 
	'N/A', 
	'85', 
	'N/A', 
	(f"{novocals}"), 
	'08-12-2011', 
	'09-01-2011', 
	'07-29-2019', 
	'Strawberry Gashes']

God_Of_The_Gaps_Variables = ['God Of The Gaps', 
	'1:52', 
	'F# Aeolian', 
	'120', 
	'4/4', 
	'''	Paralyze
	Paralyze me
	You deny
	You deny me
	Longing for denial's fear
	And the love is way too late
	Longing for denial's fear
	And the hatred doesn't wait
	Paralyze
	Paralyze me
	You deny
	You deny me
	Was it clear
	Has patience lost it's mind
	Did hatred lose it all to stir the slumbering
	Or was hope hard to find
	Longing for denial's fear
	And the love is way too late
	Longing for denial's fear
	And the hatred doesn't ever wait''', 
	'02-02-2016', 
	'02-04-2016', 
	'05-05-2020', 
	'God Of The Gaps']

Last_Of_October_Variables = ['Last Of October', 
	'2:40', 
	'B Aeolian', 
	'132', 
	'4/4', 
	'''	Once upon
	The midnight moon it's...
	A coorelated story that I never knew
	(Tell it right)
	The same lies
	It's been a good night but
	It's one week
	Longer than the angels cry
	October she weeps
	Slowly as she sleeps
	(When all things come to an ending)
	October she weeps
	I couldn't see
	Any clearer 
	All that's ever been
	(Right in front of me)
	Right in front of you
	The same lies
	It's been a good night but
	It's one week
	Longer than the angels lie
	October she weeps
	Slowly as she sleeps
	(When all things come to an ending)
	October she weeps
	(You'll find)
	The same lies
	It's been a good night but
	It's one week
	Longer than the angels lie
	October she weeps
	Slowly as she sleeps
	(When all things come to an ending)''', 
	'08-03-2016', 
	'09-15-2018', 
	'05-05-2020', 
	'God Of The Gaps']

De_Finibus_Bonorum_Et_Malorum_Variables = ['De Finibus Bonorum Et Malorum', 
	'1:19', 
	'C Double Harmonic Minor', 
	'120', 
	'4/4', 
	(f"{novocals}"), 
	'01-13-2024', 
	'03-20-2024', 
	'04-04-2024', 
	'Open Source Limbic System']

Sleepwalking_In_Los_Angeles_Variables = ['Sleepwalking In Los Angeles', 
	'4:25', 
	'C# Harmonic Minor', 
	'96', 
	'4/4', 
	'''	Sara says there's no one around
	Culminating nothing right now
	You can never say enough
	Turn away and then save yourself
	There is no help allowed
	You could fix it if you wanted to
	But you chose to break it into me
	Why are you
	In denial
	Why are you
	Self is in the bottom of a self served I'd
	And I am not trying to prove to you anything
	Ego had someone missing
	(Time to stepdown)
	You had more on your mind
	(On your mind) (time to step...)
	You wish you were everything
	(It's the same thing)
	Everything seemed so right
	Why is a pseudo so loud
	Terminating everything right now
	Was an evil in your pocket before you were born
	Or was it something more vain like this anthem was for
	Forewarned
	Something strong
	What could it be if you were
	Wrong
	Why are you
	In denial
	Why are you
	In denial
	Self is in the bottom of a self served I'd
	And I am not trying to prove to you anything
	Ego had someone missing
	(Time to stepdown)
	You had more on your mind
	(On your mind) (time to step...)
	You wish you were everything
	(It's the same thing)
	Everything seemed so right
	Now that you know
	(Now that you're)
	You're out of control
	(It's time to)
	Bring it on back
	(Now that you're)
	You're out of control
	Now that you know
	(Now that you're)
	You're out of control
	(It's time to)
	Bring it on back
	(Right)
	Self is in the bottom of a self served I'd
	And I am not trying to prove to you anything
	Ego had someone missing
	(Time to stepdown)
	You had more on your mind
	(On your mind) (time to step...)
	You wish you were everything
	(It's the same thing)
	Everything seemed so right
	(Time to time to)
	Stepdown
	Why won't you
	Stepdown
	(Time to
	Life anymore)
	Stepdown stepdown
	(Can you not do this for me)
	Why won't you
	Stepdown''', 
	'01-15-2024', 
	'03-20-2024', 
	'04-04-2024', 
	'Open Source Limbic System']

The_Call_Of_The_Void_Variables = ['The Call Of The Void', 
	'1:04', 
	'G# Double Harmonic Minor', 
	'120', 
	'4/4', 
	'''	(My Head is spinning.
	All of my most sensitive areas we're inflamed.
	My extremeties pulsating with tingling sensation.
	The lines between them begin to dissapear.
	I began to float, up and away from my body.)''', 
	'01-13-2024', 
	'03-20-2024', 
	'04-04-2024', 
	'Open Source Limbic System']

Lacrimosa_Variables = ['Lacrimosa', 
	'0:39', 
	'N/A', 
	'80', 
	'4/4', 
	'''	(When I woke up this morning...
	I heard a disturbing sound.
	I said when I woke up this morning...
	I heard a disturbing sound.
	What I heard...
	was the jingle jangle of a thousand lost souls.)''',
	'02-27-2024', 
	'03-20-2024', 
	'04-04-2024', 
	'Open Source Limbic System']

############
#Incunabula#
############

#Automate the rest of the below, change title, change variable names (use all vars at bottom, take out the stuff first then do what i said before these parenthesis)

Incunabula = SongMetadata((f"{Incunabula_Variables[0]}"),
	(f"{Incunabula_Variables[1]}"), 
	(f"{Incunabula_Variables[2]}"),
	(f"{Incunabula_Variables[3]}"), 
	(f"{Incunabula_Variables[4]}"), 
	(f"{Incunabula_Variables[5]}"),
	(f"{Incunabula_Variables[6]}"), 
	(f"{Incunabula_Variables[7]}"), 
	(f"{Incunabula_Variables[8]}"),
	(f"{Incunabula_Variables[9]}"),
	((f"{Incunabula_Variables[0]}\n"),
	(f"{Incunabula_Variables[1]}"), 
	(f"{Incunabula_Variables[2]}"),
	(f"{Incunabula_Variables[3]}"), 
	(f"{Incunabula_Variables[4]}\n\nLyrics: \n"), 
	(f"{Incunabula_Variables[5]}\n\nStart Date:"),
	(f"{Incunabula_Variables[6]}\nEnd Date:"), 
	(f"{Incunabula_Variables[7]}\nRelease Date:"), 
	(f"{Incunabula_Variables[8]}\n\nAlbum(s):"),
    (f"{Incunabula_Variables[9]}")))

Forest_Is_Trees = SongMetadata((f"{Forest_Is_Trees_Variables[0]}"),
    (f"{Forest_Is_Trees_Variables[1]}"), 
    (f"{Forest_Is_Trees_Variables[2]}"),
    (f"{Forest_Is_Trees_Variables[3]}"), 
    (f"{Forest_Is_Trees_Variables[4]}"), 
    (f"{Forest_Is_Trees_Variables[5]}"),
    (f"{Forest_Is_Trees_Variables[6]}"), 
    (f"{Forest_Is_Trees_Variables[7]}"), 
    (f"{Forest_Is_Trees_Variables[8]}"),
    (f"{Forest_Is_Trees_Variables[9]}"),
    ((f"{Forest_Is_Trees_Variables[0]}\n"),
    (f"{Forest_Is_Trees_Variables[1]}"), 
    (f"{Forest_Is_Trees_Variables[2]}"),
    (f"{Forest_Is_Trees_Variables[3]}"), 
    (f"{Forest_Is_Trees_Variables[4]}\n\nLyrics: \n"), 
    (f"{Forest_Is_Trees_Variables[5]}\n\nStart Date:"),
    (f"{Forest_Is_Trees_Variables[6]}\nEnd Date:"), 
    (f"{Forest_Is_Trees_Variables[7]}\nRelease Date:"), 
    (f"{Forest_Is_Trees_Variables[8]}\n\nAlbum(s):"),
    (f"{Forest_Is_Trees_Variables[9]}")))


Living_In_A_Halo = SongMetadata((f"{Living_In_A_Halo_Variables[0]}"),
    (f"{Living_In_A_Halo_Variables[1]}"), 
    (f"{Living_In_A_Halo_Variables[2]}"),
    (f"{Living_In_A_Halo_Variables[3]}"), 
    (f"{Living_In_A_Halo_Variables[4]}"), 
    (f"{Living_In_A_Halo_Variables[5]}"),
    (f"{Living_In_A_Halo_Variables[6]}"), 
    (f"{Living_In_A_Halo_Variables[7]}"), 
    (f"{Living_In_A_Halo_Variables[8]}"),
    (f"{Living_In_A_Halo_Variables[9]}"),
    ((f"{Living_In_A_Halo_Variables[0]}\n"),
    (f"{Living_In_A_Halo_Variables[1]}"), 
    (f"{Living_In_A_Halo_Variables[2]}"),
    (f"{Living_In_A_Halo_Variables[3]}"), 
    (f"{Living_In_A_Halo_Variables[4]}\n\nLyrics: \n"), 
    (f"{Living_In_A_Halo_Variables[5]}\n\nStart Date:"),
    (f"{Living_In_A_Halo_Variables[6]}\nEnd Date:"), 
    (f"{Living_In_A_Halo_Variables[7]}\nRelease Date:"), 
    (f"{Living_In_A_Halo_Variables[8]}\n\nAlbum(s):"),
    (f"{Living_In_A_Halo_Variables[9]}")))


Stepdown = SongMetadata((f"{Stepdown_Variables[0]}"),
    (f"{Stepdown_Variables[1]}"), 
    (f"{Stepdown_Variables[2]}"),
    (f"{Stepdown_Variables[3]}"), 
    (f"{Stepdown_Variables[4]}"), 
    (f"{Stepdown_Variables[5]}"),
    (f"{Stepdown_Variables[6]}"), 
    (f"{Stepdown_Variables[7]}"), 
    (f"{Stepdown_Variables[8]}"),
    (f"{Stepdown_Variables[9]}"),
    ((f"{Stepdown_Variables[0]}\n"),
    (f"{Stepdown_Variables[1]}"), 
    (f"{Stepdown_Variables[2]}"),
    (f"{Stepdown_Variables[3]}"), 
    (f"{Stepdown_Variables[4]}\n\nLyrics: \n"), 
    (f"{Stepdown_Variables[5]}\n\nStart Date:"),
    (f"{Stepdown_Variables[6]}\nEnd Date:"), 
    (f"{Stepdown_Variables[7]}\nRelease Date:"), 
    (f"{Stepdown_Variables[8]}\n\nAlbum(s):"),
    (f"{Stepdown_Variables[9]}")))


Putting_On_The_Ritz = SongMetadata((f"{Putting_On_The_Ritz_Variables[0]}"),
    (f"{Putting_On_The_Ritz_Variables[1]}"), 
    (f"{Putting_On_The_Ritz_Variables[2]}"),
    (f"{Putting_On_The_Ritz_Variables[3]}"), 
    (f"{Putting_On_The_Ritz_Variables[4]}"), 
    (f"{Putting_On_The_Ritz_Variables[5]}"),
    (f"{Putting_On_The_Ritz_Variables[6]}"), 
    (f"{Putting_On_The_Ritz_Variables[7]}"), 
    (f"{Putting_On_The_Ritz_Variables[8]}"),
    (f"{Putting_On_The_Ritz_Variables[9]}"),
    ((f"{Putting_On_The_Ritz_Variables[0]}\n"),
    (f"{Putting_On_The_Ritz_Variables[1]}"), 
    (f"{Putting_On_The_Ritz_Variables[2]}"),
    (f"{Putting_On_The_Ritz_Variables[3]}"), 
    (f"{Putting_On_The_Ritz_Variables[4]}\n\nLyrics: \n"), 
    (f"{Putting_On_The_Ritz_Variables[5]}\n\nStart Date:"),
    (f"{Putting_On_The_Ritz_Variables[6]}\nEnd Date:"), 
    (f"{Putting_On_The_Ritz_Variables[7]}\nRelease Date:"), 
    (f"{Putting_On_The_Ritz_Variables[8]}\n\nAlbum(s):"),
    (f"{Putting_On_The_Ritz_Variables[9]}")))


Putting_On_The_Ritz_Single = SongMetadata((f"{Putting_On_The_Ritz_Single_Variables[0]}"),
    (f"{Putting_On_The_Ritz_Single_Variables[1]}"), 
    (f"{Putting_On_The_Ritz_Single_Variables[2]}"),
    (f"{Putting_On_The_Ritz_Single_Variables[3]}"), 
    (f"{Putting_On_The_Ritz_Single_Variables[4]}"), 
    (f"{Putting_On_The_Ritz_Single_Variables[5]}"),
    (f"{Putting_On_The_Ritz_Single_Variables[6]}"), 
    (f"{Putting_On_The_Ritz_Single_Variables[7]}"), 
    (f"{Putting_On_The_Ritz_Single_Variables[8]}"),
    (f"{Putting_On_The_Ritz_Single_Variables[9]}"),
    ((f"{Putting_On_The_Ritz_Single_Variables[0]}\n"),
    (f"{Putting_On_The_Ritz_Single_Variables[1]}"), 
    (f"{Putting_On_The_Ritz_Single_Variables[2]}"),
    (f"{Putting_On_The_Ritz_Single_Variables[3]}"), 
    (f"{Putting_On_The_Ritz_Single_Variables[4]}\n\nLyrics: \n"), 
    (f"{Putting_On_The_Ritz_Single_Variables[5]}\n\nStart Date:"),
    (f"{Putting_On_The_Ritz_Single_Variables[6]}\nEnd Date:"), 
    (f"{Putting_On_The_Ritz_Single_Variables[7]}\nRelease Date:"), 
    (f"{Putting_On_The_Ritz_Single_Variables[8]}\n\nAlbum(s):"),
    (f"{Putting_On_The_Ritz_Single_Variables[9]}")))

Incunabula_Revised = SongMetadata((f"{Incunabula_Revised_Variables[0]}"),
    (f"{Incunabula_Revised_Variables[1]}"), 
    (f"{Incunabula_Revised_Variables[2]}"),
    (f"{Incunabula_Revised_Variables[3]}"), 
    (f"{Incunabula_Revised_Variables[4]}"), 
    (f"{Incunabula_Revised_Variables[5]}"),
    (f"{Incunabula_Revised_Variables[6]}"), 
    (f"{Incunabula_Revised_Variables[7]}"), 
    (f"{Incunabula_Revised_Variables[8]}"),
    (f"{Incunabula_Revised_Variables[9]}"),
    ((f"{Incunabula_Revised_Variables[0]}\n"),
    (f"{Incunabula_Revised_Variables[1]}"), 
    (f"{Incunabula_Revised_Variables[2]}"),
    (f"{Incunabula_Revised_Variables[3]}"), 
    (f"{Incunabula_Revised_Variables[4]}\n\nLyrics: \n"), 
    (f"{Incunabula_Revised_Variables[5]}\n\nStart Date:"),
    (f"{Incunabula_Revised_Variables[6]}\nEnd Date:"), 
    (f"{Incunabula_Revised_Variables[7]}\nRelease Date:"), 
    (f"{Incunabula_Revised_Variables[8]}\n\nAlbum(s):"),
    (f"{Incunabula_Revised_Variables[9]}")))


Nervosa = SongMetadata((f"{Nervosa_Variables[0]}"),
    (f"{Nervosa_Variables[1]}"), 
    (f"{Nervosa_Variables[2]}"),
    (f"{Nervosa_Variables[3]}"), 
    (f"{Nervosa_Variables[4]}"), 
    (f"{Nervosa_Variables[5]}"),
    (f"{Nervosa_Variables[6]}"), 
    (f"{Nervosa_Variables[7]}"), 
    (f"{Nervosa_Variables[8]}"),
    (f"{Nervosa_Variables[9]}"),
    ((f"{Nervosa_Variables[0]}\n"),
    (f"{Nervosa_Variables[1]}"), 
    (f"{Nervosa_Variables[2]}"),
    (f"{Nervosa_Variables[3]}"), 
    (f"{Nervosa_Variables[4]}\n\nLyrics: \n"), 
    (f"{Nervosa_Variables[5]}\n\nStart Date:"),
    (f"{Nervosa_Variables[6]}\nEnd Date:"), 
    (f"{Nervosa_Variables[7]}\nRelease Date:"), 
    (f"{Nervosa_Variables[8]}\n\nAlbum(s):"),
    (f"{Nervosa_Variables[9]}")))


Beyond_The_Trees = SongMetadata((f"{Beyond_The_Trees_Variables[0]}"),
    (f"{Beyond_The_Trees_Variables[1]}"), 
    (f"{Beyond_The_Trees_Variables[2]}"),
    (f"{Beyond_The_Trees_Variables[3]}"), 
    (f"{Beyond_The_Trees_Variables[4]}"), 
    (f"{Beyond_The_Trees_Variables[5]}"),
    (f"{Beyond_The_Trees_Variables[6]}"), 
    (f"{Beyond_The_Trees_Variables[7]}"), 
    (f"{Beyond_The_Trees_Variables[8]}"),
    (f"{Beyond_The_Trees_Variables[9]}"),
    ((f"{Beyond_The_Trees_Variables[0]}\n"),
    (f"{Beyond_The_Trees_Variables[1]}"), 
    (f"{Beyond_The_Trees_Variables[2]}"),
    (f"{Beyond_The_Trees_Variables[3]}"), 
    (f"{Beyond_The_Trees_Variables[4]}\n\nLyrics: \n"), 
    (f"{Beyond_The_Trees_Variables[5]}\n\nStart Date:"),
    (f"{Beyond_The_Trees_Variables[6]}\nEnd Date:"), 
    (f"{Beyond_The_Trees_Variables[7]}\nRelease Date:"), 
    (f"{Beyond_The_Trees_Variables[8]}\n\nAlbum(s):"),
    (f"{Beyond_The_Trees_Variables[9]}")))


Open_Source_Nervous_System = SongMetadata((f"{Open_Source_Nervous_System_Variables[0]}"),
    (f"{Open_Source_Nervous_System_Variables[1]}"), 
    (f"{Open_Source_Nervous_System_Variables[2]}"),
    (f"{Open_Source_Nervous_System_Variables[3]}"), 
    (f"{Open_Source_Nervous_System_Variables[4]}"), 
    (f"{Open_Source_Nervous_System_Variables[5]}"),
    (f"{Open_Source_Nervous_System_Variables[6]}"), 
    (f"{Open_Source_Nervous_System_Variables[7]}"), 
    (f"{Open_Source_Nervous_System_Variables[8]}"),
    (f"{Open_Source_Nervous_System_Variables[9]}"),
    ((f"{Open_Source_Nervous_System_Variables[0]}\n"),
    (f"{Open_Source_Nervous_System_Variables[1]}"), 
    (f"{Open_Source_Nervous_System_Variables[2]}"),
    (f"{Open_Source_Nervous_System_Variables[3]}"), 
    (f"{Open_Source_Nervous_System_Variables[4]}\n\nLyrics: \n"), 
    (f"{Open_Source_Nervous_System_Variables[5]}\n\nStart Date:"),
    (f"{Open_Source_Nervous_System_Variables[6]}\nEnd Date:"), 
    (f"{Open_Source_Nervous_System_Variables[7]}\nRelease Date:"), 
    (f"{Open_Source_Nervous_System_Variables[8]}\n\nAlbum(s):"),
    (f"{Open_Source_Nervous_System_Variables[9]}")))


Amphetamine = SongMetadata((f"{Amphetamine_Variables[0]}"),
    (f"{Amphetamine_Variables[1]}"), 
    (f"{Amphetamine_Variables[2]}"),
    (f"{Amphetamine_Variables[3]}"), 
    (f"{Amphetamine_Variables[4]}"), 
    (f"{Amphetamine_Variables[5]}"),
    (f"{Amphetamine_Variables[6]}"), 
    (f"{Amphetamine_Variables[7]}"), 
    (f"{Amphetamine_Variables[8]}"),
    (f"{Amphetamine_Variables[9]}"),
    ((f"{Amphetamine_Variables[0]}\n"),
    (f"{Amphetamine_Variables[1]}"), 
    (f"{Amphetamine_Variables[2]}"),
    (f"{Amphetamine_Variables[3]}"), 
    (f"{Amphetamine_Variables[4]}\n\nLyrics: \n"), 
    (f"{Amphetamine_Variables[5]}\n\nStart Date:"),
    (f"{Amphetamine_Variables[6]}\nEnd Date:"), 
    (f"{Amphetamine_Variables[7]}\nRelease Date:"), 
    (f"{Amphetamine_Variables[8]}\n\nAlbum(s):"),
    (f"{Amphetamine_Variables[9]}")))


Positivity_For_The_Masochist = SongMetadata((f"{Positivity_For_The_Masochist_Variables[0]}"),
    (f"{Positivity_For_The_Masochist_Variables[1]}"), 
    (f"{Positivity_For_The_Masochist_Variables[2]}"),
    (f"{Positivity_For_The_Masochist_Variables[3]}"), 
    (f"{Positivity_For_The_Masochist_Variables[4]}"), 
    (f"{Positivity_For_The_Masochist_Variables[5]}"),
    (f"{Positivity_For_The_Masochist_Variables[6]}"), 
    (f"{Positivity_For_The_Masochist_Variables[7]}"), 
    (f"{Positivity_For_The_Masochist_Variables[8]}"),
    (f"{Positivity_For_The_Masochist_Variables[9]}"),
    ((f"{Positivity_For_The_Masochist_Variables[0]}\n"),
    (f"{Positivity_For_The_Masochist_Variables[1]}"), 
    (f"{Positivity_For_The_Masochist_Variables[2]}"),
    (f"{Positivity_For_The_Masochist_Variables[3]}"), 
    (f"{Positivity_For_The_Masochist_Variables[4]}\n\nLyrics: \n"), 
    (f"{Positivity_For_The_Masochist_Variables[5]}\n\nStart Date:"),
    (f"{Positivity_For_The_Masochist_Variables[6]}\nEnd Date:"), 
    (f"{Positivity_For_The_Masochist_Variables[7]}\nRelease Date:"), 
    (f"{Positivity_For_The_Masochist_Variables[8]}\n\nAlbum(s):"),
    (f"{Positivity_For_The_Masochist_Variables[9]}")))


Nervous_System = SongMetadata((f"{Nervous_System_Variables[0]}"),
    (f"{Nervous_System_Variables[1]}"), 
    (f"{Nervous_System_Variables[2]}"),
    (f"{Nervous_System_Variables[3]}"), 
    (f"{Nervous_System_Variables[4]}"), 
    (f"{Nervous_System_Variables[5]}"),
    (f"{Nervous_System_Variables[6]}"), 
    (f"{Nervous_System_Variables[7]}"), 
    (f"{Nervous_System_Variables[8]}"),
    (f"{Nervous_System_Variables[9]}"),
    ((f"{Nervous_System_Variables[0]}\n"),
    (f"{Nervous_System_Variables[1]}"), 
    (f"{Nervous_System_Variables[2]}"),
    (f"{Nervous_System_Variables[3]}"), 
    (f"{Nervous_System_Variables[4]}\n\nLyrics: \n"), 
    (f"{Nervous_System_Variables[5]}\n\nStart Date:"),
    (f"{Nervous_System_Variables[6]}\nEnd Date:"), 
    (f"{Nervous_System_Variables[7]}\nRelease Date:"), 
    (f"{Nervous_System_Variables[8]}\n\nAlbum(s):"),
    (f"{Nervous_System_Variables[9]}")))


With_No_Eyes = SongMetadata((f"{With_No_Eyes_Variables[0]}"),
    (f"{With_No_Eyes_Variables[1]}"), 
    (f"{With_No_Eyes_Variables[2]}"),
    (f"{With_No_Eyes_Variables[3]}"), 
    (f"{With_No_Eyes_Variables[4]}"), 
    (f"{With_No_Eyes_Variables[5]}"),
    (f"{With_No_Eyes_Variables[6]}"), 
    (f"{With_No_Eyes_Variables[7]}"), 
    (f"{With_No_Eyes_Variables[8]}"),
    (f"{With_No_Eyes_Variables[9]}"),
    ((f"{With_No_Eyes_Variables[0]}\n"),
    (f"{With_No_Eyes_Variables[1]}"), 
    (f"{With_No_Eyes_Variables[2]}"),
    (f"{With_No_Eyes_Variables[3]}"), 
    (f"{With_No_Eyes_Variables[4]}\n\nLyrics: \n"), 
    (f"{With_No_Eyes_Variables[5]}\n\nStart Date:"),
    (f"{With_No_Eyes_Variables[6]}\nEnd Date:"), 
    (f"{With_No_Eyes_Variables[7]}\nRelease Date:"), 
    (f"{With_No_Eyes_Variables[8]}\n\nAlbum(s):"),
    (f"{With_No_Eyes_Variables[9]}")))


Lenvoi = SongMetadata((f"{Lenvoi_Variables[0]}"),
    (f"{Lenvoi_Variables[1]}"), 
    (f"{Lenvoi_Variables[2]}"),
    (f"{Lenvoi_Variables[3]}"), 
    (f"{Lenvoi_Variables[4]}"), 
    (f"{Lenvoi_Variables[5]}"),
    (f"{Lenvoi_Variables[6]}"), 
    (f"{Lenvoi_Variables[7]}"), 
    (f"{Lenvoi_Variables[8]}"),
    (f"{Lenvoi_Variables[9]}"),
    ((f"{Lenvoi_Variables[0]}\n"),
    (f"{Lenvoi_Variables[1]}"), 
    (f"{Lenvoi_Variables[2]}"),
    (f"{Lenvoi_Variables[3]}"), 
    (f"{Lenvoi_Variables[4]}\n\nLyrics: \n"), 
    (f"{Lenvoi_Variables[5]}\n\nStart Date:"),
    (f"{Lenvoi_Variables[6]}\nEnd Date:"), 
    (f"{Lenvoi_Variables[7]}\nRelease Date:"), 
    (f"{Lenvoi_Variables[8]}\n\nAlbum(s):"),
    (f"{Lenvoi_Variables[9]}")))


Retina = SongMetadata((f"{Retina_Variables[0]}"),
    (f"{Retina_Variables[1]}"), 
    (f"{Retina_Variables[2]}"),
    (f"{Retina_Variables[3]}"), 
    (f"{Retina_Variables[4]}"), 
    (f"{Retina_Variables[5]}"),
    (f"{Retina_Variables[6]}"), 
    (f"{Retina_Variables[7]}"), 
    (f"{Retina_Variables[8]}"),
    (f"{Retina_Variables[9]}"),
    ((f"{Retina_Variables[0]}\n"),
    (f"{Retina_Variables[1]}"), 
    (f"{Retina_Variables[2]}"),
    (f"{Retina_Variables[3]}"), 
    (f"{Retina_Variables[4]}\n\nLyrics: \n"), 
    (f"{Retina_Variables[5]}\n\nStart Date:"),
    (f"{Retina_Variables[6]}\nEnd Date:"), 
    (f"{Retina_Variables[7]}\nRelease Date:"), 
    (f"{Retina_Variables[8]}\n\nAlbum(s):"),
    (f"{Retina_Variables[9]}")))


Incunabula_Remastered = SongMetadata((f"{Incunabula_Remastered_Variables[0]}"),
    (f"{Incunabula_Remastered_Variables[1]}"), 
    (f"{Incunabula_Remastered_Variables[2]}"),
    (f"{Incunabula_Remastered_Variables[3]}"), 
    (f"{Incunabula_Remastered_Variables[4]}"), 
    (f"{Incunabula_Remastered_Variables[5]}"),
    (f"{Incunabula_Remastered_Variables[6]}"), 
    (f"{Incunabula_Remastered_Variables[7]}"), 
    (f"{Incunabula_Remastered_Variables[8]}"),
    (f"{Incunabula_Remastered_Variables[9]}"),
    ((f"{Incunabula_Remastered_Variables[0]}\n"),
    (f"{Incunabula_Remastered_Variables[1]}"), 
    (f"{Incunabula_Remastered_Variables[2]}"),
    (f"{Incunabula_Remastered_Variables[3]}"), 
    (f"{Incunabula_Remastered_Variables[4]}\n\nLyrics: \n"), 
    (f"{Incunabula_Remastered_Variables[5]}\n\nStart Date:"),
    (f"{Incunabula_Remastered_Variables[6]}\nEnd Date:"), 
    (f"{Incunabula_Remastered_Variables[7]}\nRelease Date:"), 
    (f"{Incunabula_Remastered_Variables[8]}\n\nAlbum(s):"),
    (f"{Incunabula_Remastered_Variables[9]}")))


Words = SongMetadata((f"{Words_Variables[0]}"),
    (f"{Words_Variables[1]}"), 
    (f"{Words_Variables[2]}"),
    (f"{Words_Variables[3]}"), 
    (f"{Words_Variables[4]}"), 
    (f"{Words_Variables[5]}"),
    (f"{Words_Variables[6]}"), 
    (f"{Words_Variables[7]}"), 
    (f"{Words_Variables[8]}"),
    (f"{Words_Variables[9]}"),
    ((f"{Words_Variables[0]}\n"),
    (f"{Words_Variables[1]}"), 
    (f"{Words_Variables[2]}"),
    (f"{Words_Variables[3]}"), 
    (f"{Words_Variables[4]}\n\nLyrics: \n"), 
    (f"{Words_Variables[5]}\n\nStart Date:"),
    (f"{Words_Variables[6]}\nEnd Date:"), 
    (f"{Words_Variables[7]}\nRelease Date:"), 
    (f"{Words_Variables[8]}\n\nAlbum(s):"),
    (f"{Words_Variables[9]}")))


Beyond_The_Trees_Remastered = SongMetadata((f"{Beyond_The_Trees_Remastered_Variables[0]}"),
    (f"{Beyond_The_Trees_Remastered_Variables[1]}"), 
    (f"{Beyond_The_Trees_Remastered_Variables[2]}"),
    (f"{Beyond_The_Trees_Remastered_Variables[3]}"), 
    (f"{Beyond_The_Trees_Remastered_Variables[4]}"), 
    (f"{Beyond_The_Trees_Remastered_Variables[5]}"),
    (f"{Beyond_The_Trees_Remastered_Variables[6]}"), 
    (f"{Beyond_The_Trees_Remastered_Variables[7]}"), 
    (f"{Beyond_The_Trees_Remastered_Variables[8]}"),
    (f"{Beyond_The_Trees_Remastered_Variables[9]}"),
    ((f"{Beyond_The_Trees_Remastered_Variables[0]}\n"),
    (f"{Beyond_The_Trees_Remastered_Variables[1]}"), 
    (f"{Beyond_The_Trees_Remastered_Variables[2]}"),
    (f"{Beyond_The_Trees_Remastered_Variables[3]}"), 
    (f"{Beyond_The_Trees_Remastered_Variables[4]}\n\nLyrics: \n"), 
    (f"{Beyond_The_Trees_Remastered_Variables[5]}\n\nStart Date:"),
    (f"{Beyond_The_Trees_Remastered_Variables[6]}\nEnd Date:"), 
    (f"{Beyond_The_Trees_Remastered_Variables[7]}\nRelease Date:"), 
    (f"{Beyond_The_Trees_Remastered_Variables[8]}\n\nAlbum(s):"),
    (f"{Beyond_The_Trees_Remastered_Variables[9]}")))


Stepdown_Prologue = SongMetadata((f"{Stepdown_Prologue_Variables[0]}"),
    (f"{Stepdown_Prologue_Variables[1]}"), 
    (f"{Stepdown_Prologue_Variables[2]}"),
    (f"{Stepdown_Prologue_Variables[3]}"), 
    (f"{Stepdown_Prologue_Variables[4]}"), 
    (f"{Stepdown_Prologue_Variables[5]}"),
    (f"{Stepdown_Prologue_Variables[6]}"), 
    (f"{Stepdown_Prologue_Variables[7]}"), 
    (f"{Stepdown_Prologue_Variables[8]}"),
    (f"{Stepdown_Prologue_Variables[9]}"),
    ((f"{Stepdown_Prologue_Variables[0]}\n"),
    (f"{Stepdown_Prologue_Variables[1]}"), 
    (f"{Stepdown_Prologue_Variables[2]}"),
    (f"{Stepdown_Prologue_Variables[3]}"), 
    (f"{Stepdown_Prologue_Variables[4]}\n\nLyrics: \n"), 
    (f"{Stepdown_Prologue_Variables[5]}\n\nStart Date:"),
    (f"{Stepdown_Prologue_Variables[6]}\nEnd Date:"), 
    (f"{Stepdown_Prologue_Variables[7]}\nRelease Date:"), 
    (f"{Stepdown_Prologue_Variables[8]}\n\nAlbum(s):"),
    (f"{Stepdown_Prologue_Variables[9]}")))


Stepdown_Alternate = SongMetadata((f"{Stepdown_Alternate_Variables[0]}"),
    (f"{Stepdown_Alternate_Variables[1]}"), 
    (f"{Stepdown_Alternate_Variables[2]}"),
    (f"{Stepdown_Alternate_Variables[3]}"), 
    (f"{Stepdown_Alternate_Variables[4]}"), 
    (f"{Stepdown_Alternate_Variables[5]}"),
    (f"{Stepdown_Alternate_Variables[6]}"), 
    (f"{Stepdown_Alternate_Variables[7]}"), 
    (f"{Stepdown_Alternate_Variables[8]}"),
    (f"{Stepdown_Alternate_Variables[9]}"),
    ((f"{Stepdown_Alternate_Variables[0]}\n"),
    (f"{Stepdown_Alternate_Variables[1]}"), 
    (f"{Stepdown_Alternate_Variables[2]}"),
    (f"{Stepdown_Alternate_Variables[3]}"), 
    (f"{Stepdown_Alternate_Variables[4]}\n\nLyrics: \n"), 
    (f"{Stepdown_Alternate_Variables[5]}\n\nStart Date:"),
    (f"{Stepdown_Alternate_Variables[6]}\nEnd Date:"), 
    (f"{Stepdown_Alternate_Variables[7]}\nRelease Date:"), 
    (f"{Stepdown_Alternate_Variables[8]}\n\nAlbum(s):"),
    (f"{Stepdown_Alternate_Variables[9]}")))


Nervosa_II = SongMetadata((f"{Nervosa_II_Variables[0]}"),
    (f"{Nervosa_II_Variables[1]}"), 
    (f"{Nervosa_II_Variables[2]}"),
    (f"{Nervosa_II_Variables[3]}"), 
    (f"{Nervosa_II_Variables[4]}"), 
    (f"{Nervosa_II_Variables[5]}"),
    (f"{Nervosa_II_Variables[6]}"), 
    (f"{Nervosa_II_Variables[7]}"), 
    (f"{Nervosa_II_Variables[8]}"),
    (f"{Nervosa_II_Variables[9]}"),
    ((f"{Nervosa_II_Variables[0]}\n"),
    (f"{Nervosa_II_Variables[1]}"), 
    (f"{Nervosa_II_Variables[2]}"),
    (f"{Nervosa_II_Variables[3]}"), 
    (f"{Nervosa_II_Variables[4]}\n\nLyrics: \n"), 
    (f"{Nervosa_II_Variables[5]}\n\nStart Date:"),
    (f"{Nervosa_II_Variables[6]}\nEnd Date:"), 
    (f"{Nervosa_II_Variables[7]}\nRelease Date:"), 
    (f"{Nervosa_II_Variables[8]}\n\nAlbum(s):"),
    (f"{Nervosa_II_Variables[9]}")))

What_Saturn_Lies_In_Death = SongMetadata((f"{What_Saturn_Lies_In_Death_Variables[0]}"),
    (f"{What_Saturn_Lies_In_Death_Variables[1]}"), 
    (f"{What_Saturn_Lies_In_Death_Variables[2]}"),
    (f"{What_Saturn_Lies_In_Death_Variables[3]}"), 
    (f"{What_Saturn_Lies_In_Death_Variables[4]}"), 
    (f"{What_Saturn_Lies_In_Death_Variables[5]}"),
    (f"{What_Saturn_Lies_In_Death_Variables[6]}"), 
    (f"{What_Saturn_Lies_In_Death_Variables[7]}"), 
    (f"{What_Saturn_Lies_In_Death_Variables[8]}"),
    (f"{What_Saturn_Lies_In_Death_Variables[9]}"),
    ((f"{What_Saturn_Lies_In_Death_Variables[0]}\n"),
    (f"{What_Saturn_Lies_In_Death_Variables[1]}"), 
    (f"{What_Saturn_Lies_In_Death_Variables[2]}"),
    (f"{What_Saturn_Lies_In_Death_Variables[3]}"), 
    (f"{What_Saturn_Lies_In_Death_Variables[4]}\n\nLyrics: \n"), 
    (f"{What_Saturn_Lies_In_Death_Variables[5]}\n\nStart Date:"),
    (f"{What_Saturn_Lies_In_Death_Variables[6]}\nEnd Date:"), 
    (f"{What_Saturn_Lies_In_Death_Variables[7]}\nRelease Date:"), 
    (f"{What_Saturn_Lies_In_Death_Variables[8]}\n\nAlbum(s):"),
    (f"{What_Saturn_Lies_In_Death_Variables[9]}")))

Putting_On_The_Ritz_Remastered = SongMetadata((f"{Putting_On_The_Ritz_Remastered_Variables[0]}"),
    (f"{Putting_On_The_Ritz_Remastered_Variables[1]}"), 
    (f"{Putting_On_The_Ritz_Remastered_Variables[2]}"),
    (f"{Putting_On_The_Ritz_Remastered_Variables[3]}"), 
    (f"{Putting_On_The_Ritz_Remastered_Variables[4]}"), 
    (f"{Putting_On_The_Ritz_Remastered_Variables[5]}"),
    (f"{Putting_On_The_Ritz_Remastered_Variables[6]}"), 
    (f"{Putting_On_The_Ritz_Remastered_Variables[7]}"), 
    (f"{Putting_On_The_Ritz_Remastered_Variables[8]}"),
    (f"{Putting_On_The_Ritz_Remastered_Variables[9]}"),
    ((f"{Putting_On_The_Ritz_Remastered_Variables[0]}\n"),
    (f"{Putting_On_The_Ritz_Remastered_Variables[1]}"), 
    (f"{Putting_On_The_Ritz_Remastered_Variables[2]}"),
    (f"{Putting_On_The_Ritz_Remastered_Variables[3]}"), 
    (f"{Putting_On_The_Ritz_Remastered_Variables[4]}\n\nLyrics: \n"), 
    (f"{Putting_On_The_Ritz_Remastered_Variables[5]}\n\nStart Date:"),
    (f"{Putting_On_The_Ritz_Remastered_Variables[6]}\nEnd Date:"), 
    (f"{Putting_On_The_Ritz_Remastered_Variables[7]}\nRelease Date:"), 
    (f"{Putting_On_The_Ritz_Remastered_Variables[8]}\n\nAlbum(s):"),
    (f"{Putting_On_The_Ritz_Remastered_Variables[9]}")))


Deluge = SongMetadata((f"{Deluge_Variables[0]}"),
    (f"{Deluge_Variables[1]}"), 
    (f"{Deluge_Variables[2]}"),
    (f"{Deluge_Variables[3]}"), 
    (f"{Deluge_Variables[4]}"), 
    (f"{Deluge_Variables[5]}"),
    (f"{Deluge_Variables[6]}"), 
    (f"{Deluge_Variables[7]}"), 
    (f"{Deluge_Variables[8]}"),
    (f"{Deluge_Variables[9]}"),
    ((f"{Deluge_Variables[0]}\n"),
    (f"{Deluge_Variables[1]}"), 
    (f"{Deluge_Variables[2]}"),
    (f"{Deluge_Variables[3]}"), 
    (f"{Deluge_Variables[4]}\n\nLyrics: \n"), 
    (f"{Deluge_Variables[5]}\n\nStart Date:"),
    (f"{Deluge_Variables[6]}\nEnd Date:"), 
    (f"{Deluge_Variables[7]}\nRelease Date:"), 
    (f"{Deluge_Variables[8]}\n\nAlbum(s):"),
    (f"{Deluge_Variables[9]}")))


Heaven_Isnt_Here = SongMetadata((f"{Heaven_Isnt_Here_Variables[0]}"),
    (f"{Heaven_Isnt_Here_Variables[1]}"), 
    (f"{Heaven_Isnt_Here_Variables[2]}"),
    (f"{Heaven_Isnt_Here_Variables[3]}"), 
    (f"{Heaven_Isnt_Here_Variables[4]}"), 
    (f"{Heaven_Isnt_Here_Variables[5]}"),
    (f"{Heaven_Isnt_Here_Variables[6]}"), 
    (f"{Heaven_Isnt_Here_Variables[7]}"), 
    (f"{Heaven_Isnt_Here_Variables[8]}"),
    (f"{Heaven_Isnt_Here_Variables[9]}"),
    ((f"{Heaven_Isnt_Here_Variables[0]}\n"),
    (f"{Heaven_Isnt_Here_Variables[1]}"), 
    (f"{Heaven_Isnt_Here_Variables[2]}"),
    (f"{Heaven_Isnt_Here_Variables[3]}"), 
    (f"{Heaven_Isnt_Here_Variables[4]}\n\nLyrics: \n"), 
    (f"{Heaven_Isnt_Here_Variables[5]}\n\nStart Date:"),
    (f"{Heaven_Isnt_Here_Variables[6]}\nEnd Date:"), 
    (f"{Heaven_Isnt_Here_Variables[7]}\nRelease Date:"), 
    (f"{Heaven_Isnt_Here_Variables[8]}\n\nAlbum(s):"),
    (f"{Heaven_Isnt_Here_Variables[9]}")))


Dr_Faust = SongMetadata((f"{Dr_Faust_Variables[0]}"),
    (f"{Dr_Faust_Variables[1]}"), 
    (f"{Dr_Faust_Variables[2]}"),
    (f"{Dr_Faust_Variables[3]}"), 
    (f"{Dr_Faust_Variables[4]}"), 
    (f"{Dr_Faust_Variables[5]}"),
    (f"{Dr_Faust_Variables[6]}"), 
    (f"{Dr_Faust_Variables[7]}"), 
    (f"{Dr_Faust_Variables[8]}"),
    (f"{Dr_Faust_Variables[9]}"),
    ((f"{Dr_Faust_Variables[0]}\n"),
    (f"{Dr_Faust_Variables[1]}"), 
    (f"{Dr_Faust_Variables[2]}"),
    (f"{Dr_Faust_Variables[3]}"), 
    (f"{Dr_Faust_Variables[4]}\n\nLyrics: \n"), 
    (f"{Dr_Faust_Variables[5]}\n\nStart Date:"),
    (f"{Dr_Faust_Variables[6]}\nEnd Date:"), 
    (f"{Dr_Faust_Variables[7]}\nRelease Date:"), 
    (f"{Dr_Faust_Variables[8]}\n\nAlbum(s):"),
    (f"{Dr_Faust_Variables[9]}")))

Mind_Harvest = SongMetadata((f"{Mind_Harvest_Variables[0]}"),
    (f"{Mind_Harvest_Variables[1]}"), 
    (f"{Mind_Harvest_Variables[2]}"),
    (f"{Mind_Harvest_Variables[3]}"), 
    (f"{Mind_Harvest_Variables[4]}"), 
    (f"{Mind_Harvest_Variables[5]}"),
    (f"{Mind_Harvest_Variables[6]}"), 
    (f"{Mind_Harvest_Variables[7]}"), 
    (f"{Mind_Harvest_Variables[8]}"),
    (f"{Mind_Harvest_Variables[9]}"),
    ((f"{Mind_Harvest_Variables[0]}\n"),
    (f"{Mind_Harvest_Variables[1]}"), 
    (f"{Mind_Harvest_Variables[2]}"),
    (f"{Mind_Harvest_Variables[3]}"), 
    (f"{Mind_Harvest_Variables[4]}\n\nLyrics: \n"), 
    (f"{Mind_Harvest_Variables[5]}\n\nStart Date:"),
    (f"{Mind_Harvest_Variables[6]}\nEnd Date:"), 
    (f"{Mind_Harvest_Variables[7]}\nRelease Date:"), 
    (f"{Mind_Harvest_Variables[8]}\n\nAlbum(s):"),
    (f"{Mind_Harvest_Variables[9]}")))

Open_Source_Nervous_System_Demo = SongMetadata((f"{Open_Source_Nervous_System_Demo_Variables[0]}"),
    (f"{Open_Source_Nervous_System_Demo_Variables[1]}"), 
    (f"{Open_Source_Nervous_System_Demo_Variables[2]}"),
    (f"{Open_Source_Nervous_System_Demo_Variables[3]}"), 
    (f"{Open_Source_Nervous_System_Demo_Variables[4]}"), 
    (f"{Open_Source_Nervous_System_Demo_Variables[5]}"),
    (f"{Open_Source_Nervous_System_Demo_Variables[6]}"), 
    (f"{Open_Source_Nervous_System_Demo_Variables[7]}"), 
    (f"{Open_Source_Nervous_System_Demo_Variables[8]}"),
    (f"{Open_Source_Nervous_System_Demo_Variables[9]}"),
    ((f"{Open_Source_Nervous_System_Demo_Variables[0]}\n"),
    (f"{Open_Source_Nervous_System_Demo_Variables[1]}"), 
    (f"{Open_Source_Nervous_System_Demo_Variables[2]}"),
    (f"{Open_Source_Nervous_System_Demo_Variables[3]}"), 
    (f"{Open_Source_Nervous_System_Demo_Variables[4]}\n\nLyrics: \n"), 
    (f"{Open_Source_Nervous_System_Demo_Variables[5]}\n\nStart Date:"),
    (f"{Open_Source_Nervous_System_Demo_Variables[6]}\nEnd Date:"), 
    (f"{Open_Source_Nervous_System_Demo_Variables[7]}\nRelease Date:"), 
    (f"{Open_Source_Nervous_System_Demo_Variables[8]}\n\nAlbum(s):"),
    (f"{Open_Source_Nervous_System_Demo_Variables[9]}")))


Last_October = SongMetadata((f"{Last_October_Variables[0]}"),
    (f"{Last_October_Variables[1]}"), 
    (f"{Last_October_Variables[2]}"),
    (f"{Last_October_Variables[3]}"), 
    (f"{Last_October_Variables[4]}"), 
    (f"{Last_October_Variables[5]}"),
    (f"{Last_October_Variables[6]}"), 
    (f"{Last_October_Variables[7]}"), 
    (f"{Last_October_Variables[8]}"),
    (f"{Last_October_Variables[9]}"),
    ((f"{Last_October_Variables[0]}\n"),
    (f"{Last_October_Variables[1]}"), 
    (f"{Last_October_Variables[2]}"),
    (f"{Last_October_Variables[3]}"), 
    (f"{Last_October_Variables[4]}\n\nLyrics: \n"), 
    (f"{Last_October_Variables[5]}\n\nStart Date:"),
    (f"{Last_October_Variables[6]}\nEnd Date:"), 
    (f"{Last_October_Variables[7]}\nRelease Date:"), 
    (f"{Last_October_Variables[8]}\n\nAlbum(s):"),
    (f"{Last_October_Variables[9]}")))


Heer_Public_Archive_1943 = SongMetadata((f"{Heer_Public_Archive_1943_Variables[0]}"),
    (f"{Heer_Public_Archive_1943_Variables[1]}"), 
    (f"{Heer_Public_Archive_1943_Variables[2]}"),
    (f"{Heer_Public_Archive_1943_Variables[3]}"), 
    (f"{Heer_Public_Archive_1943_Variables[4]}"), 
    (f"{Heer_Public_Archive_1943_Variables[5]}"),
    (f"{Heer_Public_Archive_1943_Variables[6]}"), 
    (f"{Heer_Public_Archive_1943_Variables[7]}"), 
    (f"{Heer_Public_Archive_1943_Variables[8]}"),
    (f"{Heer_Public_Archive_1943_Variables[9]}"),
    ((f"{Heer_Public_Archive_1943_Variables[0]}\n"),
    (f"{Heer_Public_Archive_1943_Variables[1]}"), 
    (f"{Heer_Public_Archive_1943_Variables[2]}"),
    (f"{Heer_Public_Archive_1943_Variables[3]}"), 
    (f"{Heer_Public_Archive_1943_Variables[4]}\n\nLyrics: \n"), 
    (f"{Heer_Public_Archive_1943_Variables[5]}\n\nStart Date:"),
    (f"{Heer_Public_Archive_1943_Variables[6]}\nEnd Date:"), 
    (f"{Heer_Public_Archive_1943_Variables[7]}\nRelease Date:"), 
    (f"{Heer_Public_Archive_1943_Variables[8]}\n\nAlbum(s):"),
    (f"{Heer_Public_Archive_1943_Variables[9]}")))


Embryo = SongMetadata((f"{Embryo_Variables[0]}"),
    (f"{Embryo_Variables[1]}"), 
    (f"{Embryo_Variables[2]}"),
    (f"{Embryo_Variables[3]}"), 
    (f"{Embryo_Variables[4]}"), 
    (f"{Embryo_Variables[5]}"),
    (f"{Embryo_Variables[6]}"), 
    (f"{Embryo_Variables[7]}"), 
    (f"{Embryo_Variables[8]}"),
    (f"{Embryo_Variables[9]}"),
    ((f"{Embryo_Variables[0]}\n"),
    (f"{Embryo_Variables[1]}"), 
    (f"{Embryo_Variables[2]}"),
    (f"{Embryo_Variables[3]}"), 
    (f"{Embryo_Variables[4]}\n\nLyrics: \n"), 
    (f"{Embryo_Variables[5]}\n\nStart Date:"),
    (f"{Embryo_Variables[6]}\nEnd Date:"), 
    (f"{Embryo_Variables[7]}\nRelease Date:"), 
    (f"{Embryo_Variables[8]}\n\nAlbum(s):"),
    (f"{Embryo_Variables[9]}")))


Putting_On_The_Ritz_Radio_Edit = SongMetadata((f"{Putting_On_The_Ritz_Radio_Edit_Variables[0]}"),
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[1]}"), 
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[2]}"),
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[3]}"), 
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[4]}"), 
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[5]}"),
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[6]}"), 
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[7]}"), 
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[8]}"),
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[9]}"),
    ((f"{Putting_On_The_Ritz_Radio_Edit_Variables[0]}\n"),
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[1]}"), 
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[2]}"),
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[3]}"), 
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[4]}\n\nLyrics: \n"), 
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[5]}\n\nStart Date:"),
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[6]}\nEnd Date:"), 
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[7]}\nRelease Date:"), 
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[8]}\n\nAlbum(s):"),
    (f"{Putting_On_The_Ritz_Radio_Edit_Variables[9]}")))


Latrodectus = SongMetadata((f"{Latrodectus_Variables[0]}"),
    (f"{Latrodectus_Variables[1]}"), 
    (f"{Latrodectus_Variables[2]}"),
    (f"{Latrodectus_Variables[3]}"), 
    (f"{Latrodectus_Variables[4]}"), 
    (f"{Latrodectus_Variables[5]}"),
    (f"{Latrodectus_Variables[6]}"), 
    (f"{Latrodectus_Variables[7]}"), 
    (f"{Latrodectus_Variables[8]}"),
    (f"{Latrodectus_Variables[9]}"),
    ((f"{Latrodectus_Variables[0]}\n"),
    (f"{Latrodectus_Variables[1]}"), 
    (f"{Latrodectus_Variables[2]}"),
    (f"{Latrodectus_Variables[3]}"), 
    (f"{Latrodectus_Variables[4]}\n\nLyrics: \n"), 
    (f"{Latrodectus_Variables[5]}\n\nStart Date:"),
    (f"{Latrodectus_Variables[6]}\nEnd Date:"), 
    (f"{Latrodectus_Variables[7]}\nRelease Date:"), 
    (f"{Latrodectus_Variables[8]}\n\nAlbum(s):"),
    (f"{Latrodectus_Variables[9]}")))

Stella_Splendens = SongMetadata((f"{Stella_Splendens_Variables[0]}"),
    (f"{Stella_Splendens_Variables[1]}"), 
    (f"{Stella_Splendens_Variables[2]}"),
    (f"{Stella_Splendens_Variables[3]}"), 
    (f"{Stella_Splendens_Variables[4]}"), 
    (f"{Stella_Splendens_Variables[5]}"),
    (f"{Stella_Splendens_Variables[6]}"), 
    (f"{Stella_Splendens_Variables[7]}"), 
    (f"{Stella_Splendens_Variables[8]}"),
    (f"{Stella_Splendens_Variables[9]}"),
    ((f"{Stella_Splendens_Variables[0]}\n"),
    (f"{Stella_Splendens_Variables[1]}"), 
    (f"{Stella_Splendens_Variables[2]}"),
    (f"{Stella_Splendens_Variables[3]}"), 
    (f"{Stella_Splendens_Variables[4]}\n\nLyrics: \n"), 
    (f"{Stella_Splendens_Variables[5]}\n\nStart Date:"),
    (f"{Stella_Splendens_Variables[6]}\nEnd Date:"), 
    (f"{Stella_Splendens_Variables[7]}\nRelease Date:"), 
    (f"{Stella_Splendens_Variables[8]}\n\nAlbum(s):"),
    (f"{Stella_Splendens_Variables[9]}")))


Maslows_Du_Vide = SongMetadata((f"{Maslows_Du_Vide_Variables[0]}"),
    (f"{Maslows_Du_Vide_Variables[1]}"), 
    (f"{Maslows_Du_Vide_Variables[2]}"),
    (f"{Maslows_Du_Vide_Variables[3]}"), 
    (f"{Maslows_Du_Vide_Variables[4]}"), 
    (f"{Maslows_Du_Vide_Variables[5]}"),
    (f"{Maslows_Du_Vide_Variables[6]}"), 
    (f"{Maslows_Du_Vide_Variables[7]}"), 
    (f"{Maslows_Du_Vide_Variables[8]}"),
    (f"{Maslows_Du_Vide_Variables[9]}"),
    ((f"{Maslows_Du_Vide_Variables[0]}\n"),
    (f"{Maslows_Du_Vide_Variables[1]}"), 
    (f"{Maslows_Du_Vide_Variables[2]}"),
    (f"{Maslows_Du_Vide_Variables[3]}"), 
    (f"{Maslows_Du_Vide_Variables[4]}\n\nLyrics: \n"), 
    (f"{Maslows_Du_Vide_Variables[5]}\n\nStart Date:"),
    (f"{Maslows_Du_Vide_Variables[6]}\nEnd Date:"), 
    (f"{Maslows_Du_Vide_Variables[7]}\nRelease Date:"), 
    (f"{Maslows_Du_Vide_Variables[8]}\n\nAlbum(s):"),
    (f"{Maslows_Du_Vide_Variables[9]}")))


Strawberry_Gashes = SongMetadata((f"{Strawberry_Gashes_Variables[0]}"),
    (f"{Strawberry_Gashes_Variables[1]}"), 
    (f"{Strawberry_Gashes_Variables[2]}"),
    (f"{Strawberry_Gashes_Variables[3]}"), 
    (f"{Strawberry_Gashes_Variables[4]}"), 
    (f"{Strawberry_Gashes_Variables[5]}"),
    (f"{Strawberry_Gashes_Variables[6]}"), 
    (f"{Strawberry_Gashes_Variables[7]}"), 
    (f"{Strawberry_Gashes_Variables[8]}"),
    (f"{Strawberry_Gashes_Variables[9]}"),
    ((f"{Strawberry_Gashes_Variables[0]}\n"),
    (f"{Strawberry_Gashes_Variables[1]}"), 
    (f"{Strawberry_Gashes_Variables[2]}"),
    (f"{Strawberry_Gashes_Variables[3]}"), 
    (f"{Strawberry_Gashes_Variables[4]}\n\nLyrics: \n"), 
    (f"{Strawberry_Gashes_Variables[5]}\n\nStart Date:"),
    (f"{Strawberry_Gashes_Variables[6]}\nEnd Date:"), 
    (f"{Strawberry_Gashes_Variables[7]}\nRelease Date:"), 
    (f"{Strawberry_Gashes_Variables[8]}\n\nAlbum(s):"),
    (f"{Strawberry_Gashes_Variables[9]}")))

Lorem_Ipsum = SongMetadata((f"{Lorem_Ipsum_Variables[0]}"),
    (f"{Lorem_Ipsum_Variables[1]}"), 
    (f"{Lorem_Ipsum_Variables[2]}"),
    (f"{Lorem_Ipsum_Variables[3]}"), 
    (f"{Lorem_Ipsum_Variables[4]}"), 
    (f"{Lorem_Ipsum_Variables[5]}"),
    (f"{Lorem_Ipsum_Variables[6]}"), 
    (f"{Lorem_Ipsum_Variables[7]}"), 
    (f"{Lorem_Ipsum_Variables[8]}"),
    (f"{Lorem_Ipsum_Variables[9]}"),
    ((f"{Lorem_Ipsum_Variables[0]}\n"),
    (f"{Lorem_Ipsum_Variables[1]}"), 
    (f"{Lorem_Ipsum_Variables[2]}"),
    (f"{Lorem_Ipsum_Variables[3]}"), 
    (f"{Lorem_Ipsum_Variables[4]}\n\nLyrics: \n"), 
    (f"{Lorem_Ipsum_Variables[5]}\n\nStart Date:"),
    (f"{Lorem_Ipsum_Variables[6]}\nEnd Date:"), 
    (f"{Lorem_Ipsum_Variables[7]}\nRelease Date:"), 
    (f"{Lorem_Ipsum_Variables[8]}\n\nAlbum(s):"),
    (f"{Lorem_Ipsum_Variables[9]}")))


By_Proxy = SongMetadata((f"{By_Proxy_Variables[0]}"),
    (f"{By_Proxy_Variables[1]}"), 
    (f"{By_Proxy_Variables[2]}"),
    (f"{By_Proxy_Variables[3]}"), 
    (f"{By_Proxy_Variables[4]}"), 
    (f"{By_Proxy_Variables[5]}"),
    (f"{By_Proxy_Variables[6]}"), 
    (f"{By_Proxy_Variables[7]}"), 
    (f"{By_Proxy_Variables[8]}"),
    (f"{By_Proxy_Variables[9]}"),
    ((f"{By_Proxy_Variables[0]}\n"),
    (f"{By_Proxy_Variables[1]}"), 
    (f"{By_Proxy_Variables[2]}"),
    (f"{By_Proxy_Variables[3]}"), 
    (f"{By_Proxy_Variables[4]}\n\nLyrics: \n"), 
    (f"{By_Proxy_Variables[5]}\n\nStart Date:"),
    (f"{By_Proxy_Variables[6]}\nEnd Date:"), 
    (f"{By_Proxy_Variables[7]}\nRelease Date:"), 
    (f"{By_Proxy_Variables[8]}\n\nAlbum(s):"),
    (f"{By_Proxy_Variables[9]}")))


Lappel_Du_Vide = SongMetadata((f"{Lappel_Du_Vide_Variables[0]}"),
    (f"{Lappel_Du_Vide_Variables[1]}"), 
    (f"{Lappel_Du_Vide_Variables[2]}"),
    (f"{Lappel_Du_Vide_Variables[3]}"), 
    (f"{Lappel_Du_Vide_Variables[4]}"), 
    (f"{Lappel_Du_Vide_Variables[5]}"),
    (f"{Lappel_Du_Vide_Variables[6]}"), 
    (f"{Lappel_Du_Vide_Variables[7]}"), 
    (f"{Lappel_Du_Vide_Variables[8]}"),
    (f"{Lappel_Du_Vide_Variables[9]}"),
    ((f"{Lappel_Du_Vide_Variables[0]}\n"),
    (f"{Lappel_Du_Vide_Variables[1]}"), 
    (f"{Lappel_Du_Vide_Variables[2]}"),
    (f"{Lappel_Du_Vide_Variables[3]}"), 
    (f"{Lappel_Du_Vide_Variables[4]}\n\nLyrics: \n"), 
    (f"{Lappel_Du_Vide_Variables[5]}\n\nStart Date:"),
    (f"{Lappel_Du_Vide_Variables[6]}\nEnd Date:"), 
    (f"{Lappel_Du_Vide_Variables[7]}\nRelease Date:"), 
    (f"{Lappel_Du_Vide_Variables[8]}\n\nAlbum(s):"),
    (f"{Lappel_Du_Vide_Variables[9]}")))


Heer_Public_Archive_1945 = SongMetadata((f"{Heer_Public_Archive_1945_Variables[0]}"),
    (f"{Heer_Public_Archive_1945_Variables[1]}"), 
    (f"{Heer_Public_Archive_1945_Variables[2]}"),
    (f"{Heer_Public_Archive_1945_Variables[3]}"), 
    (f"{Heer_Public_Archive_1945_Variables[4]}"), 
    (f"{Heer_Public_Archive_1945_Variables[5]}"),
    (f"{Heer_Public_Archive_1945_Variables[6]}"), 
    (f"{Heer_Public_Archive_1945_Variables[7]}"), 
    (f"{Heer_Public_Archive_1945_Variables[8]}"),
    (f"{Heer_Public_Archive_1945_Variables[9]}"),
    ((f"{Heer_Public_Archive_1945_Variables[0]}\n"),
    (f"{Heer_Public_Archive_1945_Variables[1]}"), 
    (f"{Heer_Public_Archive_1945_Variables[2]}"),
    (f"{Heer_Public_Archive_1945_Variables[3]}"), 
    (f"{Heer_Public_Archive_1945_Variables[4]}\n\nLyrics: \n"), 
    (f"{Heer_Public_Archive_1945_Variables[5]}\n\nStart Date:"),
    (f"{Heer_Public_Archive_1945_Variables[6]}\nEnd Date:"), 
    (f"{Heer_Public_Archive_1945_Variables[7]}\nRelease Date:"), 
    (f"{Heer_Public_Archive_1945_Variables[8]}\n\nAlbum(s):"),
    (f"{Heer_Public_Archive_1945_Variables[9]}")))


Strawberry_Gashes_Single = SongMetadata((f"{Strawberry_Gashes_Single_Variables[0]}"),
    (f"{Strawberry_Gashes_Single_Variables[1]}"), 
    (f"{Strawberry_Gashes_Single_Variables[2]}"),
    (f"{Strawberry_Gashes_Single_Variables[3]}"), 
    (f"{Strawberry_Gashes_Single_Variables[4]}"), 
    (f"{Strawberry_Gashes_Single_Variables[5]}"),
    (f"{Strawberry_Gashes_Single_Variables[6]}"), 
    (f"{Strawberry_Gashes_Single_Variables[7]}"), 
    (f"{Strawberry_Gashes_Single_Variables[8]}"),
    (f"{Strawberry_Gashes_Single_Variables[9]}"),
    ((f"{Strawberry_Gashes_Single_Variables[0]}\n"),
    (f"{Strawberry_Gashes_Single_Variables[1]}"), 
    (f"{Strawberry_Gashes_Single_Variables[2]}"),
    (f"{Strawberry_Gashes_Single_Variables[3]}"), 
    (f"{Strawberry_Gashes_Single_Variables[4]}\n\nLyrics: \n"), 
    (f"{Strawberry_Gashes_Single_Variables[5]}\n\nStart Date:"),
    (f"{Strawberry_Gashes_Single_Variables[6]}\nEnd Date:"), 
    (f"{Strawberry_Gashes_Single_Variables[7]}\nRelease Date:"), 
    (f"{Strawberry_Gashes_Single_Variables[8]}\n\nAlbum(s):"),
    (f"{Strawberry_Gashes_Single_Variables[9]}")))

Miss_Nothing = SongMetadata((f"{Miss_Nothing_Variables[0]}"),
    (f"{Miss_Nothing_Variables[1]}"), 
    (f"{Miss_Nothing_Variables[2]}"),
    (f"{Miss_Nothing_Variables[3]}"), 
    (f"{Miss_Nothing_Variables[4]}"), 
    (f"{Miss_Nothing_Variables[5]}"),
    (f"{Miss_Nothing_Variables[6]}"), 
    (f"{Miss_Nothing_Variables[7]}"), 
    (f"{Miss_Nothing_Variables[8]}"),
    (f"{Miss_Nothing_Variables[9]}"),
    ((f"{Miss_Nothing_Variables[0]}\n"),
    (f"{Miss_Nothing_Variables[1]}"), 
    (f"{Miss_Nothing_Variables[2]}"),
    (f"{Miss_Nothing_Variables[3]}"), 
    (f"{Miss_Nothing_Variables[4]}\n\nLyrics: \n"), 
    (f"{Miss_Nothing_Variables[5]}\n\nStart Date:"),
    (f"{Miss_Nothing_Variables[6]}\nEnd Date:"), 
    (f"{Miss_Nothing_Variables[7]}\nRelease Date:"), 
    (f"{Miss_Nothing_Variables[8]}\n\nAlbum(s):"),
    (f"{Miss_Nothing_Variables[9]}")))


Heer_Public_Archive_1944 = SongMetadata((f"{Heer_Public_Archive_1944_Variables[0]}"),
    (f"{Heer_Public_Archive_1944_Variables[1]}"), 
    (f"{Heer_Public_Archive_1944_Variables[2]}"),
    (f"{Heer_Public_Archive_1944_Variables[3]}"), 
    (f"{Heer_Public_Archive_1944_Variables[4]}"), 
    (f"{Heer_Public_Archive_1944_Variables[5]}"),
    (f"{Heer_Public_Archive_1944_Variables[6]}"), 
    (f"{Heer_Public_Archive_1944_Variables[7]}"), 
    (f"{Heer_Public_Archive_1944_Variables[8]}"),
    (f"{Heer_Public_Archive_1944_Variables[9]}"),
    ((f"{Heer_Public_Archive_1944_Variables[0]}\n"),
    (f"{Heer_Public_Archive_1944_Variables[1]}"), 
    (f"{Heer_Public_Archive_1944_Variables[2]}"),
    (f"{Heer_Public_Archive_1944_Variables[3]}"), 
    (f"{Heer_Public_Archive_1944_Variables[4]}\n\nLyrics: \n"), 
    (f"{Heer_Public_Archive_1944_Variables[5]}\n\nStart Date:"),
    (f"{Heer_Public_Archive_1944_Variables[6]}\nEnd Date:"), 
    (f"{Heer_Public_Archive_1944_Variables[7]}\nRelease Date:"), 
    (f"{Heer_Public_Archive_1944_Variables[8]}\n\nAlbum(s):"),
    (f"{Heer_Public_Archive_1944_Variables[9]}")))


God_Of_The_Gaps = SongMetadata((f"{God_Of_The_Gaps_Variables[0]}"),
    (f"{God_Of_The_Gaps_Variables[1]}"), 
    (f"{God_Of_The_Gaps_Variables[2]}"),
    (f"{God_Of_The_Gaps_Variables[3]}"), 
    (f"{God_Of_The_Gaps_Variables[4]}"), 
    (f"{God_Of_The_Gaps_Variables[5]}"),
    (f"{God_Of_The_Gaps_Variables[6]}"), 
    (f"{God_Of_The_Gaps_Variables[7]}"), 
    (f"{God_Of_The_Gaps_Variables[8]}"),
    (f"{God_Of_The_Gaps_Variables[9]}"),
    ((f"{God_Of_The_Gaps_Variables[0]}\n"),
    (f"{God_Of_The_Gaps_Variables[1]}"), 
    (f"{God_Of_The_Gaps_Variables[2]}"),
    (f"{God_Of_The_Gaps_Variables[3]}"), 
    (f"{God_Of_The_Gaps_Variables[4]}\n\nLyrics: \n"), 
    (f"{God_Of_The_Gaps_Variables[5]}\n\nStart Date:"),
    (f"{God_Of_The_Gaps_Variables[6]}\nEnd Date:"), 
    (f"{God_Of_The_Gaps_Variables[7]}\nRelease Date:"), 
    (f"{God_Of_The_Gaps_Variables[8]}\n\nAlbum(s):"),
    (f"{God_Of_The_Gaps_Variables[9]}")))


Last_Of_October = SongMetadata((f"{Last_Of_October_Variables[0]}"),
    (f"{Last_Of_October_Variables[1]}"), 
    (f"{Last_Of_October_Variables[2]}"),
    (f"{Last_Of_October_Variables[3]}"), 
    (f"{Last_Of_October_Variables[4]}"), 
    (f"{Last_Of_October_Variables[5]}"),
    (f"{Last_Of_October_Variables[6]}"), 
    (f"{Last_Of_October_Variables[7]}"), 
    (f"{Last_Of_October_Variables[8]}"),
    (f"{Last_Of_October_Variables[9]}"),
    ((f"{Last_Of_October_Variables[0]}\n"),
    (f"{Last_Of_October_Variables[1]}"), 
    (f"{Last_Of_October_Variables[2]}"),
    (f"{Last_Of_October_Variables[3]}"), 
    (f"{Last_Of_October_Variables[4]}\n\nLyrics: \n"), 
    (f"{Last_Of_October_Variables[5]}\n\nStart Date:"),
    (f"{Last_Of_October_Variables[6]}\nEnd Date:"), 
    (f"{Last_Of_October_Variables[7]}\nRelease Date:"), 
    (f"{Last_Of_October_Variables[8]}\n\nAlbum(s):"),
    (f"{Last_Of_October_Variables[9]}")))


De_Finibus_Bonorum_Et_Malorum = SongMetadata((f"{De_Finibus_Bonorum_Et_Malorum_Variables[0]}"),
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[1]}"), 
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[2]}"),
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[3]}"), 
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[4]}"), 
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[5]}"),
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[6]}"), 
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[7]}"), 
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[8]}"),
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[9]}"),
    ((f"{De_Finibus_Bonorum_Et_Malorum_Variables[0]}\n"),
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[1]}"), 
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[2]}"),
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[3]}"), 
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[4]}\n\nLyrics: \n"), 
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[5]}\n\nStart Date:"),
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[6]}\nEnd Date:"), 
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[7]}\nRelease Date:"), 
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[8]}\n\nAlbum(s):"),
    (f"{De_Finibus_Bonorum_Et_Malorum_Variables[9]}")))


Sleepwalking_In_Los_Angeles = SongMetadata((f"{Sleepwalking_In_Los_Angeles_Variables[0]}"),
    (f"{Sleepwalking_In_Los_Angeles_Variables[1]}"), 
    (f"{Sleepwalking_In_Los_Angeles_Variables[2]}"),
    (f"{Sleepwalking_In_Los_Angeles_Variables[3]}"), 
    (f"{Sleepwalking_In_Los_Angeles_Variables[4]}"), 
    (f"{Sleepwalking_In_Los_Angeles_Variables[5]}"),
    (f"{Sleepwalking_In_Los_Angeles_Variables[6]}"), 
    (f"{Sleepwalking_In_Los_Angeles_Variables[7]}"), 
    (f"{Sleepwalking_In_Los_Angeles_Variables[8]}"),
    (f"{Sleepwalking_In_Los_Angeles_Variables[9]}"),
    ((f"{Sleepwalking_In_Los_Angeles_Variables[0]}\n"),
    (f"{Sleepwalking_In_Los_Angeles_Variables[1]}"), 
    (f"{Sleepwalking_In_Los_Angeles_Variables[2]}"),
    (f"{Sleepwalking_In_Los_Angeles_Variables[3]}"), 
    (f"{Sleepwalking_In_Los_Angeles_Variables[4]}\n\nLyrics: \n"), 
    (f"{Sleepwalking_In_Los_Angeles_Variables[5]}\n\nStart Date:"),
    (f"{Sleepwalking_In_Los_Angeles_Variables[6]}\nEnd Date:"), 
    (f"{Sleepwalking_In_Los_Angeles_Variables[7]}\nRelease Date:"), 
    (f"{Sleepwalking_In_Los_Angeles_Variables[8]}\n\nAlbum(s):"),
    (f"{Sleepwalking_In_Los_Angeles_Variables[9]}")))





The_Call_Of_The_Void = SongMetadata((f"{The_Call_Of_The_Void_Variables[0]}"),
    (f"{The_Call_Of_The_Void_Variables[1]}"), 
    (f"{The_Call_Of_The_Void_Variables[2]}"),
    (f"{The_Call_Of_The_Void_Variables[3]}"), 
    (f"{The_Call_Of_The_Void_Variables[4]}"), 
    (f"{The_Call_Of_The_Void_Variables[5]}"),
    (f"{The_Call_Of_The_Void_Variables[6]}"), 
    (f"{The_Call_Of_The_Void_Variables[7]}"), 
    (f"{The_Call_Of_The_Void_Variables[8]}"),
    (f"{The_Call_Of_The_Void_Variables[9]}"),
    ((f"{The_Call_Of_The_Void_Variables[0]}\n"),
    (f"{The_Call_Of_The_Void_Variables[1]}"), 
    (f"{The_Call_Of_The_Void_Variables[2]}"),
    (f"{The_Call_Of_The_Void_Variables[3]}"), 
    (f"{The_Call_Of_The_Void_Variables[4]}\n\nLyrics: \n"), 
    (f"{The_Call_Of_The_Void_Variables[5]}\n\nStart Date:"),
    (f"{The_Call_Of_The_Void_Variables[6]}\nEnd Date:"), 
    (f"{The_Call_Of_The_Void_Variables[7]}\nRelease Date:"), 
    (f"{The_Call_Of_The_Void_Variables[8]}\n\nAlbum(s):"),
    (f"{The_Call_Of_The_Void_Variables[9]}")))


Lacrimosa = SongMetadata((f"{Lacrimosa_Variables[0]}"),
    (f"{Lacrimosa_Variables[1]}"), 
    (f"{Lacrimosa_Variables[2]}"),
    (f"{Lacrimosa_Variables[3]}"), 
    (f"{Lacrimosa_Variables[4]}"), 
    (f"{Lacrimosa_Variables[5]}"),
    (f"{Lacrimosa_Variables[6]}"), 
    (f"{Lacrimosa_Variables[7]}"), 
    (f"{Lacrimosa_Variables[8]}"),
    (f"{Lacrimosa_Variables[9]}"),
    ((f"{Lacrimosa_Variables[0]}\n"),
    (f"{Lacrimosa_Variables[1]}"), 
    (f"{Lacrimosa_Variables[2]}"),
    (f"{Lacrimosa_Variables[3]}"), 
    (f"{Lacrimosa_Variables[4]}\n\nLyrics: \n"), 
    (f"{Lacrimosa_Variables[5]}\n\nStart Date:"),
    (f"{Lacrimosa_Variables[6]}\nEnd Date:"), 
    (f"{Lacrimosa_Variables[7]}\nRelease Date:"), 
    (f"{Lacrimosa_Variables[8]}\n\nAlbum(s):"),
    (f"{Lacrimosa_Variables[9]}")))

#####
#All#
#####

def All_Titles():
    return f'''{Incunabula.title}
{Forest_Is_Trees.title}
{Living_In_A_Halo.title}
{Stepdown.title}
{Putting_On_The_Ritz.title}
{Putting_On_The_Ritz_Single.title}
{Incunabula_Revised.title}
{Nervosa.title}
{Beyond_The_Trees.title}
{Open_Source_Nervous_System.title}
{Amphetamine.title}
{Positivity_For_The_Masochist.title}
{Nervous_System.title}
{With_No_Eyes.title}
{Lenvoi.title}
{Retina.title}
{Incunabula_Remastered.title}
{Words.title}
{Beyond_The_Trees_Remastered.title}
{Stepdown_Prologue.title}
{Stepdown_Alternate.title}
{Nervosa_II.title}
{What_Saturn_Lies_In_Death.title}
{Putting_On_The_Ritz_Remastered.title}
{Deluge.title}
{Heaven_Isnt_Here.title}
{Dr_Faust.title}
{Mind_Harvest.title}
{Open_Source_Nervous_System_Demo.title}
{Last_October.title}
{Heer_Public_Archive_1943.title}
{Embryo.title}
{Putting_On_The_Ritz_Radio_Edit.title}
{Latrodectus.title}
{Stella_Splendens.title}
{Maslows_Du_Vide.title}
{Strawberry_Gashes.title}
{Lorem_Ipsum.title}
{By_Proxy.title}
{Lappel_Du_Vide.title}
{Heer_Public_Archive_1945.title}
{Strawberry_Gashes_Single.title}
{Miss_Nothing.title}
{Heer_Public_Archive_1944.title}
{God_Of_The_Gaps.title}
{Last_Of_October.title}
{De_Finibus_Bonorum_Et_Malorum.title}
{Sleepwalking_In_Los_Angeles.title}
{The_Call_Of_The_Void.title}
{Lacrimosa.title}'''

def All_Lengths():
    return f'''{Incunabula.title}
{Incunabula.length}

{Forest_Is_Trees.title}
{Forest_Is_Trees.length}

{Living_In_A_Halo.title}
{Living_In_A_Halo.length}

{Stepdown.title}
{Stepdown.length}

{Putting_On_The_Ritz.title}
{Putting_On_The_Ritz.length}

{Putting_On_The_Ritz_Single.title}
{Putting_On_The_Ritz_Single.length}

{Incunabula_Revised.title}
{Incunabula_Revised.length}

{Nervosa.title}
{Nervosa.length}

{Beyond_The_Trees.title}
{Beyond_The_Trees.length}

{Open_Source_Nervous_System.title}
{Open_Source_Nervous_System.length}

{Amphetamine.title}
{Amphetamine.length}

{Positivity_For_The_Masochist.title}
{Positivity_For_The_Masochist.length}

{Nervous_System.title}
{Nervous_System.length}

{With_No_Eyes.title}
{With_No_Eyes.length}

{Lenvoi.title}
{Lenvoi.length}

{Retina.title}
{Retina.length}

{Incunabula_Remastered.title}
{Incunabula_Remastered.length}

{Words.title}
{Words.length}

{Beyond_The_Trees_Remastered.title}
{Beyond_The_Trees_Remastered.length}

{Stepdown_Prologue.title}
{Stepdown_Prologue.length}

{Stepdown_Alternate.title}
{Stepdown_Alternate.length}

{Nervosa_II.title}
{Nervosa_II.length}

{What_Saturn_Lies_In_Death.title}
{What_Saturn_Lies_In_Death.length}

{Putting_On_The_Ritz_Remastered.title}
{Putting_On_The_Ritz_Remastered.length}

{Deluge.title}
{Deluge.length}

{Heaven_Isnt_Here.title}
{Heaven_Isnt_Here.length}

{Dr_Faust.title}
{Dr_Faust.length}

{Mind_Harvest.title}
{Mind_Harvest.length}

{Open_Source_Nervous_System_Demo.title}
{Open_Source_Nervous_System_Demo.length}

{Last_October.title}
{Last_October.length}

{Heer_Public_Archive_1943.title}
{Heer_Public_Archive_1943.length}

{Embryo.title}
{Embryo.length}

{Putting_On_The_Ritz_Radio_Edit.title}
{Putting_On_The_Ritz_Radio_Edit.length}

{Latrodectus.title}
{Latrodectus.length}

{Stella_Splendens.title}
{Stella_Splendens.length}

{Maslows_Du_Vide.title}
{Maslows_Du_Vide.length}

{Strawberry_Gashes.title}
{Strawberry_Gashes.length}

{Lorem_Ipsum.title}
{Lorem_Ipsum.length}

{By_Proxy.title}
{By_Proxy.length}

{Lappel_Du_Vide.title}
{Lappel_Du_Vide.length}

{Heer_Public_Archive_1945.title}
{Heer_Public_Archive_1945.length}

{Strawberry_Gashes_Single.title}
{Strawberry_Gashes_Single.length}

{Miss_Nothing.title}
{Miss_Nothing.length}

{Heer_Public_Archive_1944.title}
{Heer_Public_Archive_1944.length}

{God_Of_The_Gaps.title}
{God_Of_The_Gaps.length}

{Last_Of_October.title}
{Last_Of_October.length}

{De_Finibus_Bonorum_Et_Malorum.title}
{De_Finibus_Bonorum_Et_Malorum.length}

{Sleepwalking_In_Los_Angeles.title}
{Sleepwalking_In_Los_Angeles.length}

{The_Call_Of_The_Void.title}
{The_Call_Of_The_Void.length}

{Lacrimosa.title}
{Lacrimosa.length}'''


def All_Scales():
    return f'''{Incunabula.title}
{Incunabula.scale}

{Forest_Is_Trees.title}
{Forest_Is_Trees.scale}

{Living_In_A_Halo.title}
{Living_In_A_Halo.scale}

{Stepdown.title}
{Stepdown.scale}

{Putting_On_The_Ritz.title}
{Putting_On_The_Ritz.scale}

{Putting_On_The_Ritz_Single.title}
{Putting_On_The_Ritz_Single.scale}

{Incunabula_Revised.title}
{Incunabula_Revised.scale}

{Nervosa.title}
{Nervosa.scale}

{Beyond_The_Trees.title}
{Beyond_The_Trees.scale}

{Open_Source_Nervous_System.title}
{Open_Source_Nervous_System.scale}

{Amphetamine.title}
{Amphetamine.scale}

{Positivity_For_The_Masochist.title}
{Positivity_For_The_Masochist.scale}

{Nervous_System.title}
{Nervous_System.scale}

{With_No_Eyes.title}
{With_No_Eyes.scale}

{Lenvoi.title}
{Lenvoi.scale}

{Retina.title}
{Retina.scale}

{Incunabula_Remastered.title}
{Incunabula_Remastered.scale}

{Words.title}
{Words.scale}

{Beyond_The_Trees_Remastered.title}
{Beyond_The_Trees_Remastered.scale}

{Stepdown_Prologue.title}
{Stepdown_Prologue.scale}

{Stepdown_Alternate.title}
{Stepdown_Alternate.scale}

{Nervosa_II.title}
{Nervosa_II.scale}

{What_Saturn_Lies_In_Death.title}
{What_Saturn_Lies_In_Death.scale}

{Putting_On_The_Ritz_Remastered.title}
{Putting_On_The_Ritz_Remastered.scale}

{Deluge.title}
{Deluge.scale}

{Heaven_Isnt_Here.title}
{Heaven_Isnt_Here.scale}

{Dr_Faust.title}
{Dr_Faust.scale}

{Mind_Harvest.title}
{Mind_Harvest.scale}

{Open_Source_Nervous_System_Demo.title}
{Open_Source_Nervous_System_Demo.scale}

{Last_October.title}
{Last_October.scale}

{Heer_Public_Archive_1943.title}
{Heer_Public_Archive_1943.scale}

{Embryo.title}
{Embryo.scale}

{Putting_On_The_Ritz_Radio_Edit.title}
{Putting_On_The_Ritz_Radio_Edit.scale}

{Latrodectus.title}
{Latrodectus.scale}

{Stella_Splendens.title}
{Stella_Splendens.scale}

{Maslows_Du_Vide.title}
{Maslows_Du_Vide.scale}

{Strawberry_Gashes.title}
{Strawberry_Gashes.scale}

{Lorem_Ipsum.title}
{Lorem_Ipsum.scale}

{By_Proxy.title}
{By_Proxy.scale}

{Lappel_Du_Vide.title}
{Lappel_Du_Vide.scale}

{Heer_Public_Archive_1945.title}
{Heer_Public_Archive_1945.scale}

{Strawberry_Gashes_Single.title}
{Strawberry_Gashes_Single.scale}

{Miss_Nothing.title}
{Miss_Nothing.scale}

{Heer_Public_Archive_1944.title}
{Heer_Public_Archive_1944.scale}

{God_Of_The_Gaps.title}
{God_Of_The_Gaps.scale}

{Last_Of_October.title}
{Last_Of_October.scale}

{De_Finibus_Bonorum_Et_Malorum.title}
{De_Finibus_Bonorum_Et_Malorum.scale}

{Sleepwalking_In_Los_Angeles.title}
{Sleepwalking_In_Los_Angeles.scale}

{The_Call_Of_The_Void.title}
{The_Call_Of_The_Void.scale}

{Lacrimosa.title}
{Lacrimosa.scale}'''

def All_BPMs():
    return f'''{Incunabula.title}
{Incunabula.bpm}

{Forest_Is_Trees.title}
{Forest_Is_Trees.bpm}

{Living_In_A_Halo.title}
{Living_In_A_Halo.bpm}

{Stepdown.title}
{Stepdown.bpm}

{Putting_On_The_Ritz.title}
{Putting_On_The_Ritz.bpm}

{Putting_On_The_Ritz_Single.title}
{Putting_On_The_Ritz_Single.bpm}

{Incunabula_Revised.title}
{Incunabula_Revised.bpm}

{Nervosa.title}
{Nervosa.bpm}

{Beyond_The_Trees.title}
{Beyond_The_Trees.bpm}

{Open_Source_Nervous_System.title}
{Open_Source_Nervous_System.bpm}

{Amphetamine.title}
{Amphetamine.bpm}

{Positivity_For_The_Masochist.title}
{Positivity_For_The_Masochist.bpm}

{Nervous_System.title}
{Nervous_System.bpm}

{With_No_Eyes.title}
{With_No_Eyes.bpm}

{Lenvoi.title}
{Lenvoi.bpm}

{Retina.title}
{Retina.bpm}

{Incunabula_Remastered.title}
{Incunabula_Remastered.bpm}

{Words.title}
{Words.bpm}

{Beyond_The_Trees_Remastered.title}
{Beyond_The_Trees_Remastered.bpm}

{Stepdown_Prologue.title}
{Stepdown_Prologue.bpm}

{Stepdown_Alternate.title}
{Stepdown_Alternate.bpm}

{Nervosa_II.title}
{Nervosa_II.bpm}

{What_Saturn_Lies_In_Death.title}
{What_Saturn_Lies_In_Death.bpm}

{Putting_On_The_Ritz_Remastered.title}
{Putting_On_The_Ritz_Remastered.bpm}

{Deluge.title}
{Deluge.bpm}

{Heaven_Isnt_Here.title}
{Heaven_Isnt_Here.bpm}

{Dr_Faust.title}
{Dr_Faust.bpm}

{Mind_Harvest.title}
{Mind_Harvest.bpm}

{Open_Source_Nervous_System_Demo.title}
{Open_Source_Nervous_System_Demo.bpm}

{Last_October.title}
{Last_October.bpm}

{Heer_Public_Archive_1943.title}
{Heer_Public_Archive_1943.bpm}

{Embryo.title}
{Embryo.bpm}

{Putting_On_The_Ritz_Radio_Edit.title}
{Putting_On_The_Ritz_Radio_Edit.bpm}

{Latrodectus.title}
{Latrodectus.bpm}

{Stella_Splendens.title}
{Stella_Splendens.bpm}

{Maslows_Du_Vide.title}
{Maslows_Du_Vide.bpm}

{Strawberry_Gashes.title}
{Strawberry_Gashes.bpm}

{Lorem_Ipsum.title}
{Lorem_Ipsum.bpm}

{By_Proxy.title}
{By_Proxy.bpm}

{Lappel_Du_Vide.title}
{Lappel_Du_Vide.bpm}

{Heer_Public_Archive_1945.title}
{Heer_Public_Archive_1945.bpm}

{Strawberry_Gashes_Single.title}
{Strawberry_Gashes_Single.bpm}

{Miss_Nothing.title}
{Miss_Nothing.bpm}

{Heer_Public_Archive_1944.title}
{Heer_Public_Archive_1944.bpm}

{God_Of_The_Gaps.title}
{God_Of_The_Gaps.bpm}

{Last_Of_October.title}
{Last_Of_October.bpm}

{De_Finibus_Bonorum_Et_Malorum.title}
{De_Finibus_Bonorum_Et_Malorum.bpm}

{Sleepwalking_In_Los_Angeles.title}
{Sleepwalking_In_Los_Angeles.bpm}

{The_Call_Of_The_Void.title}
{The_Call_Of_The_Void.bpm}

{Lacrimosa.title}
{Lacrimosa.bpm}'''

def All_TimeSignatures():
    return f'''{Incunabula.title}
{Incunabula.timesignature}

{Forest_Is_Trees.title}
{Forest_Is_Trees.timesignature}

{Living_In_A_Halo.title}
{Living_In_A_Halo.timesignature}

{Stepdown.title}
{Stepdown.timesignature}

{Putting_On_The_Ritz.title}
{Putting_On_The_Ritz.timesignature}

{Putting_On_The_Ritz_Single.title}
{Putting_On_The_Ritz_Single.timesignature}

{Incunabula_Revised.title}
{Incunabula_Revised.timesignature}

{Nervosa.title}
{Nervosa.timesignature}

{Beyond_The_Trees.title}
{Beyond_The_Trees.timesignature}

{Open_Source_Nervous_System.title}
{Open_Source_Nervous_System.timesignature}

{Amphetamine.title}
{Amphetamine.timesignature}

{Positivity_For_The_Masochist.title}
{Positivity_For_The_Masochist.timesignature}

{Nervous_System.title}
{Nervous_System.timesignature}

{With_No_Eyes.title}
{With_No_Eyes.timesignature}

{Lenvoi.title}
{Lenvoi.timesignature}

{Retina.title}
{Retina.timesignature}

{Incunabula_Remastered.title}
{Incunabula_Remastered.timesignature}

{Words.title}
{Words.timesignature}

{Beyond_The_Trees_Remastered.title}
{Beyond_The_Trees_Remastered.timesignature}

{Stepdown_Prologue.title}
{Stepdown_Prologue.timesignature}

{Stepdown_Alternate.title}
{Stepdown_Alternate.timesignature}

{Nervosa_II.title}
{Nervosa_II.timesignature}

{What_Saturn_Lies_In_Death.title}
{What_Saturn_Lies_In_Death.timesignature}

{Putting_On_The_Ritz_Remastered.title}
{Putting_On_The_Ritz_Remastered.timesignature}

{Deluge.title}
{Deluge.timesignature}

{Heaven_Isnt_Here.title}
{Heaven_Isnt_Here.timesignature}

{Dr_Faust.title}
{Dr_Faust.timesignature}

{Mind_Harvest.title}
{Mind_Harvest.timesignature}

{Open_Source_Nervous_System_Demo.title}
{Open_Source_Nervous_System_Demo.timesignature}

{Last_October.title}
{Last_October.timesignature}

{Heer_Public_Archive_1943.title}
{Heer_Public_Archive_1943.timesignature}

{Embryo.title}
{Embryo.timesignature}

{Putting_On_The_Ritz_Radio_Edit.title}
{Putting_On_The_Ritz_Radio_Edit.timesignature}

{Latrodectus.title}
{Latrodectus.timesignature}

{Stella_Splendens.title}
{Stella_Splendens.timesignature}

{Maslows_Du_Vide.title}
{Maslows_Du_Vide.timesignature}

{Strawberry_Gashes.title}
{Strawberry_Gashes.timesignature}

{Lorem_Ipsum.title}
{Lorem_Ipsum.timesignature}

{By_Proxy.title}
{By_Proxy.timesignature}

{Lappel_Du_Vide.title}
{Lappel_Du_Vide.timesignature}

{Heer_Public_Archive_1945.title}
{Heer_Public_Archive_1945.timesignature}

{Strawberry_Gashes_Single.title}
{Strawberry_Gashes_Single.timesignature}

{Miss_Nothing.title}
{Miss_Nothing.timesignature}

{Heer_Public_Archive_1944.title}
{Heer_Public_Archive_1944.timesignature}

{God_Of_The_Gaps.title}
{God_Of_The_Gaps.timesignature}

{Last_Of_October.title}
{Last_Of_October.timesignature}

{De_Finibus_Bonorum_Et_Malorum.title}
{De_Finibus_Bonorum_Et_Malorum.timesignature}

{Sleepwalking_In_Los_Angeles.title}
{Sleepwalking_In_Los_Angeles.timesignature}

{The_Call_Of_The_Void.title}
{The_Call_Of_The_Void.timesignature}

{Lacrimosa.title}
{Lacrimosa.timesignature}'''

def All_Lyrics():
    return f'''{Incunabula.title}
{Incunabula.lyrics}

{Forest_Is_Trees.title}
{Forest_Is_Trees.lyrics}

{Living_In_A_Halo.title}
{Living_In_A_Halo.lyrics}

{Stepdown.title}
{Stepdown.lyrics}

{Putting_On_The_Ritz.title}
{Putting_On_The_Ritz.lyrics}

{Putting_On_The_Ritz_Single.title}
{Putting_On_The_Ritz_Single.lyrics}

{Incunabula_Revised.title}
{Incunabula_Revised.lyrics}

{Nervosa.title}
{Nervosa.lyrics}

{Beyond_The_Trees.title}
{Beyond_The_Trees.lyrics}

{Open_Source_Nervous_System.title}
{Open_Source_Nervous_System.lyrics}

{Amphetamine.title}
{Amphetamine.lyrics}

{Positivity_For_The_Masochist.title}
{Positivity_For_The_Masochist.lyrics}

{Nervous_System.title}
{Nervous_System.lyrics}

{With_No_Eyes.title}
{With_No_Eyes.lyrics}

{Lenvoi.title}
{Lenvoi.lyrics}

{Retina.title}
{Retina.lyrics}

{Incunabula_Remastered.title}
{Incunabula_Remastered.lyrics}

{Words.title}
{Words.lyrics}

{Beyond_The_Trees_Remastered.title}
{Beyond_The_Trees_Remastered.lyrics}

{Stepdown_Prologue.title}
{Stepdown_Prologue.lyrics}

{Stepdown_Alternate.title}
{Stepdown_Alternate.lyrics}

{Nervosa_II.title}
{Nervosa_II.lyrics}

{What_Saturn_Lies_In_Death.title}
{What_Saturn_Lies_In_Death.lyrics}

{Putting_On_The_Ritz_Remastered.title}
{Putting_On_The_Ritz_Remastered.lyrics}

{Deluge.title}
{Deluge.lyrics}

{Heaven_Isnt_Here.title}
{Heaven_Isnt_Here.lyrics}

{Dr_Faust.title}
{Dr_Faust.lyrics}

{Mind_Harvest.title}
{Mind_Harvest.lyrics}

{Open_Source_Nervous_System_Demo.title}
{Open_Source_Nervous_System_Demo.lyrics}

{Last_October.title}
{Last_October.lyrics}

{Heer_Public_Archive_1943.title}
{Heer_Public_Archive_1943.lyrics}

{Embryo.title}
{Embryo.lyrics}

{Putting_On_The_Ritz_Radio_Edit.title}
{Putting_On_The_Ritz_Radio_Edit.lyrics}

{Latrodectus.title}
{Latrodectus.lyrics}

{Stella_Splendens.title}
{Stella_Splendens.lyrics}

{Maslows_Du_Vide.title}
{Maslows_Du_Vide.lyrics}

{Strawberry_Gashes.title}
{Strawberry_Gashes.lyrics}

{Lorem_Ipsum.title}
{Lorem_Ipsum.lyrics}

{By_Proxy.title}
{By_Proxy.lyrics}

{Lappel_Du_Vide.title}
{Lappel_Du_Vide.lyrics}

{Heer_Public_Archive_1945.title}
{Heer_Public_Archive_1945.lyrics}

{Strawberry_Gashes_Single.title}
{Strawberry_Gashes_Single.lyrics}

{Miss_Nothing.title}
{Miss_Nothing.lyrics}

{Heer_Public_Archive_1944.title}
{Heer_Public_Archive_1944.lyrics}

{God_Of_The_Gaps.title}
{God_Of_The_Gaps.lyrics}

{Last_Of_October.title}
{Last_Of_October.lyrics}

{De_Finibus_Bonorum_Et_Malorum.title}
{De_Finibus_Bonorum_Et_Malorum.lyrics}

{Sleepwalking_In_Los_Angeles.title}
{Sleepwalking_In_Los_Angeles.lyrics}

{The_Call_Of_The_Void.title}
{The_Call_Of_The_Void.lyrics}

{Lacrimosa.title}
{Lacrimosa.lyrics}'''

def All_Start_Dates():
    return f'''{Incunabula.title}
{Incunabula.start}

{Forest_Is_Trees.title}
{Forest_Is_Trees.start}

{Living_In_A_Halo.title}
{Living_In_A_Halo.start}

{Stepdown.title}
{Stepdown.start}

{Putting_On_The_Ritz.title}
{Putting_On_The_Ritz.start}

{Putting_On_The_Ritz_Single.title}
{Putting_On_The_Ritz_Single.start}

{Incunabula_Revised.title}
{Incunabula_Revised.start}

{Nervosa.title}
{Nervosa.start}

{Beyond_The_Trees.title}
{Beyond_The_Trees.start}

{Open_Source_Nervous_System.title}
{Open_Source_Nervous_System.start}

{Amphetamine.title}
{Amphetamine.start}

{Positivity_For_The_Masochist.title}
{Positivity_For_The_Masochist.start}

{Nervous_System.title}
{Nervous_System.start}

{With_No_Eyes.title}
{With_No_Eyes.start}

{Lenvoi.title}
{Lenvoi.start}

{Retina.title}
{Retina.start}

{Incunabula_Remastered.title}
{Incunabula_Remastered.start}

{Words.title}
{Words.start}

{Beyond_The_Trees_Remastered.title}
{Beyond_The_Trees_Remastered.start}

{Stepdown_Prologue.title}
{Stepdown_Prologue.start}

{Stepdown_Alternate.title}
{Stepdown_Alternate.start}

{Nervosa_II.title}
{Nervosa_II.start}

{What_Saturn_Lies_In_Death.title}
{What_Saturn_Lies_In_Death.start}

{Putting_On_The_Ritz_Remastered.title}
{Putting_On_The_Ritz_Remastered.start}

{Deluge.title}
{Deluge.start}

{Heaven_Isnt_Here.title}
{Heaven_Isnt_Here.start}

{Dr_Faust.title}
{Dr_Faust.start}

{Mind_Harvest.title}
{Mind_Harvest.start}

{Open_Source_Nervous_System_Demo.title}
{Open_Source_Nervous_System_Demo.start}

{Last_October.title}
{Last_October.start}

{Heer_Public_Archive_1943.title}
{Heer_Public_Archive_1943.start}

{Embryo.title}
{Embryo.start}

{Putting_On_The_Ritz_Radio_Edit.title}
{Putting_On_The_Ritz_Radio_Edit.start}

{Latrodectus.title}
{Latrodectus.start}

{Stella_Splendens.title}
{Stella_Splendens.start}

{Maslows_Du_Vide.title}
{Maslows_Du_Vide.start}

{Strawberry_Gashes.title}
{Strawberry_Gashes.start}

{Lorem_Ipsum.title}
{Lorem_Ipsum.start}

{By_Proxy.title}
{By_Proxy.start}

{Lappel_Du_Vide.title}
{Lappel_Du_Vide.start}

{Heer_Public_Archive_1945.title}
{Heer_Public_Archive_1945.start}

{Strawberry_Gashes_Single.title}
{Strawberry_Gashes_Single.start}

{Miss_Nothing.title}
{Miss_Nothing.start}

{Heer_Public_Archive_1944.title}
{Heer_Public_Archive_1944.start}

{God_Of_The_Gaps.title}
{God_Of_The_Gaps.start}

{Last_Of_October.title}
{Last_Of_October.start}

{De_Finibus_Bonorum_Et_Malorum.title}
{De_Finibus_Bonorum_Et_Malorum.start}

{Sleepwalking_In_Los_Angeles.title}
{Sleepwalking_In_Los_Angeles.start}

{The_Call_Of_The_Void.title}
{The_Call_Of_The_Void.start}

{Lacrimosa.title}
{Lacrimosa.start}'''

def All_End_Dates():
    return f'''{Incunabula.title}
{Incunabula.end}

{Forest_Is_Trees.title}
{Forest_Is_Trees.end}

{Living_In_A_Halo.title}
{Living_In_A_Halo.end}

{Stepdown.title}
{Stepdown.end}

{Putting_On_The_Ritz.title}
{Putting_On_The_Ritz.end}

{Putting_On_The_Ritz_Single.title}
{Putting_On_The_Ritz_Single.end}

{Incunabula_Revised.title}
{Incunabula_Revised.end}

{Nervosa.title}
{Nervosa.end}

{Beyond_The_Trees.title}
{Beyond_The_Trees.end}

{Open_Source_Nervous_System.title}
{Open_Source_Nervous_System.end}

{Amphetamine.title}
{Amphetamine.end}

{Positivity_For_The_Masochist.title}
{Positivity_For_The_Masochist.end}

{Nervous_System.title}
{Nervous_System.end}

{With_No_Eyes.title}
{With_No_Eyes.end}

{Lenvoi.title}
{Lenvoi.end}

{Retina.title}
{Retina.end}

{Incunabula_Remastered.title}
{Incunabula_Remastered.end}

{Words.title}
{Words.end}

{Beyond_The_Trees_Remastered.title}
{Beyond_The_Trees_Remastered.end}

{Stepdown_Prologue.title}
{Stepdown_Prologue.end}

{Stepdown_Alternate.title}
{Stepdown_Alternate.end}

{Nervosa_II.title}
{Nervosa_II.end}

{What_Saturn_Lies_In_Death.title}
{What_Saturn_Lies_In_Death.end}

{Putting_On_The_Ritz_Remastered.title}
{Putting_On_The_Ritz_Remastered.end}

{Deluge.title}
{Deluge.end}

{Heaven_Isnt_Here.title}
{Heaven_Isnt_Here.end}

{Dr_Faust.title}
{Dr_Faust.end}

{Mind_Harvest.title}
{Mind_Harvest.end}

{Open_Source_Nervous_System_Demo.title}
{Open_Source_Nervous_System_Demo.end}

{Last_October.title}
{Last_October.end}

{Heer_Public_Archive_1943.title}
{Heer_Public_Archive_1943.end}

{Embryo.title}
{Embryo.end}

{Putting_On_The_Ritz_Radio_Edit.title}
{Putting_On_The_Ritz_Radio_Edit.end}

{Latrodectus.title}
{Latrodectus.end}

{Stella_Splendens.title}
{Stella_Splendens.end}

{Maslows_Du_Vide.title}
{Maslows_Du_Vide.end}

{Strawberry_Gashes.title}
{Strawberry_Gashes.end}

{Lorem_Ipsum.title}
{Lorem_Ipsum.end}

{By_Proxy.title}
{By_Proxy.end}

{Lappel_Du_Vide.title}
{Lappel_Du_Vide.end}

{Heer_Public_Archive_1945.title}
{Heer_Public_Archive_1945.end}

{Strawberry_Gashes_Single.title}
{Strawberry_Gashes_Single.end}

{Miss_Nothing.title}
{Miss_Nothing.end}

{Heer_Public_Archive_1944.title}
{Heer_Public_Archive_1944.end}

{God_Of_The_Gaps.title}
{God_Of_The_Gaps.end}

{Last_Of_October.title}
{Last_Of_October.end}

{De_Finibus_Bonorum_Et_Malorum.title}
{De_Finibus_Bonorum_Et_Malorum.end}

{Sleepwalking_In_Los_Angeles.title}
{Sleepwalking_In_Los_Angeles.end}

{The_Call_Of_The_Void.title}
{The_Call_Of_The_Void.end}

{Lacrimosa.title}
{Lacrimosa.end}'''

def All_Release_Dates():
    return f'''{Incunabula.title}
{Incunabula.release}

{Forest_Is_Trees.title}
{Forest_Is_Trees.release}

{Living_In_A_Halo.title}
{Living_In_A_Halo.release}

{Stepdown.title}
{Stepdown.release}

{Putting_On_The_Ritz.title}
{Putting_On_The_Ritz.release}

{Putting_On_The_Ritz_Single.title}
{Putting_On_The_Ritz_Single.release}

{Incunabula_Revised.title}
{Incunabula_Revised.release}

{Nervosa.title}
{Nervosa.release}

{Beyond_The_Trees.title}
{Beyond_The_Trees.release}

{Open_Source_Nervous_System.title}
{Open_Source_Nervous_System.release}

{Amphetamine.title}
{Amphetamine.release}

{Positivity_For_The_Masochist.title}
{Positivity_For_The_Masochist.release}

{Nervous_System.title}
{Nervous_System.release}

{With_No_Eyes.title}
{With_No_Eyes.release}

{Lenvoi.title}
{Lenvoi.release}

{Retina.title}
{Retina.release}

{Incunabula_Remastered.title}
{Incunabula_Remastered.release}

{Words.title}
{Words.release}

{Beyond_The_Trees_Remastered.title}
{Beyond_The_Trees_Remastered.release}

{Stepdown_Prologue.title}
{Stepdown_Prologue.release}

{Stepdown_Alternate.title}
{Stepdown_Alternate.release}

{Nervosa_II.title}
{Nervosa_II.release}

{What_Saturn_Lies_In_Death.title}
{What_Saturn_Lies_In_Death.release}

{Putting_On_The_Ritz_Remastered.title}
{Putting_On_The_Ritz_Remastered.release}

{Deluge.title}
{Deluge.release}

{Heaven_Isnt_Here.title}
{Heaven_Isnt_Here.release}

{Dr_Faust.title}
{Dr_Faust.release}

{Mind_Harvest.title}
{Mind_Harvest.release}

{Open_Source_Nervous_System_Demo.title}
{Open_Source_Nervous_System_Demo.release}

{Last_October.title}
{Last_October.release}

{Heer_Public_Archive_1943.title}
{Heer_Public_Archive_1943.release}

{Embryo.title}
{Embryo.release}

{Putting_On_The_Ritz_Radio_Edit.title}
{Putting_On_The_Ritz_Radio_Edit.release}

{Latrodectus.title}
{Latrodectus.release}

{Stella_Splendens.title}
{Stella_Splendens.release}

{Maslows_Du_Vide.title}
{Maslows_Du_Vide.release}

{Strawberry_Gashes.title}
{Strawberry_Gashes.release}

{Lorem_Ipsum.title}
{Lorem_Ipsum.release}

{By_Proxy.title}
{By_Proxy.release}

{Lappel_Du_Vide.title}
{Lappel_Du_Vide.release}

{Heer_Public_Archive_1945.title}
{Heer_Public_Archive_1945.release}

{Strawberry_Gashes_Single.title}
{Strawberry_Gashes_Single.release}

{Miss_Nothing.title}
{Miss_Nothing.release}

{Heer_Public_Archive_1944.title}
{Heer_Public_Archive_1944.release}

{God_Of_The_Gaps.title}
{God_Of_The_Gaps.release}

{Last_Of_October.title}
{Last_Of_October.release}

{De_Finibus_Bonorum_Et_Malorum.title}
{De_Finibus_Bonorum_Et_Malorum.release}

{Sleepwalking_In_Los_Angeles.title}
{Sleepwalking_In_Los_Angeles.release}

{The_Call_Of_The_Void.title}
{The_Call_Of_The_Void.release}

{Lacrimosa.title}
{Lacrimosa.release}'''

def All_Albums():
    return f'''{Incunabula.title}
{Incunabula.album}

{Forest_Is_Trees.title}
{Forest_Is_Trees.album}

{Living_In_A_Halo.title}
{Living_In_A_Halo.album}

{Stepdown.title}
{Stepdown.album}

{Putting_On_The_Ritz.title}
{Putting_On_The_Ritz.album}

{Putting_On_The_Ritz_Single.title}
{Putting_On_The_Ritz_Single.album}

{Incunabula_Revised.title}
{Incunabula_Revised.album}

{Nervosa.title}
{Nervosa.album}

{Beyond_The_Trees.title}
{Beyond_The_Trees.album}

{Open_Source_Nervous_System.title}
{Open_Source_Nervous_System.album}

{Amphetamine.title}
{Amphetamine.album}

{Positivity_For_The_Masochist.title}
{Positivity_For_The_Masochist.album}

{Nervous_System.title}
{Nervous_System.album}

{With_No_Eyes.title}
{With_No_Eyes.album}

{Lenvoi.title}
{Lenvoi.album}

{Retina.title}
{Retina.album}

{Incunabula_Remastered.title}
{Incunabula_Remastered.album}

{Words.title}
{Words.album}

{Beyond_The_Trees_Remastered.title}
{Beyond_The_Trees_Remastered.album}

{Stepdown_Prologue.title}
{Stepdown_Prologue.album}

{Stepdown_Alternate.title}
{Stepdown_Alternate.album}

{Nervosa_II.title}
{Nervosa_II.album}

{What_Saturn_Lies_In_Death.title}
{What_Saturn_Lies_In_Death.album}

{Putting_On_The_Ritz_Remastered.title}
{Putting_On_The_Ritz_Remastered.album}

{Deluge.title}
{Deluge.album}

{Heaven_Isnt_Here.title}
{Heaven_Isnt_Here.album}

{Dr_Faust.title}
{Dr_Faust.album}

{Mind_Harvest.title}
{Mind_Harvest.album}

{Open_Source_Nervous_System_Demo.title}
{Open_Source_Nervous_System_Demo.album}

{Last_October.title}
{Last_October.album}

{Heer_Public_Archive_1943.title}
{Heer_Public_Archive_1943.album}

{Embryo.title}
{Embryo.album}

{Putting_On_The_Ritz_Radio_Edit.title}
{Putting_On_The_Ritz_Radio_Edit.album}

{Latrodectus.title}
{Latrodectus.album}

{Stella_Splendens.title}
{Stella_Splendens.album}

{Maslows_Du_Vide.title}
{Maslows_Du_Vide.album}

{Strawberry_Gashes.title}
{Strawberry_Gashes.album}

{Lorem_Ipsum.title}
{Lorem_Ipsum.album}

{By_Proxy.title}
{By_Proxy.album}

{Lappel_Du_Vide.title}
{Lappel_Du_Vide.album}

{Heer_Public_Archive_1945.title}
{Heer_Public_Archive_1945.album}

{Strawberry_Gashes_Single.title}
{Strawberry_Gashes_Single.album}

{Miss_Nothing.title}
{Miss_Nothing.album}

{Heer_Public_Archive_1944.title}
{Heer_Public_Archive_1944.album}

{God_Of_The_Gaps.title}
{God_Of_The_Gaps.album}

{Last_Of_October.title}
{Last_Of_October.album}

{De_Finibus_Bonorum_Et_Malorum.title}
{De_Finibus_Bonorum_Et_Malorum.album}

{Sleepwalking_In_Los_Angeles.title}
{Sleepwalking_In_Los_Angeles.album}

{The_Call_Of_The_Void.title}
{The_Call_Of_The_Void.album}

{Lacrimosa.title}
{Lacrimosa.album}'''

def All():
	return ((f"{Incunabula.title}\n"),
(f"{Incunabula.length}"),
(f"{Incunabula.scale}"),
(f"{Incunabula.bpm}"),
(f"{Incunabula.timesignature}\n\nLyrics: \n"),
(f"{Incunabula.lyrics}\n\nStart Date:"),
(f"{Incunabula.start}\nEnd Date:"),
(f"{Incunabula.end}\nRelease Date:"),
(f"{Incunabula.release}\n\nAlbum(s):"),
(f"{Incunabula.album}\n\n"),
(f"{Forest_Is_Trees.title}\n"),
(f"{Forest_Is_Trees.length}"),
(f"{Forest_Is_Trees.scale}"),
(f"{Forest_Is_Trees.bpm}"),
(f"{Forest_Is_Trees.timesignature}\n\nLyrics: \n"),
(f"{Forest_Is_Trees.lyrics}\n\nStart Date:"),
(f"{Forest_Is_Trees.start}\nEnd Date:"),
(f"{Forest_Is_Trees.end}\nRelease Date:"),
(f"{Forest_Is_Trees.release}\n\nAlbum(s):"),
(f"{Forest_Is_Trees.album}\n\n"),
(f"{Living_In_A_Halo.title}\n"),
(f"{Living_In_A_Halo.length}"),
(f"{Living_In_A_Halo.scale}"),
(f"{Living_In_A_Halo.bpm}"),
(f"{Living_In_A_Halo.timesignature}\n\nLyrics: \n"),
(f"{Living_In_A_Halo.lyrics}\n\nStart Date:"),
(f"{Living_In_A_Halo.start}\nEnd Date:"),
(f"{Living_In_A_Halo.end}\nRelease Date:"),
(f"{Living_In_A_Halo.release}\n\nAlbum(s):"),
(f"{Living_In_A_Halo.album}\n\n"),
(f"{Stepdown.title}\n"),
(f"{Stepdown.length}"),
(f"{Stepdown.scale}"),
(f"{Stepdown.bpm}"),
(f"{Stepdown.timesignature}\n\nLyrics: \n"),
(f"{Stepdown.lyrics}\n\nStart Date:"),
(f"{Stepdown.start}\nEnd Date:"),
(f"{Stepdown.end}\nRelease Date:"),
(f"{Stepdown.release}\n\nAlbum(s):"),
(f"{Stepdown.album}\n\n"),
(f"{Putting_On_The_Ritz.title}\n"),
(f"{Putting_On_The_Ritz.length}"),
(f"{Putting_On_The_Ritz.scale}"),
(f"{Putting_On_The_Ritz.bpm}"),
(f"{Putting_On_The_Ritz.timesignature}\n\nLyrics: \n"),
(f"{Putting_On_The_Ritz.lyrics}\n\nStart Date:"),
(f"{Putting_On_The_Ritz.start}\nEnd Date:"),
(f"{Putting_On_The_Ritz.end}\nRelease Date:"),
(f"{Putting_On_The_Ritz.release}\n\nAlbum(s):"),
(f"{Putting_On_The_Ritz.album}\n\n"),
(f"{Putting_On_The_Ritz_Single.title}\n"),
(f"{Putting_On_The_Ritz_Single.length}"),
(f"{Putting_On_The_Ritz_Single.scale}"),
(f"{Putting_On_The_Ritz_Single.bpm}"),
(f"{Putting_On_The_Ritz_Single.timesignature}\n\nLyrics: \n"),
(f"{Putting_On_The_Ritz_Single.lyrics}\n\nStart Date:"),
(f"{Putting_On_The_Ritz_Single.start}\nEnd Date:"),
(f"{Putting_On_The_Ritz_Single.end}\nRelease Date:"),
(f"{Putting_On_The_Ritz_Single.release}\n\nAlbum(s):"),
(f"{Putting_On_The_Ritz_Single.album}\n\n"),
(f"{Incunabula_Revised.title}\n"),
(f"{Incunabula_Revised.length}"),
(f"{Incunabula_Revised.scale}"),
(f"{Incunabula_Revised.bpm}"),
(f"{Incunabula_Revised.timesignature}\n\nLyrics: \n"),
(f"{Incunabula_Revised.lyrics}\n\nStart Date:"),
(f"{Incunabula_Revised.start}\nEnd Date:"),
(f"{Incunabula_Revised.end}\nRelease Date:"),
(f"{Incunabula_Revised.release}\n\nAlbum(s):"),
(f"{Incunabula_Revised.album}\n\n"),
(f"{Nervosa.title}\n"),
(f"{Nervosa.length}"),
(f"{Nervosa.scale}"),
(f"{Nervosa.bpm}"),
(f"{Nervosa.timesignature}\n\nLyrics: \n"),
(f"{Nervosa.lyrics}\n\nStart Date:"),
(f"{Nervosa.start}\nEnd Date:"),
(f"{Nervosa.end}\nRelease Date:"),
(f"{Nervosa.release}\n\nAlbum(s):"),
(f"{Nervosa.album}\n\n"),
(f"{Beyond_The_Trees.title}\n"),
(f"{Beyond_The_Trees.length}"),
(f"{Beyond_The_Trees.scale}"),
(f"{Beyond_The_Trees.bpm}"),
(f"{Beyond_The_Trees.timesignature}\n\nLyrics: \n"),
(f"{Beyond_The_Trees.lyrics}\n\nStart Date:"),
(f"{Beyond_The_Trees.start}\nEnd Date:"),
(f"{Beyond_The_Trees.end}\nRelease Date:"),
(f"{Beyond_The_Trees.release}\n\nAlbum(s):"),
(f"{Beyond_The_Trees.album}\n\n"),
(f"{Open_Source_Nervous_System.title}\n"),
(f"{Open_Source_Nervous_System.length}"),
(f"{Open_Source_Nervous_System.scale}"),
(f"{Open_Source_Nervous_System.bpm}"),
(f"{Open_Source_Nervous_System.timesignature}\n\nLyrics: \n"),
(f"{Open_Source_Nervous_System.lyrics}\n\nStart Date:"),
(f"{Open_Source_Nervous_System.start}\nEnd Date:"),
(f"{Open_Source_Nervous_System.end}\nRelease Date:"),
(f"{Open_Source_Nervous_System.release}\n\nAlbum(s):"),
(f"{Open_Source_Nervous_System.album}\n\n"),
(f"{Amphetamine.title}\n"),
(f"{Amphetamine.length}"),
(f"{Amphetamine.scale}"),
(f"{Amphetamine.bpm}"),
(f"{Amphetamine.timesignature}\n\nLyrics: \n"),
(f"{Amphetamine.lyrics}\n\nStart Date:"),
(f"{Amphetamine.start}\nEnd Date:"),
(f"{Amphetamine.end}\nRelease Date:"),
(f"{Amphetamine.release}\n\nAlbum(s):"),
(f"{Amphetamine.album}\n\n"),
(f"{Positivity_For_The_Masochist.title}\n"),
(f"{Positivity_For_The_Masochist.length}"),
(f"{Positivity_For_The_Masochist.scale}"),
(f"{Positivity_For_The_Masochist.bpm}"),
(f"{Positivity_For_The_Masochist.timesignature}\n\nLyrics: \n"),
(f"{Positivity_For_The_Masochist.lyrics}\n\nStart Date:"),
(f"{Positivity_For_The_Masochist.start}\nEnd Date:"),
(f"{Positivity_For_The_Masochist.end}\nRelease Date:"),
(f"{Positivity_For_The_Masochist.release}\n\nAlbum(s):"),
(f"{Positivity_For_The_Masochist.album}\n\n"),
(f"{Nervous_System.title}\n"),
(f"{Nervous_System.length}"),
(f"{Nervous_System.scale}"),
(f"{Nervous_System.bpm}"),
(f"{Nervous_System.timesignature}\n\nLyrics: \n"),
(f"{Nervous_System.lyrics}\n\nStart Date:"),
(f"{Nervous_System.start}\nEnd Date:"),
(f"{Nervous_System.end}\nRelease Date:"),
(f"{Nervous_System.release}\n\nAlbum(s):"),
(f"{Nervous_System.album}\n\n"),
(f"{With_No_Eyes.title}\n"),
(f"{With_No_Eyes.length}"),
(f"{With_No_Eyes.scale}"),
(f"{With_No_Eyes.bpm}"),
(f"{With_No_Eyes.timesignature}\n\nLyrics: \n"),
(f"{With_No_Eyes.lyrics}\n\nStart Date:"),
(f"{With_No_Eyes.start}\nEnd Date:"),
(f"{With_No_Eyes.end}\nRelease Date:"),
(f"{With_No_Eyes.release}\n\nAlbum(s):"),
(f"{With_No_Eyes.album}\n\n"),
(f"{Lenvoi.title}\n"),
(f"{Lenvoi.length}"),
(f"{Lenvoi.scale}"),
(f"{Lenvoi.bpm}"),
(f"{Lenvoi.timesignature}\n\nLyrics: \n"),
(f"{Lenvoi.lyrics}\n\nStart Date:"),
(f"{Lenvoi.start}\nEnd Date:"),
(f"{Lenvoi.end}\nRelease Date:"),
(f"{Lenvoi.release}\n\nAlbum(s):"),
(f"{Lenvoi.album}\n\n"),
(f"{Retina.title}\n"),
(f"{Retina.length}"),
(f"{Retina.scale}"),
(f"{Retina.bpm}"),
(f"{Retina.timesignature}\n\nLyrics: \n"),
(f"{Retina.lyrics}\n\nStart Date:"),
(f"{Retina.start}\nEnd Date:"),
(f"{Retina.end}\nRelease Date:"),
(f"{Retina.release}\n\nAlbum(s):"),
(f"{Retina.album}\n\n"),
(f"{Incunabula_Remastered.title}\n"),
(f"{Incunabula_Remastered.length}"),
(f"{Incunabula_Remastered.scale}"),
(f"{Incunabula_Remastered.bpm}"),
(f"{Incunabula_Remastered.timesignature}\n\nLyrics: \n"),
(f"{Incunabula_Remastered.lyrics}\n\nStart Date:"),
(f"{Incunabula_Remastered.start}\nEnd Date:"),
(f"{Incunabula_Remastered.end}\nRelease Date:"),
(f"{Incunabula_Remastered.release}\n\nAlbum(s):"),
(f"{Incunabula_Remastered.album}\n\n"),
(f"{Words.title}\n"),
(f"{Words.length}"),
(f"{Words.scale}"),
(f"{Words.bpm}"),
(f"{Words.timesignature}\n\nLyrics: \n"),
(f"{Words.lyrics}\n\nStart Date:"),
(f"{Words.start}\nEnd Date:"),
(f"{Words.end}\nRelease Date:"),
(f"{Words.release}\n\nAlbum(s):"),
(f"{Words.album}\n\n"),
(f"{Beyond_The_Trees_Remastered.title}\n"),
(f"{Beyond_The_Trees_Remastered.length}"),
(f"{Beyond_The_Trees_Remastered.scale}"),
(f"{Beyond_The_Trees_Remastered.bpm}"),
(f"{Beyond_The_Trees_Remastered.timesignature}\n\nLyrics: \n"),
(f"{Beyond_The_Trees_Remastered.lyrics}\n\nStart Date:"),
(f"{Beyond_The_Trees_Remastered.start}\nEnd Date:"),
(f"{Beyond_The_Trees_Remastered.end}\nRelease Date:"),
(f"{Beyond_The_Trees_Remastered.release}\n\nAlbum(s):"),
(f"{Beyond_The_Trees_Remastered.album}\n\n"),
(f"{Stepdown_Prologue.title}\n"),
(f"{Stepdown_Prologue.length}"),
(f"{Stepdown_Prologue.scale}"),
(f"{Stepdown_Prologue.bpm}"),
(f"{Stepdown_Prologue.timesignature}\n\nLyrics: \n"),
(f"{Stepdown_Prologue.lyrics}\n\nStart Date:"),
(f"{Stepdown_Prologue.start}\nEnd Date:"),
(f"{Stepdown_Prologue.end}\nRelease Date:"),
(f"{Stepdown_Prologue.release}\n\nAlbum(s):"),
(f"{Stepdown_Prologue.album}\n\n"),
(f"{Stepdown_Alternate.title}\n"),
(f"{Stepdown_Alternate.length}"),
(f"{Stepdown_Alternate.scale}"),
(f"{Stepdown_Alternate.bpm}"),
(f"{Stepdown_Alternate.timesignature}\n\nLyrics: \n"),
(f"{Stepdown_Alternate.lyrics}\n\nStart Date:"),
(f"{Stepdown_Alternate.start}\nEnd Date:"),
(f"{Stepdown_Alternate.end}\nRelease Date:"),
(f"{Stepdown_Alternate.release}\n\nAlbum(s):"),
(f"{Stepdown_Alternate.album}\n\n"),
(f"{Nervosa_II.title}\n"),
(f"{Nervosa_II.length}"),
(f"{Nervosa_II.scale}"),
(f"{Nervosa_II.bpm}"),
(f"{Nervosa_II.timesignature}\n\nLyrics: \n"),
(f"{Nervosa_II.lyrics}\n\nStart Date:"),
(f"{Nervosa_II.start}\nEnd Date:"),
(f"{Nervosa_II.end}\nRelease Date:"),
(f"{Nervosa_II.release}\n\nAlbum(s):"),
(f"{Nervosa_II.album}\n\n"),
(f"{What_Saturn_Lies_In_Death.title}\n"),
(f"{What_Saturn_Lies_In_Death.length}"),
(f"{What_Saturn_Lies_In_Death.scale}"),
(f"{What_Saturn_Lies_In_Death.bpm}"),
(f"{What_Saturn_Lies_In_Death.timesignature}\n\nLyrics: \n"),
(f"{What_Saturn_Lies_In_Death.lyrics}\n\nStart Date:"),
(f"{What_Saturn_Lies_In_Death.start}\nEnd Date:"),
(f"{What_Saturn_Lies_In_Death.end}\nRelease Date:"),
(f"{What_Saturn_Lies_In_Death.release}\n\nAlbum(s):"),
(f"{What_Saturn_Lies_In_Death.album}\n\n"),
(f"{Putting_On_The_Ritz_Remastered.title}\n"),
(f"{Putting_On_The_Ritz_Remastered.length}"),
(f"{Putting_On_The_Ritz_Remastered.scale}"),
(f"{Putting_On_The_Ritz_Remastered.bpm}"),
(f"{Putting_On_The_Ritz_Remastered.timesignature}\n\nLyrics: \n"),
(f"{Putting_On_The_Ritz_Remastered.lyrics}\n\nStart Date:"),
(f"{Putting_On_The_Ritz_Remastered.start}\nEnd Date:"),
(f"{Putting_On_The_Ritz_Remastered.end}\nRelease Date:"),
(f"{Putting_On_The_Ritz_Remastered.release}\n\nAlbum(s):"),
(f"{Putting_On_The_Ritz_Remastered.album}\n\n"),
(f"{Deluge.title}\n"),
(f"{Deluge.length}"),
(f"{Deluge.scale}"),
(f"{Deluge.bpm}"),
(f"{Deluge.timesignature}\n\nLyrics: \n"),
(f"{Deluge.lyrics}\n\nStart Date:"),
(f"{Deluge.start}\nEnd Date:"),
(f"{Deluge.end}\nRelease Date:"),
(f"{Deluge.release}\n\nAlbum(s):"),
(f"{Deluge.album}\n\n"),
(f"{Heaven_Isnt_Here.title}\n"),
(f"{Heaven_Isnt_Here.length}"),
(f"{Heaven_Isnt_Here.scale}"),
(f"{Heaven_Isnt_Here.bpm}"),
(f"{Heaven_Isnt_Here.timesignature}\n\nLyrics: \n"),
(f"{Heaven_Isnt_Here.lyrics}\n\nStart Date:"),
(f"{Heaven_Isnt_Here.start}\nEnd Date:"),
(f"{Heaven_Isnt_Here.end}\nRelease Date:"),
(f"{Heaven_Isnt_Here.release}\n\nAlbum(s):"),
(f"{Heaven_Isnt_Here.album}\n\n"),
(f"{Dr_Faust.title}\n"),
(f"{Dr_Faust.length}"),
(f"{Dr_Faust.scale}"),
(f"{Dr_Faust.bpm}"),
(f"{Dr_Faust.timesignature}\n\nLyrics: \n"),
(f"{Dr_Faust.lyrics}\n\nStart Date:"),
(f"{Dr_Faust.start}\nEnd Date:"),
(f"{Dr_Faust.end}\nRelease Date:"),
(f"{Dr_Faust.release}\n\nAlbum(s):"),
(f"{Dr_Faust.album}\n\n"),
(f"{Mind_Harvest.title}\n"),
(f"{Mind_Harvest.length}"),
(f"{Mind_Harvest.scale}"),
(f"{Mind_Harvest.bpm}"),
(f"{Mind_Harvest.timesignature}\n\nLyrics: \n"),
(f"{Mind_Harvest.lyrics}\n\nStart Date:"),
(f"{Mind_Harvest.start}\nEnd Date:"),
(f"{Mind_Harvest.end}\nRelease Date:"),
(f"{Mind_Harvest.release}\n\nAlbum(s):"),
(f"{Mind_Harvest.album}\n\n"),
(f"{Open_Source_Nervous_System_Demo.title}\n"),
(f"{Open_Source_Nervous_System_Demo.length}"),
(f"{Open_Source_Nervous_System_Demo.scale}"),
(f"{Open_Source_Nervous_System_Demo.bpm}"),
(f"{Open_Source_Nervous_System_Demo.timesignature}\n\nLyrics: \n"),
(f"{Open_Source_Nervous_System_Demo.lyrics}\n\nStart Date:"),
(f"{Open_Source_Nervous_System_Demo.start}\nEnd Date:"),
(f"{Open_Source_Nervous_System_Demo.end}\nRelease Date:"),
(f"{Open_Source_Nervous_System_Demo.release}\n\nAlbum(s):"),
(f"{Open_Source_Nervous_System_Demo.album}\n\n"),
(f"{Last_October.title}\n"),
(f"{Last_October.length}"),
(f"{Last_October.scale}"),
(f"{Last_October.bpm}"),
(f"{Last_October.timesignature}\n\nLyrics: \n"),
(f"{Last_October.lyrics}\n\nStart Date:"),
(f"{Last_October.start}\nEnd Date:"),
(f"{Last_October.end}\nRelease Date:"),
(f"{Last_October.release}\n\nAlbum(s):"),
(f"{Last_October.album}\n\n"),
(f"{Heer_Public_Archive_1943.title}\n"),
(f"{Heer_Public_Archive_1943.length}"),
(f"{Heer_Public_Archive_1943.scale}"),
(f"{Heer_Public_Archive_1943.bpm}"),
(f"{Heer_Public_Archive_1943.timesignature}\n\nLyrics: \n"),
(f"{Heer_Public_Archive_1943.lyrics}\n\nStart Date:"),
(f"{Heer_Public_Archive_1943.start}\nEnd Date:"),
(f"{Heer_Public_Archive_1943.end}\nRelease Date:"),
(f"{Heer_Public_Archive_1943.release}\n\nAlbum(s):"),
(f"{Heer_Public_Archive_1943.album}\n\n"),
(f"{Embryo.title}\n"),
(f"{Embryo.length}"),
(f"{Embryo.scale}"),
(f"{Embryo.bpm}"),
(f"{Embryo.timesignature}\n\nLyrics: \n"),
(f"{Embryo.lyrics}\n\nStart Date:"),
(f"{Embryo.start}\nEnd Date:"),
(f"{Embryo.end}\nRelease Date:"),
(f"{Embryo.release}\n\nAlbum(s):"),
(f"{Embryo.album}\n\n"),
(f"{Putting_On_The_Ritz_Radio_Edit.title}\n"),
(f"{Putting_On_The_Ritz_Radio_Edit.length}"),
(f"{Putting_On_The_Ritz_Radio_Edit.scale}"),
(f"{Putting_On_The_Ritz_Radio_Edit.bpm}"),
(f"{Putting_On_The_Ritz_Radio_Edit.timesignature}\n\nLyrics: \n"),
(f"{Putting_On_The_Ritz_Radio_Edit.lyrics}\n\nStart Date:"),
(f"{Putting_On_The_Ritz_Radio_Edit.start}\nEnd Date:"),
(f"{Putting_On_The_Ritz_Radio_Edit.end}\nRelease Date:"),
(f"{Putting_On_The_Ritz_Radio_Edit.release}\n\nAlbum(s):"),
(f"{Putting_On_The_Ritz_Radio_Edit.album}\n\n"),
(f"{Latrodectus.title}\n"),
(f"{Latrodectus.length}"),
(f"{Latrodectus.scale}"),
(f"{Latrodectus.bpm}"),
(f"{Latrodectus.timesignature}\n\nLyrics: \n"),
(f"{Latrodectus.lyrics}\n\nStart Date:"),
(f"{Latrodectus.start}\nEnd Date:"),
(f"{Latrodectus.end}\nRelease Date:"),
(f"{Latrodectus.release}\n\nAlbum(s):"),
(f"{Latrodectus.album}\n\n"),
(f"{Stella_Splendens.title}\n"),
(f"{Stella_Splendens.length}"),
(f"{Stella_Splendens.scale}"),
(f"{Stella_Splendens.bpm}"),
(f"{Stella_Splendens.timesignature}\n\nLyrics: \n"),
(f"{Stella_Splendens.lyrics}\n\nStart Date:"),
(f"{Stella_Splendens.start}\nEnd Date:"),
(f"{Stella_Splendens.end}\nRelease Date:"),
(f"{Stella_Splendens.release}\n\nAlbum(s):"),
(f"{Stella_Splendens.album}\n\n"),
(f"{Maslows_Du_Vide.title}\n"),
(f"{Maslows_Du_Vide.length}"),
(f"{Maslows_Du_Vide.scale}"),
(f"{Maslows_Du_Vide.bpm}"),
(f"{Maslows_Du_Vide.timesignature}\n\nLyrics: \n"),
(f"{Maslows_Du_Vide.lyrics}\n\nStart Date:"),
(f"{Maslows_Du_Vide.start}\nEnd Date:"),
(f"{Maslows_Du_Vide.end}\nRelease Date:"),
(f"{Maslows_Du_Vide.release}\n\nAlbum(s):"),
(f"{Maslows_Du_Vide.album}\n\n"),
(f"{Strawberry_Gashes.title}\n"),
(f"{Strawberry_Gashes.length}"),
(f"{Strawberry_Gashes.scale}"),
(f"{Strawberry_Gashes.bpm}"),
(f"{Strawberry_Gashes.timesignature}\n\nLyrics: \n"),
(f"{Strawberry_Gashes.lyrics}\n\nStart Date:"),
(f"{Strawberry_Gashes.start}\nEnd Date:"),
(f"{Strawberry_Gashes.end}\nRelease Date:"),
(f"{Strawberry_Gashes.release}\n\nAlbum(s):"),
(f"{Strawberry_Gashes.album}\n\n"),
(f"{Lorem_Ipsum.title}\n"),
(f"{Lorem_Ipsum.length}"),
(f"{Lorem_Ipsum.scale}"),
(f"{Lorem_Ipsum.bpm}"),
(f"{Lorem_Ipsum.timesignature}\n\nLyrics: \n"),
(f"{Lorem_Ipsum.lyrics}\n\nStart Date:"),
(f"{Lorem_Ipsum.start}\nEnd Date:"),
(f"{Lorem_Ipsum.end}\nRelease Date:"),
(f"{Lorem_Ipsum.release}\n\nAlbum(s):"),
(f"{Lorem_Ipsum.album}\n\n"),
(f"{By_Proxy.title}\n"),
(f"{By_Proxy.length}"),
(f"{By_Proxy.scale}"),
(f"{By_Proxy.bpm}"),
(f"{By_Proxy.timesignature}\n\nLyrics: \n"),
(f"{By_Proxy.lyrics}\n\nStart Date:"),
(f"{By_Proxy.start}\nEnd Date:"),
(f"{By_Proxy.end}\nRelease Date:"),
(f"{By_Proxy.release}\n\nAlbum(s):"),
(f"{By_Proxy.album}\n\n"),
(f"{Lappel_Du_Vide.title}\n"),
(f"{Lappel_Du_Vide.length}"),
(f"{Lappel_Du_Vide.scale}"),
(f"{Lappel_Du_Vide.bpm}"),
(f"{Lappel_Du_Vide.timesignature}\n\nLyrics: \n"),
(f"{Lappel_Du_Vide.lyrics}\n\nStart Date:"),
(f"{Lappel_Du_Vide.start}\nEnd Date:"),
(f"{Lappel_Du_Vide.end}\nRelease Date:"),
(f"{Lappel_Du_Vide.release}\n\nAlbum(s):"),
(f"{Lappel_Du_Vide.album}\n\n"),
(f"{Heer_Public_Archive_1945.title}\n"),
(f"{Heer_Public_Archive_1945.length}"),
(f"{Heer_Public_Archive_1945.scale}"),
(f"{Heer_Public_Archive_1945.bpm}"),
(f"{Heer_Public_Archive_1945.timesignature}\n\nLyrics: \n"),
(f"{Heer_Public_Archive_1945.lyrics}\n\nStart Date:"),
(f"{Heer_Public_Archive_1945.start}\nEnd Date:"),
(f"{Heer_Public_Archive_1945.end}\nRelease Date:"),
(f"{Heer_Public_Archive_1945.release}\n\nAlbum(s):"),
(f"{Heer_Public_Archive_1945.album}\n\n"),
(f"{Strawberry_Gashes_Single.title}\n"),
(f"{Strawberry_Gashes_Single.length}"),
(f"{Strawberry_Gashes_Single.scale}"),
(f"{Strawberry_Gashes_Single.bpm}"),
(f"{Strawberry_Gashes_Single.timesignature}\n\nLyrics: \n"),
(f"{Strawberry_Gashes_Single.lyrics}\n\nStart Date:"),
(f"{Strawberry_Gashes_Single.start}\nEnd Date:"),
(f"{Strawberry_Gashes_Single.end}\nRelease Date:"),
(f"{Strawberry_Gashes_Single.release}\n\nAlbum(s):"),
(f"{Strawberry_Gashes_Single.album}\n\n"),
(f"{Miss_Nothing.title}\n"),
(f"{Miss_Nothing.length}"),
(f"{Miss_Nothing.scale}"),
(f"{Miss_Nothing.bpm}"),
(f"{Miss_Nothing.timesignature}\n\nLyrics: \n"),
(f"{Miss_Nothing.lyrics}\n\nStart Date:"),
(f"{Miss_Nothing.start}\nEnd Date:"),
(f"{Miss_Nothing.end}\nRelease Date:"),
(f"{Miss_Nothing.release}\n\nAlbum(s):"),
(f"{Miss_Nothing.album}\n\n"),
(f"{Heer_Public_Archive_1944.title}\n"),
(f"{Heer_Public_Archive_1944.length}"),
(f"{Heer_Public_Archive_1944.scale}"),
(f"{Heer_Public_Archive_1944.bpm}"),
(f"{Heer_Public_Archive_1944.timesignature}\n\nLyrics: \n"),
(f"{Heer_Public_Archive_1944.lyrics}\n\nStart Date:"),
(f"{Heer_Public_Archive_1944.start}\nEnd Date:"),
(f"{Heer_Public_Archive_1944.end}\nRelease Date:"),
(f"{Heer_Public_Archive_1944.release}\n\nAlbum(s):"),
(f"{Heer_Public_Archive_1944.album}\n\n"),
(f"{God_Of_The_Gaps.title}\n"),
(f"{God_Of_The_Gaps.length}"),
(f"{God_Of_The_Gaps.scale}"),
(f"{God_Of_The_Gaps.bpm}"),
(f"{God_Of_The_Gaps.timesignature}\n\nLyrics: \n"),
(f"{God_Of_The_Gaps.lyrics}\n\nStart Date:"),
(f"{God_Of_The_Gaps.start}\nEnd Date:"),
(f"{God_Of_The_Gaps.end}\nRelease Date:"),
(f"{God_Of_The_Gaps.release}\n\nAlbum(s):"),
(f"{God_Of_The_Gaps.album}\n\n"),
(f"{Last_Of_October.title}\n"),
(f"{Last_Of_October.length}"),
(f"{Last_Of_October.scale}"),
(f"{Last_Of_October.bpm}"),
(f"{Last_Of_October.timesignature}\n\nLyrics: \n"),
(f"{Last_Of_October.lyrics}\n\nStart Date:"),
(f"{Last_Of_October.start}\nEnd Date:"),
(f"{Last_Of_October.end}\nRelease Date:"),
(f"{Last_Of_October.release}\n\nAlbum(s):"),
(f"{Last_Of_October.album}\n\n"),
(f"{De_Finibus_Bonorum_Et_Malorum.title}\n"),
(f"{De_Finibus_Bonorum_Et_Malorum.length}"),
(f"{De_Finibus_Bonorum_Et_Malorum.scale}"),
(f"{De_Finibus_Bonorum_Et_Malorum.bpm}"),
(f"{De_Finibus_Bonorum_Et_Malorum.timesignature}\n\nLyrics: \n"),
(f"{De_Finibus_Bonorum_Et_Malorum.lyrics}\n\nStart Date:"),
(f"{De_Finibus_Bonorum_Et_Malorum.start}\nEnd Date:"),
(f"{De_Finibus_Bonorum_Et_Malorum.end}\nRelease Date:"),
(f"{De_Finibus_Bonorum_Et_Malorum.release}\n\nAlbum(s):"),
(f"{De_Finibus_Bonorum_Et_Malorum.album}\n\n"),
(f"{Sleepwalking_In_Los_Angeles.title}\n"),
(f"{Sleepwalking_In_Los_Angeles.length}"),
(f"{Sleepwalking_In_Los_Angeles.scale}"),
(f"{Sleepwalking_In_Los_Angeles.bpm}"),
(f"{Sleepwalking_In_Los_Angeles.timesignature}\n\nLyrics: \n"),
(f"{Sleepwalking_In_Los_Angeles.lyrics}\n\nStart Date:"),
(f"{Sleepwalking_In_Los_Angeles.start}\nEnd Date:"),
(f"{Sleepwalking_In_Los_Angeles.end}\nRelease Date:"),
(f"{Sleepwalking_In_Los_Angeles.release}\n\nAlbum(s):"),
(f"{Sleepwalking_In_Los_Angeles.album}\n\n"),
(f"{The_Call_Of_The_Void.title}\n"),
(f"{The_Call_Of_The_Void.length}"),
(f"{The_Call_Of_The_Void.scale}"),
(f"{The_Call_Of_The_Void.bpm}"),
(f"{The_Call_Of_The_Void.timesignature}\n\nLyrics: \n"),
(f"{The_Call_Of_The_Void.lyrics}\n\nStart Date:"),
(f"{The_Call_Of_The_Void.start}\nEnd Date:"),
(f"{The_Call_Of_The_Void.end}\nRelease Date:"),
(f"{The_Call_Of_The_Void.release}\n\nAlbum(s):"),
(f"{The_Call_Of_The_Void.album}\n\n"),
(f"{Lacrimosa.title}\n"),
(f"{Lacrimosa.length}"),
(f"{Lacrimosa.scale}"),
(f"{Lacrimosa.bpm}"),
(f"{Lacrimosa.timesignature}\n\nLyrics: \n"),
(f"{Lacrimosa.lyrics}\n\nStart Date:"),
(f"{Lacrimosa.start}\nEnd Date:"),
(f"{Lacrimosa.end}\nRelease Date:"),
(f"{Lacrimosa.release}\n\nAlbum(s):"),
(f"{Lacrimosa.album}\n\n"),)

All = SongMetadata(All_Titles(),
All_Lengths(),
All_Scales(),
All_BPMs(),
All_TimeSignatures(),
All_Lyrics(),
All_Start_Dates(),
All_End_Dates(),
All_Release_Dates(),
All_Albums(),
All())