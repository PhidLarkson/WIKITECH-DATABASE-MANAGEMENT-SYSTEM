from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from django.contrib.auth.decorators import login_required
from .forms import MembershipForm


# Create your views here.
@login_required
def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'Member': members})

@login_required
def member_details(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'view_member.html', {'member': member})

# add a 
@login_required
def add_member(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            member.author = request.user  # Set the author before saving
            member.save()
            return redirect('member_list')
    else:
        form = MembershipForm()
    return render(request, 'new_member.html', {'form': form})

# to remove members
@login_required
def remove_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('Member') 
    # return render(request, 'delete_member.html', {'member': member})


# update member info
@login_required
def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MembershipForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_details', pk=member.pk)
    else:
        form = MembershipForm(instance=member)
    return render(request, 'edit_member.html', {'form': form, 'member': member})