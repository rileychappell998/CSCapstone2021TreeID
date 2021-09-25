from mysite.settings import BASE_DIR
from treeID.models import Comment
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db import connection
from django.shortcuts import render
from .forms import QueryForm
from .forms import CommentForm
from .forms import CommentListForm
from django.template.response import TemplateResponse
from django.views.generic.list import ListView


def redirect(request):
    return HttpResponseRedirect('/treeID/query/')

def get_query(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QueryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QueryForm()

    return render(request, 'query.html', {'form': form})

def get_comment(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentForm()

    return render(request, 'comment.html', {'form': form})

def index(request):
    ID = str(request.POST.get('query'))
    fields_to_query = ["id","group_", "leaf_fall", "name", "genus", "species_name", "family", "age_min", "age_max", "height_min", "height_max", "comments"]
    context_dict = {}
    for column in fields_to_query:
        query = "SELECT "+column+" FROM tree_data_cleaned WHERE id=%s;"
        cursor = connection.cursor()
        cursor.execute(query, [ID])
        query_response = cursor.fetchall()
        if len(query_response) != 1 or len(query_response[0]) != 1:
            raise ValueError('query response malformed')
        response = query_response[0][0]
        context_dict[column] = response
    return TemplateResponse(request, 'ID_response.html', context_dict)

def comment_handler(request):
    ID = str(request.POST.get('ID'))
    comment_text = str(request.POST.get('comment'))
    can_contact = request.POST.get('can_contact')
    if can_contact == "on":
        can_contact = True
    else:
        can_contact = False
    contact_info = request.POST.get('contact_info')
    save = request.POST.get('save')
    comment = Comment()
    comment.ID = ID
    comment.comment_text = comment_text
    comment.can_contact = can_contact
    comment.contact_info= contact_info

    if len(request.FILES) == 1:
        comment.photo= request.FILES["photo"]
    if save:
        comment.save()
    return HttpResponseRedirect('/treeID/query/')

def comment_viewer(request):
    model = Comment
    if request.method == 'POST':
        form = CommentListForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/admin/comment_views/')
        else:
            form = CommentListForm()
    form = CommentListForm()
    comments = Comment.objects.all()
    context = {
                'form': form,
                'comments': comments
                }
    return render(request, 'treeID/comment_list.html', context)

def comment_approval(request, id):
   comment = Comment.objects.get(pk = id)
   comment.approval = request.POST.get('approval')
   comment.approval = False
   comment.save()
   """
   comment = Comment()
   comment.approval = request.POST.get('approval')
   if comment.approval == "on":
       comment.approval = False
   else:
       comment.approval = False
   ID = str(request.POST.get('ID'))
   comment_text = str(request.POST.get('comment'))
   can_contact = request.POST.get('can_contact')
   if can_contact == "on":
       can_contact = True
   else:
       can_contact = False
   contact_info = request.POST.get('contact_info')
   print(comment.ID)
   comment.ID = ID
   comment.comment_text = comment_text
   comment.can_contact = can_contact
   comment.contact_info= contact_info
   #comment.approval = comment.approval
   comment.save()
   """
   return HttpResponseRedirect('/admin/comment_views')
 
"""
def comment_approval(request):
    approval = request.POST.get('approval')
    if approval == "on":
        approval = True
    else:
        approval = False
    return HttpResponseRedirect('/admin/comment_views/')
    
def get_approval(request):
# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentListForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentListForm()
    model = Comment
    comments = Comment.objects.all()
    context = {'comments':comments}

    return render(request, 'comment_list.html', context)
    
class CommentListView(ListView):
    model = Comment
    def get_context_data(self, *args, **kwargs):

        comments = Comment.objects.all()
        context = {'comments': comments}

        return context
    """