from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import patent_service

app = Flask(__name__)
origins_allowed = {"origins": "*"}
cors = CORS(app, resources={r"/*": origins_allowed})


class SearchPatents(Resource):
	def __init__(self):
		self.patent_service = patent_service.PatentService()

	def get(self):
		return {"technext api": "online"}

	def post(self):
		request_data = request.json

		if "query" in request_data:
			query_term = request_data["query"]
			search_results = self.patent_service.search_patents(query_term)

			return {"results": search_results}

		else:
			return {"message" : "invalid query"}

class HealthCheck(Resource):
	def get(self):
		return {"message" : "movies health check"}


api = Api()
api.add_resource(SearchPatents, '/patents')
api.add_resource(HealthCheck, '/healthcheck')

api.init_app(app)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080)

# import patent_service

# def handler(event, context):
# 	patent_service = patent_service.PatentService()
# 	if "query" in event:
# 		query_term = event["query"]
# 		search_results = patent_service.search_patents(query_term)

# 		return {"results": search_results}

# 	else:
# 		return {"message" : "invalid query"}
