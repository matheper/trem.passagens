# -*- coding: utf-8 -*-

from plone.directives import form
from zope import interface, schema
from trem.passagens.config import MessageFactory as _

# Formulários #

class ILocal(form.Schema):
    """ Interface que descreve representanção de Local.
    """
    cidade = schema.TextLine(
        title=_(u'Cidade'),
        )

class IViagem(form.Schema):
    """ Interface de representação de Viagem.
    """
    cidade_origem = schema.Choice(
        title=_(u'Cidade Origem'),
        description=_(u'Selecione a cidade origem.'),
        required=True,
        vocabulary='trem.passagens.local-vocab')


    cidade_destino = schema.Choice(
        title=_(u'Cidade Origem'),
        description=_(u'Selecione a cidade origem.'),
        required=True,
        vocabulary='trem.passagens.local-vocab')

    horario = schema.Time(
        title=_(u'Horário'),
        description=_(u'Selecione o horário de saída.'),
        required=True,
        )
