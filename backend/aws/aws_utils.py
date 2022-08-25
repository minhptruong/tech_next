import boto3

config_region = "us-east-1"
def aws_credentials():
	return boto3.Session().get_credentials()

#cloud_search
patent_search = "http://search-technext-text-iupnbg2xczjdy5pypdvbr545zu.us-east-1.cloudsearch.amazonaws.com"
patent_document = "http://doc-technext-text-iupnbg2xczjdy5pypdvbr545zu.us-east-1.cloudsearch.amazonaws.com"

