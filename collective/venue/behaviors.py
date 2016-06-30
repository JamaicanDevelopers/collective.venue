# -*- coding: utf-8 -*-
from collective.venue import messageFactory as _
from collective.venue.utils import get_base_path
from plone import api
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider
from zope.schema.interfaces import IContextAwareDefaultFactory


@provider(IContextAwareDefaultFactory)
def default_location(context):
    """Provide default location.
    """
    default = api.portal.get_registry_record('collective.venue.default_venue')
    return default or ''


@provider(IFormFieldProvider)
class ILocation(model.Schema):

    location_uid = schema.Choice(
        title=_(u'label_event_location', default=u'Location'),
        description=_(
            u'description_event_location',
            default=u'Select a location.'),
        required=False,
        missing_value='',
        defaultFactory=default_location,
        vocabulary='plone.app.vocabularies.Catalog',
    )
    form.widget(
        'location_uid',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['Venue'],
            'basePath': get_base_path
        }
    )

    location_notes = schema.Text(
        title=_(
            u'label_event_location_notes',
            default=u'Location notes'),
        description=_(
            u'description_event_location_notes',
            default=u'One-time location or additional Information.'),
        required=False,
        default=None,
    )

    location_url = schema.URI(
        title=_(
            u'label_event_location_url',
            default=u'location URL'),
        description=_(
            u'description_event_location_url',
            default=u'One-time location URL.'),
        required=False,
        default=None,
    )


@provider(IContextAwareDefaultFactory)
def default_organizer(context):
    """Provide default organizer.
    """
    default = api.portal.get_registry_record('collective.venue.default_organizer')  # noqa
    return default or ''


@provider(IFormFieldProvider)
class IOrganizer(model.Schema):

    organizer_uid = schema.Choice(
        title=_(u'label_event_organizer', default=u'Organizer'),
        description=_(
            u'description_event_organizer',
            default=u'Select an organizer.'),
        required=False,
        missing_value='',
        defaultFactory=default_organizer,
        vocabulary='plone.app.vocabularies.Catalog',
    )
    form.widget(
        'organizer_uid',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['Venue'],
            'basePath': get_base_path
        }
    )

    organizer_notes = schema.Text(
        title=_(
            u'label_event_organizer_notes',
            default=u'Organizer notes'),
        description=_(
            u'description_event_organizer_notes',
            default=u'One-time organizer or additional Information.'),
        required=False,
        default=None,
    )

    organizer_url = schema.URI(
        title=_(
            u'label_event_organizer_url',
            default=u'Organizer URL'),
        description=_(
            u'description_event_organizer_url',
            default=u'One-time organizer URL.'),
        required=False,
        default=None,
    )
