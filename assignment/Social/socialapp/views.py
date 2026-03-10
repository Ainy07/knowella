from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.db.models import Q
from django.core.cache import cache

# Hot Topics API
class HotTopicsView(APIView):
    
    def get(self, request):

        cached_posts = cache.get("hot_topics")

        if cached_posts:
            return Response(cached_posts)

        posts = Post.objects.order_by("-trending_score")[:20]

        serializer = PostSerializer(posts, many=True)

        cache.set("hot_topics", serializer.data, timeout=300)

        return Response(serializer.data)

# Category Posts
class CategoryPostsView(APIView):

    def get(self, request):

        category = request.GET.get("category")

        posts = Post.objects.filter(category__name=category)

        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)


# Search Posts
class SearchPostsView(APIView):

    def get(self, request):

        query = request.GET.get("q")
        if not query:
            return Response({"error": "Query parameter required"})

        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)