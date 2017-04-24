from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import AWS
from .forms import AWSForm, AWSHomeForm
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
import boto
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.db import connection

def aws(request):
    # aws_object = AWS()
    sum = 0
    user_id = request.user.id
    query = ("Select * from aws where user_id = %d" % (user_id))
    aws_result = AWS.objects.raw(query)
    # cursor = connection.cursor()
    # cursor.execute(query)
    # result = cursor.fetchall()
    for val in aws_result:
        sum = sum+1
    form = AWSForm(request.POST or None)
    if form.is_valid():
        if sum == 0:
            if request.method == 'GET':
                print "I am in get"
                context = {
                    "form": form,
                }

                return render_to_response("AWS_CP.html", context, context_instance=RequestContext(request))

            if request.method == 'POST':
                print "it is post"
                print request.POST
                aws_key = form.cleaned_data['aws_access_key']
                aws_secret = form.cleaned_data['aws_secret_key']
                instance = AWS(user_id = user_id, aws_access_key=aws_key, aws_secret_key=aws_secret)
                # instance = form.save(commit=False)
                # instance.user_id = user_id
                # user = User.objects.only('id').get(id = user_id)
                # print user
                # aws_instance = AWS.objects.create(user_id=user)
                # aws_instance.save()
                instance.save()
                print aws_key, aws_secret
                aws_create(request)
                return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))
    else:
        print "I am here in aws_home when entries are there"
        return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))


def aws_create(request):
    print "aws_home **************************"
    # if request.method == 'POST':
    # user_id = request.user.id
    # print user_id
    # # aws_model = AWS()
    # # print aws_model.all()
    # aws_access_key_id = ''
    # aws_secret_access_key = ''
    # ec2 = boto.connect_ec2(aws_access_key_id=aws_access_key_id,
    # aws_secret_access_key=aws_secret_access_key)
    # parsed_data = []
    # user_Data = {}
    # # checking all zones
    # # data   = list(ec2.get_all_zones())
    # list_data = list(boto.ec2.regions())
    # # dict_data = dict(list_data)
    # # print list_data
    # list_data = [(1, 'region1'), (2, 'region2'), (3,'region3')]
    # # data = {key: i for i , key in enumerate(list_data)}
    # form = AWSHomeForm(my_choices = list_data)
    # context = {
    # "form" : form,
    # }
    # aws_get_keys()
    # test = request.POST.get("zone", "region", "image", "min_count", "max_count", "key_name", "inst_type", "monitoring")
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        zone = request.POST.get("zone")
        region = request.POST.get("region")
        image = request.POST.get("image")
        min = request.POST.get("min")
        max = request.POST.get("max")
        key_name = request.POST.get("key_name")
        inst_type = request.POST.get("inst_type")
        check_status = request.POST.get("check_status")

        print zone, region, image, min, max, key_name, inst_type, check_status
        # response_data = {}
        # try:
        #     response_data['result'] = 'done!'
        #     response_data['message'] = test
        # except:
        #     response_data['result'] = 'nup!'
        #     response_data['message'] = "not correct"

    return render_to_response("aws_create.html", {}, context_instance = RequestContext(request))
    # return HttpResponse(json.dumps(response_data),content_type="application/json")


def aws_home(request):
    print "aws_inst **************************"
    # if request.method == 'POST':
    # user_id = request.user.id
    # print user_id
    # # aws_model = AWS()
    # # print aws_model.all()
    # aws_access_key_id = ''
    # aws_secret_access_key = ''
    # ec2 = boto.connect_ec2(aws_access_key_id=aws_access_key_id,
    # aws_secret_access_key=aws_secret_access_key)
    # parsed_data = []
    # user_Data = {}
    # # checking all zones
    # # data   = list(ec2.get_all_zones())
    # list_data = list(boto.ec2.regions())
    # # dict_data = dict(list_data)
    # # print list_data
    # list_data = [(1, 'region1'), (2, 'region2'), (3,'region3')]
    # # data = {key: i for i , key in enumerate(list_data)}
    # form = AWSHomeForm(my_choices = list_data)
    # context = {
    # "form" : form,
    # }
    # aws_get_keys()
    # test = request.POST.get("zone", "region", "image", "min_count", "max_count", "key_name", "inst_type", "monitoring")
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        selectOP = request.POST.get("selectOP")

        print selectOP

    return render_to_response("aws_home.html", {}, context_instance = RequestContext(request))
    # return HttpResponse(json.dumps(response_data),content_type="application/json")

def aws_delete(request):
    print "aws_delete **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        instance = request.POST.get("instance")

        print instance

    return render_to_response("aws_delete.html", {}, context_instance = RequestContext(request))


def aws_get_keys():
    aws = AWS.objects.raw("Select * from aws where user_id = 4")
    for val in aws:
        access_key = val.aws_access_key
        secret_key = val.aws_secret_key
        print access_key, secret_key
