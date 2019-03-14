from xml.etree import ElementTree
with open('text.opml', 'rt') as f:
    tree = ElementTree.parse(f)
print(tree)