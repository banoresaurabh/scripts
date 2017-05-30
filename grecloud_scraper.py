import json
import requests
from bs4 import BeautifulSoup

global fh
s = requests.session()

def give_me_json_list(json_string):
	json_object_list = list(json.loads(json_string))
	return json_object_list

def initiate_file_opr():
	global fh
	fh = open("barrons_wordlist.txt","w")
	fh.write("Barron's high frequency 333\n\n\n")

def fill_the_file(json_object_list):
	global fh
	for job in json_object_list:
		fh.write(str(job["word_id"])+"\t")
		fh.write(job["word_name"]+"\n\t")
		fh.write("--> "+job["word_meaning"]+"\n\t")
		fh.write("--> "+job["word_mnemonic"]+"\n\n\n")
	print("------------------------------------------------------")

def catch_response(base_url):
	try:
			initiate_file_opr()
			for box in range(1,15):
				url = base_url + str(box)
				print(url)
				page = s.get(url)
				json_response = page.text
				json_object_list = give_me_json_list(json_response)
				fill_the_file(json_object_list)
			fh.close()
			print("Done!!!!")				

	except Exception as e:
		print("Network error!! try again!!")
	

catch_response("http://www.grecloud.com/services/get_words.php?box_set=1&box_id=")	

