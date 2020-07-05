import i6

import pytest
import os


def test_cli():
    i6.cli(menu=False).run()
