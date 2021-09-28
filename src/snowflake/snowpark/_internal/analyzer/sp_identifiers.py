#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2021 Snowflake Computing Inc. All right reserved.
#
from typing import Optional


class IdentifierWithDatabase:
    database: Optional[str] = None


class TableIdentifier(IdentifierWithDatabase):
    def __init__(self, table: str, database_name: Optional[str] = None):
        self.table = table
        self.database = database_name