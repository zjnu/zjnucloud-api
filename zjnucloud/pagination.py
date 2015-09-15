from rest_framework.pagination import PageNumberPagination
from rest_framework.compat import OrderedDict
from rest_framework.response import Response


class MyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

    def get_paginated_response(self, data):
        info = OrderedDict()
        info['count'] = self.page_size
        info['total'] = self.page.paginator.count
        info['previous'] = self.get_previous_link()
        info['next'] = self.get_next_link()
        info['result'] = data
        return Response(info)
