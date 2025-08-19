from django.http import JsonResponse

SAFE_METHODS = ["GET"]

class RoleRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        user = getattr(request, "user", None)

        if user and user.is_authenticated:
            if path.startswith("/api/users/") and user.role != "admin":
                return JsonResponse({"detail": "Forbidden"}, status=403)

            if path.startswith("/api/posts/"):
                if request.method in SAFE_METHODS:
                    return self.get_response(request)
                elif user.role == "viewer":
                    return JsonResponse({"detail": "Forbidden"}, status=403)

        return self.get_response(request)
