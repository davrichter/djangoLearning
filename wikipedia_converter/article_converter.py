import unicodedata


def article_convert(article):
    # article_modified = article.replace(",", "")
    # article_modified = article_modified.replace(".", "")
    # article_modified = article_modified.replace(";", "")
    article_modified = ""

    # remove commas, periods or semicolons only if they dont come after a number
    for i in range(len(article)):
        if (article[i] == "," or article[i] == "." or article[i] == ";") and i >= 1:
            if is_number(article[i - 1]):
                article_modified += article[i]

        else:
            article_modified += article[i]

    return article_modified


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
