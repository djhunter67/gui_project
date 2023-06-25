"""Keep track of all of the discharge\
instructions and medications that a patient has been given."""

#!/usr/bin/env python3  # noqa: E265
# -*- coding: utf-8 -*-

import subprocess

import dearpygui.dearpygui as dpg

from .universal.helpers import screen_size

ROWS, COLUMNS = screen_size(subprocess)


def main():
    """Main function of the program."""

    dpg.create_context()
    dpg.create_viewport(
        title="Medical Tracker",
        width=COLUMNS*5,
        height=ROWS*5,
    )

    with dpg.window(
            tag="Primary_Window",
            label="Primary_Window",
            pos=(
                0,
                0
            ),
            height=dpg.get_viewport_height(),
            width=dpg.get_viewport_width(),
    ):

        with dpg.child_window(
                tag="left_top_quad",
                label="",
                pos=(
                    0,
                    0
                ),
                height=dpg.get_item_height(item="Primary_Window")//2,
                width=dpg.get_item_width(item="Primary_Window")//2,
        ):

            dpg.add_button(
                tag="left_button",
                label="left_button",
                pos=(
                    0,
                    0
                ),
                height=dpg.get_item_height(item="left_top_quad"),
                width=dpg.get_item_width(item="left_top_quad"),
                callback=lambda: print("Left_Button pressed."),
            )

        with dpg.child_window(
                tag="right_top_quad",
                label="",
                pos=(
                    0,
                    dpg.get_item_height(item="Primary_Window")/2
                ),
                height=dpg.get_item_height(item="Primary_Window")//2,
                width=dpg.get_item_width(item="Primary_Window")//2,
        ):

            dpg.add_button(
                tag="left_button2",
                label="left_button2",
                pos=(
                    0,
                    0
                ),
                height=dpg.get_item_height(item="right_top_quad"),
                width=dpg.get_item_width(item="right_top_quad"),
                callback=lambda: print("Left_Button2 pressed."),
            )

        with dpg.child_window(
                tag="bottom_left_quad",
                label="",
                pos=(
                    dpg.get_item_width(item="Primary_Window")/2,
                    0
                ),
                height=dpg.get_item_height(item="Primary_Window")//2,
                width=dpg.get_item_width(item="Primary_Window")//2,
        ):

            dpg.add_button(
                tag="right_button3",
                label="right_button3",
                pos=(
                    0,
                    0
                ),
                height=dpg.get_item_height(item="bottom_left_quad"),
                width=dpg.get_item_width(item="bottom_left_quad"),
                callback=lambda: print("Right_Button3 pressed."),
            )

        with dpg.child_window(
                tag="bottom_right_quad",
                label="",
                pos=(
                    dpg.get_item_width(item="Primary_Window")/2,
                    dpg.get_item_height(item="Primary_Window")/2
                ),
                height=dpg.get_item_height(item="Primary_Window")//2,
                width=dpg.get_item_width(item="Primary_Window")//2,
        ):

            dpg.add_button(
                tag="right_button4",
                label="right_button4",
                pos=(
                    0,
                    0
                ),
                height=dpg.get_item_height(item="bottom_right_quad"),
                width=dpg.get_item_width(item="bottom_right_quad"),
                callback=lambda: print("Right_Button4 pressed."),
            )

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary_Window", True)
    # below replaces, start_dearpygui()
    while dpg.is_dearpygui_running():

        height = dpg.get_item_height(item="Primary_Window")
        width = dpg.get_item_width(item="Primary_Window")

        dpg.configure_item(
            item="left_top_quad",
            height=height//2,
            width=width//2
        )
        dpg.configure_item(
            item="right_top_quad",
            height=height//2,
            width=width//2
        )
        dpg.configure_item(
            item="bottom_left_quad",
            height=height//2,
            width=width//2
        )
        dpg.configure_item(
            item="bottom_right_quad",
            height=height//2,
            width=width//2
        )

        # Adjust the button sizes as well
        dpg.configure_item(
            item="left_button",
            height=height//2,
            width=width//2
        )
        dpg.configure_item(
            item="left_button2",
            height=height//2,
            width=width//2
        )
        dpg.configure_item(
            item="right_button3",
            height=height//2,
            width=width//2
        )
        dpg.configure_item(
            item="right_button4",
            height=height//2,
            width=width//2
        )

        # Print the frame rate
        print(f"Frame Rate: {dpg.get_frame_rate()}")

        dpg.render_dearpygui_frame()

    dpg.destroy_context()


if __name__ == '__main__':
    main()
