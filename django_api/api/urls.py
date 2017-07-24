from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import RoomCreateView, RoomDetailsView, JudgeCreateView, JudgeDetailsView, TeamCreateView, TeamDetailsView,\
    SortedRoomCreateView, SortedRoomDetailsView, MemberCreateView, MemberDetailsView, SignUpPreferenceCreateView, \
    SignUpPreferenceDetailsView, VPIPreferenceCreateView, VPIPreferenceDetailsView

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rooms/$', RoomCreateView.as_view(), name="create"),
    url(r'^rooms/(?P<pk>[0-9]+)/$', RoomDetailsView.as_view(), name="details"),
    url(r'^judges/$', JudgeCreateView.as_view(), name="create"),
    url(r'^judges/(?P<pk>[0-9]+)/$', JudgeDetailsView.as_view(), name="details"),
    url(r'^teams/$', TeamCreateView.as_view(), name="create"),
    url(r'^teams/(?P<pk>[0-9]+)/$', TeamDetailsView.as_view(), name="details"),
    url(r'^sorted_rooms/$', SortedRoomCreateView.as_view(), name="create"),
    url(r'^sorted_rooms/(?P<pk>[0-9]+)/$', SortedRoomDetailsView.as_view(), name="details"),
    url(r'^sign_up_preferences/$', SignUpPreferenceCreateView.as_view(), name="create"),
    url(r'^sign_up_preferences/(?P<pk>[0-9]+)/$', SignUpPreferenceDetailsView.as_view(), name="details"),
    url(r'^vpi_preferences/$', VPIPreferenceCreateView.as_view(), name="create"),
    url(r'^vpi_preferences/(?P<pk>[0-9]+)/$', VPIPreferenceDetailsView.as_view(), name="details"),
    url(r'^members/$', MemberCreateView.as_view(), name="create"),
    url(r'^members/(?P<pk>[0-9]+)/$', MemberDetailsView.as_view(), name="details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
