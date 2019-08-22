import markdown
from .models import *
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.shortcuts import render, get_object_or_404
from djangoblog import settings
from djangoblog.settings import base



class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = base.ARTICLE_PAGINATE_BY

    def get_queryset(self):
        return Post.objects.filter(status='p')


def article(request, pk):
    post = get_object_or_404(Post, pk=pk,)
    author = User.objects.get(id=post.author_id)
    category = Category.objects.get(id=post.category_id)
    post.increase_views()  # 阅读量加1
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.fenced_code',
        # 'markdown.extensions.tables'
    ])
    post.body = md.convert(post.body)
    if strip_tags(md.toc).strip() == '':
        post.toc = ''
    else:
       post.toc = md.toc

    # 获取相关文章
    relative_posts = Post.objects.filter(category_id=post.category_id, status='p').exclude(pk=pk).order_by('?')[:4]

    context = {}
    context['post'] = post
    context['author'] = author
    context['category'] = category
    context['relative_posts'] = relative_posts
    return render(request, 'blog/article.html', context)

class ArchivesView(ListView):
    template_name = 'blog/archives.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='p').order_by('-created_time')


# 全站所有的标签
class TagsView(ListView):
    model = Tag
    template_name = 'blog/tags.html'
    context_object_name = 'tags'


# 每个标签下的所有文章
class TagListView(ListView):
    template_name = 'blog/tag_list.html'
    context_object_name = 'posts'
    paginate_by = base.ARTICLE_PAGINATE_BY

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return Post.objects.filter(tag=tag, status='p').order_by('-created_time')

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['tag_name'] = Tag.objects.get(pk=self.kwargs.get('pk'))
        return context


class CategoryView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = base.ARTICLE_PAGINATE_BY

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return Post.objects.filter(category=cate, status='p').order_by('-created_time')

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['cate_name'] = Category.objects.get(pk=self.kwargs.get('pk'))
        return context


# 按分类展示文章
class Categories(ListView):
    model = Post
    template_name = 'blog/category_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='p')


class BooksView(ListView):
    template_name = 'book/books.html'
    context_object_name = 'books'
    paginate_by = base.BOOK_PAGINATE_BY

    def get_queryset(self):
        return Book.objects.all().order_by('-pk')


class BookListView(ListView):
    template_name = 'book/book_list.html'
    context_object_name = 'books'
    paginate_by = base.BOOK_PAGINATE_BY

    def get_queryset(self):
        tag = get_object_or_404(BookTag,pk = self.kwargs.get('pk'))
        return Book.objects.filter(tag=tag).order_by('-created_time')

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['tag_name'] = BookTag.objects.get(pk = self.kwargs.get('pk'))
        return context


class MoviesView(ListView):
    template_name = 'movie/movies.html'
    context_object_name = 'movies'
    paginate_by = base.BOOK_PAGINATE_BY

    def get_queryset(self):
        return Movie.objects.all().order_by('-created_time')


class MovieListView(ListView):
    template_name = 'movie/movie_list.html'
    context_object_name = 'movies'
    paginate_by = base.BOOK_PAGINATE_BY

    def get_queryset(self):
        tag = get_object_or_404(MovieTag,pk = self.kwargs.get('pk'))
        return Movie.objects.filter(tag=tag).order_by('-created_time')

    def get_context_data(self, **kwargs):
        context = super(MovieListView, self).get_context_data(**kwargs)
        context['tag_name'] = MovieTag.objects.get(pk = self.kwargs.get('pk'))
        return context


def messages(request):
    messages = Messages.objects.get(pk=1)
    return render(request, 'blog/messages.html', {'messages': messages})


class CoursesView(ListView):
    template_name = 'course/courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Courses.objects.all().order_by('-created_time')


def course(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    return render(request, 'course/course.html', context={'course': course})


def course_article(request, pk):
    post = get_object_or_404(Post, pk=pk)
    author = User.objects.get(id=post.author_id)
    category = Category.objects.get(id=post.category_id)
    post.increase_views()  # 阅读量加1
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body)
    if strip_tags(md.toc).strip() == '':
        post.toc = ''
    else:
        post.toc = md.toc

    # 获取相关文章
    relative_posts = Post.objects.filter(category_id=post.category_id, status='p').exclude(pk=pk).order_by('?')[:4]

    context = {}
    context['post'] = post
    context['author'] = author
    context['category'] = category
    context['relative_posts'] = relative_posts
    context['course'] = post.courses_set.first()
    return render(request, 'course/course.html', context)
