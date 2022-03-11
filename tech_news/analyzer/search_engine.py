import datetime
import re
from ..database import search_news


def format_tech_news_list(tech_news_list):
    formated_list = []
    for tech_new in tech_news_list:
        formated_list.append((tech_new["title"], tech_new["url"]))
    return formated_list


# Requisito 6
def search_by_title(title):
    tech_news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    return format_tech_news_list(tech_news_list)


# Requisito 7
def search_by_date(date):
    splitted_date = date.split("-")
    try:
        datetime.datetime(
            year=int(splitted_date[0]),
            month=int(splitted_date[1]),
            day=int(splitted_date[2])
        )

        # Por que essa solução não funciona?
        # if re.search(r'[\d]{4}-[\d]{2}-[\d]{2}', date) is None:
        #     raise ValueError("Data inválida")
    except ValueError:
        raise ValueError("Data inválida")

    date_regex = re.compile(f"^{date}")
    tech_news_list = search_news({"timestamp": date_regex})
    return format_tech_news_list(tech_news_list)


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
