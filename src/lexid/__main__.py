#!/usr/bin/env python
# This file is part of the lexid project
# https://gitlab.com/mbarkhau/lexid
#
# Copyright (c) 2020 Manuel Barkhau (mbarkhau@gmail.com) - MIT License
# SPDX-License-Identifier: MIT
import sys

import click

from lexid import next_id
from lexid import ord_val

try:
    import pretty_traceback

    pretty_traceback.install()
except ImportError:
    pass  # no need to fail because of missing dev dependency

click.disable_unicode_literals_warning = True


@click.command()
@click.option('-n'     , default=1)
@click.option('--debug', is_flag=True, default=False)
@click.argument("start_id", default="1001")
def main(start_id: str = "1001", n: int = 1, debug: bool = False) -> None:
    """Increment a lexid."""
    if debug:
        print(f"{'lexical':<13} {'numerical':>12}")

    _curr_id = start_id

    for _ in range(n):
        try:
            _next_id = next_id(_curr_id)
        except OverflowError as err:
            sys.stderr.write(f"OverflowError: {err}")
            sys.exit(1)

        if debug:
            print(f"{_curr_id:<13} {ord_val(_curr_id):>12}")
        else:
            print(_curr_id)

        _curr_id = _next_id