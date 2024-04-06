from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone

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

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=30, choices=gender_choices, default=None)
    dob = models.DateField()
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
    role = models.CharField(max_length=50, choices=role_choices, default='Head Coach')
    contact_no = models.CharField(max_length=50)

class TrainingSession(models.Model):
    training_session_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField(default=None)
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
    date = models.DateField(default=None)
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

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)
    league_choices = [
        ('National league', 'National league'),
        ('Corporate league', 'Corporate league'),
    ]
    league = models.CharField(max_length=30, choices=league_choices, default='National league')

class PlayerFeedback1(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    
    player_id = models.ForeignKey(Player, null=True, on_delete=models.CASCADE)
    training_session_id = models.ForeignKey(TrainingSession, null=True, on_delete=models.CASCADE)
    category_choices = [
        ('Observations', 'Observations'),
        ('Complaint', 'Complaint'),
    ]
    category = models.CharField(max_length=30, choices=category_choices, default='Observations')
    description = models.TextField(default=None, max_length=200)
    date = models.DateField(default=None)

class PlayerFeedback2(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey(Player, null=True, on_delete=models.CASCADE)
    match_id = models.ForeignKey(Match, null=True, on_delete=models.CASCADE)
    category_choices = [
        ('Observations', 'Observations'),
        ('Complaint', 'Complaint'),
    ]
    category = models.CharField(max_length=30, choices=category_choices, default='Observations')
    description = models.TextField(default=None, max_length=200)
    date = models.DateField(default=None)

class StaffFeedback1(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, null=True, on_delete=models.CASCADE)
    training_session_id = models.ForeignKey(TrainingSession, null=True, on_delete=models.CASCADE)
    category_choices = [
        ('Observations', 'Observations'),
        ('Complaint', 'Complaint'),
    ]
    category = models.CharField(max_length=30, choices=category_choices, default='Observations')
    description = models.TextField(default=None, max_length=200)
    date = models.DateField(default=None)

class StaffFeedback2(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, null=True, on_delete=models.CASCADE)
    match_id = models.ForeignKey(Match, null=True, on_delete=models.CASCADE)
    category_choices = [
        ('Observations', 'Observations'),
        ('Complaint', 'Complaint'),
    ]
    category = models.CharField(max_length=30, choices=category_choices, default='Observations')
    description = models.TextField(default=None, max_length=200)
    date = models.DateField(default=None)


class PlayerTeam(models.Model):
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class PlayerGame(models.Model):
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
    sets_halfs_played = models.CharField(max_length=100)
    goals_scored = models.IntegerField(null=True)
    saves_made = models.IntegerField(null=True)
    attack_kills = models.IntegerField(null=True)
    block_kills = models.IntegerField(null=True)
    cover_saves = models.IntegerField(null=True)
    receptions_delivered = models.IntegerField(null=True)

class Injury(models.Model):
    injury_id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    date_occured = models.DateField()
    body_part = models.CharField(max_length=50)
    severity_choices = [
        ('Moderate', 'Moderate'),
        ('Intense', 'Intense'),
    ]
    severity = models.CharField(max_length=50, choices=severity_choices, default='Moderate')
    estimated_recovery_date = models.DateField()


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    training_session_id = models.ForeignKey(TrainingSession, blank=True, on_delete=models.CASCADE)
    match_id = models.ForeignKey(Match, blank=True, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status_choices = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]
    status = models.CharField(max_length=30, choices=status_choices, default='Present')




class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", 1)
        extra_fields.setdefault("last_name", "System")
        extra_fields.setdefault("first_name", "Administrator")

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)


# class CustomUser(AbstractUser):
#     USER_TYPE = ((1, "Admin"), (2, "staff"), (3, "cashier"))
#     username = None 
#     user_type = models.CharField(default=2, choices=USER_TYPE, max_length=1)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)
#     email = models.EmailField(unique=True)
#     full_name = models.CharField(max_length=255, blank=True)
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#     objects = CustomUserManager()
#     department = models.ForeignKey(Department, related_name='users', on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.last_name + " " + self.first_name

