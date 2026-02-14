from django import forms
from .models import ScamReport

class ScamReportForm(forms.ModelForm):
    class Meta:
        model = ScamReport
        fields = [
            'nickname', 'avatar', 'crush_name',

            # Existing fields
            'denied_sex', 'mixed_signals', 'lies', 'ghosted', 'last_minute_cancel',
            'flirts_with_others', 'inconsistent_messages', 'ignores_messages',
            'cancels_dates_last_minute', 'posts_flirty_on_socials', 'talks_about_exes',
            'hot_and_cold_behavior', 'flakey_promises', 'sends_confusing_signals',
            'surprises_with_ghosting',

            # 💘 Valentine-specific fields
            'ignored_valentines_messages', 'ghosted_on_valentine', 'cancelled_valentine_date',
            'cheesy_gifts_received', 'flirty_texts_with_others', 'overhyped_celebration',
            'romantic_promises_broken', 'social_media_posting_without_you', 'ex_mention_on_valentine',
            'ignored_flower_delivery', 'valentine_surprise_failed'
        ]
        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'crush_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'avatar': forms.Select(attrs={'class': 'w-full p-2 border rounded-lg'}),
        }

    # Overriding init to make all Boolean fields nice Tailwind checkboxes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs.update({
                    'class': 'mr-2 accent-pink-500 w-4 h-4',
                })