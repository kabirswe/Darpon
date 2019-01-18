""" Context processors for the darpon technology project """

import uuid

from django.core.exceptions import ObjectDoesNotExist
#
# from product.models import Category, SubCategory
# # from main.models import Text, SEO
#
#
# # Context processors
def darpon_processor(request):
    # try:
    #     seo_main = SEO.objects.get(id=1)
    # except ObjectDoesNotExist:
    #     seo_main = None
    # category_list = Category.objects.all()
    # sub_category_list = SubCategory.objects.all()
    context = {
        # 'seo_main': seo_main,
        # 'category_list': category_list,
        # 'sub_category_list': sub_category_list,
    }
    return context
