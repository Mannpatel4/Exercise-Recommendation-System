from django.shortcuts import render
from django.conf import settings
import os
from .exercise import ExerciseRecommendationSystem

def index(request):
    if request.method == 'POST':
        goal = request.POST['goal']
        difficulty = request.POST['difficulty']
        location = request.POST['type']
        csv_path = os.path.join(settings.BASE_DIR, 'app', 'exercise.csv')
        recommender = ExerciseRecommendationSystem(csv_path)
        results = (recommender.reset()
                   .filter_by_goal(goal.replace("_", " ")) 
                   .filter_by_difficulty(difficulty)
                   .filter_by_location(location.replace("at ", ""))
                   .recommend())
        context = {
            'goal':goal,
            'difficulty':difficulty,
            'type':location,
            'recommendations': results
        }
        return render(request,'index.html',context)
    return render(request,'index.html')