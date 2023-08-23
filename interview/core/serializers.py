from rest_framework.views import APIView


class CustomAPIView(APIView):

    def filter_queryset(self, queryset):
        if not hasattr(self, 'filter_class'):
            return queryset

        if not self.filter_class:
            return queryset

        filter_serializer = self.filter_class(data=self.request.query_params)

        if not filter_serializer.is_valid():
            return queryset.model.objects.none()

        return queryset.filter(**filter_serializer.validated_data)
