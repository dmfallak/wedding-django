from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pprint
from .models import Guest, ShuttleFrom, ShuttleTo

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
              'side': obj.side,
              'hotel': obj.hotel,
              'shuttle-to-time': obj.shuttle_to_time,
              'shuttle-from-time': obj.shuttle_from_time,
              'attending': obj.attending,
              'responded': obj.responded
            }
          }
        }

  return json.dumps(result)

def json_to_guest(json_string):
  obj = json.loads(json_string)

  guest = Guest()

  guest.id = obj['id']
  guest.invitee = obj['attributes']['invitee']
  guest.attending_max = obj['attributes']['attending-max']
  guest.attending_num = obj['attributes']['attending-num']
  guest.guest_names = obj['attributes']['guest-names']
  guest.entree1 = obj['attributes']['entree1']
  guest.entree2 = obj['attributes']['entree2']
  guest.side = obj['attributes']['side']
  guest.hotel = obj['attributes']['hotel']
  guest.shuttle_to_time = obj['attributes']['shuttle-to-time']
  guest.shuttle_from_time = obj['attributes']['shuttle_from_time']
  guest.attending = obj['attributes']['attending']
  guest.responded = obj['attributes']['responded']

  return guest

def shuttle_to_to_json(obj):
  result = {'type': 'shuttleFrom',
            'id': obj.id,
            'attributes': {
              'time': obj.time,
              'seats-max': obj.seats_max,
              'seats-free': obj.seats_free
            }
          }

  return result

def shuttle_from_to_json(obj):
  result = {'type': 'shuttleTo',
            'id': obj.id,
            'attributes': {
              'time': obj.time,
              'seats-max': obj.seats_max,
              'seats-free': obj.seats_free
            }
          }

  return result

def guests(request):
  print json.dumps(request.GET)
  if request.GET.get('invitee'):
    invitee = request.GET.get('invitee')
    obj = Guest.objects.filter(invitee=invitee)

    if obj.count() > 0:
      result = guest_to_json(obj.first())
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


@csrf_exempt
def guests_by_id(request, guest_id):
  obj = Guest.objects.get(id=guest_id)

  if request.method == 'GET':
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
  elif request.method == 'PATCH':
    body_obj = json.loads(request.body)

    obj.invitee = body_obj['data']['attributes']['invitee']
    obj.attending_max = body_obj['data']['attributes']['attending-max']
    obj.attending_num = body_obj['data']['attributes']['attending-num']
    obj.guest_names = body_obj['data']['attributes']['guest-names']
    obj.entree1 = body_obj['data']['attributes']['entree1']
    obj.entree2 = body_obj['data']['attributes']['entree2']
    obj.side = body_obj['data']['attributes']['side']
    obj.hotel = body_obj['data']['attributes']['hotel']
    obj.shuttle_to_time = body_obj['data']['attributes']['shuttle-to-time']
    obj.shuttle_from_time = body_obj['data']['attributes']['shuttle-from-time']
    obj.attending = body_obj['data']['attributes']['attending']
    obj.responded = body_obj['data']['attributes']['responded']

    obj.save()

    return HttpResponse()


def shuttle_froms(request):
  froms = ShuttleFrom.objects.filter()

  resp_list = []

  for obj in froms:
    resp_list.append(shuttle_from_to_json(obj))

  return HttpResponse(json.dumps({"data": resp_list}), content_type="application/json")

def shuttle_tos(request):
  tos = ShuttleTo.objects.filter()

  resp_list = []

  for obj in tos:
    resp_list.append(shuttle_to_to_json(obj))

  return HttpResponse(json.dumps({"data": resp_list}), content_type="application/json")
