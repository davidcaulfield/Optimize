# import requests
# import json
# from config import _token


# # params = dict(
# # 	IdentifierType="Symbol",
# # 	Identifiers="MSFT",
# # 	FundamentalTypes=["MarketCapitalization","BookValue","CEO"],
# # 	UpdatedSince="12/01/2016",
# # 	_fields=["Company.Symbol",
# # 	"Company.Sector",
# # 	"Company.Industry",
# # 	"FundamentalsSets.Fundamentals.Type",
# # 	"FundamentalsSets.Fundamentals.Value"],
# # 	_token=_token

# # )

# base = "http://factsetfundamentals.xignite.com/xFactSetFundamentals.json/GetLatestFundamentals"

# def end_of_day_quote(base, params):
# 		response = requests.get(base, params=params)
# 		# with requests.Session() as s:
# 		# 	download = s.get(base, params=params)
# 		# 	decoded_content = download.content.decode('utf-8')
# 		# 	# cr = csv.reader(decoded_content.splitlines(), delimiter=',')
# 		# 	# my_list = list(cr)
# 		# 	# for row in my_list:
# 		return response.json()


# # a = end_of_day_quote(base, params)
# # b = a[0]['FundamentalsSets']
# # c =a[0]['FundamentalsSets'][0]['Fundamentals']


# params = dict(
# 	IdentifierType="Symbol",
# 	Identifiers="MSFT",
# 	FundamentalTypes=[
# 	"CompanyName",
# 	"GeneralIndustryClassification",
# 	"MarketCapitalization",
# 	"PERatio",
# 	"Beta12Month",
# 	"DividendYieldDaily",
# 	"HighPriceLast52Weeks",
# 	"LowPriceLast52Weeks",
# 	"50DayMovingAverage",
# 	"200DayMovingAverage",
# 	"PercentPriceChange13Weeks",
# 	"PercentPriceChange26Weeks",
# 	"PercentPriceChange52Weeks"
# 	],
# 	UpdatedSince="01/01/2017",
# 	_fields=[
# 	"FundamentalsSets.Fundamentals.Type",
# 	"FundamentalsSets.Fundamentals.Value"
# 	],
# 	_token=_token
)







