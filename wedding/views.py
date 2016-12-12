from django.shortcuts import render
from django.http import HttpResponse
import json
import pprint
from .models import Guest

def guest_to_json(obj):
  result = {'data': {
            'type': 'guest',
            'id': obj.id,
            'attributes': {
              'invitee': obj.invitee,
              'attending-max': obj.attending_max,
              'attending-num': obj.attending_num,
              'guest-names': obj.guest_names,
              'entree1': obj.entree1,
              'entree2': obj.entree2,
              'hotel': obj.hotel,
              'shuttle-to-time': obj.shuttle_to_time,
              'shuttle-from-time': obj.shuttle_from_time,
              'attending': obj.attending,
              'responded': obj.responded
            }
          }
        }

  return json.dumps(result)

def guests(request):
  print json.dumps(request.GET)
  if request.GET.get('filter[invitee]'):
    invitee = request.GET.get('filter[invitee]')
    obj = Guest.objects.get(invitee=invitee)

    if obj:
      result = guest_to_json(obj)
      status = 200

    else:
      result = {"errors":[
          {
            "title":"Could not find guest for given invitee.",
            "code":"API_ERR",
            "status":"404"
          }
        ]}

      result = json.dumps(result)
      status = 404

  else:
    result = {"errors":[
          {
            "title":"Request type not implemented.",
            "code":"API_ERR",
            "status":"404"
          }
        ]}

    result = json.dumps(result)

    status = 404

  return HttpResponse(result,
      content_type="application/json", status=status)


def guests_by_id(request, guest_id):
  obj = Guest.objects.get(id=guest_id)
  
  if obj:
    result = guest_to_json(obj)
    status = 200
  else:
    result = {"errors":[
        {
          "title":"Could not find guest for given id.",
          "code":"API_ERR",
          "status":"404"
        }
      ]}

    result = json.dumps(result)
    status = 404

  return HttpResponse(result,
      content_type="application/json", status=status)