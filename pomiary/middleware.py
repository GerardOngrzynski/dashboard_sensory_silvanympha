# plik: pomiary/middleware.py

from django.db import connection


class SchemaMiddleware:
    AVAILABLE_SCHEMAS = ['daleszyce', 'gosciecice']
    DEFAULT_SCHEMA = 'daleszyce'

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        selected_schema = request.GET.get('schema', self.DEFAULT_SCHEMA)

        if selected_schema not in self.AVAILABLE_SCHEMAS:
            selected_schema = self.DEFAULT_SCHEMA

        with connection.cursor() as cursor:
            cursor.execute(f"SET search_path TO {selected_schema}, public")

        response = self.get_response(request)
        return response