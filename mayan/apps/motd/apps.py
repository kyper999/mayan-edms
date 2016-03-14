from __future__ import unicode_literals

import logging

from django import apps
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from common import MayanAppConfig, menu_object, menu_secondary, menu_setup
from navigation import SourceColumn

from .links import (
    link_message_create, link_message_delete, link_message_edit,
    link_message_list
)

logger = logging.getLogger(__name__)


class MOTDApp(MayanAppConfig):
    name = 'motd'
    test = True
    verbose_name = _('Message of the day')

    def ready(self):
        super(MOTDApp, self).ready()

        Message = self.get_model('Message')

        SourceColumn(
            source=Message, label=_('Enabled'), attribute='enabled'
        )
        SourceColumn(
            source=Message, label=_('Start date time'),
            func=lambda context: context['object'].start_datetime or _('None')
        )
        SourceColumn(
            source=Message, label=_('End date time'),
            func=lambda context: context['object'].end_datetime or _('None')
        )

        menu_object.bind_links(
            links=(
                link_message_edit, link_message_delete
            ), sources=(Message,)
        )
        menu_secondary.bind_links(
            links=(link_message_create,),
            sources=(Message, 'motd:message_list', 'motd:message_create')
        )
        menu_setup.bind_links(
            links=(link_message_list,)
        )