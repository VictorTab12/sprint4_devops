from serpapi import GoogleSearch

params = {
  "engine": "google_shopping",
  "q": "Macbook M3",
  "api_key": "2f2afff318fb54275b1c90320748f68c46177611d91b99c226a4101debd44cd0"
}

search = GoogleSearch(params)
results = search.get_dict()
shopping_results = results["shopping_results"]