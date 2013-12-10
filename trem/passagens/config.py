# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from z3c.saconfig import named_scoped_session

Base = declarative_base()
SCOPED_SESSION_NAME = "session.trem.passagens.db"
session = named_scoped_session(SCOPED_SESSION_NAME)

import zope.i18nmessageid
MessageFactory = zope.i18nmessageid.MessageFactory('trem.passagens')
