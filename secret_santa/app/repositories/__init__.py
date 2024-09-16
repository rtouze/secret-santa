#!/usr/bin/env python3
from django.db.models import F
from app.models import (
    Participant as DbParticipant,
    Draw as DbDraw,
    DrawItem as DbDrawItem,
    ParticipantBlacklistItem,
)
from app.domain.participants import Participant, Draw, DrawItem
from django.db import transaction


class ParticipantNotFoundError(Exception):
    def __init__(self, name):
        super().__init__(f"Participant {name} not found")


class SantaRepository:
    def save_draw(self, draw):
        d = DbDraw()
        d.save()
        participant_by_name = {p.name: p for p in DbParticipant.objects.all()}
        for di in draw.items:
            db_di = DbDrawItem(
                giver=participant_by_name[di.name],
                receiver=participant_by_name[di.offers_to],
                draw=d,
            )
            db_di.save()

    def get_draws(self):
        db_draws = DbDraw.objects.order_by(F("creation_date").desc()).all()
        l = []
        for d in db_draws[:5]:
            draw_items = []
            for item in d.drawitem_set.all():
                draw_items.append(DrawItem(item.giver.name, item.receiver.name))
                print("item", item)
            l.append(Draw(draw_items, d.creation_date))
        return l

    def save_participant_list(self, participants):
        DbParticipant.objects.all().delete()
        DbDraw.objects.all().delete()
        for p in participants:
            dbp = DbParticipant(name=p.name)
            dbp.save()

    def get_participant_list(self):
        return [
            Participant(p.name, [bi.blacklisted_participant.name for bi in p.blacklisted.all()])
            for p in DbParticipant.objects.all()
        ]

    def save_participant(self, participant):
        with transaction.atomic():
            db_participants_by_name = {p.name: p for p in DbParticipant.objects.all()}

            db_participant = db_participants_by_name.get(participant.name)
            if not participant:
                raise ParticipantNotFoundError(participant.name)

            db_participant.blacklisted.all().delete()
            for blacklist_item in participant.blacklist:
                blacklisted_participant = db_participants_by_name.get(blacklist_item)
                if blacklisted_participant:
                    ParticipantBlacklistItem(
                        participant=db_participant,
                        blacklisted_participant=blacklisted_participant,
                    ).save()
