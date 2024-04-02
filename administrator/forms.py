from django import forms
from .models import Player, Administrator, Feedback, Staff, Injury, Team, PlayerTeam, PlayerGame, TrainingSession, Attendance, Match

class AdministratorForm(models.ModelForm):
    class Meta:
        model = Administrator
        fields = [
            'admin_id',
            'first_name',
            'last_name',
            'role',
            'contact_no',
        ]

class FeedbackForm(models.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'feedback_id',
            'admin_id',
            'player_id',
            'staff_id',
            'training_session_id',
            'match_id',
            'category',
        ]

class PlayerForm(models.ModelForm):
    class Meta:
        model = Player
        fields = [
            'player_id',
            'first_name',
            'last_name',
            'gender',
            'dob',
            'nationality',
            'email',
            'phone_number',
            'player_game',
            'position',
            'jersey_no',
            'medical_condition',
        ]

class PlayerTeamForm(models.ModelForm):
    class Meta:
        model = PlayerTeam
        fields = [
            'player_id',
            'team_id',
            'start_date',
            'end_date',
        ]

class PlayerGameForm(models.ModelForm):
    class Meta:
        model = PlayerGame
        fields = [
            'player_id',
            'match_id',
            'sets_halfs_played',
            'goals_scored',
            'saves_made',
            'attack_kills',
            'block_kills',
            'cover_saves',
            'receptions_delivered',
        ]

class InjuryForm(models.ModelForm):
    class Meta:
        model = Injury
        fields = [
            'injury_id',
            'player_id',
            'date_occured',
            'body_part',
            'severity',
            'estimated_recovery_date',
        ]

class TrainingSessionForm(models.ModelForm):
    class Meta:
        model = TrainingSession
        fields = [
            'training_session_id',
            'staff_id',
            'date_time',
            'location',
            'type',
            'description',
        ]

class MatchForm(models.ModelForm):
    class Meta:
        model = Match
        fields = [
            'match_id',
            'date_time',
            'home_team',
            'away_team',
            'venue',
            'game_type',
            'result',
        ]

class AttendanceForm(models.ModelForm):
    class Meta:
        model = Attendance
        fields = [
            'attendance_id',
            'player_id',
            'training_session_id',
            'match_id',
            'staff_id',
            'date',
            'status',
        ]

class TeamForm(models.ModelForm):
    class Meta:
        model = Team
        fields = [
            'team_id',
            'team_name',
            'coach_name',
            'league',
        ]

class StaffForm(models.ModelForm):
    class Meta:
        model = Staff
        fields = [
            'staff_id',
            'first_name',
            'last_name',
            'role',
        ]

