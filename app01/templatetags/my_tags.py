from django import template


register = template.Library()
@register.inclusion_tag('my_tags/headers.html')
def banner(menu_name):
    img_list = [
        "http://image.fengfengzhidao.com/gvb_1009/20231123092743__1123-h.png",
        "http://image.fengfengzhidao.com/gvb_1009/20231123092743__1123-i.png",
        "http://image.fengfengzhidao.com/gvb_1009/20231019173356__wallhaven-jxl31y.png",
        "http://image.fengfengzhidao.com/gvb_1009/20231019173356__wallhaven-57yr13.jpg",
        "http://image.fengfengzhidao.com/gvb_1009/20231123092743__1123-c.png",
    ]
    return locals()