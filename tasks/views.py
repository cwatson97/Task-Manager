from django.shortcuts import render, redirect
    # render combines a template (html) with conect (python data) and returns an http response to the browser
    # redirect tells the browser to go to a different URL --> After adding a task, go back to task list page

from .models import Task
    # Import our Task model/table fom the same app | Allows to query the database and create new tasks

# Show all tasks that our user has added to the task manager
def list_of_tasks(request):

    tasks = Task.objects.all()  # Fetchs all Task objects from the database
        # Task.onbjects is a manager that lets you query the database
        # .all() returns all rows as a QuerySet (Like a python list of Task objects)

    return render(request, 'tasks/list_of_tasks.html', {'tasks': tasks})
        # request --> sends the current http request
        # 'tasks/list_of_tasks.html' --> The template to render
        # {'tasks': tasks}  --> The context dictionary; makes the variable tasks available in the template

# Add a new task to the list
def add_new_task(request):

    if request.method =='POST': # Check if the form was submitted  |  GET visits the site  |  POST submits a form 
        title = request.POST.get('title') # Get the title from the submitted form
        Task.objects.create(title = title) # Creates a new Task in the database with the given title  |  defaults to False
        return redirect('list_of_tasks')   # After new task is created, redirect the user to the task list page
    # If the request isn't POST, the user is just visiting the 'add new task' page
    return render(request, 'tasks/add_new_task.html')