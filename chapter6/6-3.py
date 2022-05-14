glossary = {}
glossary["title"] = "字首大寫"
glossary["upper"] = "全部大寫"
glossary["lower"] = "全部小寫"
glossary["replace"] = "替換"
glossary["len"] = "字串長度"
print(glossary)

glossary = {
    'title': '字首大寫',
    'upper': '全部大寫',
    'lower': '全部小寫',
    'replace': '替換',
    'len': '字串長度',
    }
print(glossary)
for x in glossary:
    print(x+"\n\t"+glossary[x])