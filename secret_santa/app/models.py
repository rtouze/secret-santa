from django.db import models
from django.db.models.functions import Now


class Participant(models.Model):
    name = models.CharField(max_length=30, unique=True)

class ParticipantBlacklistItem(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="blacklisted")
    blacklisted_participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="blacklisted_participant")

class Draw(models.Model):
    creation_date = models.DateTimeField(db_default=Now())

class DrawItem(models.Model):
    giver = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="giver")
    receiver = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="receiver")
    draw =  models.ForeignKey(Draw, on_delete=models.CASCADE)

