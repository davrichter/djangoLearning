import unicodedata

from tld import is_tld


def article_convert(article):
    """
    remove periods, commas or semicolons if they are used as punctuation otherwise
    for example when they are used in domains don't remove them
    """
    # article_modified = article.replace(",", "")
    # article_modified = article_modified.replace(".", "")
    # article_modified = article_modified.replace(";", "")
    article_modified = ""

    for i in range(len(article) - 1):
        if (article[i] == "," or article[i] == ".") and i >= 1:
            try:
                # add it if the comma, period or semicolon is between two numbers
                if is_number(article[i - 1]) and is_number(article[i + 1]):
                    article_modified += article[i]

                # add it if the comma or period is in front of a top level domain
                elif is_tld(article[i + 1:i + 2]) or \
                        is_tld(article[i + 1:i + 3]) or \
                        is_tld(article[i + 1:i + 4]):
                    article_modified += article[i]

                # add it if the comma or period comes after a "www"
                elif article[i - 1:i - 4:-1] == "www":
                    article_modified += article[i]

            except ValueError as e:
                print(e)

        elif article[i] == ";":
            pass

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
