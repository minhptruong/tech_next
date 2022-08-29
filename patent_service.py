import os
from aws import cloud_search

class PatentService:
	def __init__(self):
		config_region = os.environ['config_region']
		patent_search_url = os.environ['patent_search']
		patent_document_url = os.environ['patent_document']
		cloudsearch_size = int(os.environ['patents_count'])

		self.cloud_search = cloud_search.CloudSearch(config_region, patent_search_url, patent_document_url, cloudsearch_size)
		self.patent_text = "patent_text"
		self.patent_id = "patent_id"
		self.random_size_default = 5
		

	def make_patent_doc(self, patent_id, patent_text):
		search_fields = {self.patent_text: patent_text}
		patent_doc = {"id": patent_id, "fields": search_fields, "type": "add"}

		return patent_doc

	def upload_batch(self, patent_documents):
		self.cloud_search.upload_documents(processed_batch)

	def search_patents(self, query):
		results = self.cloud_search.search_documents(query)

		results = list(map(lambda item: 
			{ self.patent_id: item["id"],
			self.patent_text: item["fields"]["patent_text"][0] }, results))

		return results

	def get_random_patents(self, count=None):
		# random_ints = []
		# for i in range(0, self.random_size_default):
		# 	new_id = random.randint(0, self.cloudsearch_size)
		# 	random_ints.append(new_id)

		results = self.cloud_search.fetch_random()
		return results




