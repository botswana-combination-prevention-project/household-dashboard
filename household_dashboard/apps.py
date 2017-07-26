from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'household_dashboard'
    listboard_template_name = 'household_dashboard/listboard.html'
    listboard_url_name = 'household_dashboard:listboard_url'
    base_template_name = 'edc_base/base.html'
    url_namespace = 'household_dashboard'
    admin_site_name = 'household_admin'
