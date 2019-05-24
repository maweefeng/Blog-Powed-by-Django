from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Summary,Article
from django.core.paginator import Paginator
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World！")

def get_index_summary_page(request):
    summary_list = Summary.objects.all()
   
    return render(request,'blog/index.html',
    {
      'summary_list':summary_list,  
    })




def get_index_page(request):
    # 适用与/index?page=1之类的网络请求
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    all_ariticle = Summary.objects.all()
    paginator = paginator(all_ariticle,3)
    page_aritcle_list = paginator.page(page)
    page_num = paginator.num_pages
    if page_aritcle_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    
    if page_aritcle_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page

    return render(request,'blog/index.html',{
        'aritcle_list':page_aritcle_list,
        'page_num':range(1,page_num+1),
        "curr_page":page,
        'next_page':next_page,
        'previous_page':previous_page
        }
        )



def get_detail_page(request,summary_id):
    all_ariticle = Summary.objects.all()
    cur_article = None
    for aritcle in all_ariticle:
        if aritcle.summary_id == summary_id:
            cur_article = aritcle
            break


    sectionList = cur_article.summary_content.split('\n')
    return render(request,'blog/detail.html',{'curr_aritcle':cur_article,'section_list':sectionList})

