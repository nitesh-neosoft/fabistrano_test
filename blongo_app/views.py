from django.shortcuts import render
from mongoengine import *
from models import BlogCollection
import datetime
from django.http import JsonResponse
# import json
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect
# from django import forms


# from django.views.generic import DeleteView


# class DeletePostView(DeleteView):
#     model = BlogCollection
#     template_name = 'delete.html'

#     def get_success_url(self):
#         return reverse('post_delete')



def date_calculate():
	'''Method to Calculate Start Date and End Date for Searching Records.'''

	# Taking Oldest updated record's datetime  and current datetime
	first_blog_obj = BlogCollection.objects.order_by('last_updated').first()
	if first_blog_obj:
		start_date = first_blog_obj.last_updated
	else:
		start_date = datetime.datetime.now()
	end_date = datetime.datetime.now()
	final_start_date = start_date.strftime("%Y-%m-%dT%H:%M:%S")
	final_end_date = end_date.strftime("%Y-%m-%dT%H:%M:%S")
	return final_start_date, final_end_date

def index(request):
	''' Method for Adding blogs as well as for showing existing blogs'''
	print "INDEX ENTEREDDDD"
	if request.method == "POST":
		print "INDEX POST ENTEREDDDDDD===", request.POST['search_start_time']

		start_time = request.POST['search_start_time']
		end_time = request.POST['search_end_time']

		print "###", len(start_time)
		print "###", type(start_time)

		if not start_time and not end_time:
			print "!!!!!!!"
			# raise forms.ValidationError("Invalid Start Date and End Date.")
			raise ValidationError(_("Invalid Start Date and End Date."), code = "invalid")
		elif not start_time:
			print "*******"
			raise ValidationError(_("Invalid Start Date."),
							code = "invalid")
		elif not end_time:
			raise ValidationError(_("Invalid End Date."))

		print "AFTER=======", start_time



		final_start_time = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M")
		final_end_time = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M")

		print "AFTER FINALLLLLLL=======", final_start_time

		blog_objs = BlogCollection.objects(last_updated__gte = final_start_time,
										   last_updated__lte = final_end_time)

		context = {
				'blog_objs': blog_objs,
				'start_date': start_time,
				'end_date': end_time,
			  }




		# POST method gets called on click of 'ADD POST' button.
		# Taking values entered by user
		# req_title = request.POST['title']
		# req_content = request.POST['content']

		# # Creating record in DB with fields.
		# blog_coll_obj = BlogCollection(title = req_title)
		# blog_coll_obj.content = req_content
		# blog_coll_obj.last_updated = datetime.datetime.now()
		# blog_coll_obj.save()

	# Taking all documents from collection
	elif request.method == "GET":
		print "INDEX GETTTT ENTEREDDDDDD==="
		blog_objs = BlogCollection.objects

	# final_start_date, final_end_date = date_calculate()

		context = {
					'blog_objs': blog_objs,
					# 'start_date': final_start_date,
					# 'end_date': final_end_date,
				  }
	return render(request, "index.html", context)


def create(request):
	''' Method for adding Blogs/Posts.'''
	print "CREATE ENTEREDDDD"
	
	if request.method == "POST":
		# POST method gets called on click of 'ADD POST' button.
		# Taking values entered by user
		create_req_title = request.POST['title']
		create_req_content = request.POST['content']

		# Creating record in DB with fields.
		new_blog_obj = BlogCollection(title = create_req_title)
		new_blog_obj.content = create_req_content
		new_blog_obj.last_updated = datetime.datetime.now()
		new_blog_obj.save()
		# template = "index.html"	# show home page template after adding post
		# Redirect to view named as "post-index".
		return redirect("post_index")
	else:
		template = "create.html"  # default template to show
		all_blog_objs = BlogCollection.objects	# Taking All objects for displaying in table.
		# final_start_date, final_end_date = date_calculate()

		context={
				'blog_objs': all_blog_objs,
				# 'start_date': final_start_date,
				# 'end_date': final_end_date,
				}
	
		return render(request, template, context)

def update(request):
	'''Method for showing Existing Record which we want to update
	   as well as updating the same and going back to Home Page 
	'''
	# rec_id = eval("request." + request.method + "['id']")
	# blog_inst = BlogCollection.objects(id = rec_id)[0]
	print "UPDATEE ENTEREDDDD"
	if request.method == 'POST':
		# method for updating record
		req_id = request.POST['u_id']
		blog_inst = BlogCollection.objects(id = req_id)[0]
		blog_inst.title = request.POST['u_title']
		blog_inst.content = request.POST['u_content']
		blog_inst.last_updated = datetime.datetime.now()
		blog_inst.save()

		# template = "index.html"
		#Date Calculation
		# final_start_date, final_end_date = date_calculate()
		# context = {
		# 			'blog_objs': BlogCollection.objects,
		# 			# 'start_date': final_start_date,
		# 			# 'end_date': final_end_date,
		# 			}
		return redirect("post_index")
	else:
		# method for showing record to be updated
		req_id = request.GET['update_id']
		blog_inst = BlogCollection.objects(id = req_id)[0]
		template = "update.html"
		context = {'u_blog_obj': blog_inst}
		return render(request, template, context)


# @csrf_protect
# def delete(request, pk):
# 	# print "GET BODY", request.GET
# 	print "METHOD====", request.method
# 	print "PKKKKK======", pk
# 	blog_inst = BlogCollection.objects(id = pk)
# 	# blog_obj = get_object_or_404(BlogCollection, pk=pk)
# 	print "BLOG OBJJJJJJJ ======= ", blog_inst
# 	# req_id = eval("request." + request.method + "['delete_id']")
# 	data = {}

# 	if request.method == 'POST':
# 		print "POST ENTEREDDDDD"
# 		blog_obj.delete()
# 		response_data = {
# 						  'blog_objs': BlogCollection.objects,
# 						  'start_date': final_start_date,
# 						  'end_date': final_end_date,
# 						}

# 		data['html_book_list'] = render_to_string('index.html', response_data)
# 	else:
# 		print "ELSEEEEEE"
# 		context = {'blog': blog_inst}
# 		data['html_form'] = render_to_string('partial_post_delete.html',
# 											context, request=request,)
# 	return JsonResponse(data)



@csrf_exempt
def delete(request, pk):
	'''Method for Deleting the Blog
	   as well as going back to Home page after Deleting the record.
	''' 
	print "DELTE ENTEREDDDDDDDDDDD", request.method
	# print "METHOD===", pk
	# print "PK++++++++ ", type(pk)


	# req_id = eval("request." + request.method + "['delete_id']")
	# req_id = eval(pk)
	# print "REQ ID=========", req_id
	blog_inst = BlogCollection.objects(id = pk)[0]

	print "BLOG INST=========", blog_inst
	# print error

	if request.method == "POST":
		print "ENTEREDDDDDDDDDDD"
		blog_inst.delete()	# deleting record
		template = "index.html"
		
		#Date Calculation
		final_start_date, final_end_date = date_calculate()
		# context = {
		# 			'blog_objs': BlogCollection.objects,
		# 			'start_date': final_start_date,
		# 			'end_date': final_end_date,
		# 			}
		response_data = {
						  'blog_objs': list(BlogCollection.objects),
						  'start_date': final_start_date,
						  'end_date': final_end_date,
						}
		print "RESPONSE DATA===", response_data
		# response_data.update({
		# 					'blog_objs': list(response_data)
		# 	})
		# print "RESPONSE DATA LIST===", response_data
		# print error
		# return HttpResponse(json.dumps(response_data), content_type = "application/json")
		# return JsonResponse(response_data)
		return JsonResponse({'result': 1})
		# return render(request, template, response_data)
	else:
		# return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}), content_type = "application/json")
		return JsonResponse({"nothing to see": "this isn't happening"})
	# elif request.method == "GET":
	# 	# redirecting to /delete/ url
		# template = "delete.html"
		# context = {'d_blog_obj': blog_inst}
	# return render(request, template, context)


def search(request):
	print "SEARCH ENTEREDDDD"
	if request.method == 'POST':
		start_time = request.POST['s_start_date']
		end_time = request.POST['s_end_date']

		final_start_time = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
		final_end_time = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S")

		# Search records between dates.
		filtered_blog_objs = BlogCollection.objects(last_updated__gte = final_start_time,
													last_updated__lte = final_end_time)
		context = {
					'filtered_blog_objs': filtered_blog_objs,
					'st_time': start_time,
					'en_time': end_time,
				}
	elif request.method == 'GET':
		st_time = request.GET['search_start_time']
		en_time = request.GET['search_end_time']
	
		context = {
					'st_time': st_time,
					'en_time': en_time,
		 		}
	return render(request, "search.html", context)
