import pytest
import os

from django.core import management


@pytest.mark.django_db
class TestSchemaGeneration:
    def test_generate_json_schema(self, settings):
        management.call_command("generate_json_schemas")

        schema_path = (
            f"{settings.STATICFILES_DIRS[0]}reporting/schemas/query_schema.json"
        )
        assert os.path.exists(schema_path)

        os.remove(schema_path)
