import re
content = '<dd> <i class="board-index board-index-1">1</i>'
# pattern = re.compile('',re.S)
content = re.match('<dd>.*?board-index.*?>(\d+)</i>',content)
print(content)
print(content.group())
print(content.group(0))
print(content.group(1))
