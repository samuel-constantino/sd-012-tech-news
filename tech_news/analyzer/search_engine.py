from ..database import search_news


# Requisito 6
def search_by_title(title):
    tech_news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    for tech_new in tech_news_list:
        result.append((tech_new["title"], tech_new["url"]))
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
