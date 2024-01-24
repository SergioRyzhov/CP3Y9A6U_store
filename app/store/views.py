from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import CreditOrder, Product
from .serializers import CreditOrderSerializer, ContractSerializer, ManufacturerSerializer, ProductSerializer


@api_view(['GET'])
def store_views(request, contract_id=None):
    """
    View for retrieving all manufacturer IDs with the given contract_id.
    :param request: The request object
    :param contract_id: The contract ID (default is None)
    :return: Response with a message and manufacturer IDs
    """
    if not contract_id:
        return Response({"message": f"Incorrect contract_id"})

    order_instance = CreditOrder.objects.filter(contract=contract_id)
    if not order_instance:
        return Response({"message": f"Data with contract_id {contract_id} not found"})
    products = Product.objects.filter(credit_order=order_instance[0])

    if not products:
        return Response({"message": f"Products not found"})
    manufacturer_ids = [product.manufacturer.id for product in products]
    return Response({"message": "Success", "manufacturer_ids": manufacturer_ids}, 200)


@api_view(['POST'])
def order_add(request):
    """
    Add an order using the POST method.
    """
    serializer = CreditOrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"message": "Success", "data": serializer.data}, 201)


@api_view(['POST'])
def contract_add(request):
    """
    Add a new contract using the POST method and return a success message and data.
    """
    serializer = ContractSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"message": "Success", "data": serializer.data}, 201)


@api_view(['POST'])
def manufacturer_add(request):
    """
    Add a new manufacturer using POST request.
    """
    serializer = ManufacturerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"message": "Success", "data": serializer.data}, 201)


@api_view(['POST'])
def product_add(request):
    """
    Add a new product using POST request.
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"message": "Success", "data": serializer.data}, 201)