from django.db import models
import random
from django.utils.text import slugify
import time

EMOJI_CHOICES = [
    ("😎","Cool"),("😂","Funny"),("🥲","Sad"),("💀","Dead inside"),
    ("🔥","Hot"),("🥵","Hot mess"),("🤡","Clown vibes"),("💘","Valentine vibes")
]

FUNNY_COMMENTS = [
    "Love? More like scam! 😂",
    "Run while you can! 💀",
    "Oops… you got played 😬",
    "Heartbreak incoming… 🥲",
    "Still hopeful? Bold move 😎",
    "Single and thriving! 🥵",
    "Clown alert! 🤡",
    "Cupid missed this one 💘"
]

class ScamReport(models.Model):
    nickname = models.CharField(max_length=50)
    avatar = models.CharField(max_length=10, choices=EMOJI_CHOICES, default="😎")
    crush_name = models.CharField(max_length=255)

    # Existing fields
    denied_sex = models.BooleanField(default=False)
    mixed_signals = models.BooleanField(default=False)
    lies = models.BooleanField(default=False)
    ghosted = models.BooleanField(default=False)
    last_minute_cancel = models.BooleanField(default=False)
    flirts_with_others = models.BooleanField(default=False)
    inconsistent_messages = models.BooleanField(default=False)
    ignores_messages = models.BooleanField(default=False)
    cancels_dates_last_minute = models.BooleanField(default=False)
    posts_flirty_on_socials = models.BooleanField(default=False)
    talks_about_exes = models.BooleanField(default=False)
    hot_and_cold_behavior = models.BooleanField(default=False)
    flakey_promises = models.BooleanField(default=False)
    sends_confusing_signals = models.BooleanField(default=False)
    surprises_with_ghosting = models.BooleanField(default=False)

    # 💘 Valentine Edition Fields
    ignored_valentines_messages = models.BooleanField(default=False)
    ghosted_on_valentine = models.BooleanField(default=False)
    cancelled_valentine_date = models.BooleanField(default=False)
    cheesy_gifts_received = models.BooleanField(default=False)
    flirty_texts_with_others = models.BooleanField(default=False)
    overhyped_celebration = models.BooleanField(default=False)
    romantic_promises_broken = models.BooleanField(default=False)
    social_media_posting_without_you = models.BooleanField(default=False)
    ex_mention_on_valentine = models.BooleanField(default=False)
    ignored_flower_delivery = models.BooleanField(default=False)
    valentine_surprise_failed = models.BooleanField(default=False)

    scam_level = models.IntegerField(default=0)
    comment = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_scam_level(self):
        self.scam_level = 0

        # Existing scoring
        self.scam_level += 50 if self.denied_sex else 0
        self.scam_level += 30 if self.mixed_signals else 0
        self.scam_level += 70 if self.lies else 0
        self.scam_level += 40 if self.ghosted else 0
        self.scam_level += 20 if self.last_minute_cancel else 0
        self.scam_level += 25 if self.flirts_with_others else 0
        self.scam_level += 15 if self.inconsistent_messages else 0
        self.scam_level += 20 if self.ignores_messages else 0
        self.scam_level += 20 if self.cancels_dates_last_minute else 0
        self.scam_level += 25 if self.posts_flirty_on_socials else 0
        self.scam_level += 15 if self.talks_about_exes else 0
        self.scam_level += 30 if self.hot_and_cold_behavior else 0
        self.scam_level += 25 if self.flakey_promises else 0
        self.scam_level += 20 if self.sends_confusing_signals else 0
        self.scam_level += 35 if self.surprises_with_ghosting else 0

        # Valentine-specific scoring
        self.scam_level += 30 if self.ignored_valentines_messages else 0
        self.scam_level += 40 if self.ghosted_on_valentine else 0
        self.scam_level += 25 if self.cancelled_valentine_date else 0
        self.scam_level += 15 if self.cheesy_gifts_received else 0
        self.scam_level += 20 if self.flirty_texts_with_others else 0
        self.scam_level += 20 if self.overhyped_celebration else 0
        self.scam_level += 25 if self.romantic_promises_broken else 0
        self.scam_level += 15 if self.social_media_posting_without_you else 0
        self.scam_level += 20 if self.ex_mention_on_valentine else 0
        self.scam_level += 15 if self.ignored_flower_delivery else 0
        self.scam_level += 25 if self.valentine_surprise_failed else 0

        # Random meme chaos
        self.scam_level += random.randint(0, 20)
        self.comment = random.choice(FUNNY_COMMENTS)

        return self.scam_level

    def save(self, *args, **kwargs):
        if not self.slug:
            timestamp = int(time.time())
            self.slug = slugify(f"{self.nickname}-{timestamp}")
        self.calculate_scam_level()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nickname} ({self.avatar}) vs {self.crush_name} - Scam Level: {self.scam_level}"