

def user_facebook_name(request):
    if request.user.is_authenticated:
        social_account = request.user.social_auth.all().first()
        if social_account:
            return {'user_name_bound': social_account.extra_data.get('name')}
        else:
            return {'user_name_bound': request.user.name}
    return {}
