from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print ("->",i[0],">",i[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in attrs:
            print ("->",i[0],">",i[1])

parser = MyHTMLParser()
n=int(input())

for i in range(n):
    s=input().strip()
    parser.feed(''.join(s))
