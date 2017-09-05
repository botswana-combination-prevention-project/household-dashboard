from django.apps import apps as django_apps

from edc_model_wrapper import ModelWrapper


class HouseholdLogEntryModelWrapper(ModelWrapper):

    model = 'household.householdlogentry'
    next_url_name = django_apps.get_app_config(
        'household_dashboard').listboard_url_name
    next_url_attrs = ['household_identifier', 'survey_schedule']
    querystring_attrs = ['household_log']

    @property
    def household_log(self):
        return self.object.household_log

    @property
    def household_identifier(self):
        return self.household_log.household_structure.household.household_identifier

    @property
    def survey_schedule(self):
        return self.survey_schedule_object.field_value

    @property
    def survey_schedule_object(self):
        return self.object.household_log.household_structure.survey_schedule_object
