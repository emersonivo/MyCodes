from xml.etree.ElementTree import XML
xml = XML.parse("sample.xml")

root = xml.getroot()
# def show_node(node):
#     print node.tag
#     if node.text is not None and node.text.strip():
#         print 'text: "%s"' % node.text
#     if node.tail is not None and node.tail.strip():
#         print 'tail: "%s"' % node.tail
#     for name, value in sorted(node.attrib.items()):
#         print ' %-4s = "%s"' % (name, value)
#     for child in node:
#         show_node(child)
#     return

# for elem in xml:
#     print elem
    #show_node(elem)

print root