
import requests
import json

#ensure config has the write permissions
from config import _token


params = dict(
	IdentifierType="Symbol",
	Identifiers="MSFT",
	FundamentalTypes=["MarketCapitalization","BookValue","CEO"],
	UpdatedSince="12/01/2016",
	_fields=["Company.Symbol",
	"Company.Sector",
	"Company.Industry",
	"FundamentalsSets.Fundamentals.Type",
	"FundamentalsSets.Fundamentals.Value"],
	_token=_token

)


base = "http://factsetfundamentals.xignite.com/xFactSetFundamentals.json/GetLatestFundamentals"

def end_of_day_quote(base, params):
		response = requests.get(base, params=params)
		# with requests.Session() as s:
		# 	download = s.get(base, params=params)
		# 	decoded_content = download.content.decode('utf-8')
		# 	# cr = csv.reader(decoded_content.splitlines(), delimiter=',')
		# 	# my_list = list(cr)
		# 	# for row in my_list:
		# 	# 	print(row)
		# for i in response.json():
		# 	print(i['Company'], '''


		# 		''',i['FundamentalsSets'],'''



		# 		''')
		return response.json()

a = end_of_day_quote(base, params)
# print(a[0]['Company'])

b = a[0]['FundamentalsSets']
# print(b)

c =a[0]['FundamentalsSets'][0]['Fundamentals']
print(c)
for i in c:
	print(i['Type'], i['Value'])




