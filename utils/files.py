import os

class Files():

	@staticmethod
	def create_file(name: str, content: str):
		try:
			value = ""
			x = 0
			for i in range(len(content)):
				if i != 0 and i != 1 and (i != len(content) - 1):
					value = value + content[i]
					x = x + 1
			filename = f'data/main.py'
			with open(filename, 'a') as f:
				for line in value.split('\\n'):
					f.write(f'{line}\n')
			return filename
		except Exception as e:
			print(e)
			print('Error #00003')
			return False

	@staticmethod
	def emulate(filename: str):
		try:
			emulate1 = os.popen(f'python3 {filename} >> tests/emulate1')
			emulate2 = os.popen('echo "Hello word\nSalut" >> tests/emulate2')
		except Exception as e:
			print(e)
			print('Error #00002')

	@staticmethod
	def verif():
		try:
			with open('tests/emulate1', 'r') as f1:
				e1 = f1.readlines()
			with open('tests/emulate2', 'r') as f2:
				e2 = f2.readlines()
			if len(e2) != len (e1):
				raise Exception('Different number of line')
			for i in range(len(e2)):
				if e1[i] != e2[i]:
					raise Exception('Different number of line')
			return {'res': True}
		except Exception as e:
			print(e)
			print('Error #00001')
			return {'res': False, 'msg': str(e)}

	@staticmethod
	def clean():
		try:
			os.popen('rm data/* tests/*').read()
			os.popen('touch tests/emulate1 tests/emulate2 data/main.py')
		except Exception as e:
			print('Error #00000')
			print(e)