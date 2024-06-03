from django.shortcuts import render

# Create your views here.
def view_home(request):
    return render(request, "home.html")

# create welcome view
def view_welcome(request):
    name = request.GET['name']
    # this is a dictionary of all the data that will be passed to the template
    email = request.GET['email']
    birthday = request.GET['birthday']
    # if it was a post request it would be request.POST
    # build out context data
    context_data = {
        "name": name,
        "email": email,
        "birthday": birthday
    }
    return render(request, "welcome.html", context=context_data)

# sports view
def sports(request):
    sports=["Football", "Basketball", "Tennis", "Rugby", "Golf"]
    return render(request, "sports.html", context={"sports": sports})
