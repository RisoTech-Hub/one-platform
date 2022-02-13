from rest_framework.filters import SearchFilter

from one.components.utils import _get_name_fields


class AllSearchFilter(SearchFilter):
    """Search all field of model"""

    def get_search_fields(self, view, request):
        """
        Search fields are obtained from the view, but the request is always
        passed to this method. Sub-classes can override this method to
        dynamically change the search fields based on request content.
        """
        fields = getattr(view, "search_fields", None)
        if not fields:
            fields = _get_name_fields(
                view.model._meta.get_fields(include_parents=False), ["id"]
            )
        return fields if fields else None
