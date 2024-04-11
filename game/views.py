from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from specHuman import specHuman
from specAI import specAI

def choose_game_mode(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        difficulty = request.POST.get('difficulty')
        if choice == '1':
            return HttpResponseRedirect('/play/?mode=human')
        elif choice == '2' and difficulty in ['1', '2', '3']:
            return HttpResponseRedirect(f'/play/?mode=ai&difficulty={difficulty}')
    return render(request, 'game/choose_game_mode.html')

def play_game(request):
    mode = request.GET.get('mode')
    if mode == 'human':
        specHuman()
    elif mode == 'ai':
        difficulty = request.GET.get('difficulty')
        specAI(difficulty)
    return render(request, 'game/play_game.html')
