"""urls file."""

from django.conf.urls import *
from geodata.models import *
from geodata import views
from geodata import feeds
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Q


urlpatterns = patterns(
    '',
    url(r'^feeds/patrimony/$', feeds.PatrimonyFeed(), name="feed_patrimony"),
    url(r'^feeds/construction/$', feeds.ConstructionFeed(),
        name="feed_construction"),
    url(r'^feeds/meeting/$', feeds.MeetingFeed(), name="feed_meeting"),
    url(r'^feeds/actor/$', feeds.ActorFeed(), name="feed_actor"),
    url(r'^patrimony/(?P<pk>\d+)/geojson/$',
        views.GeoJSONPatrimonyDetailView.as_view(),
        name="geojson_patrimony_detail"),
    url(r'^construction/(?P<pk>\d+)/geojson/$',
        views.GeoJSONConstructionDetailView.as_view(),
        name="geojson_construction_detail"),
    url(r'^meeting/(?P<pk>\d+)/geojson/$',
        views.GeoJSONMeetingDetailView.as_view(),
        name="geojson_meeting_detail"),
    url(r'^actor/(?P<pk>\d+)/geojson/$',
        views.GeoJSONActorDetailView.as_view(),
        name="geojson_actor_detail"),
    url(r'^patrimony/all/geojson/$', views.GeoJSONPatrimonyListView.as_view(),
        name="geojson_patrimony_list"),
    url(r'^patrimony/contemporary/geojson/$',
        views.GeoJSONPatrimonyListView.as_view(
            queryset=EarthGeoDataPatrimony.objects.filter(
                inauguration_date__gte=now() - timedelta(days=3650)))),
    url(r'^patrimony/unesco/geojson/$',
        views.GeoJSONPatrimonyListView.as_view(
            queryset=EarthGeoDataPatrimony.objects.filter(unesco=True))),
    url(r'^patrimony/vernacular/geojson/$',
        views.GeoJSONPatrimonyListView.as_view(
            queryset=EarthGeoDataPatrimony.objects.filter(architects=''))),
    url(r'^patrimony/normal/geojson/$',
        views.GeoJSONPatrimonyListView.as_view(
            queryset=EarthGeoDataPatrimony.objects.exclude(architects='').filter(
                Q(unesco=False) &
                (Q(inauguration_date__isnull=True) |
                 ~Q(inauguration_date__gte=now() - timedelta(days=3650)))))),
    url(r'^construction/all/geojson/$',
        views.GeoJSONConstructionListView.as_view(),
        name="geojson_construction_list"),
    url(r'^construction/participative/geojson/$',
        views.GeoJSONConstructionListView.as_view(
            queryset=EarthGeoDataConstruction.objects.filter(
                participative=True))),
    url(r'^construction/normal/geojson/$',
        views.GeoJSONConstructionListView.as_view(
            queryset=EarthGeoDataConstruction.objects.filter(
                participative=False))),
    url(r'^meeting/all/geojson/$', views.GeoJSONMeetingListView.as_view(),
        name="geojson_meeting_list"),
    url(r'^meeting/seminar/geojson/$',
        views.GeoJSONMeetingListView.as_view(
            queryset=EarthGeoDataMeeting.objects.filter(
                meeting_type__ident_name__icontains='seminar'))),
    url(r'^meeting/colloquium/geojson/$',
        views.GeoJSONMeetingListView.as_view(
            queryset=EarthGeoDataMeeting.objects.filter(
                meeting_type__ident_name__icontains='colloquium'))),
    url(r'^meeting/conference/geojson/$',
        views.GeoJSONMeetingListView.as_view(
            queryset=EarthGeoDataMeeting.objects.filter(
                meeting_type__ident_name__icontains='conference'))),
    url(r'^meeting/festival/geojson/$',
        views.GeoJSONMeetingListView.as_view(
            queryset=EarthGeoDataMeeting.objects.filter(
                meeting_type__ident_name__icontains='festival'))),
    url(r'^actor/all/geojson/$', views.GeoJSONActorListView.as_view(),
        name="geojson_actor_list"),
    url(r'^patrimony/all/$', views.PatrimonyListView.as_view(),
        name="show_patrimony_all"),
    url(r'^patrimony/contemporary/$',
        views.PatrimonyListView.as_view(
            queryset=EarthGeoDataPatrimony.objects.filter(
                inauguration_date__gte=now() - timedelta(days=3650))),
        name="show_patrimony_contemporary"),
    url(r'^patrimony/unesco/$',
        views.PatrimonyListView.as_view(
            queryset=EarthGeoDataPatrimony.objects.filter(unesco=True)),
        name="show_patrimony_unesco"),
    url(r'^patrimony/vernacular/$',
        views.PatrimonyListView.as_view(
            queryset=EarthGeoDataPatrimony.objects.filter(architects='')),
        name="show_patrimony_vernacular"),
    url(r'^patrimony/normal/$',
        views.PatrimonyListView.as_view(
            queryset=EarthGeoDataPatrimony.objects.exclude(architects='').filter(
                Q(unesco=False) &
                (Q(inauguration_date__isnull=True) |
                 ~Q(inauguration_date__gte=now() - timedelta(days=3650))))),
        name="show_patrimony_normal"),
    url(r'^patrimony/(?P<pk>\d+)/$', views.PatrimonyDetailView.as_view(),
        name="show_patrimony"),
    url(r'^construction/all/$', views.ConstructionListView.as_view(),
        name="show_construction_all"),
    url(r'^construction/participative/$',
        views.ConstructionListView.as_view(
            queryset=EarthGeoDataConstruction.objects.filter(
                participative=True)),
        name="show_construction_participative"),
    url(r'^construction/normal/$',
        views.ConstructionListView.as_view(
            queryset=EarthGeoDataConstruction.objects.filter(
                participative=False)),
        name="show_construction_normal"),
    url(r'^construction/(?P<pk>\d+)/$', views.ConstructionDetailView.as_view(),
        name="show_construction"),
    url(r'^meeting/all/$', views.MeetingListView.as_view(),
        name="show_meeting_all"),
    url(r'^meeting/seminar/$',
        views.MeetingListView.as_view(
            queryset=EarthGeoDataMeeting.objects.filter(
                meeting_type__ident_name__icontains='seminar')),
        name="show_meeting_seminar"),
    url(r'^meeting/colloquium/$',
        views.MeetingListView.as_view(
            queryset=EarthGeoDataMeeting.objects.filter(
                meeting_type__ident_name__icontains='colloquium')),
        name="show_meeting_colloquium"),
    url(r'^meeting/conference/$',
        views.MeetingListView.as_view(
            queryset=EarthGeoDataMeeting.objects.filter(
                meeting_type__ident_name__icontains='conference')),
        name="show_meeting_conference"),
    url(r'^meeting/festival/$',
        views.MeetingListView.as_view(
            queryset=EarthGeoDataMeeting.objects.filter(
                meeting_type__ident_name__icontains='festival')),
        name="show_meeting_festival"),
    url(r'^meeting/(?P<pk>\d+)/$', views.MeetingDetailView.as_view(),
        name="show_meeting"),
    url(r'^actor/all/$', views.ActorListView.as_view(),
        name="show_actor_all"),
    url(r'^actor/(?P<pk>\d+)/$', views.ActorDetailView.as_view(),
        name="show_actor"),
    url(r'^patrimony/(?P<pk>\d+)/edit/$', views.PatrimonyUpdateView.as_view(),
        name="edit_patrimony"),
    url(r'^construction/(?P<pk>\d+)/edit/$',
        views.ConstructionUpdateView.as_view(), name="edit_construction"),
    url(r'^meeting/(?P<pk>\d+)/edit/$', views.MeetingUpdateView.as_view(),
        name="edit_meeting"),
    url(r'^actor/(?P<pk>\d+)/edit/$', views.ActorUpdateView.as_view(),
        name="edit_actor"),
    url(r'^patrimony/(?P<pk>\d+)/delete/$',
        views.PatrimonyDeleteView.as_view(), name="delete_patrimony"),
    url(r'^construction/(?P<pk>\d+)/delete/$',
        views.ConstructionDeleteView.as_view(), name="delete_construction"),
    url(r'^meeting/(?P<pk>\d+)/delete/$', views.MeetingDeleteView.as_view(),
        name="delete_meeting"),
    url(r'^actor/(?P<pk>\d+)/delete/$', views.ActorDeleteView.as_view(),
        name="delete_actor"),
    url(r'^patrimony/add/$', views.PatrimonyCreateView.as_view(),
        name="add_patrimony"),
    url(r'^construction/add/$', views.ConstructionCreateView.as_view(),
        name="add_construction"),
    url(r'^meeting/add/$', views.MeetingCreateView.as_view(),
        name="add_meeting"),
    url(r'^actor/add/$', views.ActorCreateView.as_view(), name="add_actor"),
    url(r'^patrimony/(?P<pk>\d+)/rec/$',
        views.ToggleRecommendationPatrimonyView.as_view(),
        name="toggle_rec_patrimony"),
    url(r'^construction/(?P<pk>\d+)/rec/$',
        views.ToggleRecommendationConstructionView.as_view(),
        name="toggle_rec_construction"),
    url(r'^meeting/(?P<pk>\d+)/rec/$',
        views.ToggleRecommendationMeetingView.as_view(),
        name="toggle_rec_meeting"),
    url(r'^actor/(?P<pk>\d+)/rec/$',
        views.ToggleRecommendationActorView.as_view(),
        name="toggle_rec_actor"),
    url(r'^all/$', views.BigMapView.as_view(),
        name="show_bigmap"),
)
