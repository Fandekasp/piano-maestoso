#from django
from django.conf.urls.defaults import *

# from pianostore
from models import Track

urlpatterns = patterns('',
        url(r'^$', 'pianostore.views.tracks', name="all_tracks"),
        url(r'^(\d+)/track/$', 'pianostore.views.track', name="describe_track"),
        url(r'^your_tracks/$', 'pianostore.views.your_tracks', name="your_tracks"),
        url(r'^user_tracks/(?P<username>\w+)/$', 'pianostore.views.user_tracks',
            name="user_tracks"),
        # CRUD urls
        url(r'^add/$', 'pianostore.views.add_track', name="add_track"),
        url(r'^(\d+)/update/$', 'pianostore.views.update_track',
            name="update_track"),
        url(r'^(\d+)/delete/$', 'pianostore.views.delete_track',
            name="delete_track"),
    )