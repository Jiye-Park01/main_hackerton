from django.shortcuts import render, get_object_or_404, redirect
from .models import Group, Membership
from django.contrib.auth.decorators import login_required
from users.models import Profile

def group_detail(request, group_id):
    group = get_object_or_404(Group, id = group_id)
    return render(request, 'groups/group_detail.html', {group : 'group'})

@login_required
def join_group(request, group_id):
    group = get_object_or_404(Group, group_id)
    profile = get_object_or_404(Profile, user=request.user)
    if group.memberships.count() < group.max_members:
        Membership.objects.get_or_create(profile=profile, group=group)
    return redirect('group_detail', group_id=group_id)