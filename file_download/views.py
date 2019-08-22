import os
from django.http import HttpResponse, Http404, StreamingHttpResponse, FileResponse
#from django.contrib.auth.decorators import login_required
# Create your views here.
# Case 1: simple file download, very bad
# Reason 1: loading file to memory and consuming memory
# Can download all files, including raw python .py codes
#然而该方法有个问题，如果文件是个二进制文件，HttpResponse输出的将会是乱码。
# 对于一些二进制文件(图片，pdf)，我们更希望其直接作为附件下载。
# 当文件下载到本机后，用户就可以用自己喜欢的程序(如Adobe)打开阅读文件了。
# 这时我们可以对上述方法做出如下改进， 给response设置content_type和Content_Disposition。
# HttpResponse有个很大的弊端，其工作原理是先读取文件，载入内存，然后再输出。如果下载文件很大，该方法会占用很多内存。

def file_download(request, file_path):
    # do something...
    with open(file_path) as f:
        c = f.read()
    return HttpResponse(c)


# Case 2 Use HttpResponse to download a small file
# Good for txt, not suitable for big binary files
def media_file_download(request, file_path):
    with open(file_path, 'rb') as f:
        try:
            response = HttpResponse(f)
            response['content_type'] = "application/octet-stream"
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
        except Exception:
            raise Http404


# Case 3 Use StreamingHttpResponse to download a large file
# Good for streaming large binary files, ie. CSV files
# Do not support python file "with" handle. Consumes response time
#对于下载大文件，Django更推荐StreamingHttpResponse和FileResponse方法，
# 这两个方法将下载文件分批(Chunks)写入用户本地磁盘，先不将它们载入服务器内存。
def stream_http_download(request, file_path):
    try:
        response = StreamingHttpResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    except Exception:
        raise Http404


# Case 4 Use FileResponse to download a large file
# It streams the file out in small chunks
# It is a subclass of StreamingHttpResponse
# Use @login_required to limit download to logined users
'''FileResponse方法是SteamingHttpResponse的子类，是小编我推荐的文件下载方法。
如果我们给file_response_download加上@login_required装饰器，
那么我们就可以实现用户需要先登录才能下载某些文件的功能了。'''
def file_response_download1(request, file_path):
    try:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    except Exception:
        raise Http404


# Case 5 Limit file download type - recommended
'''然而即使加上了@login_required的装饰器，用户只要获取了文件的链接地址, 他们依然可以通过浏览器直接访问那些文件。
我们等会再谈保护文件的链接地址和文件私有化，因为此时我们还有个更大的问题需要担忧。
我们定义的下载方法可以下载所有文件，不仅包括.py文件，还包括不在media文件夹里的文件(比如非用户上传的文件)。
比如当我们直接访问127.0.0.1:8000/file/download/file_project/settings.py/时，
你会发现我们连file_project目录下的settings.py都下载了。如果哪个程序员这么蠢，你可以将他直接fire了。
所以我们在编写下载方法时，我们一定要限定那些文件可以下，哪些不能下或者限定用户只能下载media文件夹里的东西。'''
#@login_required
def file_response_download(request, file_path):
    ext = os.path.basename(file_path).split('.')[-1].lower()
    # cannot be used to download py, db and sqlite3 files.
    if ext not in ['py', 'db',  'sqlite3']:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        raise Http404

