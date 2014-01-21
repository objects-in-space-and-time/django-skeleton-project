
from django.conf import settings
from django.conf.urls.defaults import patterns, url, include

# __APP_NAME__ URLs
app_patterns = patterns('',

    url(r'^item/(?P<pk>[\w\-]+)/$',
        '__APP_LABEL__.views.item', name="item"),
    
    url(r'^item-property/(?P<pk>[\w\-]+)/(?P<prop_name>[\w\-\_]+)/$',
        '__APP_LABEL__.views.item_property', name="item_property"),

)

# __APP_NAME__ URL namespace
urlpatterns = patterns('',

    url(r'^/', include(app_patterns,
        namespace='__APP_LABEL__', app_name='__APP_LABEL__')),

)

