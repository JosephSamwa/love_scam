from django.shortcuts import render
from .forms import ScamReportForm
from .models import ScamReport
from django.http import JsonResponse

def report_view(request):
    if request.method == "POST":
        form = ScamReportForm(request.POST)
        if form.is_valid():
            report = form.save()
            return JsonResponse({
                "success": True,
                "scam_level": report.scam_level,
                "slug": report.slug
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = ScamReportForm()
    return render(request, "scam_detector/report_form.html", {"form": form})

def leaderboard_view(request):
    top_reports = ScamReport.objects.order_by('-scam_level')[:10]
    return render(request, "scam_detector/leaderboard.html", {"top_reports": top_reports})

def user_history_view(request, nickname):
    history = ScamReport.objects.filter(nickname=nickname).order_by('-created_at')
    return render(request, "scam_detector/user_history.html", {"nickname": nickname, "history": history})

def report_detail_view(request, slug):
    report = ScamReport.objects.get(slug=slug)
    return render(request, "scam_detector/report_detail.html", {"report": report})