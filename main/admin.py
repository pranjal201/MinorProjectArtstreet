from django.contrib import admin
from .models import UserDetail, Slider, Contact, Cart
from saler.models import Product, ProductSize, SalerDetail, category,   Orders, trend,ProductReview

admin.site.site_header = 'Artstreet'

admin.site.register(UserDetail)
admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(SalerDetail)
admin.site.register(Slider)
admin.site.register(category)
admin.site.register(Contact)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(trend)
admin.site.register(ProductReview)
