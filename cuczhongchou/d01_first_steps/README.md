##学习 rest-framework 文档

###quickstart
Source: django rest framework quickstart http://www.django-rest-framework.org/tutorial/quickstart/

* 创建了Article, Reporter, User, Group 等 Serializer (serializer.py), 继承的 HyperlinkedModelSerializer 很帅
* 创建了Article, Reporter, User, Group 等 ModelViewSet (view.py)  
* 使用router.url 注册 router.register 到urlpattern中 (url.py)

ModelViewSet 如此高效, 是由于集成了 5个 ModelView ( 参 tutorial/3-class-based-views )

```
class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
```


###tutorial
Source: http://www.django-rest-framework.org/tutorial/1-serialization/

* 1-serialization/: 创建Snippet model(models.py), 以及 SnippetSerializer 原始版本Raw与简化版本(serializer.py). 使用原始的JSONResponse (view.py) 实现了列表显示 参: http://localhost:8000/rest/snippets/
* 2-requests-and-responses/: 使用 @api_view 简化了reponse view的创建, 并且requests的数据获取也简化为了 request.data: 参 http://localhost:8000/rest/snippets2/
* 3-class-based-views/: 使用模板类一步步简化, 最后的 generics.ListCreateAPIView 浓缩为 几行代码. 

ListCreateAPIView 如此高效, 是由于集成了2个ModleView

```
class ListCreateAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
```


##学习 django 官方文档 (1.8)
Source: https://docs.djangoproject.com/en/1.8/intro/overview/