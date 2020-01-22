from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def carousel(value_list):
    """
    Returned good carousel template
    """
    carousel_head = '<div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel">'

    li_list = """
    <ol class="carousel-indicators">
    """
    for item in value_list:
        print(item)
        item_li = f'<li data-target="#carouselExampleCaptions" data-slide-to="{item.id}" class="active"></li>'
        li_list += item_li
    li_list += """
    </ol>
    """

    item_list = '<div class="carousel-inner">'
    for item in value_list:
        item_list += '<div class="carousel-item active">'
        item_list += f'<img src="/media/{item.good.photo}" class="d-block w-100" alt="{item.title}">'
        item_list += '<div class="carousel-caption d-none d-md-block">'
        item_list += f'<h5>{item.title}</h5>'
        item_list += f'<p>{item.desc}</p>'
        item_list += '</div></div>'
    item_list += '</div>'

    carousel_foot = """
        <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
            <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
    </div>
    """
    result = carousel_head + li_list + item_list + carousel_foot
    return mark_safe(result)
