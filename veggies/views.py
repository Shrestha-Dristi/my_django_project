from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

posts = [
    {
        "id": 0,
        "title": "Exploring Python",
        "content": "A brief guide on Python's versatile capabilities."
    },
    {
        "id": 1,
        "title": "The Art of Cooking",
        "content": "Discover the secrets behind gourmet cooking at home."
    },
    {
        "id": 2,
        "title": "Traveling the World",
        "content": "An overview of the most breathtaking travel destinations."
    }
]

def recipe(request):
    html_parts = []
    for post in posts:
        html_parts.append(f'''
        <div>
        <a href="/veggies/{post['id']}/">
            <h1>{post['id']} - {post['title']}</h1></a>
            <p>{post['content']}</p>
        </div>
        ''')

    html = ''.join(html_parts)

    # return HttpResponse(html)
    return render(request, 'veggies/home.html')

def post(request, id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:    
        html = f'''
    <h1>{post_dict['title']}</h1>
    <p>{post_dict['content']}</p>
            '''

        return HttpResponse(html)
    else:
        return HttpResponseNotFound('Ahhh,,, Schlect!!')
    

def redirect_veggies(request, id):
    return HttpResponseRedirect(f'/veggies/{id}')