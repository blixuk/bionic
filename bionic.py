import string

class Bionic:

	def __init__(self, path:str=None) -> None:
		self.fixation_factor = 1.6
		self.data = []

		if path:
			self.load(path)

	def load(self, path: str) -> None:
		with open(path, 'r') as file:
			self.data = file.readlines()
	
	def print(self, data:str=None) -> None:
		data = data if data else self.data
		for line in data:
			print(line)

	def bionify(self, data:str=None) -> str:
		data = data if data else self.data
		for posistion, line in enumerate(data):
			data[posistion] = self.bionify_line(line)
		return self.data

	def bionify_line(self, line:str) -> str:
		bionic_line = ""
		for word in line.split():
			bionic_line += f"{self.bionify_word(word)} "
		return bionic_line.strip()

	def bionify_word(self, word:str) -> str:
		if '-' in word:
			part_a, part_b = word.split('-')
			part_a_fixation = self._get_fixation(part_a)
			part_a = f"\033[0m\033[01m{part_a[:part_a_fixation]}\033[0m\033[02m{part_a[part_a_fixation:]}\033[0m"
			part_b_fixation = self._get_fixation(part_b)
			part_b = f"\033[0m\033[01m{part_b[:part_b_fixation]}\033[0m\033[02m{part_b[part_b_fixation:]}\033[0m"
			bionic_word = f"{part_a}-{part_b}"
		else:
			fixation = self._get_fixation(word)
			bionic_word = f"\033[0m\033[01m{word[:fixation]}\033[0m\033[02m{word[fixation:]}\033[0m"
		return bionic_word

	def _get_fixation(self, word: str) -> int:
		word_stripped = word.translate(str.maketrans('', '', string.punctuation))
		word_length = len(word_stripped)
		fixation = int(word_length / self.fixation_factor)
		return fixation if fixation != 0 else 1

def main():
	bionic = Bionic()
	bionic.load("PaleBlueDot.txt")
	bionic.bionify()
	bionic.print()

if __name__ == "__main__":
	main()