import sys
import fileinput

def find_req_citations(articles, impact):
    return (articles * (impact - 1)) + 1

for line in fileinput.input():
    line = line.strip()
    list = line.split()
    article_count = int(list[0])
    desired_impact = int(list[1])
    print(find_req_citations(article_count, desired_impact))

