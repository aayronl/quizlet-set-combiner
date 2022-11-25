from bs4 import BeautifulSoup
import requests

URL_LIST = [
	# URLs must be in the "https://quizlet.com/<set id>/<set name>/" format
]

def fetch_set(URL):
	headers = {'User-Agent': 'Mozilla/5.0'}
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.text, 'html.parser')
	terms = soup.findAll('div', {'class': 'SetPageTerm-content'})

	for i in terms:
		term = i.find('a', {'class': 'SetPageTerm-wordText'})
		definition = i.find('a', {'class': 'SetPageTerm-definitionText'})

		card = (term.text, definition.text)
		term_list.append(card)

	return

if __name__ == "__main__":
	term_list = []
	for url in URL_LIST:
		fetch_set(url)

	# Write to file
	f = open('terms.txt', 'w')
	for i in term_list:
		# Formatted for quizlet
		f.write(i[0] + '\t' + i[1] + '\n')