inputText = input("Enter search text:- ")
searchText = inputText.strip()
newText = searchText.replace(" ", "%20").lower()
SEARCHURL = 'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords='+newText+'origin=FACETED_SEARCH'
print(SEARCHURL)
print('https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=medical%20billing%20owner&origin=FACETED_SEARCH')