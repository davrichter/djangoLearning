def article_convert(article):
    article_modified = article.replace(",", "")
    article_modified = article_modified.replace(".", "")

    return article_modified
