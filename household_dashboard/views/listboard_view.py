from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_dashboard.views import ListboardView as BaseListboardView
from edc_dashboard.view_mixins import ListboardFilterViewMixin

from plot_dashboard.view_mixins import PlotQuerysetViewMixin

from survey import SurveyViewMixin, SurveyQuerysetViewMixin

from household_dashboard.view_mixins import HouseholdQuerysetViewMixin
from household.model_wrappers import (
    HouseholdStructureWithLogEntryWrapper)
from .listboard_filters import HouseholdListboardViewFilters


class ListboardView(SurveyViewMixin, EdcBaseViewMixin, AppConfigViewMixin,
                    ListboardFilterViewMixin, HouseholdQuerysetViewMixin,
                    PlotQuerysetViewMixin, SurveyQuerysetViewMixin, BaseListboardView):

    app_config_name = 'household_dashboard'
    navbar_item_selected = 'household_dashboard'
    model = 'household.householdstructure'
    model_wrapper_class = HouseholdStructureWithLogEntryWrapper
    listboard_view_filters = HouseholdListboardViewFilters()

    plot_queryset_lookups = ['household', 'plot']
    household_queryset_lookups = ['household']
    survey_queryset_lookups = []

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
