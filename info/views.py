from django.shortcuts import render
from info.models import *
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin 
#importing loginrequiredMixin and UserPassesTestMixin from auth.mixin
#from django.views.generic import  DetailView  # importing class based views from views.generic
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView # importing class based views from views.generic
from django.core.paginator import Paginator




# Create your views here.
def home(request):
    return render(request, 'info/index.html')


class NoticeListView(LoginRequiredMixin,ListView):
    model = Notice
    template_name = 'info/notice_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'notice'
    ordering = ['-published']
    paginate_by = 5 # pagination  (django provided )


class NoticeDetailView(LoginRequiredMixin,DetailView):
    model = Notice
    template_name = 'info/notice_detail.html' #<app>/<model>_<viewtype>.html


def about(request):
	return render(request, 'info/about.html')



def admission(request):
	return render(request, 'info/admission.html')

def faculty(request):
    teacher = Teacher.objects.all()
    context = {'teacher':teacher}
    return render(request, 'info/faculty.html',context)

def campus(request):
	return render(request, 'info/campus.html')

def contact(request):
	return render(request, 'info/contact.html')

def gallary(request):
	return render(request, 'info/gallary.html')

def noticesearch(request):

	try:
		query = request.GET.get('querynotice')
	except:
		query = None

	if query :
		query = request.GET.get('querynotice').lower()
		template = 'info/noticeresults.html'
		notresult = [item for item in Notice.objects.filter(title__icontains = query) if query in item.title.lower()]



	else:
		template = 'info/index.html'
		notresult = {}

	return render(request, template, {"notresult": notresult })


class AssignmentListView(LoginRequiredMixin,ListView):
    model = Assignment
    template_name = 'info/assignment_list.html' #<app>/<model>_<viewtype>.html
    context_objects_name = 'assignment'
    ordering = ['-published']
    paginate_by = 3 # pagination  (django provided )


class AssignmentDetailView(LoginRequiredMixin,DetailView):
    model = Assignment
    template_name = 'info/assignment_detail.html' #<app>/<model>_<viewtype>.html



def assignmentsearch(request):

	try:
		query = request.GET.get('queryassignment')
	except:
		query = None

	if query :
		query = request.GET.get('queryassignment').lower()
		template = 'info/assignmentresults.html'
		assresult = [item for item in Assignment.objects.filter(title__icontains = query) if query in item.title.lower()]


	else:
		template = 'info/index.html'
		assresult = {}

	return render(request, template, {"assresult": assresult })
