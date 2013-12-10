# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.component import provideUtility
from zope.app.component.hooks import getSite
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory

from trem.passagens.config import MessageFactory as _
from trem.passagens.config import session
from trem.passagens import tables
               
class LocalVocabulary(object):

    implements(IVocabularyFactory)

    def __call__(self, context):
        query = session.query(tables.Local).order_by(tables.Local.cidade).all()
        return SimpleVocabulary([SimpleTerm(dado.cidade, dado.cidade, dado.cidade) for dado in query])

LocalVocabularyFactory = LocalVocabulary()
provideUtility(LocalVocabularyFactory, IVocabularyFactory,
               name='trem.passagens.local-vocab')
