from django.contrib import admin
from blog.models import Post


# step 1:
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
	#fields display on change list
	list_display = ['title', 'description']

	#fields to filter the chaange list with
	list_filter = ['published', 'created']

	#fields to search in the change list 
	search_fields = ['title', 'description', 'content']

	#enable the date drill down on change list
	date_hierarchy = 'created'

	#enable the save buttons on the top of the change form

	save_on_top = True

	#prepopulate the slug fro the title - big timesaver!
	prepopulated_fields = {'slug':("title",)}

admin.site.register(Post, PostAdmin)