import datetime as dt
from typing import List, Union

import solara
import solara.lab


@solara.component
def DatePicker(
    date: solara.Reactive[dt.date],
    children: List[solara.Element] = [],
    open: Union[solara.Reactive[bool], bool] = False,
    date_format: str = "%Y-%m-%d",
):
    """
    Show a textfield, which when clicked, opens a datepicker. The input date should be a reactive variable of type `datetime.date`.

    ## Basic Example

    ```solara
    import solara
    import solara.lab as lab


    @solara.component
    def Page():
        date = solara.use_reactive(None)
        range_is_open = solara.use_reactive(False)

        controls = [
            solara.Button(
                label="Book",
                color="primary",
                on_click=lambda: range_is_open.set(not range_is_open.value),
            )
        ]

        with solara.Column():
            lab.DatePicker(
                date,
                [solara.Row(children=controls, justify="end", style="width: 100%;")],
                range_is_open,
            )
    ```

    ## Arguments

    * date: Reactive variable of type `datetime.date`, or `None`. This date is selected the first time the component is rendered.
    * children: List of Elements to be rendered under the calendar. If empty, a close button is rendered.
    * open: Controls and communicates the state of the datepicker. If True, the datepicker is open. If False, the datepicker is closed.
    Intended to be used in conjunction with a custom set of controls to close the datepicker.
    """
    date_str = date.value.strftime(f"{date_format}") if date.value is not None else None

    datepicker_is_open = solara.use_reactive(open)  # type: ignore

    def set_date_cast(value):
        date_value = dt.datetime.strptime(value, f"{date_format}").date()
        date.value = date_value

    input = solara.v.TextField(
        label="Test",
        value=date_str,
        on_v_model=set_date_cast,
        append_icon="mdi-calendar",
        readonly=True,
    )
    with solara.lab.Menu(
        activator=input,
        close_on_content_click=False,
        open=datepicker_is_open,
    ):
        with solara.v.DatePicker(v_model=date_str, on_v_model=set_date_cast):
            if len(children) > 0:
                for el in children:
                    solara.display(el)
            else:
                with solara.Row(justify="end", style="width: 100%"):
                    solara.Button("close", color="primary", on_click=lambda: datepicker_is_open.set(False))


@solara.component
def DateRangePicker(
    dates: solara.Reactive[List[dt.date]],
    children: List[solara.Element] = [],
    open: Union[solara.Reactive[bool], bool] = False,
    date_format: str = "%Y-%m-%d",
):
    """
    Show a textfield, which when clicked, opens a datepicker that allows users to select a range of dates by choosing a starting and ending date.
    The input dates should be stored in a reactive list of type `datetime.date`. The list should contain either precisely two elements.
    For an empty pre-selection of dates, pass a reactive empty list.

    ## Basic Example

    ```solara
    import solara
    import solara.lab as lab


    @solara.component
    def Page():
        dates = solara.use_reactive([])
        range_is_open = solara.use_reactive(False)

        controls = [
            solara.Button(
                label="Book",
                color="primary",
                on_click=lambda: range_is_open.set(not range_is_open.value),
            )
        ]

        with solara.Column():
            lab.DateRangePicker(
                dates,
                [solara.Row(children=controls, justify="end", style="width: 100%;")],
                range_is_open,
            )
    ```

    ## Arguments

    * dates: Reactive list with elements of type `datetime.date`. For an empty pre-selection of dates, pass a reactive empty list.
    * children: List of Elements to be rendered under the calendar. If empty, a close button is rendered.
    * open: Controls and communicates the state of the datepicker. If True, the datepicker is open. If False, the datepicker is closed.
    Intended to be used in conjunction with a custom set of controls to close the datepicker.
    """
    date_strings = [date.strftime(f"{date_format}") for date in dates.value]
    datepicker_is_open = solara.use_reactive(open)  # type: ignore

    def set_dates_cast(values):
        date_value = [dt.datetime.strptime(value, f"{date_format}").date() for value in values]
        dates.value = date_value

    input = solara.v.TextField(
        label="Test", value=" - ".join(date_strings), on_v_model=set_dates_cast, append_icon="mdi-calendar", readonly=True, style_="min-width: 280px;"
    )
    with solara.lab.Menu(
        activator=input,
        close_on_content_click=False,
        open=datepicker_is_open,
    ):
        with solara.v.DatePicker(v_model=date_strings, on_v_model=set_dates_cast, range=True):
            if len(children) > 0:
                for el in children:
                    solara.display(el)
            else:
                with solara.Row(justify="end"):
                    solara.Button("close", color="primary", on_click=lambda: datepicker_is_open.set(False))
