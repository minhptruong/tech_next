import boto3
import json
import random 

class CloudSearch:
	def __init__(self, region, search_endpoint, document_endpoint, cloudsearch_size):
		self.cloud_search = boto3.client("cloudsearchdomain", endpoint_url=search_endpoint, region_name=region)
		self.cloud_document = boto3.client("cloudsearchdomain", endpoint_url=document_endpoint, region_name=region)
		self.cloudsearch_size = cloudsearch_size
		self.random_size_default = 5
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

	def fetch_random(self):
		start_id = random.randint(0, self.cloudsearch_size-self.random_size_default + 1)
		results = self.cloud_search.search(query="matchall",queryParser='structured', start=start_id, size=self.random_size_default)

		if len(results["hits"]) > 0:
			return results["hits"]["hit"]
		else:
			return []
