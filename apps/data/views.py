from rest_framework import generics
from .models import CsvFile
from .serializers import CsvSerializer, ProcessedFileSerializer
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import json


class CvsLoadView(generics.CreateAPIView):
    queryset = CsvFile.objects.all()
    serializer_class =CsvSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['csv']
        df = pd.read_csv(file, delimiter=';', skipinitialspace=True)
        d2 = df.groupby(["customer", ])[["total"]].sum().sort_values(by='total', ascending=True)
        d3 = df.groupby(['customer', ]).agg({'item': lambda x: ' '.join(list(set(x)))})
        d4 = df.groupby(['customer']).agg({'customer': lambda x: list(x)[0]})
        result = pd.concat([d2, d3, d4], axis=1,).reindex(d2.index)
        result = result[-5:].rename(columns={'customer': 'username', 'total': 'spent_money', "item": 'gems'})
        json_list = json.loads(json.dumps(list(result.T.to_dict().values())))
        for dic in json_list:
            CsvFile.objects.create(**dic)

        return Response({'message': 'OK-the file was processed without errors'}, status=status.HTTP_201_CREATED)


class ProcessedFileView(generics.ListAPIView):
    queryset = CsvFile.objects.all().order_by('-spent_money')[:5]
    serializer_class =ProcessedFileSerializer