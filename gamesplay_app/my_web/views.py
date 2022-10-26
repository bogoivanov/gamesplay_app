from django.shortcuts import render, redirect

from gamesplay_app.my_web.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from gamesplay_app.my_web.models import Profile, Game


# Create your views here.
def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context)


def dashboard(request):
    games = Game.objects.all()
    profile = get_profile()

    context = {
        'games': games,
        'profile': profile,
    }

    return render(request, 'dashboard.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            Game.objects.all().delete()
            form.save()
            return redirect('show home')
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)


def profile_details(request):
    profile = get_profile()
    games_count = Game.objects.count()
    games = Game.objects.all()
    rating = 0
    full_name_user = ""
    if profile.first_name or profile.last_name:
        if profile.first_name and profile.last_name:
            full_name_user = f"{profile.first_name} {profile.last_name}"
        elif profile.first_name:
            full_name_user = f"{profile.first_name}"
        elif profile.last_name:
            full_name_user = f"{profile.last_name}"

    for game in games:
        rating += game.rating
    if games_count > 0:
        average_rating = rating / games_count
    else:
        average_rating = 0.0
    context = {
        'profile': profile,
        'games_count': games_count,
        'average_rating': average_rating,
        'full_name_user': full_name_user,
    }
    return render(request, 'details-profile.html', context)


def game_create(request):
    profile = get_profile()
    if request.method == 'POST':
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GameCreateForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'create-game.html', context)


def game_edit(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GameEditForm(instance=game)
    context = {
        'form': form,
        'profile': profile,
        'game': game
    }
    return render(request, 'edit-game.html', context)


def game_delete(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GameDeleteForm(instance=game)
    context = {
        'form': form,
        'profile': profile,
        'game': game
    }
    return render(request, 'delete-game.html', context)


def game_details(request, pk):
    game = Game.objects.filter(pk=pk).get()
    profile = get_profile()

    context = {
        'game': game,
        'profile': profile,
    }
    return render(request, 'details-game.html', context)
