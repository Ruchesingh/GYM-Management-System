from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from dietPlan.api.serializer import DietPlanSerializer
from dietPlan.models import DietPlan




@extend_schema(tags=["Diet Plan"])
class DietPlanView(GenericAPIView):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer

    @extend_schema(responses=DietPlanSerializer)
    def get(self, request):
        diet_plan = DietPlan.objects.all()
        serializer = DietPlanSerializer(diet_plan, many=True)
        return Response(serializer.data, 200)

    @extend_schema(request=DietPlanSerializer, responses=DietPlanSerializer)
    def post(self, request):
        data = request.data
        serializer = DietPlanSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Diet Plan Successfully Created"}, 201)

        return Response(serializer.errors, 422)


@extend_schema(tags=["Diet Plan"])
class DietPlanUpdateAndDelete(GenericAPIView):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer

    @extend_schema(request=DietPlanSerializer, responses=DietPlanSerializer)
    def put(self, request, pk):
        diet_plan = DietPlan.objects.get(id=pk)

        serializer = DietPlanSerializer(diet_plan, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Diet Plan Updated Successfully"}, 200)
        return Response(serializer.errors, 422)

    @extend_schema(responses=None)
    def delete(self, request, pk):
        diet_plan = DietPlan.objects.filter(id=pk)

        diet_plan.delete()
        return Response({"message": "Diet Plan Deleted Successfully"}, 200)