from django.urls import reverse


def get_admin_change_view_url(obj: object) -> str:
    """
    Return the URL for the admin change view for the given object.
    """
    return reverse(
        'admin:{}_{}_change'.format(
            obj._meta.app_label,
            type(obj).__name__.lower()
        ),
        args=(obj.pk,)
    )
