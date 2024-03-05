# Path: wikitech_dms/members/urls.py
from django.utils import timezone
from django.shortcuts import render, redirect,get_object_or_404
from .models import Membership, ProjectInfo, Staff, Event, EventAttendance
from .forms import MembershipForm, ProjectInfoForm, StaffForm, EventForm, EventAttendanceForm
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def member_list(request):
    members = Membership.objects.all()
    return render(request, 'member_list.html', {'members': members})

def member_detail(request, pk):
    member = get_object_or_404(Membership, pk=pk)
    return render(request, 'member_detail.html', {'member': member})


def add_member(request):
    if request.method == "POST":
        form = MembershipForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.author = request.user
            member.published_date = timezone.now()
            member.save()
            return redirect('members')
    else:
        form = MembershipForm()
    return render(request, 'new_member.html', {'form': form})

def member_edit(request, pk):
    member = Membership.objects.get(pk=pk)
    if request.method == "POST":
        form = MembershipForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save(commit=False)
            member.author = request.user
            member.published_date = timezone.now()
            member.save()
            return redirect('members')
    else:
        form = MembershipForm(instance=member)
    return render(request, 'edit_member.html', {'form': form})

# def member_delete(request, pk):
#     Membership.objects.get(pk=pk).delete()
#     return redirect('member_list')

def delete_member(request, pk):
    member = get_object_or_404(Membership, pk=pk)
    # member = Membership.objects.get(pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('members')  # Corrected redirect statement
    return render(request, 'delete_member.html', {'member': member})

