from django.urls import path
from . import views


urlpatterns = [
     path('listCategory', views.ListCategory.as_view(), name='listCategory'),
     path('createCategory', views.CreateCategory.as_view(), name='createCategory'),
     path('updateCategory', views.CreateCategory.as_view(), name='updatecategory'),
     path('deleteCategory', views.DeleteCategory.as_view(), name='deleteCategory'),
     path('getCategorydetails', views.GetCategoryDetails.as_view(), name='getCategorydetails'),
     path('get_instance_category', views.ListCategory.as_view(), name='get_instance_category'),
     path('listProduct', views.ListProduct.as_view(), name='listProduct'),
     path('createProduct', views.CreateProduct.as_view(), name='createProduct'),
     path('updateProduct', views.CreateProduct.as_view(), name='updateProduct'),
     path('deleteProduct', views.DeleteProduct.as_view(), name='deleteProduct'),
     path('getProductdetails', views.GetProductDetails.as_view(), name='getProductdetails'),
     path('listShowroom', views.ListShowroom.as_view(), name='listShowroom'),
     path('createShowroom', views.CreateShowroom.as_view(), name='createShowroom'),
     path('updateShowroom', views.CreateShowroom.as_view(), name='updateShowroom'),
     path('deleteShowroom', views.DeleteShowroom.as_view(), name='deleteShowroom'),
     path('getShowroomdetails', views.GetShowroomDetails.as_view(), name='getShowroomdetails'),
     path('listInventary', views.ListInventary.as_view(), name='listInventary'),
     path('createInventary', views.CreateInventary.as_view(), name='createInventary'),
     path('updateInventary', views.CreateInventary.as_view(), name='updateInventary'),
     path('deleteInventary', views.DeleteInventary.as_view(), name='deleteInventary'),
     path('getInventarydetails', views.GetInventaryDetails.as_view(), name='getInventarydetails'),
     path('listOrder', views.ListOrder.as_view(), name='listOrder'),
     path('createOrder', views.CreateOrder.as_view(), name='createOrder'),
     path('updateOrder', views.CreateOrder.as_view(), name='updateOrder'),
     path('deleteOrder', views.DeleteOrder.as_view(), name='deleteOrder'),
     path('getOrderdetails', views.GetOrderDetails.as_view(), name='getOrderdetails'),

     path('getNamePrice', views.GetNamePrice.as_view(), name='getNamePrice'),
     path('getDetails', views.GetDetails.as_view(), name='getDetails')
]






