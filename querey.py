
import sys

from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir


q = input("Please enter search term: ")

ix = open_dir("indexdir")
with ix.searcher(weighting=scoring.Frequency) as searcher:
    queryParser = QueryParser("description",ix.schema)
    query = queryParser.parse(q) #Search terms go inside here
    results = searcher.search(query, limit=10)
    print(results)
    print("#############################")
    for i in results:
        print("------------------------------")
        print(i)
        print("------------------------------")
    #print(results[0]['title'])
    #print(results)


