def user_directory(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)