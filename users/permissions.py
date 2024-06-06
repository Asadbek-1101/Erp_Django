from django.contrib.auth.mixins import AccessMixin

class AdminRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an admin."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.user_role != 'admin':
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class StudentRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an admin."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.user_role != 'student':
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class TeacherRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an admin."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.user_role != 'teacher':
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)