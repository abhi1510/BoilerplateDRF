from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductList(APIView):
    def get(self, request):
        return Response("This is to get all the products.", status=status.HTTP_200_OK)

    def post(self, request):
        return Response("This is to create a Product.", status=status.HTTP_202_ACCEPTED)

class ProductDetails(APIView):
    def get(self, request, product_id):
        return Response("This is to get a product details.", status=status.HTTP_200_OK)

    def put(self, request, product_id):
        return Response("This is to update a product.", status=status.HTTP_202_ACCEPTED)

    def delete(self, request, product_id):
        return Response("This is to delete a product.", status=status.HTTP_204_NO_CONTENT)
