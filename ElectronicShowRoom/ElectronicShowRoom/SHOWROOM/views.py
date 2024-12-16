
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import * 
from rest_framework.exceptions import NotFound

class ListCategory(APIView):
    def post(self, request):
        data = request.data
        category = Category.objects.filter(name=data['name'])
        serializers = ListCategorySerializer(category, many=True).data
        return Response({"List_of_category": serializers}) 
    def get_instance_category(self,Category,id):
        instance = object(Category,id)
        return ({instance})
        
class GetCategoryDetails(APIView):
    def post(self,request):
        data = request.data
        category = Category.objects.get(id = data['id'])
        serializers = ListCategorySerializer(category).data
        return Response({"get category details":serializers})
    
class CreateCategory(APIView):
    def post(self,request):
        data = request.data
        if 'id' in data:
            category = Category.objects.get(id = data['id'])
            category.name = data['name']
            category.description = data ['description']
            category.save()
            return Response({"category update successfully"})
        else:
            category = Category.objects.create(name = data ['name'],description = data['description'])
            return Response ({"category create successfully"})
          
class DeleteCategory(APIView):
    def post(self,request):
        data = request.data
        if 'id' in data:
            category = Category.objects.get(id = data['id'])
            category.delete()
            return Response ({"category delete successfully"})
        else:
            return Response({"category not found"})

class ListProduct(APIView):
    def post(self,request):
        data=request.data
        product = Product.objects.all()
        if 'name' in data:
            product = product.filter(name__icontains = data['name'])
        if 'category' in data :
            product = product.filter(category= data['category']) 
             
        if 'description' in data:
            product = product.filter(description = data['description'])
        if 'price' in data:
            product = product.filter(price = data['price'])
        if 'brand' in data:
            product = product.filter(brand = data['brand'])
        if 'image' in data:
            product = product.filter(image = data('image'))
        if 'count' in data:
            product = product.filter(count = data['count'])
            
        serializers=ListProductSerializer(product,many = True).data
        return Response({
           "List of product":serializers
            })
    
class GetProductDetails(APIView):
    def post(self,request):
        data = request.data
        product = Product.objects.get(id = data['id'])
        serializers = ListProductSerializer(product).data
        return Response({"get product details":serializers})
class CreateProduct(APIView):
    def post(self,request):
        data=request.data
        if 'id' in data:
            product = Product.objects.get(id=data['id'])
            product.name = data ['name']
            product.category.name = data ['category'] ['name']
            product.category.description = data ['category'] ['description']
            product.category.save()
            product.description = data ['description']
            product.price = data ['price']
            product.brand = data ['brand']
            product.image_url = data ['image_url']
            product.count = data ['count']
            product.save()
            return Response ({"product updated succesfully"})
        else:
            product = {}
            product['name'] = data ['name']
            product['description'] = data['description']
            product['price'] = data ['price']
            product['brand'] = data['brand']
            product['image_url'] = data ['image_url']
            product['count'] = data ['count']
            category_items = {} 
            category_items['name']=data['category']['name']
            category_items['description']=data['category']['description']
            category = Category.objects.create(**category_items) 
            product['category'] = category
            product = Product.objects.create(**product)
            return Response({"Product creation successfull"})
class DeleteProduct(APIView):
    def post (self,request):
        data = request.data
        product = Product.objects.get (id=data('id'))
        product.delete()
        return Response({"Product delete succesfull"})
class ListShowroom(APIView):
    def post (self,request):
        data = request.data
        showroom = Showroom.objects.all()
        if 'name' in data:
            showroom = showroom.filter(name__icontains= data['name'])
        if 'location' in data:
            showroom = showroom .filter(location = data['location'])
        if 'contact_info' in data:
            showroom = showroom .filter(contact_info = data['contact_info'])
        serializers = ListShowroomSerializer(showroom,many=True).data
        return Response({"list of showroom":serializers})
class GetShowroomDetails(APIView):
    def post (self,request):
        data = request.data
        showroom = Showroom.objects.get(id = data['id'])
        serializers = ListShowroomSerializer(showroom).data
        return Response ({"get showroom details":serializers})

class CreateShowroom(APIView):  
     def post (self,request):
        data = request.data
        if 'id' in data:
            showroom = Showroom.objects.get(id = data['id'])
            showroom.name = data['name']
            showroom.location = data ['location']
            showroom.contact_info =data['contact_info']
            showroom.save()
            return Response({"showroom update successfull"})
        else:
            showroom = Showroom.objects.create(name=data['name'],location=data['location'],contact_info=data['contact_info'])
            return Response({"showroom create successfull"})
class DeleteShowroom(APIView):
    def post (self,request):
        data = request.data
        showroom = Showroom.objects.get(id = data['id'])
        showroom.delete()
        return Response({"Showroom delete successfull"})
    
class ListInventary(APIView):
     def post (self,request):
        data = request.data
        inventary = Inventory.objects.all()
        if 'product' in data:
            inventary = inventary.filter(product=data['product'])
        if 'showroom' in data:
            inventary = inventary.filter(showroom=data['showroom'])
        if 'stock' in data:
            inventary = inventary.filter(stock=data['stock'])
        if 'last_updated' in data:
            inventary = inventary.filter(last_updated=data['last_updated'])
        serializers = ListInventorySerializer(inventary,many=True).data
        return Response({"list inventary":serializers})
class GetInventaryDetails(APIView):
    def post (self,request):
        data = request.data
        inventary = Inventory.objects.get(id = data['id'])
        serializers =ListInventorySerializer(inventary).data
        return Response({"get inventary details":serializers})
class CreateInventary(APIView):
    def post (self,request):
        data = request.data
        if 'id' in data:
            inventary = Inventory.objects.get(id =data['id'])
            product = inventary.product
            product.category.name = data['category']['name']
            product.category.description = data['category']['description']
            product.category.save()
            inventary.product.name = data['product']['name']
            inventary.product.description = data ['product']['description']
            inventary.product.price = data ['product']['price']
            inventary.product.brand = data ['product']['brand']
            inventary.product.image_url = data ['product']['image_url']
            inventary.product.save()
            inventary.showroom.name = data ['showroom']['name']
            inventary.showroom.location = data ['showroom']['location']
            inventary.showroom.contact_info = data ['showroom']['contact_info']
            inventary.showroom.save()
            inventary.stock = data ['stock']
            inventary.last_updated = data ['last_updated']
            inventary.save()
            return Response({"inventary updated successfully"})
        else:
            inventary = {}
            product = {}
            product['name'] = data ['name']
            product['description'] = data['description']
            product['price'] = data ['price']
            product['brand'] = data['brand']
            product['image_url'] = data ['image_url']
            category_items = {} 
            category_items['name']=data['category']['name']
            category_items['description']=data['category']['description']
            category = Category.objects.create(**category_items) 
            product['category'] = category
            product = Product.objects.create(**product)
            showroom = Showroom.objects.create(name=data['name'],location=data['location'],contact_info=data['contact_info'])
            inventary['stock'] = data ['stock']
            inventary['last_updated'] = data ['last_updated']
            inventary['product'] =product
            inventary['showroom'] = showroom
            inventary = Inventory.objects.create(**inventary)
            return Response ({"inventary create successfull"})
class DeleteInventary(APIView):
    def post (self,request):
        data = request.data
        inventary = Inventory.objects.get(id = data['id'])
        inventary.delete()
        return Response({"inventary delete successfull"})
    
class ListOrder(APIView):
    def post (self,request):
        data = request.data
        order= Order.objects.all()
        if 'product' in data:
            order= order.filter(product=data['product'])
        if 'showroom' in data:
            order = order.filter(showroom=data['showroom'])
        if 'quantity' in data:
            order = order.filter(quantity=data['quantity'])
        if 'total_price' in data:
            order = order.filter(total_price=data['total_price'])
        if 'created_at' in data:
            order= order.filter(created_at=data['created_at'])
        serializers = ListOrderSerializer(order,many=True).data
        return Response({"list of order":serializers})
class GetOrderDetails(APIView):
    def post (self,request):
        data = request.data
        order= Order.objects.get(id =data['id'])
        serializers = ListOrderSerializer(order).data
        return Response({"get order details":serializers})
class CreateOrder(APIView):
     def post (self,request):
        data = request.data
        if 'id' in data:
            order = Order.objects.get(id = data['id'])
            product = order.product
            product.category.name = data['category']['name']
            product.category.description = data['category']['description']
            product.category.save()
            product.name = data['product']['name']
            order.product.description = data ['product']['description']
            order.product.price = data ['product']['price']
            order.product.brand = data ['product']['brand']
            order.product.image_url = data ['product']['image_url']
            order.product.save()
            order.showroom.name = data ['showroom']['name']
            order.showroom.location = data ['showroom']['location']
            order.showroom.contact_info = data ['showroom']['contact_info']
            order.showroom.save()
    
            order.quantity = data['quantity']
            order.total_price = data['total_price']
            order.created_at = data ['created_at']
            order.save()
            return Response({"order updated successfull"})
        else:
            order = {}
            product = {}
            product['name'] = data ['name']
            product['description'] = data['description']
            product['price'] = data ['price']
            product['brand'] = data['brand']
            product['image_url'] = data ['image_url']
            category_items = {} 
            category_items['name']=data['category']['name']
            category_items['description']=data['category']['description']
            category = Category.objects.create(**category_items) 
            product['category'] = category
            product = Product.objects.create(**product)
            showroom = Showroom.objects.create(name=data['name'],location=data['location'],contact_info=data['contact_info'])
            order['quantity'] = data ['quantity']
            order['total_price'] = data['total_price']
            order['created_at'] = data ['created_at']
            order['product'] = product
            order['showroom'] = showroom
            order = Order.objects.create(**order)
            return Response({"order created successfull"})
class DeleteOrder(APIView):
     def post (self,request):
        data = request.data
        order= Order.objects.get(id =data['id'])
        order.delete()
        return Response({"order deleted successfull"})


class GetNamePrice(APIView):
    def post(self, request):
        data = request.data 
        if 'id' in data:
                inventory = Inventory.objects.get(id=data['id'])
                # response_data ={
                #         "showroom_name": inventory.showroom.name,
                #         "product_count": inventory.product.count
                #     }
                # return Response(response_data)
                
        '''if 'product' in data: 
             inventory = Inventory.objects.filter(product__name=data['product'])
        else:
            return Response({"error": "Invalid request"})
        #for i in inventory:
        #print(i.showroom.name)
                 
        response_data = [
                        {
                        "showroom_name": i.showroom.name,
                        "product_count": i.product.count
                    }
                    for i in inventory
                     ]
        print(response_data)          
        return Response(response_data)'''
        
        if 'product_count' in data:
            print("111",inventory)
            inventory.product.count -= data['product_count']
            inventory.product.save()
        else:
         return Response({"error": "Invalid request"})
        response_data = {
                        "showroom_name": inventory.showroom.name,
                        "product_count": inventory.product.count}
                        
        return Response(response_data)

class GetDetails(APIView):
    def post(self, request):
        data = request.data 
        if 'id' in data:
            inventory = Inventory.objects.get(id=data['id'])

        if 'brand' in data: 
            inventory, created= Inventory.objects.get_or_create(product__brand=data['brand'])
            print("4444",inventory)
            #inventary = inventary.create(product_brand=data['brand'])
            #print("3333",inventary)
            total_count = 0
            for inventory in inventory:
                total_count += inventory.product.count
            response_data = []
            response_data.append({
            "name": inventory.showroom.name,
            "brand": inventory.product.brand,
            "total_product_count": inventory.product.count  
        })
            return Response({"brands": response_data})






                                     
                                     

        
        
       
            