def article_convert(article):
    article_modified = article.replace(",", "")
    article_modified = article_modified.replace(".", "")
    article_modified = article_modified.lower()

    return article_modified
