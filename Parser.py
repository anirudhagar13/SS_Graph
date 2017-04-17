import docx2txt

class Patent:
	def __init__(self, file, patent=''):
		'''
		Fixed template to parse patents
		'''
		self.file = file
		self.patent = patent
		self.template = {'TITLE':'','INVENTOR':'',
					'FIELD':'','BACKGROUND':'',
					'CLAIMS':'','SUMMARY':'',
					'DRAWINGS':'','DETAILED':'',
					'ABSTRACT':''}
		self.Initialise()

	def getTemplate(self,part):
		'''
		Getter for different patent parts
		'''
		if part not in self.template or self.template[part] == '':
			return 'Part Not Found'

		return self.template[part]

	def Checkfix(self, line, oldheading):
		'''
		Checks if new heading has started
		'''
		for heading in self.template:
			if heading in line:
				# Heading has changed
				return heading
		return oldheading

	def Initialise(self):
		'''
		To Parse patent line by line and fill template
		'''
		if self.patent == '':
			# Need to open file
			if '.doc' in self.file or '.docx' in file:
				# Open doc file differently
				self.patent = docx2txt.process(self.file).split('\n')
			else:
				# Assume file content will be supported 
				with open(self.file,'r') as file:
					self.patent = file.readlines()

		curr_key = ''
		for line in self.patent:
			new_key = self.Checkfix(line, curr_key)

			if new_key != curr_key:
				# Change of heading has happened
				curr_key = new_key
				continue	# Skip heading line
			if curr_key == '':
				# Content hasn't started
				continue
			self.template[curr_key] += line

if __name__ == '__main__':
	p = Patent(file='Berthing (Provisional).docx')
	print p.getTemplate('BACKGROUND')