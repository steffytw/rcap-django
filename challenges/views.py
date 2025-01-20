from django.shortcuts import render
from django.http import HttpResponse,Http404, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


challenge_text = {
    "jan":"Welcome to january!",
    "feb":"Welcome to february!",
    "mar":"Welcome to march!",
    "apr":"Welcome to april!",
    "may":"Welcome to may!",
    "jun":"Welcome to june!",
    "jul":"Welcome to july!",
    "aug":"Welcome to august!",
    "sep":"Welcome to september!",
    "oct":"Welcome to october!",
    "nov":"Welcome to november!",
    "dec":None
}

def index(request):
    months = list(challenge_text.keys())
    # month_li = ""
    # for month in months:
    #     redirect_url = reverse("monthly_challenges",args=[month])
    #     month_li += f"<li><a href=\"{redirect_url}\">{month.capitalize()}</a></li>"
    # monthly_challenges_list = f"<ul>{month_li}</ul>"
    # return HttpResponse(monthly_challenges_list)
    details =  render(request,"challenges/index.html",{
        "months":months
    })
    return HttpResponse(details)


def mothly_challenges(request,month):
     try:
        month_txt = challenge_text[month]
        # msg = render_to_string("challenges/challenges.html")
        msg = render(request,"challenges/challenges.html",{
            "text":month_txt,
            "month":month
        })
        return HttpResponse(msg)
     except:
        response = render_to_string("404.html")
        # raise Http404
        return HttpResponseNotFound(response)
    


def mothly_challenges_by_number(request,month):
    months =  list(challenge_text.keys())
    print(month)
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    actual_month = months[month - 1]
    redirect_url = reverse("monthly_challenges",args=[actual_month])
    return HttpResponseRedirect(redirect_url)
    # return HttpResponseRedirect("/challenges/"+actual_month)