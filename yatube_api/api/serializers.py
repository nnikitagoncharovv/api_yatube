from rest_framework import serializers, validators

from posts.models import Group, Post, Comment


class GroupSerializer(serializers.ModelSerializer):

    title = serializers.StringRelatedField()
    slug = serializers.SlugField(
        validators=[validators.UniqueValidator(
            queryset=Group.objects.all())])
    description = serializers.CharField()

    class Meta:
        model = Group
        fields = ('id', 'slug', 'title', 'description')


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        read_only=True, validators=[validators.UniqueValidator(
            queryset=Comment.objects.all())])
    author = serializers.StringRelatedField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(),
                                              required=False)
    text = serializers.CharField()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')
        read_only_field = ('author', 'post')


class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    text = serializers.CharField(required=True)
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(),
                                               required=False)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'group', 'image', 'pub_date')


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(),
                                               required=False)
    text = serializers.CharField(required=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'group', 'pub_date')
        read_only_fields = ('author',)
