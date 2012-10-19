#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

class TextHub(Hub):
    """
      TextHub builds a text based testing environment for the SLU, DM, and NLG
      components.
      It reads text from standard input and passes it in SLU and it outputs
      the text generated by a NLG component.
    """
    def __init__(self, cfg):

        self.cfg = cfg

    def run(self):
        pass


if __name__ == '__main__':
    pass
