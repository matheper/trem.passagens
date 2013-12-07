# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import Time
from sqlalchemy import ForeignKey
from cop.relational.config import Base


class Local(Base):
    __tablename__ = "local"
    cidade = Column(String, primary_key=True)

    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

class Viagem(Base):
    __tablename__ = "viagem"

    cidade_origem = Column(String,
                           ForeignKey("local.cidade", onupdate="CASCADE"), ondelete="CASCADE"),
                           primary_key=True)

    cidade_destino = Column(String,
                           ForeignKey("local.cidade", onupdate="CASCADE"), ondelete="CASCADE"),
                           primary_key=True)

    horario = Column(Time, primary_key=True)

    def __init__(self, cidade_origem, cidade_destino, horario):
        self.cidade_origem = cidade_origem
        self.cidade_destino = cidade_destino
        self.horario = horario

#
#class FollowMember(Base):
#    __tablename__ = "follow_member" 
#    
#    followmember_follower = Column(String,
#                                   ForeignKey("member.member_id", onupdate="CASCADE", ondelete="CASCADE"),
#                                   primary_key=True)
#    followmember_following = Column(String,
#                                   ForeignKey("member.member_id", onupdate="CASCADE", ondelete="CASCADE"),
#                                   primary_key=True)
#    followmember_date = Column(DateTime)
#
#    def __init__(self, followmember_follower, followmember_following, followmember_date):
#        self.followmember_follower = followmember_follower
#        self.followmember_following = followmember_following
#        self.followmember_date = followmember_date
#
#class Member(Base):
#    __tablename__ = "member"
#
#    member_id = Column(String, primary_key=True)
#
#    def __init__(self, member_id):
#        self.member_id = member_id
#
#class Tag(Base):
#    __tablename__ = "tag"
#
#    tag_id = Column(String, primary_key=True)
#
#    def __init__(self, tag_id):
#        self.tag_id = tag_id
#
#class FollowTag(Base):
#    __tablename__ = "follow_tag" 
#
#    followtag_member = Column(String,
#                                   ForeignKey("member.member_id", onupdate="CASCADE", ondelete="CASCADE"),
#                                   primary_key=True)
#    followtag_tag = Column(String,
#                                   ForeignKey("tag.tag_id", onupdate="CASCADE", ondelete="CASCADE"),
#                                   primary_key=True)
#    followtag_type = Column(Integer, primary_key=True)
#    followtag_date = Column(DateTime)
#
#    def __init__(self, followtag_member, followtag_tag, followtag_type, followtag_date):
#        self.followtag_member = followtag_member
#        self.followtag_tag = followtag_tag
#        self.followtag_type = followtag_type
#        self.followtag_date = followtag_date
#
#class Notification(Base):
#    __tablename__ = "notification"
#
#    notification_id = Column(Integer, Sequence("notification_id_seq"), primary_key=True)
#    notification_member_id = Column(String, 
#                                    ForeignKey("member.member_id", onupdate="CASCADE", ondelete="CASCADE"),
#                                    nullable=False)
#    notification_type = Column(Integer)
#    notification_object_uid = Column(String)
#
#    def __init__(self, notification_member_id, notification_type = None, notification_object_uid = None):
#        self.notification_member_id = notification_member_id
#        if notification_type:
#            self.notification_type = notification_type
#        if notification_object_uid:
#            self.notification_object_uid = notification_object_uid
#
#class Delate(Base):
#    __tablename__ = "delate"
#
#    delate_id = Column(Integer, Sequence("delate_id_seq"), primary_key=True)
#    delate_description = Column(String, nullable=False)
#    delate_date = Column(DateTime, nullable=False)
#    delate_delator = Column(String, 
#                            ForeignKey("member.member_id", onupdate="CASCADE", ondelete="CASCADE"),
#                            nullable=False)
#    delate_delated = Column(String, 
#                            ForeignKey("member.member_id", onupdate="CASCADE", ondelete="CASCADE"),
#                            nullable=False)
#    delate_obj_url = Column(String, nullable=False)
#    delate_obj_uid = Column(String, nullable=False)
#    delate_obj_title = Column(String)
#    delate_reviewed = Column(Boolean)
#
#    def __init__(self, delate_description, delate_delator, delate_delated, delate_obj_url, delate_obj_uid, delate_obj_title):
#        self.delate_description = delate_description
#        self.delate_date = datetime.now()
#        self.delate_delator = delate_delator
#        self.delate_delated = delate_delated
#        self.delate_obj_url = delate_obj_url
#        self.delate_obj_uid = delate_obj_uid
#        self.delate_obj_title = delate_obj_title
#        self.delate_reviewed = False
#
#class DelateAllowed(Base):
#    __tablename__ = "delate_allowed"
#
#    delate_allowed_delate_id = Column(Integer, 
#                                      ForeignKey("delate.delate_id", onupdate="CASCADE", ondelete="CASCADE"),
#                                      primary_key=True)
#    delate_allowed_member_id = Column(String, 
#                                      ForeignKey("member.member_id", onupdate="CASCADE", ondelete="CASCADE"),
#                                      primary_key=True)
#
#    def __init__(self, delate_allowed_delate_id, delate_allowed_member_id):
#        self.delate_allowed_delate_id = delate_allowed_delate_id
#        self.delate_allowed_member_id = delate_allowed_member_id
