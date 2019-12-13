from __future__ import unicode_literals
from frappe import _

def get_data():

    return [
        {
            "label": _("Fieldservice"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Service Report",
                    "label": _("Service Report"),
                }
            ]
        }
    ]