"""
__________________________________________________________________________________
#####################
#ListAutomationTools#
#####################

This module returns string based modifications to every element in a user defined list.

Simple tutorial:

print (ListAutomationTools.Insert Method Here(['''List with elements on each line
List with elements on each line
List with elements on each line'''], "Insert string here", "Potential second insert string here depending on method"))
__________________________________________________________________________________

###########
##Methods##
###########

1.beginadd			adds a string to the begining of every item in a list
2.endadd			adds a string to the end of every item in a list
3.beginendadd		adds a string to the begining and end of every item in a list
4.remove			removes a string from items in a list
5.swap				swaps a string in a list with a user defined string
__________________________________________________________________________________
####################
##Method Arguments##
####################
User Defined Arguments
1.beginadd			(['''list'''], "string_to_add")
2.endadd			(['''list'''], "string_to_add")
3.beginendadd		(['''list'''], "string_to_add_beginning", "string_to_add_end")
4.remove			(['''list'''], "string_to_remove")
5.swap				(['''list'''], "string_in_list", "new_string")

To call on Metadata or other text as a list i.e. (ListAutomationTools.beginadd([SongMetadata.title(All)]
__________________________________________________________________________________
"""
######
#Main#
######
class ListAutomationTools:
	def __init__(self): 
		pass
	@classmethod
	def beginadd(cls, string_input, prefix):
		if isinstance(string_input, list):
			string_input = string_input[0] if string_input else ""
		lines = string_input.split('\n')
		return '\n'.join([prefix + s.strip() for s in lines])

	@classmethod
	def endadd(cls, string_input, suffix):
		if isinstance(string_input, list):
			string_input = string_input[0] if string_input else ""
		lines = string_input.split('\n')
		return '\n'.join([s.strip() + suffix for s in lines])

	@classmethod
	def beginendadd(cls, string_input, prefix, suffix):
		if isinstance(string_input, list):
			string_input = string_input[0] if string_input else ""
		lines = string_input.split('\n')
		return '\n'.join([prefix + s.strip() + suffix for s in lines])

	@classmethod
	def remove(cls, string_input, to_remove):
		if isinstance(string_input, list):
			string_input = string_input[0] if string_input else ""
		lines = string_input.split('\n')
		return '\n'.join([s.strip() for s in lines if s.strip() != to_remove])

	@classmethod
	def swap(cls, string_input, old_str, new_str):
		if isinstance(string_input, list):
			string_input = string_input[0] if string_input else ""
		lines = string_input.split('\n')
		return '\n'.join([s.strip().replace(old_str, new_str) for s in lines])
