# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from types import SimpleNamespace


def test_query_schema_includes_tmp_table_name():
    """QuerySchema must serialize tmp_table_name so the UI column is populated."""
    from superset.queries.schemas import QuerySchema

    query = SimpleNamespace(
        tmp_table_name="tmp_my_table",
        tab_name="tab1",
        status="success",
        rows=10,
        sql="SELECT 1",
        executed_sql="SELECT 1",
        schema="public",
        tracking_url=None,
        id=1,
        start_time=0.0,
        end_time=1.0,
        start_running_time=0.0,
        changed_on=None,
        database=None,
        sql_tables=[],
        user=None,
    )

    schema = QuerySchema()
    result = schema.dump(query)

    assert "tmp_table_name" in result
    assert result["tmp_table_name"] == "tmp_my_table"


def test_query_schema_tmp_table_name_none():
    """QuerySchema serializes tmp_table_name even when it is None."""
    from superset.queries.schemas import QuerySchema

    query = SimpleNamespace(
        tmp_table_name=None,
        tab_name="",
        status="success",
        rows=0,
        sql="",
        executed_sql="",
        schema=None,
        tracking_url=None,
        id=2,
        start_time=0.0,
        end_time=0.0,
        start_running_time=0.0,
        changed_on=None,
        database=None,
        sql_tables=[],
        user=None,
    )

    schema = QuerySchema()
    result = schema.dump(query)

    assert "tmp_table_name" in result
    assert result["tmp_table_name"] is None
