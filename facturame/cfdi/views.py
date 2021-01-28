from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .serializers import CfdiSerializer
from .models import CfdiModel


DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 2

class CfdiPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_pages': self.page.paginator.num_pages,
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)), # can not set default = self.page
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'results': data
        })

class CfdiView(generics.ListAPIView):
    queryset = CfdiModel.objects.all().order_by('-date_issued')
    serializer_class = CfdiSerializer
    pagination_class = CfdiPagination

