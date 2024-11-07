from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ComentSerializer
from .models import Coments


#Aqui creo la clase para añadir los comentarios
class AddComment(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        serializer = ComentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Código 201 para creación exitosa
        return Response(serializer.errors, status=400)  # Código 400 para errores de validación
    
class ViewComments(APIView):
    def get(self,request):
        view = Coments.objects.all()
        serializers = ComentSerializer(view,many=True) #many es para serializar varios comentarios
        return Response(serializers.data)
    
class ViewsComents(APIView):
    def get(self,request,name):
        view = Coments.objects.filter(name=name)
        serializers = ComentSerializer(view,many=True) #many es para serializar varios comentarios
        return Response(serializers.data)
    
class DeleteComents(APIView):
    def delete(self,request):
        Coments.objects.all().delete()
        return Response("Se elimino correctamente")
    
class DeleteComent(APIView):
    def delete(self,request,name):
        Coments.objects.get(name=name).delete()
        return Response("Se elimino ese comentario")

