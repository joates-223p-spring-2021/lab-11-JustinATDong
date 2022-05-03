#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:01:03 2022

@author: justindong
"""

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)