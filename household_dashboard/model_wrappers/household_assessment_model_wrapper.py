from django.apps import apps as django_apps

from edc_model_wrapper.wrappers import ModelWrapper


class HouseholdAssessmentModelWrapper(ModelWrapper):

    model = 'household.householdassessment'
    next_url_name = django_apps.get_app_config(
        'household_dashboard').listboard_url_name
    next_url_attrs = ['household_identifier', 'survey_schedule']
    querystring_attrs = ['household_structure']

    @property
    def household_structure(self):
        return self.object.household_structure.id

    @property
    def household_identifier(self):
        return self.object.household_structure.household.household_identifier

    @property
    def survey_schedule(self):
        return self.survey_schedule_object.field_value

    @property
    def survey_schedule_object(self):
        return self.object.household_structure.survey_schedule_object
