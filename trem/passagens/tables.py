# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import Time
from sqlalchemy import ForeignKey
from trem.passagens.config import Base
from zope.interface import implements
from trem.passagens import interfaces


class Local(Base):
    implements(interfaces.ILocal)
    __tablename__ = "local"
    cidade = Column(String, primary_key=True)

    def __init__(self, cidade):
        self.cidade = cidade

class Viagem(Base):
    implements(interfaces.IViagem)
    __tablename__ = "viagem"

    cidade_origem = Column(String,
                           ForeignKey("local.cidade", onupdate="CASCADE", ondelete="CASCADE"),
                           primary_key=True)

    cidade_destino = Column(String,
                           ForeignKey("local.cidade", onupdate="CASCADE", ondelete="CASCADE"),
                           primary_key=True)

    horario = Column(Time, primary_key=True)

    def __init__(self, cidade_origem, cidade_destino, horario):
        self.cidade_origem = cidade_origem
        self.cidade_destino = cidade_destino
        self.horario = horario
