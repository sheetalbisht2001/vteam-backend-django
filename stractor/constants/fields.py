import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from jsonschema import validate, exceptions as jsonschema_exceptions
from django.core import exceptions
from django.contrib.postgres.fields import JSONField
import os
import json
import inspect

class UuidPKField(models.UUIDField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', 'id')
        kwargs.setdefault('verbose_name', _('Id'))
        kwargs.setdefault('primary_key', True)
        kwargs.setdefault('default', uuid.uuid4)
        kwargs.setdefault('editable', False)
        super().__init__(*args, **kwargs)


class TitleField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', 'title')
        kwargs.setdefault('verbose_name', _('Title'))
        kwargs.setdefault('max_length', 128)
        super().__init__(*args, **kwargs)


class DescriptionField(models.TextField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', 'description')
        kwargs.setdefault('verbose_name', _('Description'))
        super().__init__(*args, **kwargs)


class IsDisabledField(models.BooleanField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', 'is_disabled')
        kwargs.setdefault('verbose_name', _('Is Disabled'))
        kwargs.setdefault('default', False)
        super().__init__(*args, **kwargs)


class DisabledAtField(models.DateTimeField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', 'disabled_at')
        kwargs.setdefault('verbose_name', _('Disabled At'))
        kwargs.setdefault('null', True)
        kwargs.setdefault('blank', True)
        super().__init__(*args, **kwargs)


class IsActiveField(models.BooleanField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', 'is_active')
        kwargs.setdefault('verbose_name', _('Is Active'))
        kwargs.setdefault('default', True)
        super().__init__(*args, **kwargs)


class IsSoftDeletedField(models.BooleanField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', 'is_soft_deleted')
        kwargs.setdefault('verbose_name', _('Is Soft Deleted'))
        kwargs.setdefault('default', False)
        super().__init__(*args, **kwargs)


class SoftDeletedAtField(models.DateTimeField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', 'soft_deleted_at')
        kwargs.setdefault('verbose_name', _('Soft Deleted At'))
        kwargs.setdefault('null', True)
        kwargs.setdefault('blank', True)
        super().__init__(*args, **kwargs)


class CreatedAtField(models.DateTimeField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', 'created_at')
        kwargs.setdefault('verbose_name', _('Created At'))
        kwargs.setdefault('auto_now_add', True)
        super().__init__(*args, **kwargs)


class UpdatedAtField(models.DateTimeField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', 'updated_at')
        kwargs.setdefault('verbose_name', _('Updated At'))
        kwargs.setdefault('auto_now', True)
        super().__init__(*args, **kwargs)


class DisplayIdField(models.IntegerField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', 'display_id')
        kwargs.setdefault('verbose_name', _('Display Id'))
        kwargs.setdefault('unique', True)
        kwargs.setdefault('editable', True)
        super().__init__(*args, **kwargs)


class DisplayTitleField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', 'display_title')
        kwargs.setdefault('verbose_name', _('Display Title'))
        kwargs.setdefault('max_length', 128)
        kwargs.setdefault('editable', True)
        super().__init__(*args, **kwargs)


class DisplayIdField(models.IntegerField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('name', 'display_id')
        kwargs.setdefault('verbose_name', _('Display Id'))
        kwargs.setdefault('unique', False)
        kwargs.setdefault('editable', True)
        super().__init__(*args, **kwargs)


class JSONSchemaField(JSONField):

    def __init__(self, *args, **kwargs):
        self.schema = kwargs.pop('schema', None)
        super().__init__(*args, **kwargs)

    @property
    def _schema_data(self):
        model_file = inspect.getfile(self.model)
        dirname = os.path.dirname(model_file)
        # schema file related to model.py path
        p = os.path.join(dirname, self.schema)
        with open(p, 'r') as file:
            return json.loads(file.read())

    def _validate_schema(self, value):
        # Disable validation when migrations are faked
        if self.model.__module__ == '__fake__':
            return True
        try:
            status = validate(value, self._schema_data)
        except jsonschema_exceptions.ValidationError as e:
            raise exceptions.ValidationError(e.message, code='invalid')
        return status

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        self._validate_schema(value)

    def pre_save(self, model_instance, add):
        value = super().pre_save(model_instance, add)
        if value and not self.null:
            self._validate_schema(value)
        return value
