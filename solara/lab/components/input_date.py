import datetime as dt
from typing import Dict, List, Optional, Tuple, Union

import solara
import solara.lab


@solara.component
def InputDate(
    value: solara.Reactive[dt.date],
    label: str = "Pick a date",
    children: List[solara.Element] = [],
    open: Union[solara.Reactive[bool], bool] = False,
    date_format: str = "%Y/%m/%d",
    first_day_of_the_week: int = 1,
    style: Optional[Union[str, Dict[str, str]]] = None,
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
            lab.InputDate(
                date,
                children=[
                    solara.Row(children=controls, justify="end", style="width: 100%;")
                ],
                open=range_is_open,
                date_format="%A, %d. %B, %Y",
                style="width: 350px;",
            )
    ```

    ## Arguments

    * value: Reactive variable of type `datetime.date`, or `None`. This date is selected the first time the component is rendered.
    * label: Text used to label the text field that triggers the datepicker.
    * children: List of Elements to be rendered under the calendar. If empty, a close button is rendered.
    * open: Controls and communicates the state of the datepicker. If True, the datepicker is open. If False, the datepicker is closed.
    Intended to be used in conjunction with a custom set of controls to close the datepicker.
    * date_format: Sets the format of the date displayed in the text field. Defaults to `"%Y/%m/%d"`.
    *first_dat_of_the_week: Sets the first day of the week, as an `int` starting count from Sunday (`=0`). Defaults to `1`, which is Monday.
    """

    def str_and_format():
        return value.value.strftime(date_format) if value.value is not None else None

    date_str = solara.use_reactive(str_and_format())

    datepicker_is_open = solara.use_reactive(open)  # type: ignore
    style_flat = solara.util._flatten_style(style)

    def set_date_cast(new_value):
        date_value = dt.datetime.strptime(new_value, "%Y-%m-%d").date()
        value.value = date_value
        date_str.set(str_and_format())

    input = solara.v.TextField(
        label=label,
        value=date_str.value,
        on_v_model=set_date_cast,
        append_icon="mdi-calendar",
        style_=style_flat,
    )
    with solara.lab.Menu(
        activator=input,
        close_on_content_click=False,
        open=datepicker_is_open,
    ):
        with solara.v.DatePicker(
            v_model=value.value,
            on_v_model=set_date_cast,
            first_day_of_week=first_day_of_the_week,
            style_="width: 100%;",
        ):
            if len(children) > 0:
                for el in children:
                    solara.display(el)
            else:
                with solara.Row(justify="end", style="width: 100%"):
                    solara.Button("close", color="primary", on_click=lambda: datepicker_is_open.set(False))


@solara.component
def InputDateRange(
    value: solara.Reactive[Tuple[dt.date, dt.date]],
    label: str = "Select dates",
    children: List[solara.Element] = [],
    open: Union[solara.Reactive[bool], bool] = False,
    date_format: str = "%Y/%m/%d",
    first_day_of_the_week: int = 1,
    style: Optional[Union[str, Dict[str, str]]] = None,
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
            lab.InputDateRange(
                dates,
                children=[
                    solara.Row(children=controls, justify="end", style="width: 100%;")
                ],
                open=range_is_open,
            )
    ```

    ## Arguments

    * value: Reactive tuple with elements of type `datetime.date`. For an empty pre-selection of dates, pass a reactive empty tuple.
    * label: Text used to label the text field that triggers the datepicker.
    * children: List of Elements to be rendered under the calendar. If empty, a close button is rendered.
    * open: Controls and communicates the state of the datepicker. If True, the datepicker is open. If False, the datepicker is closed.
    Intended to be used in conjunction with a custom set of controls to close the datepicker.
    * date_format: Sets the format of the date displayed in the text field. Defaults to `"%Y/%m/%d"`.
    *first_dat_of_the_week: Sets the first day of the week, as an `int` starting count from Sunday (`=0`). Defaults to `1`, which is Monday.
    """
    date_strings = [date.strftime(date_format) for date in value.value]
    datepicker_is_open = solara.use_reactive(open)  # type: ignore
    style_flat = solara.util._flatten_style(style)

    def set_dates_cast(values):
        date_value = [dt.datetime.strptime(item, "%Y-%m-%d").date() for item in values]
        value.value = date_value  # type: ignore

    input = solara.v.TextField(
        label=label,
        value=" - ".join(date_strings),
        on_v_model=set_dates_cast,
        append_icon="mdi-calendar",
        readonly=True,
        style_="min-width: 300px;" + style_flat,
    )
    with solara.lab.Menu(
        activator=input,
        close_on_content_click=False,
        open=datepicker_is_open,
    ):
        with solara.v.DatePicker(
            v_model=value.value,
            on_v_model=set_dates_cast,
            range=True,
            first_day_of_week=first_day_of_the_week,
            style_="width: 100%;",
        ):
            if len(children) > 0:
                for el in children:
                    solara.display(el)
            else:
                with solara.Row(justify="end"):
                    solara.Button("close", color="primary", on_click=lambda: datepicker_is_open.set(False))
