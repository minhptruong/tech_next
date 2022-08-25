import boto3
import json

class CloudSearch:
	def __init__(self, search_endpoint, document_endpoint):
		self.cloud_search = boto3.client("cloudsearchdomain", endpoint_url=search_endpoint, region_name="us-east-1")
		self.cloud_document = boto3.client("cloudsearchdomain", endpoint_url=document_endpoint, region_name="us-east-1")

		self.search_size = 50

	def upload_documents(self, documents):
		res = self.cloud_document.upload_documents(documents=json.dumps(documents), contentType='application/json')
		return res

	def delete_documents(self, documents):
		res = self.cloud_document.upload_documents(documents=json.dumps(documents), contentType='application/json')
		return res

	def search_documents(self, search_term):
		results = self.cloud_search.search(query=search_term, size=self.search_size)

		if len(results["hits"]) > 0:
			return results["hits"]["hit"]
		else:
			return []

	def suggest_documents(self, search_term, search_suggester):
		results = self.cloud_search.suggest(query=search_term, suggester=search_suggester, size=self.size)
		return results