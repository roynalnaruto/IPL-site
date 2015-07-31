from django.db import models

# Create your models here.
class Player(models.Model):
	TEAMS = (
		('MI', 'Mumbai Indians'),
		('DD', 'Delhi Daredevils'),
		('RCB', 'Royal Challengers Bangalore'),
		('KKR', 'Kolkata Knight Riders'),
		('SRH', 'Sunrisers Hyderabad'),
		('RR', 'Rajasthan Royals'),
		('KP', 'Kings XI Punjab'),
	)
	ROLES = (
		('BT', 'Batsman'),
		('BL', 'Bowler'),
		('AR', 'All-rounder'),
	)
	firstname = models.CharField(max_length = 30)
	lastname = models.CharField(max_length = 30)
	team = models.CharField(max_length = 3, choices = TEAMS)
	role = models.CharField(max_length = 2, choices = ROLES)
	img = models.ImageField()

	def __unicode__(self):
		return u'%s %s - %s' % (self.firstname, self.lastname, self.get_team_display())