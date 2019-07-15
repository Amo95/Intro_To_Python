from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
<title>Hello World</title>
</head>
<body>
<p class= 'james'>I love Python</p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print (soup.title)
print (soup.title.name)
print (soup.title.string)
print (soup.title.parent.name)
print (soup.p)
print (soup.p['james'])
