from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .ssh_connection import SSHconnection
from .serializer import UserSerializer

class UserAPI(APIView):
    def get(self, request):
        users = User.objects.all() 
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  

    def post(self, request):
        user_id = request.data.get('id')
        command = request.data.get('command')
        try:
            user = User.objects.get(id=user_id)  
        except User.DoesNotExist:
            return render(request, './ssh_templates/command_output.html', {'output': "User not found."})

        host = user.IPaddress 
        
        sshobject = SSHconnection(host, user.username, user.password)
        
        try:
            output = sshobject.executecommand(command)  # Execute the command
        except Exception as e:
            return render(request, './ssh_templates/command_output.html', {'output': f"Error executing command: {str(e)}"})

        return render(request, './ssh_templates/command_output.html', {'output': output})
