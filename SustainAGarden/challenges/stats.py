import plotly.express as px
from .models import User, Challenge, CompleteChallenge, transport_challenge
import datetime
from django.db.models import Sum

def generate_statistics_context() -> dict:
    # do some statistics processing
    users = User.objects.all()
    top = ""
    for i in users:
        if top == "":
            top = i
        elif len(i.completed_challenges.split(",")) > len(top.completed_challenges.split(",")):
            top = i

    day_users = []
    for j in range(30):
        date_joined = datetime.datetime.now() - datetime.timedelta(days=j)
        day_users.append(len(User.objects.filter(date_joined=date_joined)))
    fig = px.line(day_users, x="day", y="No of Users", title="A line chart")

    total_distance = transport_challenge.objects.aggregate(Sum('distance_covered'))

    # convert km to miles
    total_distance = total_distance * 0.621371
    co2 = (total_distance/27.5)*8887

    return {"challenges_completed": len(CompleteChallenge.objects.all()),
            "users": users,
            "most_challenges": top.username,
            "co2": co2,
            "graph": fig.to_html()}
