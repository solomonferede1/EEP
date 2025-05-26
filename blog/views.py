from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        "author": "John Doe",
        "title": "Getting Started with Python",
        "content": '''But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?''',
        "date_posted": "2023-10-15"
    },
    {
        "author": "Jane Smith",
        "title": "The Art of Web Development",
        "content": "Modern web development requires understanding...",
        "date_posted": "2023-10-20"
    },
    {
        "author": "Alex Johnson",
        "title": "Data Science Fundamentals",
        "content": "Data science combines statistics, programming...",
        "date_posted": "2023-11-05"
    },
    {
        "author": "Sarah Williams",
        "title": "Machine Learning Basics",
        "content": "Machine learning algorithms can be supervised...",
        "date_posted": "2023-11-12"
    },
    {
        "author": "Mike Brown",
        "title": "DevOps Best Practices",
        "content": "Continuous integration and deployment...",
        "date_posted": "2023-11-18"
    },
    {
        "author": "Emily Davis",
        "title": "Frontend Frameworks Comparison",
        "content": "React, Vue, and Angular each have their...",
        "date_posted": "2023-11-25"
    },
    {
        "author": "David Wilson",
        "title": "Backend Architecture Patterns",
        "content": "Microservices vs monolithic architecture...",
        "date_posted": "2023-12-01"
    },
    {
        "author": "Lisa Taylor",
        "title": "Mobile App Development Trends",
        "content": "Cross-platform frameworks like Flutter...",
        "date_posted": "2023-12-10"
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})