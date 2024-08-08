from abc import ABC, abstractmethod


# Abstract Class
class DataProcessor(ABC):
	def process_data(self):
		self.read_data()
		self.parse_data()
		self.format_data()
		self.save_data()

	@abstractmethod
	def read_data(self):
		pass

	@abstractmethod
	def parse_data(self):
		pass

	@abstractmethod
	def format_data(self):
		pass

	def save_data(self):
		print("Saving data...")


# Concrete Class for CSV
class CSVDataProcessor(DataProcessor):
	def read_data(self):
		print("Reading CSV data...")

	def parse_data(self):
		print("Parsing CSV data...")

	def format_data(self):
		print("Formatting CSV data...")


# Concrete Class for JSON
class JSONDataProcessor(DataProcessor):
	def read_data(self):
		print("Reading JSON data...")

	def parse_data(self):
		print("Parsing JSON data...")

	def format_data(self):
		print("Formatting JSON data...")


if __name__ == '__main__':
	# Example usage
	csv_processor = CSVDataProcessor()
	csv_processor.process_data()

	json_processor = JSONDataProcessor()
	json_processor.process_data()
