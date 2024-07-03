from rest_framework import serializers

from .models import Author, News, Category, Subcategory


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def validate_phone_number(self, value):
        if Author.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Bu telefon raqami allaqachon ishlatilmoqda.")
        return value


class NewsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), write_only=True, source='author')
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True,
                                                     source='category')
    subcategory = SubcategorySerializer(read_only=True)
    subcategory_id = serializers.PrimaryKeyRelatedField(queryset=Subcategory.objects.all(), write_only=True,
                                                        source='subcategory')

    class Meta:
        model = News
        fields = ['id', 'title', 'text', 'published_date', 'category', 'subcategory', 'author', 'author_id',
                  'category_id', 'subcategory_id']

    def create(self, validated_data):
        author = validated_data.pop('author')
        category = validated_data.pop('category')
        subcategory = validated_data.pop('subcategory')
        news = News.objects.create(author=author, category=category, subcategory=subcategory, **validated_data)
        return news
