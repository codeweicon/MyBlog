from django.shortcuts import render
from models import Article,Tag
from django.http import HttpResponseRedirect
# Create your views here.
def create_article(req):
	return render(req, 'create.html')
def showlist_article(req):
	return render(req, 'showlist.html')
def modify_article(req):
	return render(req, 'modify.html')


def view_article(req):
	article_list =  Article.objects.all()
	taglist = Tag.objects.all()
	# print type(taglist)
	# for tag in taglist:
	# 	print tag;
	# for i in range(len(taglist)-1,-1,-1):
	# 	print taglist[i]

	for i in range(len(article_list)-1,-1,-1):
		print	article_list[i].title ;
	# article_list1 = article_list.reverse()
	# for item in article_list1:
	# 	print item.title;

	#here i used [::-1] to set the recent article at the front of list
	#failed in using reverse()
	passcontent =  {'article_list':article_list[::-1], 'taglist':taglist}
	return render(req, 'view.html', passcontent)


def view_detail(req):
	Id = req.GET.get('id','')
	if Id == '':
		return HttpResponseRedirect('/article/detail/')
	try:
		ArticleGet = Article.objects.get(pk = Id)
	except:
		return HttpResponseRedirect('/article/detail/')
	taglist = Tag.objects.all()
	passcontent = {'ArticleGet':ArticleGet,'taglist':taglist}
	print type(ArticleGet)

	return render(req, 'view_detail.html', passcontent)


def search_article(req):
	key = req.GET.get('searchkey','')
	# print type(key.encode("utf-8"))
	print "**begin search***"
	print key
	try:
		ArticleFilter = Article.objects.filter(title__contains = key.encode("utf-8"))
	except ArticleFilter.DoesNotExist:
		return HttpResponseRedirect('/article/view/')
	taglist = Tag.objects.all()
	passcontent = {'ArticleFilter':ArticleFilter[::-1],'taglist':taglist}
	return render(req, 'search_result.html', passcontent)


def search_tags(req):
	tag = req.GET.get('tag','')
	print "***get tags***"
	# print "tag = ",tag
	
	# tag = tag[1:-1] 
	# here i don't know why it post me a tag with "" like "tag3" or "tag2"
	#the " and " make filter return a empty query set
	#so i remove it 
	# print tag
	# print type(tag)

	try:
		TagGet =  Tag.objects.filter(tag_name = tag.encode("utf-8"))
	except TagGet.DoesNotExist:
		return HttpResponseRedirect('/article/view/')

	for item in TagGet:
		print 'TagGet: ',item.tag_name,item.id

	print 'TagGet: ',TagGet[0].tag_name,TagGet[0].id

	# ArticleTagGet = Article.objects.get(tags = TagGet[0].tag_name)
	# print ArticleTagGet

	# test = Article.objects.get(pk=4)
	# print test.title,test.id
	# for item in test.tags.all():
	# 	print item

	print "oook---"
	ArticleTagGet = Article.objects.filter(tags__id = TagGet[0].id) #tags__id this is for many to many field
	for item in ArticleTagGet:
		print item
	taglist = Tag.objects.all()
	passcontent = {'ArticleTagGet':ArticleTagGet[::-1],'taglist':taglist}
	return render(req, 'tab_result.html', passcontent)




