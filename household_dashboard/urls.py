from django.conf.urls import url

from edc_constants.constants import UUID_PATTERN

from household.patterns import household_identifier
from plot.patterns import plot_identifier
from survey.patterns import survey_schedule

from .views import ListboardView

app_name = 'household_dashboard'

urlpatterns = [
    url(r'^listboard/'
        '(?P<household_identifier>' + household_identifier + ')/'
        '(?P<survey_schedule>' + survey_schedule + ')/',
        ListboardView.as_view(), name='listboard_url'),
    url(r'^listboard/'
        '(?P<household_identifier>' + household_identifier + ')/',
        ListboardView.as_view(), name='listboard_url'),
    url(r'^listboard/'
        '(?P<plot_identifier>' + plot_identifier + ')/',
        ListboardView.as_view(), name='listboard_url'),
    url(r'^listboard/'
        '(?P<household_structure>' + UUID_PATTERN.pattern + ')/',
        ListboardView.as_view(), name='listboard_url'),
    url(r'^listboard/'
        '(?P<household>' + UUID_PATTERN.pattern + ')/',
        ListboardView.as_view(), name='listboard_url'),
    url(r'^listboard/'
        '(?P<page>\d+)/',
        ListboardView.as_view(), name='listboard_url'),
    url(r'^listboard/',
        ListboardView.as_view(), name='listboard_url'),
]
