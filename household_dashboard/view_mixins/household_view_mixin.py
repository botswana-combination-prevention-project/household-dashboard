from household.models import Household
from household.model_wrappers import HouseholdModelWrapper


class HouseholdViewMixin:

    household_model_wrapper_cls = HouseholdModelWrapper

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.household = None
        self.household_wrapped = None
        self.household_identifier = None

    def get_context_data(self, **kwargs):
        """Add household to the view instance.
        """
        context = super().get_context_data(**kwargs)
        self.household_identifier = kwargs.get('household_identifier')
        if self.household_identifier:
            self.household = Household.objects.get(
                household_identifier=self.household_identifier)
            self.household_wrapped = self.household_model_wrapper_cls(
                self.household)
        context.update(household=self.household_wrapped)
        return context
