import sys 
import pandas as pd
import time
import patent_service

technext_csv_file = "full_text_test_set.csv"

class DataProcessor:
	def __init__(self):
		self.patent_service = patent_service.PatentService()
		self.upload_size = 5000
		self.patent_text = "patent_text"
		self.patent_id = "patent_id"

	def map_data(self, batch, start_index, end_index):
		patent_documents = []

		for i in range(start_index, end_index):
			patent_id = batch[self.patent_id][i]
			patent_text = batch[self.patent_text][i]

			patent_doc = self.patent_service.make_patent_doc(patent_id, patent_text)
			patent_documents.append(patent_doc)

		return patent_documents

	def process_data(self):
		technext_data = pd.read_csv(technext_csv_file, dtype=str)
		data_size = technext_data.shape[0]


		for i in range(0, data_size, self.upload_size):
			start_index = i
			end_index = i + self.upload_size

			batch = technext_data.iloc[start_index:end_index]
			processed_batch = self.map_data(batch, start_index, end_index)

			self.patent_service.upload_batch(processed_batch)

			time.sleep(10)


if __name__ == "__main__":
	processor = DataProcessor()
	processor.process_data()

