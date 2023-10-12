"""
# Date Inputs

There are two kinds of date pickers in solara, a single date picker, and a date range picker. These are introduced on this page.

# InputDate
"""
import solara
from solara.website.utils import apidoc

from . import NoPage

title = "InputDate"


__doc__ += apidoc(solara.lab.components.input_date.InputDate.f)  # type: ignore
__doc__ += "# InputDateRange"
__doc__ += apidoc(solara.lab.components.input_date.InputDateRange.f)  # type: ignore

Page = NoPage
