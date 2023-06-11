import requests
res_parse_list=[]

response=requests.get("https://ukrsibbank.com/currency-cash/")
response_text=response.text
response_parse=response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("USD"):
        for parse_elem_2 in parse_elem_1.split("<span>"):
            if parse_elem_2.startswith("USD") and parse_elem_2[10].isdigit():
                res_parse_list.append(parse_elem_2)

BNB_rate=res_parse_list=[]
print(BNB_rate)
