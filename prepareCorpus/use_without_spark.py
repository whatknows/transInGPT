# from comcrawl import IndexClient
# import pandas as pd
#
# client = IndexClient(["2019-51", "2019-47"])
# client.search("reddit.com/r/MachineLearning/*")
#
# client.results = (pd.DataFrame(client.results)
#                   .sort_values(by="timestamp")
#                   .drop_duplicates("urlkey", keep="last")
#                   .to_dict("records"))
#
# client.download()
#
# pd.DataFrame(client.results).to_csv("results.csv")
# import commoncrawl
#
# # Create a commoncrawl object
# cc = commoncrawl.CommonCrawl()
#
# # Search for pages that contain the keyword "python"
# results = cc.search("python")
#
# # Print the results
# for result in results:
#     print(result.url)

from newsplease import NewsPlease
article = NewsPlease.from_url('https://www.nytimes.com/2017/02/23/us/politics/cpac-stephen-bannon-reince-priebus.html?hp')
print(dir(article))
print(article.description)