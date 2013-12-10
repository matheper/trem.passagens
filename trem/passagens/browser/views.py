# -*- coding: utf-8 -*-

import os
import shutil
import zipfile
import tempfile

from xml.dom.minidom import Document
from five import grok
from plone.app.layout.navigation.interfaces import INavigationRoot

from trem.passagens.config import session
from trem.passagens import tables
from trem.passagens.config import MessageFactory as _
from trem.passagens.nav import url

class BaseListView(object):
    
    def show_url(self, id, vs=None):
        vs = self.view_sufix if vs is None else vs
        return url('show-'+vs, id=id)

    def add_url(self, vs=None):
        vs = self.view_sufix if vs is None else vs
        return url('add-'+vs)

    def generic_url(self, paran_url, paran=False):
        if paran:
            return url(paran_url,id=paran)
        return url(paran_url)


class LocaisView(grok.View, BaseListView):

    grok.name('list-local')
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')

    dados = []
    view_sufix = 'local'

    def update(self):
        self.request.set('disable_border', True)
        self.dados = []
        items = session.query(tables.Local).all()
        for item in items:
            self.dados.append({'id': item.cidade,
                              })

class ViagensView(grok.View, BaseListView):

    grok.name('list-viagem')
    grok.context(INavigationRoot)
    grok.require('cmf.ManagePortal')

    dados = []
    view_sufix = 'viagem'

    def update(self):
        self.request.set('disable_border', True)
        self.dados = []
        items = session.query(tables.Viagem).all()
        for item in items:
            self.dados.append({ 'origem': item.cidade_origem,
                                'destino': item.cidade_destino,
                                'horario': item.horario,
                              })
