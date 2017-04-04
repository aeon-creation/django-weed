from django.conf.urls import url
from djweed.views import get_file

urlpatterns = [
    url('^(?P<content_type_id>\d+)/(?P<object_id>[\w\-]+)/(?P<field_name>[\w\_]+)/(?P<file_name>[\w\.\_\-]*)$', get_file, name='weedfs_get_file'),
]
