class AlbumMetadata:
	def __init__(self, title, type, length, numsongs, songs, start, end, release, all): 
		self.title = title
		self.type = type
		self.length = length
		self.numsongs = numsongs
		self.songs = songs
		self.start = start
		self.end = end
		self.release = release
		self.all = all
	
	def title(self):
		return self.title

	def type(self):
		return self.type

	def length(self):
		return self.length

	def numsongs(self):
		return self.numsongs
	
	def songs(self):
		return self.songs

	def start(self):
		return self.start

	def end(self):
		return self.end

	def release(self):
		return self.release

	def all(self):
		return '\n'.join(str(item) for item in self.all)

########
#Albums#
########

Incunabula_Album_Variables = ['Incunabula',
	'EP', 
	'20:04', 
	'5', 
	'Incunabula\n Forest Is Trees\n Living In A Halo\n Stepdown\n Putting On The Ritz', 
	'04-12-2011', 
	'01-29-2013', 
	'11-02-2015']

Putting_On_The_Ritz_Album_Variables = ['Putting On The Ritz',
	'Single', 
	'2:24', 
	'1', 
	'Putting On The Ritz', 
	'10-17-2012', 
	'10-19-2012', 
	'11-06-2015']

Incunabula_Revised_Album_Variables = ['Incunabula (Revised)',
	'Single', 
	'8:58', 
	'3', 
	'Incunabula (Revised)\n Nervosa\n Beyond The Trees', 
	'12-23-2013', 
	'10-30-2016', 
	'11-15-2016']

Nervous_System_Album_Variables = ['Nervous System',
	'EP', 
	'12:30', 
	'6', 
	'Open Source Nervous System\n Amphetamine\n Positivity For The Masochist\n Nervous System\n With No Eyes\n L\'envoi' ,
	'07-19-2014', 
	'04-01-2017', 
	'05-20-2017']

Open_Source_Nervous_System_Album_Variables = ['Open Source Nervous System',
	'BSide', 
	'42:49', 
	'16', 
	'''	Retina
	Incunabula (Remastered)
	Words
	Beyond The Trees (Remastered)
	Stepdown Prologue
	Stepdown (Alternate)
	Nervosa II
	What Saturn Lies In Death
	Putting On The Ritz (Remastered)
	Deluge
	Heaven Isn't Here
	Dr. Faust
	Mind Harvest
	Open Source Nervous System (Demo)
	Last October
	Heer Public Archive 1943''', 
	'05-09-2009', 
	'05-04-2017', 
	'09-03-2017']

Open_Source_Nervous_System_II_Album_Variables = ['Open Source Nervous System II',
	'BSide', 
	'34:01', 
	'10',
	'''	Embryo
	Putting On The Ritz (Radio Edit)
	Latrodectus
	Stella Splendens
	Maslow's Du Vide
	Strawberry Gashes
	Lorem Ipsum
	By Proxy
	L'appel Du Vide
	Heer Public Archive 1945''', 
	'08-12-2011', 
	'05-19-2018', 
	'08-04-2018']

Strawberry_Gashes_Album_Variables = ['Strawberry Gashes',
	'Single', 
	'9:02', 
	'3', 
	'''	Strawberry Gashes
	Miss Nothing
	Heer Public Archive 1944''', 
	'08-12-2011', 
	'01-31-2018', 
	'07-29-2019']

God_Of_The_Gaps_Album_Variables = ['God Of The Gaps',
	'Single', 
	'4:32', 
	'2', 
	'''	God Of The Gaps
	Last Of October''', 
	'02-02-2016', 
	'09-15-2018', 
	'05-05-2020']

Open_Source_Limbic_System_Album_Variables = ['Open Source Limbic System',
	'BSide', 
	'7:27', 
	'4', 
	'''	De Finibus Bonorum Et Malorum
	Sleepwalking In Los Angeles
	The Call Of The Void
	Lacrimosa''', 
	'12-23-2023', 
	'03-20-2024', 
	'04-04-2024']

Incunabula_Album = AlbumMetadata((f"{Incunabula_Album_Variables[0]}"),
(f"{Incunabula_Album_Variables[1]}"),
(f"{Incunabula_Album_Variables[2]}"),
(f"{Incunabula_Album_Variables[3]}"),
(f"{Incunabula_Album_Variables[4]}"),
(f"{Incunabula_Album_Variables[5]}"),
(f"{Incunabula_Album_Variables[6]}"),
(f"{Incunabula_Album_Variables[7]}"),
((f"{Incunabula_Album_Variables[0]}"),
(f"{Incunabula_Album_Variables[1]}"),
(f"{Incunabula_Album_Variables[2]}"),
(f"{Incunabula_Album_Variables[3]}"),
(f"{Incunabula_Album_Variables[4]}"),
(f"{Incunabula_Album_Variables[5]}"),
(f"{Incunabula_Album_Variables[6]}"),
(f"{Incunabula_Album_Variables[7]}")))

Putting_On_The_Ritz_Album = AlbumMetadata((f"{Putting_On_The_Ritz_Album_Variables[0]}"),
(f"{Putting_On_The_Ritz_Album_Variables[1]}"),
(f"{Putting_On_The_Ritz_Album_Variables[2]}"),
(f"{Putting_On_The_Ritz_Album_Variables[3]}"),
(f"{Putting_On_The_Ritz_Album_Variables[4]}"),
(f"{Putting_On_The_Ritz_Album_Variables[5]}"),
(f"{Putting_On_The_Ritz_Album_Variables[6]}"),
(f"{Putting_On_The_Ritz_Album_Variables[7]}"),
((f"{Putting_On_The_Ritz_Album_Variables[0]}"),
(f"{Putting_On_The_Ritz_Album_Variables[1]}"),
(f"{Putting_On_The_Ritz_Album_Variables[2]}"),
(f"{Putting_On_The_Ritz_Album_Variables[3]}"),
(f"{Putting_On_The_Ritz_Album_Variables[4]}"),
(f"{Putting_On_The_Ritz_Album_Variables[5]}"),
(f"{Putting_On_The_Ritz_Album_Variables[6]}"),
(f"{Putting_On_The_Ritz_Album_Variables[7]}")))

Incunabula_Revised_Album = AlbumMetadata((f"{Incunabula_Revised_Album_Variables[0]}"),
(f"{Incunabula_Revised_Album_Variables[1]}"),
(f"{Incunabula_Revised_Album_Variables[2]}"),
(f"{Incunabula_Revised_Album_Variables[3]}"),
(f"{Incunabula_Revised_Album_Variables[4]}"),
(f"{Incunabula_Revised_Album_Variables[5]}"),
(f"{Incunabula_Revised_Album_Variables[6]}"),
(f"{Incunabula_Revised_Album_Variables[7]}"),
((f"{Incunabula_Revised_Album_Variables[0]}"),
(f"{Incunabula_Revised_Album_Variables[1]}"),
(f"{Incunabula_Revised_Album_Variables[2]}"),
(f"{Incunabula_Revised_Album_Variables[3]}"),
(f"{Incunabula_Revised_Album_Variables[4]}"),
(f"{Incunabula_Revised_Album_Variables[5]}"),
(f"{Incunabula_Revised_Album_Variables[6]}"),
(f"{Incunabula_Revised_Album_Variables[7]}")))

Nervous_System_Album = AlbumMetadata((f"{Nervous_System_Album_Variables[0]}"),
(f"{Nervous_System_Album_Variables[1]}"),
(f"{Nervous_System_Album_Variables[2]}"),
(f"{Nervous_System_Album_Variables[3]}"),
(f"{Nervous_System_Album_Variables[4]}"),
(f"{Nervous_System_Album_Variables[5]}"),
(f"{Nervous_System_Album_Variables[6]}"),
(f"{Nervous_System_Album_Variables[7]}"),
((f"{Nervous_System_Album_Variables[0]}"),
(f"{Nervous_System_Album_Variables[1]}"),
(f"{Nervous_System_Album_Variables[2]}"),
(f"{Nervous_System_Album_Variables[3]}"),
(f"{Nervous_System_Album_Variables[4]}"),
(f"{Nervous_System_Album_Variables[5]}"),
(f"{Nervous_System_Album_Variables[6]}"),
(f"{Nervous_System_Album_Variables[7]}")))

Open_Source_Nervous_System_Album = AlbumMetadata((f"{Open_Source_Nervous_System_Album_Variables[0]}"),
(f"{Open_Source_Nervous_System_Album_Variables[1]}"),
(f"{Open_Source_Nervous_System_Album_Variables[2]}"),
(f"{Open_Source_Nervous_System_Album_Variables[3]}"),
(f"{Open_Source_Nervous_System_Album_Variables[4]}"),
(f"{Open_Source_Nervous_System_Album_Variables[5]}"),
(f"{Open_Source_Nervous_System_Album_Variables[6]}"),
(f"{Open_Source_Nervous_System_Album_Variables[7]}"),
((f"{Open_Source_Nervous_System_Album_Variables[0]}"),
(f"{Open_Source_Nervous_System_Album_Variables[1]}"),
(f"{Open_Source_Nervous_System_Album_Variables[2]}"),
(f"{Open_Source_Nervous_System_Album_Variables[3]}"),
(f"{Open_Source_Nervous_System_Album_Variables[4]}"),
(f"{Open_Source_Nervous_System_Album_Variables[5]}"),
(f"{Open_Source_Nervous_System_Album_Variables[6]}"),
(f"{Open_Source_Nervous_System_Album_Variables[7]}")))

Open_Source_Nervous_System_II_Album = AlbumMetadata((f"{Open_Source_Nervous_System_II_Album_Variables[0]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[1]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[2]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[3]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[4]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[5]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[6]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[7]}"),
((f"{Open_Source_Nervous_System_II_Album_Variables[0]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[1]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[2]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[3]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[4]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[5]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[6]}"),
(f"{Open_Source_Nervous_System_II_Album_Variables[7]}")))

Strawberry_Gashes_Album = AlbumMetadata((f"{Strawberry_Gashes_Album_Variables[0]}"),
(f"{Strawberry_Gashes_Album_Variables[1]}"),
(f"{Strawberry_Gashes_Album_Variables[2]}"),
(f"{Strawberry_Gashes_Album_Variables[3]}"),
(f"{Strawberry_Gashes_Album_Variables[4]}"),
(f"{Strawberry_Gashes_Album_Variables[5]}"),
(f"{Strawberry_Gashes_Album_Variables[6]}"),
(f"{Strawberry_Gashes_Album_Variables[7]}"),
((f"{Strawberry_Gashes_Album_Variables[0]}"),
(f"{Strawberry_Gashes_Album_Variables[1]}"),
(f"{Strawberry_Gashes_Album_Variables[2]}"),
(f"{Strawberry_Gashes_Album_Variables[3]}"),
(f"{Strawberry_Gashes_Album_Variables[4]}"),
(f"{Strawberry_Gashes_Album_Variables[5]}"),
(f"{Strawberry_Gashes_Album_Variables[6]}"),
(f"{Strawberry_Gashes_Album_Variables[7]}")))

God_Of_The_Gaps_Album = AlbumMetadata((f"{God_Of_The_Gaps_Album_Variables[0]}"),
(f"{God_Of_The_Gaps_Album_Variables[1]}"),
(f"{God_Of_The_Gaps_Album_Variables[2]}"),
(f"{God_Of_The_Gaps_Album_Variables[3]}"),
(f"{God_Of_The_Gaps_Album_Variables[4]}"),
(f"{God_Of_The_Gaps_Album_Variables[5]}"),
(f"{God_Of_The_Gaps_Album_Variables[6]}"),
(f"{God_Of_The_Gaps_Album_Variables[7]}"),
((f"{God_Of_The_Gaps_Album_Variables[0]}"),
(f"{God_Of_The_Gaps_Album_Variables[1]}"),
(f"{God_Of_The_Gaps_Album_Variables[2]}"),
(f"{God_Of_The_Gaps_Album_Variables[3]}"),
(f"{God_Of_The_Gaps_Album_Variables[4]}"),
(f"{God_Of_The_Gaps_Album_Variables[5]}"),
(f"{God_Of_The_Gaps_Album_Variables[6]}"),
(f"{God_Of_The_Gaps_Album_Variables[7]}")))

Open_Source_Limbic_System_Album = AlbumMetadata((f"{Open_Source_Limbic_System_Album_Variables[0]}"),
(f"{Open_Source_Limbic_System_Album_Variables[1]}"),
(f"{Open_Source_Limbic_System_Album_Variables[2]}"),
(f"{Open_Source_Limbic_System_Album_Variables[3]}"),
(f"{Open_Source_Limbic_System_Album_Variables[4]}"),
(f"{Open_Source_Limbic_System_Album_Variables[5]}"),
(f"{Open_Source_Limbic_System_Album_Variables[6]}"),
(f"{Open_Source_Limbic_System_Album_Variables[7]}"),
((f"{Open_Source_Limbic_System_Album_Variables[0]}"),
(f"{Open_Source_Limbic_System_Album_Variables[1]}"),
(f"{Open_Source_Limbic_System_Album_Variables[2]}"),
(f"{Open_Source_Limbic_System_Album_Variables[3]}"),
(f"{Open_Source_Limbic_System_Album_Variables[4]}"),
(f"{Open_Source_Limbic_System_Album_Variables[5]}"),
(f"{Open_Source_Limbic_System_Album_Variables[6]}"),
(f"{Open_Source_Limbic_System_Album_Variables[7]}")))