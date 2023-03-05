from django.test import TestCase,Client
from bs4 import BeautifulSoup
from .models import Post
# Create your tests here.

class TestView(TestCase):

    def setUP(self):
        self.client=Client()
    def test_post_list(self):
        #1-1 포스트 목록 페이지 가져오기
        response=self.client.get('/blog/')
        #1-2 정삭적 페이지 로드 확인
        self.assertEqual(response.status_code,200)
        #1-3 페이지 타이틀은 'Blog'이다
        soup=BeautifulSoup(response.content,'html.parser')
        self.assertEqual(soup.title.text,'Blog')

        navbar=soup.nav

        self.assertIn('Blog',navbar.text)
        self.assertIn('About Me',navbar.text)

        #2.1 포스트 게시물이 없다면
        self.assertEqual(Post.objects.count(),0)
        #2.2 main_area 에 아직 게시물이 없다고 뜬다
        main_area=soup.find('div',id='main-area')
        self.assertIn('아직 게시물이 없습니다',main_area.text)


        #3.1 포스트가 2개 있다면
        post_001=Post.objects.create(
            title='첫 번째 포스트입니다',
            content='Hello World we ar the one',
        )

        post_002=Post.objects.create(
            title='두번째 포스트입니다 ',
            content='1등이 전부는 아닐껄요',

        )

        self.assertEqual(Post.objects.count(),2)



        #3.2
        response= self.client.get('/blog/')
        soup= BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code,200)

        #3.3 main area에 포스트 2개의 제목이 존재한다면
        main_area=soup.find('div',id='main-area')
        self.assertIn(post_001.title,main_area.text)
        self.assertIn(post_002.title,main_area.text)

        #3.4 '아직 게시물이 없습니다 문구는 안나타남'
        self.assertNotIn('아직 게시물이없습니다',main_area.text)

    def test_post_detail(self):
        #1.1 Post 하나 존재할때
        post_001=Post.objects.create(
            title='첫 번째 포스트입니다',
            content='Hello World. We are the world',
        )
        #1.2
        self.assertEqual(post_001.get_absolute_url(),'/blog/1')

        #2. 첫 번째 포스트의 상세 페이지 테스트
        response= self.client.get(post_001.get_absolute_url())
        self.assertEqual(response.status_code,200)
        soup=BeautifulSoup(response.content,'html.parser')

        #2.2 포스트 목록 페이지와 똑같은 내비게이션
        navbar=soup.nav
        self.assertIn('Blog',navbar.text)
        self.assertIn('About Me',navbar.text)

        #2.3 첫 번째 포스트의 제목이 웹 브라이저 탭 타이틀에 있다
        self.assertIn(post_001,soup.title.text)

        #2.4
        main_area=soup.find('div',id='main-area')
        post_area=main_area.find('div',id='post-area')
        self.assertIn(post_001.title,post_area.text)

        #2.5 첫번째 포스트의 작성자가 포스트 영역에 있다

        #2.6
        self.assertIn(post_001.content,post_area.text)