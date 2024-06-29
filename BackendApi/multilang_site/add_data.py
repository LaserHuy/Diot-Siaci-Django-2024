import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multilang_site.settings')
django.setup()

from main.models import Post

# Add data to the database

post1 = [
    {
        'title': '🎯 Strategies for Effective Urgent Ticket Classification',
        'content': 'Strategies for effective urgent ticket classification, including criteria for classifying urgency, helping non-technical people understand urgency, and tools and practices for managing urgent tickets.',
        'imageUrl': 'https://media.dev.to/cdn-cgi/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flqjfqxw3qb3kqgtis9ol.jpeg',
    },
    {
        'title': 'Stop Using UUIDs in Your Database',
        'content': 'This post discusses the performance issues and storage impact of using UUIDs as keys in a database.',
        'imageUrl': 'https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/d317dcd3b3d8a276f6002a1c49f7ca9a?_a=AQAEuiZ',
    },
    {
        'title': 'Couchbase on Rails: A Guide to Introducing Dynamic and Adaptive Data to Your Application',
        'content': 'Discover how to fully integrate Couchbase into your Ruby on Rails application to handle dynamic and adaptive data structures. The post compares document and relational models, discusses performance trade-offs, and provides code examples for caching and using a Couchbase Ruby ORM. It highlights the ease of transitioning from ActiveRecord to Couchbase and introduces caching mechanisms to optimize performance.',
        'imageUrl': 'https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/dad0980157aff70b67a4cf0cf264e04f?_a=AQAEuiZ',
    },
    {
        'title': 'Where and How to Sell Graphic Design Online',
        'content': 'Graphics are crucial in enhancing visual appeal, and digital marketplaces are excellent platforms to sell graphic designs. These marketplaces allow authors to showcase their work, gain broad exposure, and join a community of designers. Getting started involves signing up, following marketplace rules, and uploading your products. Improving visibility and sales can be achieved by creating unique products, updating based on user feedback, and engaging with clients.',
        'imageUrl': 'https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/6743b17feb43843b1fc320ad141e1076?_a=AQAEuiZ',
    },
]

for post_data in post1:
    post = Post(
        title=post_data['title'],
        content=post_data['content'],
        imageUrl=post_data['imageUrl'],
    )
    post.save()
    print("Sample posts added successfully")