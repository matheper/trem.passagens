# -*- coding: utf-8 -*-
from z3c.saconfig import named_scoped_session
from trem.passagens.config import Base
from trem.passagens.config import SCOPED_SESSION_NAME

Session = named_scoped_session(SCOPED_SESSION_NAME)

def isNotRelational(context):
    return context.readDataFile("trem.passagens.marker") is None

def createTables(context):
    """Creates tables
    """
    if isNotRelational(context):
        return

    Base.metadata.create_all(bind=Session.bind)
