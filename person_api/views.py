from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from person_api.models import Person
from person_api.serializers import PersonSerializer
from rest_framework import status


@api_view(['GET'])
def ApiOverview(request):
	"""
    Returns a list of available API endpoints and their corresponding URLs.
    """
	api_urls = {
		'all_persons': '/',
		'Search by name': '/?name=name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/person/pk/delete'
	}

	return Response(api_urls)

@api_view(['POST'])
def add_person(request):
    """
    Add a new person to the database.

    Args:
        request (Request): The HTTP request object.

    Returns:
        Response: The HTTP response object.

    Raises:
        ValidationError: If the data already exists in the database.
    """
    person = PersonSerializer(data=request.data)

    if person.is_valid():
        person.save()
        response = Response()
        
        response.data = {
            'message': 'Person Created Successfully',
            'data': person.data
        }
        return response
    else:
        return Response(person.errors, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])	
def view_persons(request):
	"""
    Retrieves a list of persons based on query parameters.
    Args:
        request (Request): The HTTP request object.
    Returns:
        Response: The HTTP response containing the serialized list of persons.
    Raises:
        Http404: If no persons are found.
    """
	# checking for the parameters from the URL
	if request.query_params:
		persons = Person.objects.filter(**request.query_params.dict())
	else:
		persons = Person.objects.all()

	# if there is something in persons else raise error
	if persons:
		serializer = PersonSerializer(persons, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
@api_view(['POST'])
def update_person(request, pk):
    """
    Update a Person object based on the given primary key.
    Args:
        request (Request): The request object containing the updated data.
        pk (int): The primary key of the Person object to be updated.
    Returns:
        Response: The updated data if successful, or a 404 status if the Person object does not exist or the data is invalid.
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    person = PersonSerializer(instance=person, data=request.data)

    if person.is_valid():
        person.save()
        response = Response()
        response.data = {
            'message': 'Person Updated Successfully',
            'data': person.data
        }
        return response
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_person(request, pk):
    """
    Delete a person by their primary key.
    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the person to delete.
    Returns:
        Response: The HTTP response indicating the success of the deletion.
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    person.delete()
    response = Response()
    response.data = {
            'message': 'Person Deleted Successfully',
        }
    return response
# Create your views here.
