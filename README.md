# django_project


# 파이참으로 실행시 가이드  


## 파이참이 작업하기 훨씬 편하다 .gitigonre 만들고 사항 적용해줄것


### 실습 따라하기 
- 1. 파이참 인터프리터 가상환경 설정하기 
- 2. pip 장고
- 3. project 시작 app만들기 
- 4. 모델 만들기  
- 5. makemigrations, migrate 하고 나서 깃 올리고 gitignore에 migrations/ 추가 
- 6. 자신의 모델 가상환경 .gitnore에 올려놓고 사용할것 



### class view에서 주의사항
- ListView는 기본적으로 _list가 붙은 파일을 템플릿으로 사용함
- Updateview, CreateView는 _form.html을 자동으 사용 
- Detailview는 _detail.html을 사용한다
- 이러한 구조가 마음에 들지 않을때는 
- template_name = '템플릿주소.html'으로 고정가능
- 
### 모델 관계에서의 받아오는법 
- x 모델이 있고 y모델에서 x모델을 외래키나
- 다대다 관계로 받아오면 x.y_set으로 받아온다
- 아주 중요한 부분이죠 


# model에 카테고리 slug로 만들고
```angular2html
model.py에서
class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=200,unique=True,allow_unicode=True)

    def __str__(self):
        return self.name

admin.py에서 

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category,CategoryAdmin)

```
- 이 결과 자동으로 슬러그 필드에 name값이 들어감  

## class view에서 콘텍스트 데이터 사용법

```
    def get_context_data(self, **kwargs):
        context=super(PostList,self).get_context_data()
        context['categories']= Category.objects.all()
        context['no_category_post_count']=Post.objects.filter(category=None).count()

        return context

```
- 이런식으로 딕셔너리를 만들어주고 넣어주는 형태로
- context_date를 상속해서 넣어주면됩니다


# 전체적인 틀은 class_view로 짜줌
- class view로 짜주고 몇몇 필터링된 자료의 경우
- function view로 짜줍시다.
```
def tag_page(request,slug):
    tag=Tag.objects.get(slug=slug)
    post_list=tag.post_set.all()

    return render(
        request,
        'blog/post_list.html',
    {
        'post_list':post_list,
        'tag':tag,
        'categories':Category.objects.all(),
        'no_category_post_count':Post.objects.filter(category=None).count(),
    }
    )

```
- 이렇게 기존의 post_list 템플릿을 그대로 활용하는
- tag page를 만들어 준거죠