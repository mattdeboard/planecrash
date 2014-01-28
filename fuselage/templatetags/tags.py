from django import template

register = template.Library()


def get_category_title(article_list):
    return article_list[0].category.title

register.simple_tag(get_category_title)
