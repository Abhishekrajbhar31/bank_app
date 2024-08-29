from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Branch , Bank
from .serializers import BranchSerializer , BankSerializer

# class BranchListView(APIView):
    
#     def get(self, request, format=None):
#         branches = Branch.objects.all()
#         serializer = BranchSerializer(branches, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_branches(request):
     brances = Branch.objects.all()
     serializer = BranchSerializer(brances, many=True)
     return Response(serializer.data, status=status.HTTP_200_OK)
 
@api_view(['GET'])
def get_bank(request):
    bank = Bank.objects.all()
    serializer = BankSerializer(bank , many=True)
    return Response(serializer.data , status=status.HTTP_200_OK)

@api_view(['POST'])
def create_bank(request):
    serializer = BankSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BranchDetailView(APIView):
    
#     def get(self, request, ifsc_code, format=None):
        # try:
        #     branch = Branch.objects.get(ifsc_code=ifsc_code)
        #     serializer = BranchSerializer(branch)
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # except Branch.DoesNotExist:
        #     return Response({"error": "Branch not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def get_branch(request,ifsc_code):
    try:
        branch = Branch.objects.get(ifsc_code=ifsc_code)
        serializer = BranchSerializer(branch)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Branch.DoesNotExist:
        return Response({"error": "Branch not found"}, status=status.HTTP_404_NOT_FOUND)

     

# class BranchCreateView(APIView):
    
#     def post(self, request):
#         serializer = BranchSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def create_branch(request):
    bank = BankSerializer(data=request.data)
    if bank.is_valid():
        bank.save()
        print(bank.data)
        bank_new = Bank.objects.get(id = bank.data['id'])
    else:
        print(bank.errors, " errordd")
    serializer = BranchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        branch = Branch.objects.get(id = serializer.data['id'])
        branch.bank = bank_new
        branch.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


