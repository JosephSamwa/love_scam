from django.urls import path
from .views import report_view, leaderboard_view, user_history_view, report_detail_view


urlpatterns = [
    path("", report_view, name="report"),
    path("leaderboard/", leaderboard_view, name="leaderboard"),
    path("history/<str:nickname>/", user_history_view, name="user_history"),
    path("report/<slug:slug>/", report_detail_view, name="report_detail"),
]