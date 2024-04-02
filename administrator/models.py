from django.db import models

# Create your models here.
class Administrator(models.Model):
    admin_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role_choices = [
        ('Manager', 'Manager'),
        ('Head Coach', 'Head Coach'),
        ('Sports Administrator', 'Sports Administrator'),
    ]
    role = models.CharField(max_length=50, choices=role_choices, default='Manager')
    contact_no = models.CharField(max_length=50)

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    admin_id = models.ForeignKey(Administrator, null=True)
    player_id = models.ForeignKey(Player, null=True)
    staff_id = models.ForeignKey(Staff, null=True)
    training_session_id = models.ForeignKey(TrainingSession, null=True)
    match_id = models.ForeignKey(Match, null=True)
    category_choices = [
        ('Observations', 'Observations'),
        ('Complaint', 'Complaint'),
    ]
    category = models.CharField(max_length=30, choices=category_choices, default='Observations')

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=30, choices=gender_choices, default=None)
    dob = models.DateTimeField()
    nationality = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50)
    player_game_choices = [
        ('Volleyball', 'Volleyball'),
        ('Football', 'Football'),
        ('Basketball', 'Basketball'),
        ('Netball', 'Netball'),
    ]
    player_game = models.CharField(max_length=50, choices=player_game_choices, default='Volleyball')
    position = models.CharField(max_length=100)
    jersey_no = models.IntegerField()
    medical_condition = models.CharField(max_length=100)

class PlayerTeam(models.Model):
    player_id = models.ForeignKey(Player)
    team_id = models.ForeignKey(Team)
    start_date = models.DateField()
    end_date = models.DateField()

class PlayerGame(models.Model):
    player_id = models.ForeignKey(Player)
    match_id = models.ForeignKey(Match)
    sets_halfs_played = models.CharField(max_length=100)
    goals_scored = models.IntegerField(null=True)
    saves_made = models.IntegerField(null=True)
    attack_kills = models.IntegerField(null=True)
    block_kills = models.IntegerField(null=True)
    cover_saves = models.IntegerField(null=True)
    receptions_delivered = models.IntegerField(null=True)

class Injury(models.Model):
    injury_id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey(Player)
    date_occured = models.DateField()
    body_part = models.CharField(max_length=50)
    severity_choices = [
        ('Moderate', 'Moderate'),
        ('Intense', 'Intense'),
    ]
    severity = models.CharField(max_length=50, choices=severity_choices, default='Moderate')
    estimated_recovery_date = models.DateField()

class TrainingSession(models.Model):
    training_session_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    type_choices = [
        ('Game Situations', 'Game situations'),
        ('Physical Fitness', 'Physical Fitness'),
        ('Mental Fitness', 'Mental Fitness'),
    ]
    type = models.CharField(max_length=50, choices=type_choices, default='Game Situations')
    description = models.TextField(blank=True, max_length=500)

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    game_type_choices = [
        ('League game', 'League game'),
        ('Friendly game', 'Friendly game'),
        ('Tournament game', 'Tournament game')
    ]
    game_type = models.CharField(max_length=30, choices=game_type_choices, default='League game')
    result_choices = [
        ('Win', 'Win'),
        ('Loss', 'Loss'),
        ('Draw', 'Draw'),
    ]
    result = models.CharField(max_length=30, choices=result_choices, default='Win')


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey(Player)
    training_session_id = models.ForeignKey(TrainingSession, blank=True)
    match_id = models.ForeignKey(Match, blank=True)
    staff_id = models.ForeignKey(Staff, blank=True)
    date = models.DateTimeField()
    status_choices = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]
    status = models.CharField(max_length=30, choices=status_choices, default='Present')


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)
    league_choices = [
        ('National league', 'National league'),
        ('Corporate league', 'Corporate league'),
    ]
    league = models.CharField(max_length=30, choices=league_choices, default='National league')

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role_choices = [
        ('Head Coach', 'Head Coach'),
        ('Assistant Coach', 'Assistant Coach'),
        ('Manager', 'Manager'),
        ('Fitness Coach', 'Fitness Coach'),
        ('Team Doctor', 'Team Doctor'),
    ]
    role = modesl.CharField(max_length=50, choices=role_choices, default='Head Coach')