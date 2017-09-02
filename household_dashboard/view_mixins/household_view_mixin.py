from django.apps import apps as django_apps

from ..model_wrappers import HouseholdModelWrapper


class HouseholdViewMixin:

    household_model = 'household.household'
    household_model_wrapper_cls = HouseholdModelWrapper

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.household = None
        self.household_wrapped = None
        self.household_identifier = None

    @property
    def household_model_cls(self):
        return django_apps.get_model(self.household_model)

    def get_context_data(self, **kwargs):
        """Add household to the view instance.
        """
        context = super().get_context_data(**kwargs)
        self.household_identifier = kwargs.get('household_identifier')
        if self.household_identifier:
            self.household = self.household_model_cls.objects.get(
                household_identifier=self.household_identifier)
            self.household_wrapped = self.household_model_wrapper_cls(
                self.household)
        context.update(household=self.household_wrapped)
        return context
