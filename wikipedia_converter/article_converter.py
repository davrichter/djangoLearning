def article_convert(article):
    article_modified = article.replace(",", "")
    article_modified = article_modified.replace(".", "")
    article_modified = article_modified.lower()

    return article_modified
"""
    x = 0
    while x + 100 < len(article):
        x += 100
        for i in range(0, 100):
            if article[i] == ".":
                article_modified = article_modified[:i] + "<br>" + article_modified[i:]
"""

