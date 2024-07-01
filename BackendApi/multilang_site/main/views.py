from django.shortcuts import render
from .models import Post, PostTranslation
from django.conf import settings
import openai
from whoosh.qparser import MultifieldParser
from whoosh import index

openai.api_key = settings.OPENAI_API_KEY

def home(request):
    query = request.GET.get('query')
    posts = Post.objects.all()

    if query:
        ix = index.open_dir(settings.WHOOSH_INDEX)
        with ix.searcher() as searcher:
            query_parser = MultifieldParser(['title', 'content'], ix.schema)
            parsed_query = query_parser.parse(query)
            results = searcher.search(parsed_query, limit=None)
            post_ids = [int(result['path'].split('/')[-1]) for result in results]
            posts = Post.objects.filter(id__in=post_ids)

    # Augment results with GPT
    gpt_results = []
    if posts:
        gpt_results = augment_with_gpt(query, posts)

    return render(request, 'home.html', {'posts': posts, 'gpt_results': gpt_results, 'query': query})

def augment_with_gpt(query, posts):
    documents = "\n\n".join([post.translations.filter(language_code='en').first().content for post in posts if post.translations.filter(language_code='en').exists()])
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"Q: {query}\nA: Based on the following documents:\n{documents}\nAnswer:",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer = response.choices[0].text.strip()
    return {'answer': answer, 'posts': posts}
