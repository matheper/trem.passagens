# -*- coding: utf-8 -*-

from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot

from trem.passagens.browser.forms import base
from trem.passagens.config import MessageFactory as _
from trem.passagens.config import session
from trem.passagens.interfaces import IViagem
from trem.passagens.tables import Viagem

class ViagemAddForm(base.AddFormTP):
    """
        Formulário de cadastro de uma Viagem.
    """

    grok.context(INavigationRoot)
    grok.name('add-viagem')
    grok.require('cmf.ManagePortal')
    
    schema = IViagem
    klass = Viagem
    label = _(u'Adicionar Viagem')
    description = _(u'Formulário de cadastro de uma Viagem')

    def createAndAdd(self, data):
        v = Viagem(data['cidade_origem'], data['cidade_destino'], data['horario'])
        session.add(v)
        session.flush()


class ViagemEditForm(base.EditFormTP):
    """
        Formulário de edição de uma Viagem.
    """

    grok.context(INavigationRoot)
    grok.name('edit-viagem')
    grok.require('cmf.ManagePortal')

    schema = IViagem
    klass = Viagem
    label = _(u'Editar Viagem')
    descrition = _(u'Formulário de edição de uma Viagem.')


class ViagemShowForm(base.ShowFormTP):
    """
        Formulário de visualização de uma Viagem.
    """
    
    grok.context(INavigationRoot)
    grok.name('show-viagem')
    grok.require('cmf.ManagePortal')

    schema = IViagem
    klass = Viagem
    label = _(u'Detalhes do Viagem')
    description = _(u'Formulário de visualização de uma Viagem.')

    def getContent(self):
        return session.query(self.klass).get(self.rec_id('origem'))

    def rec_id(self):
        return self.request.get('id', self.request.get('form.widgets.id', None))
