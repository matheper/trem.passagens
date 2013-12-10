# -*- coding: utf-8 -*-

from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot

from trem.passagens.browser.forms import base
from trem.passagens.config import MessageFactory as _
from trem.passagens.config import session
from trem.passagens.interfaces import ILocal
from trem.passagens.tables import Local

class LocalAddForm(base.AddFormTP):
    """
        Formulário de cadastro de um Local.
    """

    grok.context(INavigationRoot)
    grok.name('add-local')
    grok.require('cmf.ManagePortal')
    
    schema = ILocal
    klass = Local
    label = _(u'Adicionar Local')
    description = _(u'Formulário de cadastro de um Local')

    def createAndAdd(self, data):
        p = Local(data['cidade'])
        session.add(p)
        session.flush()


class LocalEditForm(base.EditFormTP):
    """
        Formulário de edição de um Local.
    """

    grok.context(INavigationRoot)
    grok.name('edit-local')
    grok.require('cmf.ManagePortal')

    schema = ILocal
    klass = Local
    label = _(u'Editar Local')
    descrition = _(u'Formulário de edição de um Local.')


class LocalShowForm(base.ShowFormTP):
    """
        Formulário de visualização de um Local.
    """
    
    grok.context(INavigationRoot)
    grok.name('show-local')
    grok.require('cmf.ManagePortal')

    schema = ILocal
    klass = Local
    label = _(u'Detalhes do Local')
    description = _(u'Formulário de visualização de uma Local.')
