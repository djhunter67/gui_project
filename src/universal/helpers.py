#!/usr/bin/env python3  # noqa: E265

import subprocess


def screen_size(tool: subprocess.Popen) -> tuple[int, int]:
    """Get the screen size of the current monitor."""

    rows, columns = tool.check_output(['stty', 'size']).split()
    return int(rows), int(columns)


def main():
    """Test function for the universal.helper module."""

    # Get the resolution of the current monitor
    rows, columns = subprocess.check_output(['stty', 'size']).split()

    print(f"rows: {int(rows)}, columns: {int(columns)}")


if __name__ == '__main__':
    main()
