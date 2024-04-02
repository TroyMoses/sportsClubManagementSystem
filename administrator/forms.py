from django import forms
from .models import Player, Administrator, Feedback, Staff, Injury, Team, PlayerTeam, PlayerGame, TrainingSession, Attendance, Match
from django.contrib.auth.hashers import make_password
from .models import Department

class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = [
            'admin_id',
            'first_name',
            'last_name',
            'contact_no',
            'role',
        ]

class FeedbackForm(forms.ModelForm):
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

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'player_id',
            'first_name',
            'last_name',
            'dob',
            'nationality',
            'email',
            'phone_number',
            'position',
            'jersey_no',
            'medical_condition',
            'player_game',
            'gender',
        ]

class PlayerTeamForm(forms.ModelForm):
    class Meta:
        model = PlayerTeam
        fields = [
            'player_id',
            'team_id',
            'start_date',
            'end_date',
        ]

class PlayerGameForm(forms.ModelForm):
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

class InjuryForm(forms.ModelForm):
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

class TrainingSessionForm(forms.ModelForm):
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

class MatchForm(forms.ModelForm):
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

class AttendanceForm(forms.ModelForm):
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

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'team_id',
            'team_name',
            'coach_name',
            'league',
        ]

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            'staff_id',
            'first_name',
            'last_name',
            'role',
        ]



class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

# class CustomUserForm(FormSettings):
#     email = forms.EmailField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput)
    
#     widget = {
#         'password': forms.PasswordInput(),
#     }

#     def __init__(self, *args, **kwargs):
#         super(CustomUserForm, self).__init__(*args, **kwargs)
#         if kwargs.get('instance'):
#             instance = kwargs.get('instance')
#             self.fields['password'].required = False
#             for field in CustomUser._meta.fields:
#                 if field.name not in ['id', 'user_ptr', 'password']:  # Exclude inherited fields
#                     self.fields[field.name].initial = getattr(instance, field.name)
#             if instance.pk is not None:
#                 self.fields['password'].widget.attrs['placeholder'] = "Fill this only if you wish to update password"
#         else:
#             self.fields['first_name'].required = True
#             self.fields['last_name'].required = True

#     def clean_email(self):
#         email = self.cleaned_data['email'].lower()
#         if self.instance.pk is None:  # Insert
#             if CustomUser.objects.filter(email=email).exists():
#                 raise forms.ValidationError("The given email is already registered")
#         else:  # Update
#             db_email = CustomUser.objects.get(id=self.instance.pk).email.lower()
#             if db_email != email:  # There has been changes
#                 if CustomUser.objects.filter(email=email).exists():
#                     raise forms.ValidationError("The given email is already registered")
#         return email

#     def clean_password(self):
#         password = self.cleaned_data.get("password", None)
#         if self.instance.pk is not None:
#             if not password:
#                 return self.instance.password
#         return make_password(password)

#     class Meta:
#         model = CustomUser
#         fields = ['last_name', 'first_name', 'email', 'password', 'department']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user

