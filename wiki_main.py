from workers.WikiWorker import WikiWorker

wikiWorker = WikiWorker()
symbol_list = []
for symbol in wikiWorker.get_sp_500_companies():
    symbol_list.append(symbol)
   
length = len(symbol_list)
print(length)
    
    