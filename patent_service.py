import os
from aws import cloud_search, aws_utils

class PatentService:
	def __init__(self):

		config_region = os.environ['config_region']
		patent_search_url = os.environ['patent_search']
		patent_document_url = os.environ['patent_document']

		self.cloud_search = cloud_search.CloudSearch(config_region, patent_search_url, patent_document_url)
		self.patent_text = "patent_text"
		self.patent_id = "patent_id"

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
