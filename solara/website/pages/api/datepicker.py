"""
# DatePicker

There are two kinds of date pickers in solara, a single date picker, and a date range picker. These are introduced on this page.

# DatePicker
"""
import solara
from solara.website.utils import apidoc

from . import NoPage

title = "DatePicker"


__doc__ += apidoc(solara.lab.components.datepicker.DatePicker.f)  # type: ignore
__doc__ += "# DateRangePicker"
__doc__ += apidoc(solara.lab.components.datepicker.DateRangePicker.f)  # type: ignore

Page = NoPage
