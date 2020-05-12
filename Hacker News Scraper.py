import requests, pprint
from bs4 import BeautifulSoup

page = 1
megasub, megalinks = [], []

while page<=15: #This value shows how many pages the data is gotten from.
	res = requests.get(f"https://news.ycombinator.com/news?p={page}")
	soup = BeautifulSoup(res.text, 'html.parser')
	links = soup.select('.storylink')
	subtext = soup.select('.subtext')
	megasub += subtext
	megalinks += links
	page = page + 1
else:
	print("The data's been collected:")

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key = lambda k:k["votes"], reverse = True)

def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[idx].select(".score")
		if len(vote):
			points = int(vote[0].getText().replace(' points',""))
			if points > 250: # You can change this value depending on how many minimal votes do you want an article to have
				hn.append({'title': title,'link':href, "votes": points})
	return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(megalinks, megasub))

