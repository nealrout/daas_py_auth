from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import PermissionDenied

class FacilityPermission(BasePermission):
    def has_permission(self, request, view):
        auth = JWTAuthentication()
        user, token = auth.authenticate(request) or (None, None)

        if not user or not token:
            return False

        # Extract facilities from JWT claims
        facilities_claim = token.get("facilities", [])

        # Get requested facility (from query params, headers, or body)
        requested_facility = request.query_params.get("facility")

        if requested_facility not in facilities_claim:
            raise PermissionDenied("You do not have access to this facility.")

        return True
