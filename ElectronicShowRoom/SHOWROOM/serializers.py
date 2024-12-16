from rest_framework import serializers 
from .models import * 

class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','id','description'] 
class ListProductSerializer(serializers.ModelSerializer):
    category_details = serializers.SerializerMethodField() 
    class Meta:
        model = Product
        fields = ['name','id','description','price','brand','count','image_url','category_details']
    def get_category_details(self,obj):
        return{
               'name':obj.category.name, 
               'description':obj.category.description
        }
class ListShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ['name','location','contact_info']
class ListInventorySerializer(serializers.ModelSerializer):
    product_details = serializers.SerializerMethodField() 
    showroom_details = serializers.SerializerMethodField()
    class Meta:
        model =  Inventory
        fields = ['stock','last_updated','product_details','showroom_details']
    def get_product_details(self,obj):
        return{
            'name': obj.product.name,
            'description' : obj.product.description,
            'price' : obj.product.price,
            'brand': obj.product.brand,
            'image_url' : obj.product.image_url,
            'name': obj.product.category.name,
            'description' : obj.product.category.description
            }
    def get_showroom_details(self,obj):
        return{
            'name' : obj.showroom.name,
            'location' : obj.showroom.location,
            'contact_info' : obj. showroom.contact_info
        }
class ListOrderSerializer(serializers.ModelSerializer):
    product_details = serializers.SerializerMethodField() 
    showroom_details = serializers.SerializerMethodField()
    class Meta:
        model =  Order
        fields = ['quantity','total_price','created_at','product_details','showroom_details']
    def get_product_details(self,obj):
        return{
            'name': obj.product.name,
            'description' : obj.product.description,
            'price' : obj.product.price,
            'brand': obj.product.brand,
            'image_url' : obj.product.image_url,
            'name': obj.product.category.name,
            'description' : obj.product.category.description 
            }
    def get_showroom_details(self,obj):
        return{
            'name' : obj.showroom.name,
            'location' : obj.showroom.location,
            'contact_info' : obj. showroom.contact_info
        }
        
    


        